
"""
Streamlit web interface for the Legal Chatbot

This module provides a web interface for the Legal Chatbot using Streamlit.
"""
import os
import streamlit as st
from agents.summarization_agent import summarize_answer
from agents.query_agent import load_index, get_relevant_docs
from dotenv import load_dotenv
MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")

import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Page configuration
st.set_page_config(page_title="🧑‍⚖️ Legal ChatBot", layout="centered")
st.title("🧑‍⚖️ Ask legal questions and get simplified answers")


# Cache the retriever to avoid reloading documents on each query
@st.cache_resource
def get_retriever():
    """
    Load and cache the document retriever
    
    Returns:
        A document retriever object
    """
    try:
        pdf_paths = [
            "data/Guide-to-Litigation-in-India.pdf",
            "data/PDFFile5b28c9ce64e524.54675199.pdf"
        ]
        
        # Check if files exist
        missing_files = [path for path in pdf_paths if not os.path.exists(path)]
        if missing_files:
            st.error(f"❌ Error: The following PDF files are missing: {', '.join(missing_files)}")
            st.stop()
        
        return load_index(pdf_paths)
    except Exception as e:
        logger.error(f"Error in get_retriever: {str(e)}")
        st.error(f"❌ Error loading documents: {str(e)}")
        st.stop()

# Initialize session state for chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Display chat history
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Load the retriever
try:
    retriever = get_retriever()
    st.success("✅ Legal documents loaded and indexed successfully!")
except Exception as e:
    st.error(f"❌ Failed to load documents: {str(e)}")
    st.stop()

# Get user input
query = st.chat_input("Enter your legal question:")

if query:
    # Add user message to chat history
    st.session_state.chat_history.append({"role": "user", "content": query})
    
    # Display user message
    with st.chat_message("user"):
        st.write(query)
    
    # Display assistant response
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        message_placeholder.text("🔍 Searching for relevant information...")
        
        try:
            # Query Agent: Retrieve relevant documents
            docs = get_relevant_docs(query, retriever)
            
            if not docs:
                response = "❓ I couldn't find specific information about that. Could you rephrase your question?"
            else:
                message_placeholder.text("💡 Found relevant information. Generating simplified answer...")
                
                # Summarization Agent: Generate simplified answer
                response = summarize_answer(docs, query)
            
            # Update the message placeholder with the final response
            message_placeholder.write(response)
            
            # Add assistant response to chat history
            st.session_state.chat_history.append({"role": "assistant", "content": response})
            
        except Exception as e:
            logger.error(f"Error processing query: {str(e)}")
            message_placeholder.error(f"❌ Sorry, an error occurred: {str(e)}")
