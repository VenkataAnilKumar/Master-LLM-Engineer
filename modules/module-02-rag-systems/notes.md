# Module 02: RAG Systems

**Duration:** Week 3-4 | **Level:** Intermediate

## 📚 Module Overview

Retrieval-Augmented Generation (RAG) combines LLMs with external knowledge retrieval to provide accurate, up-to-date, and source-attributed responses.

**Learning Objectives:**
- Understand RAG architecture and workflow
- Implement document processing and chunking strategies
- Work with vector databases (FAISS, ChromaDB, Pinecone)
- Build hybrid search (dense + sparse retrieval)
- Optimize retrieval quality and relevance
- Handle multi-modal RAG (text, images, tables)

---

## Table of Contents

1. [Introduction to RAG](#1-introduction-to-rag)
2. [Document Processing & Chunking](#2-document-processing--chunking)
3. [Vector Databases](#3-vector-databases)
4. [Retrieval Strategies](#4-retrieval-strategies)
5. [Advanced RAG Techniques](#5-advanced-rag-techniques)
6. [Evaluation & Optimization](#6-evaluation--optimization)

---

## 1. Introduction to RAG

### What is RAG?

RAG enhances LLM responses by retrieving relevant context from external knowledge bases before generation.

**Traditional LLM:**
```
User Query → LLM → Response
```

**RAG System:**
```
User Query → Retriever → Relevant Docs → LLM + Context → Response
```

### Why RAG?

- **Accuracy:** Ground responses in factual data
- **Up-to-date:** Access current information beyond training cutoff
- **Source Attribution:** Cite sources for credibility
- **Domain-Specific:** Leverage private/proprietary knowledge
- **Reduced Hallucination:** Constrain generation to retrieved context

### RAG Pipeline

```
1. Indexing (Offline)
   Documents → Chunking → Embedding → Vector Store

2. Retrieval (Query Time)
   User Query → Embedding → Search Vector Store → Top-K Docs

3. Generation
   Query + Retrieved Docs → LLM → Response + Citations
```

---

## 2. Document Processing & Chunking

### Document Loaders

```python
from langchain.document_loaders import (
    PyPDFLoader,
    TextLoader,
    UnstructuredMarkdownLoader,
    CSVLoader,
    WebBaseLoader
)

# Load PDF
loader = PyPDFLoader("document.pdf")
documents = loader.load()

# Load from web
loader = WebBaseLoader("https://example.com/article")
docs = loader.load()
```

### Chunking Strategies

#### 1. **Fixed-Size Chunking**
```python
from langchain.text_splitter import RecursiveCharacterTextSplitter

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200,
    separators=["\n\n", "\n", " ", ""]
)

chunks = text_splitter.split_documents(documents)
```

#### 2. **Semantic Chunking**
```python
# Split by meaning, not just size
from langchain.text_splitter import SemanticChunker

chunker = SemanticChunker(embeddings, breakpoint_threshold_amount=75)
chunks = chunker.split_documents(documents)
```

#### 3. **Parent-Child Chunking**
```python
# Store small chunks for retrieval, large chunks for context
from langchain.retrievers import ParentDocumentRetriever

parent_splitter = RecursiveCharacterTextSplitter(chunk_size=2000)
child_splitter = RecursiveCharacterTextSplitter(chunk_size=400)
```

### Best Practices

- **Chunk Size:** 500-1000 tokens (balance retrieval precision vs context)
- **Overlap:** 10-20% to maintain context continuity
- **Metadata:** Include source, page number, timestamps
- **Format:** Preserve headers, code blocks, tables

---

## 3. Vector Databases

### Popular Options

| Database | Type | Best For | Scalability |
|----------|------|----------|-------------|
| FAISS | Local | Prototyping, small datasets | Moderate |
| ChromaDB | Embedded | Development, easy setup | Good |
| Pinecone | Cloud | Production, managed service | Excellent |
| Weaviate | Self-hosted | Advanced search, multi-tenancy | Excellent |
| Qdrant | Cloud/Self-hosted | High performance, filters | Excellent |

### FAISS Implementation

```python
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings

# Create embeddings
embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

# Create vector store
vectorstore = FAISS.from_documents(chunks, embeddings)

# Save for later
vectorstore.save_local("faiss_index")

# Load
loaded_vectorstore = FAISS.load_local("faiss_index", embeddings)

# Search
results = vectorstore.similarity_search("What is RAG?", k=5)
```

### ChromaDB Implementation

```python
import chromadb
from langchain.vectorstores import Chroma

# Initialize client
client = chromadb.Client()

# Create collection
vectorstore = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    collection_name="my_knowledge_base",
    persist_directory="./chroma_db"
)

# Query with metadata filter
results = vectorstore.similarity_search(
    "machine learning",
    k=5,
    filter={"source": "research_papers"}
)
```

### Pinecone Implementation

```python
import pinecone
from langchain.vectorstores import Pinecone

# Initialize
pinecone.init(api_key="your-key", environment="your-env")

# Create index
index_name = "llm-knowledge-base"
pinecone.create_index(name=index_name, dimension=1536, metric="cosine")

# Create vectorstore
vectorstore = Pinecone.from_documents(chunks, embeddings, index_name=index_name)

# Query
results = vectorstore.similarity_search_with_score("RAG systems", k=10)
```

---

## 4. Retrieval Strategies

### Dense Retrieval (Semantic Search)

```python
# Vector similarity search
results = vectorstore.similarity_search(query, k=5)
```

**Pros:** Captures semantic meaning
**Cons:** May miss exact keyword matches

### Sparse Retrieval (BM25)

```python
from langchain.retrievers import BM25Retriever

bm25_retriever = BM25Retriever.from_documents(documents)
results = bm25_retriever.get_relevant_documents("specific keyword")
```

**Pros:** Excellent for keyword/exact matches
**Cons:** Misses semantic similarity

### Hybrid Search (Best of Both)

```python
from langchain.retrievers import EnsembleRetriever

# Combine dense and sparse
dense_retriever = vectorstore.as_retriever(search_kwargs={"k": 10})
sparse_retriever = BM25Retriever.from_documents(documents)

ensemble_retriever = EnsembleRetriever(
    retrievers=[dense_retriever, sparse_retriever],
    weights=[0.5, 0.5]
)

results = ensemble_retriever.get_relevant_documents(query)
```

### MMR (Maximal Marginal Relevance)

```python
# Retrieve diverse, non-redundant results
results = vectorstore.max_marginal_relevance_search(
    query,
    k=5,
    fetch_k=20,
    lambda_mult=0.5  # 0=diversity, 1=relevance
)
```

---

## 5. Advanced RAG Techniques

### Re-ranking

```python
from langchain.retrievers import ContextualCompressionRetriever
from langchain.retrievers.document_compressors import CohereRerank

# First retrieve, then re-rank
base_retriever = vectorstore.as_retriever(search_kwargs={"k": 20})
compressor = CohereRerank(model="rerank-english-v2.0")

compression_retriever = ContextualCompressionRetriever(
    base_compressor=compressor,
    base_retriever=base_retriever
)

results = compression_retriever.get_relevant_documents(query)
```

### Query Expansion

```python
def expand_query(query: str, llm):
    """Generate multiple query variations."""
    prompt = f"""Generate 3 variations of this query that capture different aspects:
    Query: {query}
    
    Variations:
    1."""
    
    response = llm.predict(prompt)
    return [query] + parse_variations(response)

# Search with all variations
all_results = []
for q in expand_query(user_query, llm):
    all_results.extend(vectorstore.similarity_search(q, k=3))
```

### Hypothetical Document Embeddings (HyDE)

```python
def hyde_search(query: str, llm, vectorstore):
    """Generate hypothetical answer, then search."""
    # Step 1: Generate hypothetical answer
    prompt = f"Write a detailed answer to: {query}"
    hypothetical_answer = llm.predict(prompt)
    
    # Step 2: Search using hypothetical answer
    results = vectorstore.similarity_search(hypothetical_answer, k=5)
    return results
```

---

## 6. Evaluation & Optimization

### RAG Metrics

```python
from ragas import evaluate
from ragas.metrics import (
    faithfulness,
    answer_relevancy,
    context_precision,
    context_recall
)

results = evaluate(
    dataset,
    metrics=[faithfulness, answer_relevancy, context_precision, context_recall]
)
```

**Key Metrics:**
- **Faithfulness:** Response grounded in context?
- **Answer Relevancy:** Response addresses query?
- **Context Precision:** Retrieved docs are relevant?
- **Context Recall:** All needed info retrieved?

### Optimization Strategies

1. **Chunk Size Tuning:**
   - Test: 200, 500, 1000, 2000 tokens
   - Measure retrieval precision

2. **Embedding Model Selection:**
   - Compare: OpenAI, Cohere, sentence-transformers
   - Evaluate on domain-specific data

3. **Retrieval Configuration:**
   - Adjust k (number of results)
   - Tune similarity thresholds
   - Optimize hybrid search weights

4. **Context Compression:**
   - Use re-ranking to reduce context
   - Extract only relevant sentences

---

## 🎯 Key Takeaways

1. **RAG** combines retrieval with generation for accurate, sourced responses
2. **Chunking strategy** critically impacts retrieval quality
3. **Vector databases** enable semantic search at scale
4. **Hybrid search** combines semantic + keyword matching
5. **Advanced techniques** (re-ranking, HyDE) improve relevance
6. **Evaluation** with proper metrics ensures quality

---

## 📝 Practice Exercises

See [exercises/](exercises/) for hands-on practice:
1. Build a simple RAG system for a document collection
2. Implement hybrid search and compare with dense-only
3. Optimize chunking strategy for a specific use case
4. Evaluate RAG quality with RAGAS
5. Build a multi-source RAG (PDFs + web + databases)

---

## ➡️ Next Module

Continue to [Module 03: Prompt Engineering](../module-03-prompt-engineering/notes.md)

---

**Questions?** Open an issue or discussion!
