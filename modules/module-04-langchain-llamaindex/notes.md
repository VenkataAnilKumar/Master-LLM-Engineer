# Module 04: LangChain & LlamaIndex

**Duration:** Week 6-7 | **Level:** Intermediate to Advanced

## LangChain Core Concepts

### 1. Components
- **Models:** LLM wrappers (OpenAI, Claude, etc.)
- **Prompts:** Template management
- **Chains:** Link components sequentially
- **Agents:** Dynamic decision-making
- **Memory:** Conversation state
- **Callbacks:** Monitoring and logging

### 2. Building Chains
```python
from langchain.chains import LLMChain, SequentialChain

# Simple chain
chain = LLMChain(llm=llm, prompt=prompt)

# Sequential chain
chain = SequentialChain(
    chains=[chain1, chain2, chain3],
    input_variables=["input"],
    output_variables=["output"]
)
```

### 3. Agents
```python
from langchain.agents import create_openai_functions_agent, Tool

tools = [
    Tool(name="Search", func=search_func),
    Tool(name="Calculator", func=calc_func)
]

agent = create_openai_functions_agent(llm=llm, tools=tools)
```

## LlamaIndex Overview

### 1. Data Connectors
- Load from 100+ data sources
- Supports PDFs, APIs, databases, cloud storage

### 2. Indexing
```python
from llama_index import VectorStoreIndex, SimpleDirectoryReader

documents = SimpleDirectoryReader('data').load_data()
index = VectorStoreIndex.from_documents(documents)
```

### 3. Query Engine
```python
query_engine = index.as_query_engine()
response = query_engine.query("What is the revenue?")
```

### 4. Advanced Features
- **Sub-question queries:** Break complex questions
- **Multi-document agents:** Route to appropriate docs
- **Query transformations:** Optimize retrieval

## Comparison

| Feature | LangChain | LlamaIndex |
|---------|-----------|------------|
| Focus | General LLM orchestration | Document indexing/querying |
| Agents | Strong | Moderate |
| RAG | Good | Excellent |
| Learning Curve | Moderate | Easier |
| Use Case | Complex workflows | Knowledge base QA |

## Practice: Build an agent-based research assistant

➡️ [Next: Module 05](../module-05-backend-llm-api/notes.md)
