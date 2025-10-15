# Module 01: LLM Fundamentals

**Duration:** Week 1-2 | **Level:** Beginner to Intermediate

---

## 📚 Module Overview

This module covers the foundational concepts of Large Language Models (LLMs), including transformer architecture, tokenization, embeddings, and how modern LLMs work under the hood.

**Learning Objectives:**
- Understand transformer architecture and attention mechanisms
- Master tokenization and embedding concepts
- Learn about different LLM architectures (GPT, BERT, Claude, Gemini)
- Understand model parameters, context windows, and temperature
- Work with OpenAI, Anthropic, and Google APIs

---

## 📖 Table of Contents

1. [Introduction to LLMs](#1-introduction-to-llms)
2. [Transformer Architecture](#2-transformer-architecture)
3. [Tokenization & Embeddings](#3-tokenization--embeddings)
4. [Popular LLM Models](#4-popular-llm-models)
5. [Working with LLM APIs](#5-working-with-llm-apis)
6. [Key Parameters & Configuration](#6-key-parameters--configuration)
7. [Best Practices](#7-best-practices)

---

## 1. Introduction to LLMs

### What are Large Language Models?

Large Language Models are neural networks trained on massive text corpora to understand and generate human-like text. They are foundation models that can be adapted for various NLP tasks.

**Key Characteristics:**
- **Scale:** Billions to trillions of parameters
- **Pre-training:** Trained on diverse internet text
- **Few-shot Learning:** Can perform tasks with minimal examples
- **Generative:** Can create coherent, contextual text

### Evolution of LLMs

```
2017: Transformer Architecture (Attention is All You Need)
2018: BERT (Bidirectional Encoder Representations)
2019: GPT-2 (1.5B parameters)
2020: GPT-3 (175B parameters)
2022: ChatGPT, InstructGPT
2023: GPT-4, Claude 2, Llama 2, Gemini
2024: Claude 3, GPT-4 Turbo, Gemini Pro
2025: Multi-modal LLMs, Specialized models
```

### Applications

- **Conversational AI:** Chatbots, virtual assistants
- **Content Generation:** Writing, summarization, translation
- **Code Generation:** GitHub Copilot, code completion
- **Question Answering:** RAG systems, knowledge bases
- **Data Analysis:** Insights, reporting

---

## 2. Transformer Architecture

### Core Concepts

The transformer architecture revolutionized NLP by introducing the **attention mechanism**, allowing models to process entire sequences in parallel.

### Key Components

#### 1. **Self-Attention Mechanism**

```
Attention(Q, K, V) = softmax(QK^T / √d_k) * V

Where:
- Q = Query matrix
- K = Key matrix
- V = Value matrix
- d_k = Dimension of key vectors
```

**Purpose:** Allows the model to focus on relevant parts of the input when processing each token.

#### 2. **Multi-Head Attention**

Instead of single attention, use multiple "heads" to capture different aspects:

```python
# Simplified concept
MultiHeadAttention = Concat(head_1, ..., head_h) * W^O

Where each head computes:
head_i = Attention(QW_i^Q, KW_i^K, VW_i^V)
```

#### 3. **Position Encoding**

Since transformers process tokens in parallel, position encoding adds sequence order information:

```python
PE(pos, 2i) = sin(pos / 10000^(2i/d_model))
PE(pos, 2i+1) = cos(pos / 10000^(2i/d_model))
```

#### 4. **Feed-Forward Networks**

After attention, each position passes through a feed-forward network:

```python
FFN(x) = max(0, xW_1 + b_1)W_2 + b_2
```

### Encoder-Decoder Architecture

```
Input → Embedding → Positional Encoding
    ↓
Encoder Stack (N layers)
├── Multi-Head Attention
├── Add & Norm
├── Feed Forward
└── Add & Norm
    ↓
Decoder Stack (N layers)
├── Masked Multi-Head Attention
├── Add & Norm
├── Cross-Attention
├── Add & Norm
├── Feed Forward
└── Add & Norm
    ↓
Output → Linear → Softmax → Predictions
```

### Decoder-Only Models (GPT)

Modern LLMs like GPT use **decoder-only** architecture:

```
Input Tokens
    ↓
Token Embeddings + Position Embeddings
    ↓
Decoder Block 1
├── Masked Self-Attention
├── Layer Norm
├── Feed Forward
└── Layer Norm
    ↓
Decoder Block 2...N (repeated)
    ↓
Final Layer Norm
    ↓
Output Projection
    ↓
Next Token Probabilities
```

---

## 3. Tokenization & Embeddings

### Tokenization

**Definition:** Breaking text into smaller units (tokens) that the model can process.

#### Types of Tokenization

1. **Word-level:** Split by words
   - Example: "Hello world" → ["Hello", "world"]
   - Issue: Large vocabulary, OOV problems

2. **Character-level:** Split into characters
   - Example: "Hello" → ["H", "e", "l", "l", "o"]
   - Issue: Long sequences

3. **Subword Tokenization** (Modern approach)
   - **BPE (Byte Pair Encoding):** GPT models
   - **WordPiece:** BERT models
   - **SentencePiece:** Universal tokenizer

#### Example: GPT Tokenization

```python
from tiktoken import encoding_for_model

enc = encoding_for_model("gpt-4")
tokens = enc.encode("Hello, world!")
# Output: [9906, 11, 1917, 0]

# Decode
text = enc.decode(tokens)
# Output: "Hello, world!"
```

**Key Points:**
- 1 token ≈ 4 characters in English
- 1 token ≈ ¾ of a word
- Special tokens: `<|endoftext|>`, `<|im_start|>`, etc.

### Embeddings

**Definition:** Dense vector representations of tokens in high-dimensional space.

#### Token Embeddings

```python
# Simplified concept
token_id = 1000
embedding_dim = 768
embedding = embedding_matrix[token_id]  # Shape: (768,)
```

**Properties:**
- Captures semantic meaning
- Similar words have similar vectors
- Dimension: 768 (BERT), 1536 (OpenAI), 4096+ (GPT-4)

#### Semantic Similarity

```python
import numpy as np

def cosine_similarity(vec1, vec2):
    return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))

# Example
similarity("king", "queen")  # High similarity
similarity("king", "car")    # Low similarity
```

#### Embedding Models

Popular embedding models:
- **OpenAI:** `text-embedding-3-small`, `text-embedding-3-large`
- **Sentence Transformers:** `all-MiniLM-L6-v2`, `all-mpnet-base-v2`
- **Cohere:** `embed-english-v3.0`
- **Google:** `textembedding-gecko@003`

---

## 4. Popular LLM Models

### GPT Series (OpenAI)

| Model | Parameters | Context Window | Best For |
|-------|-----------|----------------|----------|
| GPT-3.5 Turbo | ~175B | 16K tokens | Fast, cost-effective |
| GPT-4 | ~1.7T | 8K tokens | Complex reasoning |
| GPT-4 Turbo | ~1.7T | 128K tokens | Long documents |
| GPT-4o | ~1.7T | 128K tokens | Multimodal tasks |

**Strengths:**
- Excellent instruction following
- Strong reasoning capabilities
- Wide API ecosystem

**Use Cases:**
- Chatbots, content generation, code assistance

### Claude Series (Anthropic)

| Model | Context Window | Best For |
|-------|----------------|----------|
| Claude 3 Haiku | 200K tokens | Fast, cost-effective |
| Claude 3 Sonnet | 200K tokens | Balanced performance |
| Claude 3 Opus | 200K tokens | Complex reasoning |

**Strengths:**
- Longest context window
- Strong safety alignment
- Excellent long-document understanding

**Use Cases:**
- Document analysis, research, content moderation

### Gemini Series (Google)

| Model | Context Window | Best For |
|-------|----------------|----------|
| Gemini 1.0 Pro | 32K tokens | General tasks |
| Gemini 1.5 Pro | 1M tokens | Massive context |
| Gemini Ultra | TBA | Advanced reasoning |

**Strengths:**
- Multimodal (text, images, video)
- Extremely long context
- Fast inference

**Use Cases:**
- Multimodal applications, video analysis

### Open-Source Models

- **Llama 2/3:** Meta's open models (7B - 70B)
- **Mistral:** High-performance 7B model
- **Falcon:** 40B parameter model
- **MPT:** MosaicML's efficient models

---

## 5. Working with LLM APIs

### OpenAI API

```python
from openai import OpenAI

client = OpenAI(api_key="your-api-key")

response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Explain quantum computing."}
    ],
    temperature=0.7,
    max_tokens=500
)

print(response.choices[0].message.content)
```

### Anthropic API (Claude)

```python
import anthropic

client = anthropic.Anthropic(api_key="your-api-key")

response = client.messages.create(
    model="claude-3-opus-20240229",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": "Explain quantum computing."}
    ]
)

print(response.content[0].text)
```

### Google Gemini API

```python
import google.generativeai as genai

genai.configure(api_key="your-api-key")
model = genai.GenerativeModel('gemini-pro')

response = model.generate_content("Explain quantum computing.")
print(response.text)
```

---

## 6. Key Parameters & Configuration

### Temperature (0.0 - 2.0)

Controls randomness in output generation:

```python
# Temperature = 0 (Deterministic)
response = model.generate(prompt, temperature=0.0)
# Output: Always the same, most probable tokens

# Temperature = 1 (Balanced)
response = model.generate(prompt, temperature=1.0)
# Output: Creative but coherent

# Temperature = 2 (Creative)
response = model.generate(prompt, temperature=2.0)
# Output: Very creative, potentially incoherent
```

**Use Cases:**
- **Low (0-0.3):** Factual Q&A, code generation
- **Medium (0.7-1.0):** General conversation
- **High (1.5-2.0):** Creative writing, brainstorming

### Top-P (Nucleus Sampling)

Alternative to temperature, samples from top probability mass:

```python
# Top-P = 0.1 (Conservative)
response = model.generate(prompt, top_p=0.1)

# Top-P = 0.9 (Diverse)
response = model.generate(prompt, top_p=0.9)
```

### Max Tokens

Maximum length of generated response:

```python
response = model.generate(
    prompt,
    max_tokens=500  # Stop after 500 tokens
)
```

### Frequency & Presence Penalty

Reduce repetition in outputs:

```python
response = client.chat.completions.create(
    model="gpt-4",
    messages=messages,
    frequency_penalty=0.5,  # Penalize frequent tokens
    presence_penalty=0.5    # Penalize repeated topics
)
```

---

## 7. Best Practices

### 1. API Key Security

```python
# ✅ Good
import os
api_key = os.getenv("OPENAI_API_KEY")

# ❌ Bad
api_key = "sk-abc123..."  # Never hardcode!
```

### 2. Error Handling

```python
from openai import OpenAI, OpenAIError

client = OpenAI()

try:
    response = client.chat.completions.create(
        model="gpt-4",
        messages=messages
    )
except OpenAIError as e:
    print(f"API error: {e}")
```

### 3. Rate Limiting

```python
import time
from tenacity import retry, stop_after_attempt, wait_exponential

@retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=2, max=10)
)
def call_llm(prompt):
    return client.chat.completions.create(...)
```

### 4. Cost Optimization

```python
# Use appropriate models
models = {
    "simple": "gpt-3.5-turbo",      # $0.0015/1K tokens
    "complex": "gpt-4",             # $0.03/1K tokens
    "long_context": "gpt-4-turbo"   # $0.01/1K tokens
}

# Estimate costs
def estimate_cost(text, model="gpt-4"):
    tokens = len(enc.encode(text))
    cost_per_1k = 0.03  # GPT-4 input
    return (tokens / 1000) * cost_per_1k
```

### 5. Context Management

```python
def truncate_context(messages, max_tokens=4000):
    """Keep conversation within token limit."""
    total_tokens = sum(count_tokens(m['content']) for m in messages)
    
    while total_tokens > max_tokens and len(messages) > 1:
        messages.pop(1)  # Remove oldest message (keep system)
        total_tokens = sum(count_tokens(m['content']) for m in messages)
    
    return messages
```

---

## 🎯 Key Takeaways

1. **Transformers** use attention mechanisms to process sequences efficiently
2. **Tokenization** breaks text into subword units for model processing
3. **Embeddings** capture semantic meaning in vector space
4. **Different models** excel at different tasks (GPT-4: reasoning, Claude: long context, Gemini: multimodal)
5. **Parameters** like temperature and top-p control output creativity
6. **Best practices** include secure key management, error handling, and cost optimization

---

## 📝 Practice Exercises

See [exercises/](exercises/) folder for hands-on practice:
1. **Exercise 1:** Tokenization experiments
2. **Exercise 2:** Embedding similarity
3. **Exercise 3:** API integration
4. **Exercise 4:** Parameter tuning
5. **Exercise 5:** Multi-model comparison

---

## 📚 Additional Resources

### Papers
- [Attention Is All You Need (2017)](https://arxiv.org/abs/1706.03762)
- [BERT: Pre-training of Deep Bidirectional Transformers (2018)](https://arxiv.org/abs/1810.04805)
- [Language Models are Few-Shot Learners (GPT-3, 2020)](https://arxiv.org/abs/2005.14165)

### Tools
- [OpenAI Tokenizer](https://platform.openai.com/tokenizer)
- [Hugging Face Transformers](https://huggingface.co/transformers/)
- [LangChain Documentation](https://python.langchain.com/)

### Interactive Learning
- [Illustrated Transformer](http://jalammar.github.io/illustrated-transformer/)
- [3Blue1Brown - Neural Networks](https://www.youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi)

---

## ➡️ Next Module

Continue to [Module 02: RAG Systems](../module-02-rag-systems/notes.md) to learn how to build Retrieval-Augmented Generation systems.

---

**Questions?** Open an issue or discussion in the repository!
