# System Architecture Diagrams

This directory contains architecture diagrams for various components and systems covered in the Master LLM Engineer program.

## Table of Contents

1. [Basic RAG Architecture](#basic-rag-architecture)
2. [Advanced RAG with Hybrid Search](#advanced-rag-with-hybrid-search)
3. [Multi-Agent System](#multi-agent-system)
4. [Production LLM Architecture](#production-llm-architecture)
5. [Multi-Modal RAG](#multi-modal-rag)
6. [Microservices Architecture](#microservices-architecture)

---

## Basic RAG Architecture

Simple RAG pipeline for document question answering.

```mermaid
flowchart TB
    subgraph "Indexing Phase"
        A[Documents] --> B[Document Loader]
        B --> C[Text Splitter]
        C --> D[Embedding Model]
        D --> E[(Vector Store)]
    end
    
    subgraph "Retrieval Phase"
        F[User Query] --> G[Embedding Model]
        G --> H[Similarity Search]
        E --> H
        H --> I[Top-K Documents]
    end
    
    subgraph "Generation Phase"
        I --> J[Prompt Template]
        F --> J
        J --> K[LLM]
        K --> L[Answer]
    end
    
    style A fill:#4CAF50
    style F fill:#2196F3
    style L fill:#FF6B6B
```

**Use Cases:**
- Document Q&A
- Knowledge base search
- Research assistant

**Key Components:**
- Document Loader: Reads various file formats
- Text Splitter: Chunks documents intelligently
- Embedding Model: Converts text to vectors
- Vector Store: FAISS, Chroma, Pinecone
- LLM: GPT-4, Claude, Gemini

---

## Advanced RAG with Hybrid Search

Enhanced RAG with multiple retrieval strategies and re-ranking.

```mermaid
flowchart TB
    A[User Query] --> B[Query Understanding]
    B --> C[Query Expansion]
    
    C --> D[Semantic Search]
    C --> E[Keyword Search BM25]
    
    D --> F[Vector Matches]
    E --> G[Keyword Matches]
    
    F --> H[Hybrid Fusion]
    G --> H
    
    H --> I[Re-ranking Model]
    I --> J[Top-K Relevant Docs]
    
    J --> K[Context Formation]
    A --> K
    
    K --> L[LLM with Context]
    L --> M[Answer + Sources]
    
    M --> N{Feedback}
    N -->|Good| O[Log Success]
    N -->|Bad| P[Log for Improvement]
    
    style A fill:#4CAF50
    style M fill:#FF6B6B
    style I fill:#FFA726
```

**Components:**
1. **Query Understanding**
   - Intent classification
   - Entity extraction
   - Query rewriting

2. **Hybrid Search**
   - Semantic: Vector similarity
   - Keyword: BM25 algorithm
   - Fusion: Reciprocal Rank Fusion

3. **Re-ranking**
   - Cross-encoder models
   - Cohere rerank
   - Custom scoring

4. **Context Formation**
   - Relevant chunk selection
   - Context window management
   - Source tracking

---

## Multi-Agent System

LangChain agent architecture with multiple tools.

```mermaid
flowchart TB
    A[User Input] --> B[Agent Core LLM]
    
    B --> C{Action Decision}
    
    C -->|Tool 1| D[Python REPL]
    C -->|Tool 2| E[Web Search]
    C -->|Tool 3| F[RAG System]
    C -->|Tool 4| G[Calculator]
    C -->|Done| H[Final Answer]
    
    D --> I[Observation]
    E --> I
    F --> I
    G --> I
    
    I --> B
    
    H --> J[Response]
    
    subgraph "Agent Memory"
        K[(Conversation History)]
    end
    
    B <--> K
    
    style A fill:#4CAF50
    style J fill:#FF6B6B
    style B fill:#2196F3
```

**Agent Types:**
- **ReAct:** Reasoning + Acting
- **Function Calling:** Structured tool use
- **Plan-and-Execute:** Multi-step planning

**Tool Examples:**
- Python REPL: Execute code
- Web Search: DuckDuckGo, Google
- RAG: Internal knowledge base
- Calculator: Math operations
- API Calls: External services

---

## Production LLM Architecture

Full-stack production system with monitoring and scaling.

```mermaid
flowchart TB
    subgraph "Client Layer"
        A[Web UI]
        B[Mobile App]
        C[API Clients]
    end
    
    subgraph "Load Balancer"
        D[Nginx/ALB]
    end
    
    A --> D
    B --> D
    C --> D
    
    subgraph "API Layer"
        D --> E[FastAPI Instance 1]
        D --> F[FastAPI Instance 2]
        D --> G[FastAPI Instance N]
    end
    
    subgraph "Application Services"
        E --> H[Auth Service]
        E --> I[RAG Service]
        E --> J[Document Service]
        
        H --> K[(PostgreSQL)]
        I --> L[(Vector DB)]
        J --> M[S3 Storage]
    end
    
    subgraph "Caching Layer"
        E --> N[(Redis)]
        F --> N
        G --> N
    end
    
    subgraph "Background Jobs"
        O[Celery Workers]
        P[Queue - RabbitMQ]
        J --> P
        P --> O
        O --> L
    end
    
    subgraph "External LLM APIs"
        I --> Q[OpenAI]
        I --> R[Claude]
        I --> S[Gemini]
    end
    
    subgraph "Monitoring"
        T[LangSmith]
        U[Prometheus]
        V[Grafana]
        
        E --> T
        E --> U
        U --> V
    end
    
    style A fill:#4CAF50
    style E fill:#2196F3
    style Q fill:#FFC107
```

**Key Features:**
- **Horizontal Scaling:** Multiple API instances
- **Caching:** Redis for frequent queries
- **Async Processing:** Background jobs for heavy tasks
- **Monitoring:** Full observability stack
- **Security:** Authentication, rate limiting
- **High Availability:** Load balancing, redundancy

---

## Multi-Modal RAG

RAG system supporting text, images, and audio.

```mermaid
flowchart TB
    subgraph "Input Processing"
        A[Text Input] --> F[Text Processor]
        B[Image Input] --> G[Vision LLM GPT-4V]
        C[Audio Input] --> H[Whisper STT]
        D[Video Input] --> I[Frame Extractor]
    end
    
    subgraph "Embedding Generation"
        F --> J[Text Embeddings]
        G --> K[Image Embeddings CLIP]
        H --> J
        I --> K
    end
    
    subgraph "Vector Store"
        J --> L[(Multi-Modal Vector DB)]
        K --> L
    end
    
    subgraph "Retrieval"
        M[User Query] --> N[Query Type Detection]
        N --> O[Appropriate Retrieval]
        L --> O
        O --> P[Relevant Content]
    end
    
    subgraph "Generation"
        P --> Q[Multi-Modal LLM]
        M --> Q
        Q --> R[Text Response]
        Q --> S[Image Generation]
    end
    
    style M fill:#4CAF50
    style R fill:#FF6B6B
    style L fill:#FFA726
```

**Capabilities:**
- **Text:** Traditional RAG
- **Images:** Visual question answering
- **Audio:** Transcription and understanding
- **Video:** Frame analysis and summarization

**Models:**
- GPT-4V (Vision)
- Claude 3 (Multi-modal)
- CLIP (Image embeddings)
- Whisper (Speech-to-text)
- DALL-E (Image generation)

---

## Microservices Architecture

Enterprise-scale microservices for LLM applications.

```mermaid
flowchart TB
    subgraph "API Gateway"
        A[Kong/API Gateway]
    end
    
    subgraph "Core Services"
        B[Auth Service]
        C[User Service]
        D[Document Service]
        E[Query Service]
        F[Conversation Service]
    end
    
    A --> B
    A --> C
    A --> D
    A --> E
    A --> F
    
    subgraph "AI Services"
        G[Embedding Service]
        H[LLM Gateway]
        I[Evaluation Service]
    end
    
    E --> G
    E --> H
    
    subgraph "Data Stores"
        J[(PostgreSQL)]
        K[(MongoDB)]
        L[(Vector DB)]
        M[(Redis)]
    end
    
    B --> J
    C --> J
    D --> K
    F --> J
    G --> L
    E --> M
    
    subgraph "Message Queue"
        N[Kafka/RabbitMQ]
    end
    
    D --> N
    N --> G
    
    subgraph "Monitoring & Logging"
        O[ELK Stack]
        P[Prometheus]
        Q[Jaeger Tracing]
    end
    
    B --> O
    C --> O
    D --> O
    E --> O
    F --> O
    
    E --> P
    E --> Q
    
    style A fill:#4CAF50
    style E fill:#2196F3
    style H fill:#FFC107
```

**Service Responsibilities:**
- **Auth Service:** JWT, OAuth, permissions
- **User Service:** User management, profiles
- **Document Service:** Upload, processing, storage
- **Query Service:** RAG orchestration
- **Conversation Service:** Chat history, context
- **Embedding Service:** Vector generation
- **LLM Gateway:** Multi-provider routing
- **Evaluation Service:** Quality metrics

---

## Data Flow Patterns

### 1. Synchronous Query Flow
```mermaid
sequenceDiagram
    participant User
    participant API
    participant RAG
    participant VectorDB
    participant LLM
    
    User->>API: POST /query
    API->>RAG: process_query()
    RAG->>VectorDB: search()
    VectorDB-->>RAG: relevant_docs
    RAG->>LLM: generate(context)
    LLM-->>RAG: response
    RAG-->>API: result
    API-->>User: JSON response
```

### 2. Async Document Processing
```mermaid
sequenceDiagram
    participant User
    participant API
    participant Queue
    participant Worker
    participant VectorDB
    
    User->>API: POST /upload
    API->>Queue: add_job(doc_id)
    API-->>User: 202 Accepted
    Queue->>Worker: process_document
    Worker->>Worker: extract_text()
    Worker->>Worker: chunk_text()
    Worker->>Worker: generate_embeddings()
    Worker->>VectorDB: store_vectors()
    Worker->>API: update_status(complete)
```

### 3. Streaming Response
```mermaid
sequenceDiagram
    participant User
    participant API
    participant LLM
    
    User->>API: POST /query/stream
    API->>LLM: stream_generate()
    loop Streaming
        LLM-->>API: token
        API-->>User: SSE/WebSocket
    end
    LLM-->>API: done
    API-->>User: close stream
```

---

## Design Patterns

### Repository Pattern
```python
class VectorStoreRepository(ABC):
    @abstractmethod
    def add_documents(self, docs: List[Document]) -> List[str]:
        pass
    
    @abstractmethod
    def similarity_search(self, query: str, k: int) -> List[Document]:
        pass

class FAISSRepository(VectorStoreRepository):
    # Implementation
    pass

class PineconeRepository(VectorStoreRepository):
    # Implementation
    pass
```

### Factory Pattern
```python
class LLMFactory:
    @staticmethod
    def create_llm(provider: str, **kwargs) -> BaseLLM:
        if provider == "openai":
            return OpenAILLM(**kwargs)
        elif provider == "anthropic":
            return AnthropicLLM(**kwargs)
        elif provider == "google":
            return GoogleLLM(**kwargs)
        raise ValueError(f"Unknown provider: {provider}")
```

### Strategy Pattern
```python
class RetrievalStrategy(ABC):
    @abstractmethod
    def retrieve(self, query: str) -> List[Document]:
        pass

class SemanticRetrieval(RetrievalStrategy):
    # Vector similarity
    pass

class HybridRetrieval(RetrievalStrategy):
    # Semantic + Keyword
    pass
```

---

## Best Practices

### 1. Scalability
- Use async/await for I/O operations
- Implement caching for frequent queries
- Batch process embeddings
- Use connection pooling

### 2. Reliability
- Implement retry logic with exponential backoff
- Use circuit breakers for external APIs
- Health checks for all services
- Graceful degradation

### 3. Security
- API key rotation
- Rate limiting per user/org
- Input validation and sanitization
- Encrypt sensitive data at rest

### 4. Monitoring
- Log all LLM calls with context
- Track token usage and costs
- Monitor latency percentiles
- Set up alerts for anomalies

---

## Tools for Creating Diagrams

- **Mermaid:** Markdown-based diagrams (used here)
- **Draw.io:** Visual diagram editor
- **Lucidchart:** Professional diagramming
- **PlantUML:** Code-based UML diagrams
- **Excalidraw:** Hand-drawn style diagrams

---

[← Back to Resources](../README.md)
