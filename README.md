# Multi-Agent System for Legal Document Analysis

## 🧑‍⚖️ Overview

A **multi-agent legal chatbot** that analyzes Indian legal documents and provides simplified, easy-to-understand answers to legal questions. The system uses advanced AI to convert complex legal language into plain, actionable explanations.

---

## 🧠 Multi-Agent System Design

### 📌 Query Agent
- Uses **vector search** to find relevant document sections  
- Implements:
  - Document loading and processing
  - Text chunking (1000 chars with 100 char overlap)
  - Embedding generation using Mistral AI
- Utilizes **Mistral AI embeddings** (`mistral-embed`) for semantic search  
- Returns the **most relevant document chunks** for a given query

### ✨ Summarization Agent
- Extracts key explanations from complex legal topics  
- Converts **legal jargon into plain language**  
- Uses **Mistral Large** (`mistral-large-latest`) to generate simplified answers  
- Preserves **accuracy** while improving **readability**
- Provides structured, step-by-step responses

---

## 🏗️ System Architecture

```plaintext
legal_chatbot/
├── agents/
│   ├── __init__.py
│   ├── query_agent.py            # Handles document retrieval
│   └── summarization_agent.py    # Handles text simplification
├── data/
│   ├── Guide-to-Litigation-in-India.pdf
│   └── PDFFile5b28c9ce64e524.54675199.pdf
├── main.py                       # CLI interface
├── app.py                        # Streamlit web interface
├── requirements.txt              # Dependencies
└── README.md                     # This file
```

### 🔄 Workflow Process

```
User Query → Query Agent → Relevant Documents → Summarization Agent → Simplified Answer
```

---

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Mistral AI API key (required)

### 1. Clone the Repository

```bash
git clone <repository-url>
cd Multi-Agent-System-for-Legal-Document-Analysis
```

### 2. Set Up Environment

#### Get Mistral AI API Key
1. Visit [Mistral AI Console](https://console.mistral.ai/)
2. Sign up/Login to your account
3. Navigate to API Keys section
4. Create a new API key
5. Copy the API key (you'll need it for the next step)

#### Configure Environment Variables
Create a `.env` file in the project root:

```bash
# Create .env file
echo "MISTRAL_API_KEY=your_actual_api_key_here" > .env
```

**⚠️ Important**: Replace `your_actual_api_key_here` with your actual Mistral AI API key.

### 3. Install Dependencies

```bash
# Create virtual environment (recommended)
python -m venv .venv

# Activate virtual environment
# On Windows:
.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 4. Verify Data Files

Ensure the following PDF files are present in the `data/` directory:
- `Guide-to-Litigation-in-India.pdf`
- `PDFFile5b28c9ce64e524.54675199.pdf`

---

## 🎯 Usage

### Option 1: Web Interface (Recommended)

```bash
streamlit run app.py
```

**Features:**
- Modern chat interface
- Message history
- Real-time responses
- Loading indicators

### Option 2: Command Line Interface

```bash
python main.py
```

**Features:**
- Simple text-based interaction
- Type 'exit' to quit
- Direct console output

---

## 💡 Example Usage

### Sample Question
**User asks:** *"What are the steps involved in filing a lawsuit in India?"*

### System Response Workflow

1. **Query Agent** retrieves relevant sections from legal documents
2. **Summarization Agent** converts legal terms into simplified steps:

```
Step 1: Prepare necessary documents
Step 2: File a petition in court  
Step 3: Serve notice to the opposing party
Step 4: Attend hearings and follow court procedures
```

3. **User receives** a clear and concise answer in plain language

---

## 🔧 Configuration

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `MISTRAL_API_KEY` | Your Mistral AI API key | ✅ Yes |

### Model Configuration

The system uses:
- **Embeddings**: `mistral-embed` for document vectorization
- **Text Generation**: `mistral-large-latest` for summarization
- **Temperature**: 0 (for consistent, factual responses)

---

## 💰 Cost Considerations

- **Mistral API** uses usage-based pricing
- **Embeddings** are relatively inexpensive (per token)
- **Text generation** (Mistral Large) costs more per request
- Monitor your usage to avoid unexpected charges

---

## 🛠️ Troubleshooting

### Common Issues

1. **"MISTRAL_API_KEY is not set"**
   - Ensure you've created a `.env` file
   - Verify the API key is correct
   - Restart your terminal/IDE

2. **"PDF files are missing"**
   - Check that PDF files exist in the `data/` directory
   - Verify file names match exactly

3. **Import errors**
   - Ensure all dependencies are installed: `pip install -r requirements.txt`
   - Activate your virtual environment

4. **API rate limits**
   - Mistral AI has rate limits
   - Wait between requests if you hit limits

---

## 📚 Dependencies

- `langchain` - LLM application framework
- `langchain-community` - Community integrations
- `langchain-mistralai` - Mistral AI integration
- `faiss-cpu` - Vector similarity search
- `pypdf` - PDF document processing
- `python-dotenv` - Environment variable management
- `streamlit` - Web interface framework
- `tqdm` - Progress bars

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

---

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 🆘 Support

If you encounter issues:
1. Check the troubleshooting section above
2. Verify your API key is valid
3. Ensure all dependencies are installed
4. Check that PDF files are present in the data directory

