# 🛠️ Environment Setup Guide

This guide will help you set up your development environment for the Master LLM Engineer program.

## Prerequisites

### System Requirements
- **Operating System:** Windows 10/11, macOS 10.15+, or Linux (Ubuntu 20.04+)
- **RAM:** Minimum 8GB (16GB recommended)
- **Storage:** 20GB free space
- **Internet:** Stable connection for API calls

### Required Software
- **Python:** 3.10 or higher ([Download](https://www.python.org/downloads/))
- **Git:** Latest version ([Download](https://git-scm.com/downloads))
- **VS Code:** Recommended IDE ([Download](https://code.visualstudio.com/))

## Step 1: Clone the Repository

```bash
git clone https://github.com/VenkataAnilKumar/Master-LLM-Engineer.git
cd Master-LLM-Engineer
```

## Step 2: Python Environment Setup

### Option A: Using venv (Recommended)

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### Option B: Using conda

```bash
# Create conda environment
conda create -n llm-engineer python=3.11
conda activate llm-engineer
```

## Step 3: Install Dependencies

```bash
# Upgrade pip
pip install --upgrade pip

# Install core dependencies
pip install -r requirements.txt

# Install development dependencies (optional)
pip install -r requirements-dev.txt
```

## Step 4: API Keys Setup

### Required API Keys

1. **OpenAI API Key** (Required)
   - Sign up at [OpenAI Platform](https://platform.openai.com/)
   - Navigate to API Keys section
   - Create new key

2. **Anthropic API Key** (Optional but recommended)
   - Sign up at [Anthropic Console](https://console.anthropic.com/)
   - Generate API key

3. **Google AI API Key** (Optional)
   - Sign up at [Google AI Studio](https://makersuite.google.com/)
   - Create API key

4. **Pinecone API Key** (For Week 4)
   - Sign up at [Pinecone](https://www.pinecone.io/)
   - Create free tier account
   - Get API key and environment

### Configure Environment Variables

```bash
# Copy the example environment file
cp .env.example .env

# Edit .env with your API keys
# On Windows:
notepad .env
# On macOS/Linux:
nano .env
```

Add your API keys to `.env`:

```env
# OpenAI
OPENAI_API_KEY=sk-...

# Anthropic
ANTHROPIC_API_KEY=sk-ant-...

# Google
GOOGLE_API_KEY=...

# Pinecone
PINECONE_API_KEY=...
PINECONE_ENVIRONMENT=...

# Optional: LangSmith (for monitoring)
LANGCHAIN_API_KEY=...
LANGCHAIN_TRACING_V2=true
LANGCHAIN_PROJECT=master-llm-engineer
```

## Step 5: VS Code Setup (Recommended)

### Install Extensions

```bash
# Install via VS Code or command line
code --install-extension ms-python.python
code --install-extension ms-python.vscode-pylance
code --install-extension ms-toolsai.jupyter
code --install-extension GitHub.copilot
code --install-extension ms-azuretools.vscode-docker
```

### Configure VS Code

1. Open the repository folder in VS Code
2. Select Python interpreter: `Ctrl+Shift+P` → "Python: Select Interpreter" → Choose your venv
3. Enable auto-save: File → Auto Save

## Step 6: Verify Installation

Run the verification script:

```bash
python verify_setup.py
```

Expected output:
```
✅ Python version: 3.11.x
✅ All required packages installed
✅ OpenAI API key configured
✅ Environment setup complete!
```

## Step 7: Test Your First LLM Call

```python
# test_api.py
from openai import OpenAI

client = OpenAI()

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Hello, world!"}]
)

print(response.choices[0].message.content)
```

Run:
```bash
python test_api.py
```

## Package Overview

### Core Dependencies
- `openai>=1.12.0` - OpenAI API client
- `anthropic>=0.18.0` - Claude API client
- `google-generativeai>=0.3.0` - Gemini API client
- `langchain>=0.1.0` - LLM framework
- `langchain-openai` - LangChain OpenAI integration
- `langchain-community` - Community integrations
- `llama-index>=0.10.0` - Data framework for LLMs
- `chromadb>=0.4.0` - Vector database
- `faiss-cpu>=1.7.4` - Facebook AI similarity search
- `pinecone-client>=3.0.0` - Pinecone vector DB client

### Data Processing
- `pypdf2>=3.0.0` - PDF processing
- `python-docx>=1.0.0` - DOCX processing
- `pandas>=2.0.0` - Data manipulation
- `numpy>=1.24.0` - Numerical computing

### Web & API
- `fastapi>=0.109.0` - Web framework
- `uvicorn>=0.27.0` - ASGI server
- `streamlit>=1.31.0` - UI framework
- `requests>=2.31.0` - HTTP library
- `httpx>=0.26.0` - Async HTTP client

### Utilities
- `python-dotenv>=1.0.0` - Environment variables
- `pydantic>=2.0.0` - Data validation
- `tiktoken>=0.6.0` - Token counting
- `tenacity>=8.2.0` - Retry logic

### Development Tools
- `pytest>=8.0.0` - Testing framework
- `black>=24.0.0` - Code formatter
- `ruff>=0.2.0` - Linter
- `jupyter>=1.0.0` - Notebooks

## Troubleshooting

### Issue: "ModuleNotFoundError"
```bash
# Ensure virtual environment is activated
# Reinstall dependencies
pip install -r requirements.txt
```

### Issue: "API key not found"
```bash
# Verify .env file exists and contains keys
cat .env  # Linux/macOS
type .env  # Windows

# Ensure python-dotenv is installed
pip install python-dotenv
```

### Issue: "SSL Certificate Error"
```bash
# Update certificates
pip install --upgrade certifi
```

### Issue: "Slow API responses"
- Check internet connection
- Verify API rate limits
- Consider using gpt-3.5-turbo for testing

## Optional: Docker Setup

For containerized development:

```bash
# Build Docker image
docker build -t llm-engineer .

# Run container
docker run -it --env-file .env llm-engineer
```

## Next Steps

1. ✅ Verify all installations complete
2. ✅ Test API connectivity
3. ✅ Read through Week 1 materials
4. 🚀 Start [Week 1: LLM Foundations](week-01-llm-foundations/README.md)

## Support

- **Issues:** [GitHub Issues](https://github.com/VenkataAnilKumar/Master-LLM-Engineer/issues)
- **Discussions:** [GitHub Discussions](https://github.com/VenkataAnilKumar/Master-LLM-Engineer/discussions)
- **Discord:** [Join Community](#)

---

[← Back to README](README.md) | [Start Week 1 →](week-01-llm-foundations/README.md)
