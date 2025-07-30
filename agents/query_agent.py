"""
Query Agent Module

This module is responsible for fetching relevant sections from legal documents
based on user queries using vector search.
"""
import os
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_mistralai import MistralAIEmbeddings
MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")

import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def load_index(pdf_paths: list):
    """
    Load and index PDF documents for retrieval.
    
    Args:
        pdf_paths: List of paths to PDF documents
        
    Returns:
        A retriever object that can fetch relevant documents
        
    Raises:
        FileNotFoundError: If any of the specified PDF files are not found
    """
    try:
        all_pages = []
        for pdf_path in pdf_paths:
            if not os.path.exists(pdf_path):
                raise FileNotFoundError(f"❌ File not found: {pdf_path}")
            
            logger.info(f"Loading PDF: {pdf_path}")
            loader = PyPDFLoader(pdf_path)
            all_pages.extend(loader.load())
        
        logger.info(f"Loaded {len(all_pages)} pages from {len(pdf_paths)} documents")
        
        # Split documents into chunks
        splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
        chunks = splitter.split_documents(all_pages)
        logger.info(f"Created {len(chunks)} chunks for indexing")
        
        # Fetch MISTRAL_API_KEY from environment
        api_key = os.getenv("MISTRAL_API_KEY")
        if not api_key:
            raise ValueError("❌ MISTRAL_API_KEY is not set in the environment variables.")
        
        # Use Mistral embeddings
        embeddings = MistralAIEmbeddings(model="mistral-embed", api_key=api_key)
        
        # Create vector store
        vectorstore = FAISS.from_documents(chunks, embedding=embeddings)
        logger.info("Vector store created successfully")
        
        return vectorstore.as_retriever()
    
    except Exception as e:
        logger.error(f"Error in load_index: {str(e)}")
        raise

def get_relevant_docs(query: str, retriever):
    """
    Retrieve relevant document chunks based on a query.
    
    Args:
        query: The user's question
        retriever: The retriever object from load_index
        
    Returns:
        List of relevant document chunks
    """
    try:
        logger.info(f"Retrieving documents for query: {query}")
        relevant_docs = retriever.get_relevant_documents(query)
        logger.info(f"Retrieved {len(relevant_docs)} relevant documents")
        return relevant_docs
    
    except Exception as e:
        logger.error(f"Error in get_relevant_docs: {str(e)}")
        raise