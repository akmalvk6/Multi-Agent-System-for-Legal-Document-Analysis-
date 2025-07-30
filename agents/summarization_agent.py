"""
Summarization Agent Module

This module is responsible for extracting key explanations from complex legal topics
and converting them into plain, easy-to-understand language while preserving accuracy.
"""

import os
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_mistralai import ChatMistralAI
MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def create_summarizer_chain():
    """
    Create a chain for summarizing legal information into simple language.
    
    Returns:
        A LLMChain object configured for legal summarization
    """
    try:
        # Initialize the LLM
        llm = ChatMistralAI(
            model="mistral-large-latest",
            temperature=0,
            max_retries=2,   
              )
        
        # Create the prompt template
        prompt = PromptTemplate(
            input_variables=["context", "question"],
            template="""
            You are a legal assistant AI with two main functions:

            1. Query Agent:
            - Retrieved relevant sections from the Guide to Litigation in India.
            - Extract procedural steps related to lawsuit filing.

            2. Summarization Agent:
            - Convert complex legal terms into simple, easy-to-understand steps.
            - Format the answer like this:

            Query Agent:

            [Relevant legal excerpts and extracted procedural steps]

            Summarization Agent:

            Step 1: [Simple explanation of first step]
            Step 2: [Simple explanation of second step]
            Step 3: [Simple explanation of third step]
            Step 4: [Simple explanation of fourth step]

            Response:
            "[Concise summary in plain language]. Would you like more details on any step?"

            ---

            Example output:

            Query Agent:

            Retrieves relevant sections from the Guide to Litigation in India.

            Extracts procedural steps related to lawsuit filing.

            Summarization Agent:

            Converts legal terms into simple steps:

            Step 1: Prepare necessary documents.

            Step 2: File a petition in court.

            Step 3: Serve notice to the opposing party.

            Step 4: Attend hearings and follow court procedures.

            Response:
            "Filing a lawsuit in India involves preparing legal documents, submitting a petition in court, serving a notice to the opposing party, and attending hearings. Would you like more details on any step?"


            
            Context:
            {context}
            
            Question:
            {question}
            
            Simplified Answer:"""
        )
        
        # Create and return the chain
        summarizer_chain = LLMChain(llm=llm, prompt=prompt)
        logger.info("Summarizer chain created successfully")
        return summarizer_chain
    
    except Exception as e:
        logger.error(f"Error in create_summarizer_chain: {str(e)}")
        raise

def summarize_answer(docs, question):
    """
    Summarize legal information into a simple, understandable answer.
    
    Args:
        docs: List of document chunks retrieved by the Query Agent
        question: The user's original question
        
    Returns:
        A simplified answer to the user's question
    """
    try:
        logger.info(f"Summarizing answer for question: {question}")
        
        # Combine the context from all documents
        combined_context = "\n\n".join(doc.page_content for doc in docs)
        logger.info(f"Combined context length: {len(combined_context)} characters")
        
        # Create the summarizer chain
        summarizer_chain = create_summarizer_chain()
        
        # Generate the response
        response = summarizer_chain.run(context=combined_context, question=question)
        logger.info("Answer summarization completed")
        
        return response
    
    except Exception as e:
        logger.error(f"Error in summarize_answer: {str(e)}")
        raise