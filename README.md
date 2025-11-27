# Zero-To-GenAI

🚀 Master Generative AI from scratch. A complete beginner's roadmap covering LLMs, Prompt Engineering, RAG, and building your first AI applications with hands-on code examples.

## 📚 Learning Roadmap

### 1. Fundamentals (`01-Fundamentals/`)
- Introduction to Generative AI
- Understanding Large Language Models (LLMs)
- Key concepts: tokens, embeddings, transformers
- Setting up your development environment

### 2. Prompt Engineering (`02-Prompt-Engineering/`)
- Basics of prompt design
- Zero-shot and few-shot prompting
- Chain-of-thought prompting
- Best practices and common patterns

### 3. Working with APIs (`03-APIs/`)
- OpenAI API basics
- Google Generative AI (Gemini)
- Managing API keys securely with dotenv
- Building your first AI-powered application

### 4. Retrieval-Augmented Generation (`04-RAG/`)
- Introduction to RAG architecture
- Vector databases and embeddings
- Building a simple RAG pipeline
- Using LangChain for RAG applications

### 5. Projects (`05-Projects/`)
- Hands-on projects to apply your learning
- Building chatbots and assistants
- Document Q&A systems
- Real-world GenAI applications

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

4. Create a `.env` file in the project root:
```
OPENAI_API_KEY=your-openai-api-key
GOOGLE_API_KEY=your-google-api-key
```

## 🚀 Quick Start

Run the basic API demo:
```bash
python 03-APIs/start.py
```

## 📁 Project Structure

```
Zero-To-GenAI/
├── 01-Fundamentals/      # Core GenAI concepts
├── 02-Prompt-Engineering/ # Prompt design techniques
├── 03-APIs/              # API integration examples
│   └── start.py          # Basic API call demo
├── 04-RAG/               # RAG implementations
├── 05-Projects/          # Hands-on projects
├── .env                  # API keys (not tracked)
├── .gitignore            # Git ignore rules
├── requirements.txt      # Python dependencies
└── README.md             # This file
```

## 📝 License

This project is open source and available for learning purposes.

## 🤝 Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.
