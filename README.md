# Multi-Agent System Architecture for Legal Chatbot

## Overview

The system follows a **modular architecture** with a clear separation of concerns between two specialized agents.

---

## 🧠 Multi-Agent System Design

### 📌 Query Agent
- Uses **vector search** to find relevant document sections  
- Implements:
  - Document loading  
  - Text chunking  
  - Embedding generation  
- Utilizes **Mistral AI embeddings** for semantic search  
- Returns the **most relevant document chunks** for a given query

### ✨ Summarization Agent
- Extracts key explanations from complex legal topics  
- Converts **legal jargon into plain language**  
- Uses **Gemini 2.0** to generate simplified answers  
- Preserves **accuracy** while improving **readability**

---

## 🏗️ System Structure

```plaintext
legal_chatbot/
├── agents/
│   ├── __init__.py
│   ├── query_agent.py            # Handles document retrieval
│   └── summarization_agent.py    # Handles text simplification
├── data/
│   ├── Guide-to-Litigation-in-India.pdf
│   └── Legal-Compliance-Corporate-Laws.pdf
├── __init__.py
├── main.py                       # CLI interface
├── app.py                        # Streamlit web interface
└── requirements.txt              # Dependencies

User Query 
   ↓
Query Agent 
   ↓
Relevant Documents 
   ↓
Summarization Agent 
   ↓
Simplified Answer 
   ↓
User


💡 Example Flow
User Asks:

"What are the steps involved in filing a lawsuit in India?"

System Response Workflow:

Query Agent retrieves relevant sections from legal documents

Summarization Agent converts legal terms into simplified steps

User receives a clear and concise answer

