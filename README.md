# Zero-To-GenAI

🚀 Master Generative AI from scratch. A complete beginner's roadmap covering LLMs, Prompt Engineering, RAG, and building your first AI applications with hands-on code examples.

## 📚 Learning Roadmap

### 1. Fundamentals (`01-Fundamentals/`)
- **01_Intro_to_GenAI.ipynb** - Generative vs Discriminative AI, how LLMs work
- **01_Intro_to_Tokens.ipynb** - Tokenization with tiktoken, temperature settings
- Key concepts: tokens, embeddings, context windows

### 2. Prompt Engineering (`02-Prompt-Engineering/`)
- **02_Prompting_Strategies.ipynb** - Complete prompting guide
- Zero-shot and few-shot prompting
- Chain-of-thought prompting
- System prompts for personality control

### 3. API Interactions (`03-API-Interactions/`)
- **start.py** - Basic OpenAI API demo
- **simple_chatbot.py** - CLI chatbot with conversation memory
- **langchain_memory.ipynb** - LangChain memory management
- Managing API keys securely with python-dotenv

### 4. Retrieval-Augmented Generation (`04-RAG/`)
- **04_RAG_Basics.ipynb** - Complete RAG pipeline tutorial
- Document loading, chunking, and embeddings
- Vector storage with ChromaDB
- Building RAG chains with LCEL

### 5. Projects (`05-Projects/`)
- **cli_researcher.py** - AI-powered research assistant CLI tool
- **web_chatbot.py** - Modern web-based chatbot using Streamlit
- Generates structured Markdown research summaries
- Extensible with web search (Tavily/Serper)

### 6. Agents (`06-Agents/`)
- **06_Intro_to_Agents.ipynb** - Building autonomous agents with tools
- Understanding the Think-Act-Observe loop
- Creating custom tools with LangChain

## 🛠️ Setup

### Prerequisites
- Python 3.8+
- An API key from OpenAI or Google AI

### Installation

1. Clone the repository:
```bash
git clone https://github.com/ravindranath-sawane/Zero-To-GenAI.git
cd Zero-To-GenAI
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file (use `.env.example` as template):
```bash
cp .env.example .env
# Then edit .env with your API keys
```

```
OPENAI_API_KEY=your-openai-api-key
GOOGLE_API_KEY=your-google-api-key
```

## 🚀 Quick Start

Run the basic API demo:
```bash
python 03-API-Interactions/start.py
```

Run the interactive chatbot:
```bash
python 03-API-Interactions/simple_chatbot.py
```

Run the research assistant:
```bash
python 05-Projects/cli_researcher.py --topic "Artificial Intelligence"
```

Run the web chatbot:
```bash
streamlit run 05-Projects/web_chatbot.py
```

## 📁 Project Structure

```
Zero-To-GenAI/
├── 01-Fundamentals/
│   ├── 01_Intro_to_GenAI.ipynb      # GenAI concepts & LLM basics
│   └── 01_Intro_to_Tokens.ipynb     # Tokenization & temperature
├── 02-Prompt-Engineering/
│   └── 02_Prompting_Strategies.ipynb # Zero/few-shot, CoT, system prompts
├── 03-API-Interactions/
│   ├── start.py                      # Basic API demo
│   ├── simple_chatbot.py             # CLI chatbot with memory
│   └── langchain_memory.ipynb        # LangChain memory management
├── 04-RAG/
│   ├── 04_RAG_Basics.ipynb           # Complete RAG tutorial
│   └── sample.txt                    # Sample data for RAG demo
├── 05-Projects/
│   ├── cli_researcher.py             # AI research assistant CLI
│   └── web_chatbot.py                # Streamlit web chatbot
├── 06-Agents/
│   └── 06_Intro_to_Agents.ipynb      # Introduction to AI Agents
├── .env.example                       # API key template
├── .env                               # Your API keys (not tracked)
├── .gitignore                         # Git ignore rules
├── requirements.txt                   # Python dependencies
└── README.md                          # This file
```

## 📝 License

This project is open source and available for learning purposes.

## 🤝 Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

