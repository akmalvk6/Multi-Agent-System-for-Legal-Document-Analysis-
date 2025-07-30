"""
Main application module for the Legal Chatbot

This module integrates the Query Agent and Summarization Agent to create
a multi-agent chatbot that answers legal questions.
"""
import os
from legal_chatbot.agents.query_agent import load_index, get_relevant_docs
from legal_chatbot.agents.summarization_agent import summarize_answer
from dotenv import load_dotenv
MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")

import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

def main():
    """
    Main function to run the Legal Chatbot in CLI mode
    """
    try:
        # Welcome message
        print("🧑‍⚖️ Welcome to Legal ChatBot - Ask legal questions and get simplified answers")
        print("Type 'exit' to quit the application\n")
        
        # Load the document index (this could be cached for better performance)
        logger.info("Loading document index...")
        pdf_paths = [
            "data/Guide-to-Litigation-in-India.pdf",
            "/Users/pasha/chatbotlegal/data/PDFFile5b28c9ce64e524.54675199.pdf"
        ]
        
        # Check if files exist and provide helpful message if not
        missing_files = [path for path in pdf_paths if not os.path.exists(path)]
        if missing_files:
            print(f"❌ Error: The following PDF files are missing:")
            for file in missing_files:
                print(f"  - {file}")
            print("\nPlease place the required PDF files in the correct locations and try again.")
            return
        
        # Load the index
        retriever = load_index(pdf_paths)
        print("✅ Documents loaded and indexed successfully!\n")
        
        # Main interaction loop
        while True:
            # Get user query
            query = input("Ask a legal question (or type 'exit' to quit): ")
            
            # Check for exit command
            if query.lower() == 'exit':
                print("\nThank you for using Legal ChatBot. Goodbye!")
                break
            
            # Skip empty queries
            if not query.strip():
                continue
            
            try:
                print("\n🔍 Searching for relevant information...")
                # Query Agent: Retrieve relevant documents
                docs = get_relevant_docs(query, retriever)
                
                if not docs:
                    print("❓ I couldn't find specific information about that. Could you rephrase your question?")
                    continue
                
                print("💡 Found relevant information. Generating simplified answer...")
                
                # Summarization Agent: Generate simplified answer
                answer = summarize_answer(docs, query)
                
                # Display the answer
                print("\n🤖 Simplified Answer:\n")
                print(answer)
                print("\n" + "-"*50 + "\n")
                
            except Exception as e:
                logger.error(f"Error processing query: {str(e)}")
                print(f"❌ Sorry, an error occurred: {str(e)}")
    
    except Exception as e:
        logger.error(f"Error in main function: {str(e)}")
        print(f"❌ An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    main()