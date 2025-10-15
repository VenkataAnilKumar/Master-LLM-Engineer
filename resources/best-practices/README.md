# Industry Best Practices for LLM Applications

Production-grade best practices for building, deploying, and maintaining LLM applications.

## Table of Contents

1. [Security Best Practices](#security-best-practices)
2. [Scaling Strategies](#scaling-strategies)
3. [Monitoring & Observability](#monitoring--observability)
4. [Cost Optimization](#cost-optimization)
5. [Code Quality](#code-quality)
6. [Deployment Strategies](#deployment-strategies)
7. [Performance Optimization](#performance-optimization)

---

## Security Best Practices

### 1. API Key Management

**❌ Bad Practice:**
```python
# Hardcoded API key - NEVER DO THIS
openai_api_key = "sk-proj-abc123..."
```

**✅ Good Practice:**
```python
# Use environment variables
import os
from dotenv import load_dotenv

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

if not openai_api_key:
    raise ValueError("OPENAI_API_KEY not found in environment")
```

**Best Practices:**
- Store keys in environment variables or secret managers
- Use different keys for dev/staging/production
- Rotate keys regularly (every 90 days)
- Never commit `.env` files to git
- Use secret managers (AWS Secrets Manager, Azure Key Vault)

### 2. Input Validation & Sanitization

```python
from pydantic import BaseModel, Field, validator

class QueryRequest(BaseModel):
    query: str = Field(..., min_length=1, max_length=1000)
    top_k: int = Field(default=5, ge=1, le=20)
    
    @validator('query')
    def validate_query(cls, v):
        # Remove potentially harmful characters
        sanitized = v.strip()
        
        # Check for injection attempts
        if any(char in sanitized for char in ['<script>', 'DROP TABLE']):
            raise ValueError("Invalid query content")
        
        return sanitized
```

**Key Points:**
- Always validate input length
- Sanitize user inputs
- Use Pydantic for request validation
- Set reasonable limits

### 3. Prompt Injection Prevention

```python
class PromptGuard:
    INJECTION_PATTERNS = [
        r"ignore previous instructions",
        r"disregard all",
        r"forget everything",
        r"new instructions:",
    ]
    
    def is_safe(self, user_input: str) -> bool:
        """Check for prompt injection attempts"""
        import re
        
        lower_input = user_input.lower()
        
        for pattern in self.INJECTION_PATTERNS:
            if re.search(pattern, lower_input):
                return False
        
        return True
    
    def sanitize(self, user_input: str) -> str:
        """Sanitize user input"""
        # Use clear delimiters
        return f"User query: ```{user_input}```"

# Usage
guard = PromptGuard()

if not guard.is_safe(user_input):
    raise ValueError("Potential prompt injection detected")

safe_prompt = guard.sanitize(user_input)
```

**Best Practices:**
- Use clear delimiters for user inputs
- Implement content filtering
- Log suspicious inputs
- Use system messages to reinforce instructions

### 4. PII Detection & Redaction

```python
import re
from typing import Dict, List

class PIIRedactor:
    def __init__(self):
        self.patterns = {
            'email': r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',
            'phone': r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b',
            'ssn': r'\b\d{3}-\d{2}-\d{4}\b',
            'credit_card': r'\b\d{4}[-\s]?\d{4}[-\s]?\d{4}[-\s]?\d{4}\b'
        }
    
    def detect(self, text: str) -> Dict[str, List[str]]:
        """Detect PII in text"""
        findings = {}
        
        for pii_type, pattern in self.patterns.items():
            matches = re.findall(pattern, text)
            if matches:
                findings[pii_type] = matches
        
        return findings
    
    def redact(self, text: str) -> str:
        """Redact PII from text"""
        redacted = text
        
        for pii_type, pattern in self.patterns.items():
            redacted = re.sub(pattern, f'[{pii_type.upper()}_REDACTED]', redacted)
        
        return redacted

# Usage
redactor = PIIRedactor()

# Check for PII
pii_found = redactor.detect(user_input)
if pii_found:
    logging.warning(f"PII detected: {pii_found.keys()}")

# Redact before sending to LLM
safe_text = redactor.redact(user_input)
```

### 5. Rate Limiting

```python
from fastapi import FastAPI, HTTPException, Request
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded

limiter = Limiter(key_func=get_remote_address)
app = FastAPI()
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

@app.post("/query")
@limiter.limit("10/minute")  # 10 requests per minute
async def query(request: Request, query: QueryRequest):
    # Handle query
    pass

# Organization-level rate limiting
from functools import wraps
from collections import defaultdict
import time

class OrganizationRateLimiter:
    def __init__(self):
        self.requests = defaultdict(list)
    
    def check_limit(self, org_id: str, limit: int, window: int) -> bool:
        """Check if org is within rate limit"""
        now = time.time()
        
        # Clean old requests
        self.requests[org_id] = [
            ts for ts in self.requests[org_id]
            if now - ts < window
        ]
        
        # Check limit
        if len(self.requests[org_id]) >= limit:
            return False
        
        self.requests[org_id].append(now)
        return True
```

### 6. Authentication & Authorization

```python
from fastapi import Depends, HTTPException, Security
from fastapi.security import APIKeyHeader
from jose import JWTError, jwt
from datetime import datetime, timedelta

API_KEY_HEADER = APIKeyHeader(name="X-API-Key")
SECRET_KEY = os.getenv("JWT_SECRET_KEY")
ALGORITHM = "HS256"

def verify_api_key(api_key: str = Security(API_KEY_HEADER)):
    """Verify API key"""
    # Check API key in database
    if not is_valid_api_key(api_key):
        raise HTTPException(status_code=401, detail="Invalid API key")
    
    return api_key

def create_access_token(data: dict, expires_delta: timedelta = None):
    """Create JWT token"""
    to_encode = data.copy()
    
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(hours=1)
    
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    
    return encoded_jwt

def verify_token(token: str):
    """Verify JWT token"""
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

# Role-based access control
def require_role(required_role: str):
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, user=None, **kwargs):
            if user.role != required_role:
                raise HTTPException(status_code=403, detail="Insufficient permissions")
            return await func(*args, user=user, **kwargs)
        return wrapper
    return decorator
```

---

## Scaling Strategies

### 1. Caching

```python
from functools import lru_cache
import hashlib
import redis
import json

class QueryCache:
    def __init__(self, redis_client):
        self.redis = redis_client
        self.ttl = 3600  # 1 hour
    
    def get_cache_key(self, query: str, **params) -> str:
        """Generate cache key"""
        key_data = f"{query}:{json.dumps(params, sort_keys=True)}"
        return hashlib.md5(key_data.encode()).hexdigest()
    
    def get(self, query: str, **params):
        """Get cached result"""
        key = self.get_cache_key(query, **params)
        cached = self.redis.get(key)
        
        if cached:
            return json.loads(cached)
        
        return None
    
    def set(self, query: str, result: dict, **params):
        """Cache result"""
        key = self.get_cache_key(query, **params)
        self.redis.setex(
            key,
            self.ttl,
            json.dumps(result)
        )

# Usage
cache = QueryCache(redis.Redis(host='localhost', port=6379))

@app.post("/query")
async def query(request: QueryRequest):
    # Check cache
    cached_result = cache.get(request.query, top_k=request.top_k)
    if cached_result:
        return cached_result
    
    # Process query
    result = process_query(request)
    
    # Cache result
    cache.set(request.query, result, top_k=request.top_k)
    
    return result
```

### 2. Async/Await for I/O Operations

```python
import asyncio
from typing import List

async def embed_texts_batch(texts: List[str]) -> List[List[float]]:
    """Embed multiple texts in parallel"""
    async with aiohttp.ClientSession() as session:
        tasks = [embed_text(session, text) for text in texts]
        embeddings = await asyncio.gather(*tasks)
    
    return embeddings

async def hybrid_search(query: str):
    """Parallel semantic and keyword search"""
    semantic_task = semantic_search(query)
    keyword_task = keyword_search(query)
    
    semantic_results, keyword_results = await asyncio.gather(
        semantic_task,
        keyword_task
    )
    
    return merge_results(semantic_results, keyword_results)
```

### 3. Background Job Processing

```python
from celery import Celery
from celery.result import AsyncResult

celery_app = Celery('tasks', broker='redis://localhost:6379/0')

@celery_app.task(bind=True)
def process_document(self, document_id: str):
    """Process document in background"""
    try:
        # Update status
        update_status(document_id, "processing")
        
        # Process document
        doc = load_document(document_id)
        chunks = chunk_document(doc)
        embeddings = generate_embeddings(chunks)
        store_in_vector_db(embeddings)
        
        # Update status
        update_status(document_id, "completed")
        
    except Exception as e:
        update_status(document_id, "failed")
        raise

# API endpoint
@app.post("/documents/upload")
async def upload_document(file: UploadFile):
    # Save file
    document_id = save_file(file)
    
    # Queue processing job
    task = process_document.delay(document_id)
    
    return {
        "document_id": document_id,
        "job_id": task.id,
        "status": "queued"
    }
```

### 4. Connection Pooling

```python
from sqlalchemy import create_engine
from sqlalchemy.pool import QueuePool

# Database connection pool
engine = create_engine(
    DATABASE_URL,
    poolclass=QueuePool,
    pool_size=20,
    max_overflow=40,
    pool_pre_ping=True,
    pool_recycle=3600
)

# Redis connection pool
redis_pool = redis.ConnectionPool(
    host='localhost',
    port=6379,
    max_connections=50
)

redis_client = redis.Redis(connection_pool=redis_pool)
```

### 5. Load Balancing

```nginx
# nginx.conf
upstream api_servers {
    least_conn;
    server api1.example.com:8000 weight=1;
    server api2.example.com:8000 weight=1;
    server api3.example.com:8000 weight=1;
}

server {
    listen 80;
    
    location /api/ {
        proxy_pass http://api_servers;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

---

## Monitoring & Observability

### 1. Structured Logging

```python
import logging
import json
from datetime import datetime

class JSONFormatter(logging.Formatter):
    def format(self, record):
        log_data = {
            "timestamp": datetime.utcnow().isoformat(),
            "level": record.levelname,
            "message": record.getMessage(),
            "module": record.module,
            "function": record.funcName,
        }
        
        # Add extra fields
        if hasattr(record, 'user_id'):
            log_data['user_id'] = record.user_id
        
        if hasattr(record, 'request_id'):
            log_data['request_id'] = record.request_id
        
        if record.exc_info:
            log_data['exception'] = self.formatException(record.exc_info)
        
        return json.dumps(log_data)

# Configure logger
logger = logging.getLogger(__name__)
handler = logging.StreamHandler()
handler.setFormatter(JSONFormatter())
logger.addHandler(handler)
logger.setLevel(logging.INFO)

# Usage
logger.info(
    "Query processed",
    extra={
        "user_id": user_id,
        "request_id": request_id,
        "latency_ms": latency,
        "tokens_used": tokens
    }
)
```

### 2. Metrics Collection

```python
from prometheus_client import Counter, Histogram, Gauge
import time

# Define metrics
query_counter = Counter(
    'rag_queries_total',
    'Total number of queries',
    ['status', 'model']
)

query_latency = Histogram(
    'rag_query_latency_seconds',
    'Query latency in seconds',
    ['model']
)

token_usage = Counter(
    'rag_tokens_total',
    'Total tokens used',
    ['model', 'type']
)

active_requests = Gauge(
    'rag_active_requests',
    'Number of active requests'
)

# Usage
@app.post("/query")
async def query(request: QueryRequest):
    active_requests.inc()
    start_time = time.time()
    
    try:
        result = await process_query(request)
        
        # Record metrics
        query_counter.labels(status='success', model=request.model).inc()
        query_latency.labels(model=request.model).observe(time.time() - start_time)
        token_usage.labels(model=request.model, type='prompt').inc(result.prompt_tokens)
        token_usage.labels(model=request.model, type='completion').inc(result.completion_tokens)
        
        return result
        
    except Exception as e:
        query_counter.labels(status='error', model=request.model).inc()
        raise
        
    finally:
        active_requests.dec()
```

### 3. Distributed Tracing

```python
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.jaeger.thrift import JaegerExporter

# Setup tracing
trace.set_tracer_provider(TracerProvider())
jaeger_exporter = JaegerExporter(
    agent_host_name="localhost",
    agent_port=6831,
)

trace.get_tracer_provider().add_span_processor(
    BatchSpanProcessor(jaeger_exporter)
)

tracer = trace.get_tracer(__name__)

# Usage
@app.post("/query")
async def query(request: QueryRequest):
    with tracer.start_as_current_span("query_handler"):
        with tracer.start_as_current_span("retrieval"):
            docs = await retrieve_documents(request.query)
        
        with tracer.start_as_current_span("generation"):
            response = await generate_response(request.query, docs)
        
        return response
```

### 4. LangSmith Integration

```python
from langsmith import Client
from langchain.callbacks import LangChainTracer

langsmith_client = Client()
tracer = LangChainTracer(project_name="production-rag")

# Use with LangChain
chain = create_rag_chain()
result = chain.invoke(
    {"query": query},
    config={"callbacks": [tracer]}
)
```

---

## Cost Optimization

### 1. Model Selection Strategy

```python
class ModelRouter:
    def __init__(self):
        self.models = {
            "simple": {"name": "gpt-3.5-turbo", "cost_per_1k": 0.002},
            "complex": {"name": "gpt-4", "cost_per_1k": 0.03},
            "fast": {"name": "gpt-3.5-turbo-16k", "cost_per_1k": 0.003}
        }
    
    def select_model(self, query: str, complexity_score: float) -> str:
        """Select appropriate model based on query complexity"""
        if complexity_score < 0.3:
            return self.models["simple"]["name"]
        elif complexity_score < 0.7:
            return self.models["fast"]["name"]
        else:
            return self.models["complex"]["name"]
    
    def estimate_query_complexity(self, query: str) -> float:
        """Estimate query complexity (0-1)"""
        factors = {
            "length": min(len(query) / 500, 1.0),
            "questions": query.count("?") * 0.1,
            "keywords": any(kw in query.lower() for kw in [
                "analyze", "compare", "explain in detail"
            ])
        }
        
        return min(sum(factors.values()) / len(factors), 1.0)
```

### 2. Token Optimization

```python
def optimize_context(
    query: str,
    documents: List[str],
    max_tokens: int = 3000
) -> str:
    """Optimize context to fit within token limit"""
    import tiktoken
    
    enc = tiktoken.encoding_for_model("gpt-4")
    
    # Prioritize documents by relevance
    sorted_docs = sorted(documents, key=lambda x: x.relevance_score, reverse=True)
    
    context_parts = []
    current_tokens = len(enc.encode(query))
    
    for doc in sorted_docs:
        doc_tokens = len(enc.encode(doc.content))
        
        if current_tokens + doc_tokens > max_tokens:
            # Truncate document
            remaining_tokens = max_tokens - current_tokens
            if remaining_tokens > 100:  # Minimum useful size
                truncated = enc.decode(enc.encode(doc.content)[:remaining_tokens])
                context_parts.append(truncated)
            break
        
        context_parts.append(doc.content)
        current_tokens += doc_tokens
    
    return "\n\n".join(context_parts)
```

### 3. Caching Strategy

```python
class SmartCache:
    def __init__(self, redis_client):
        self.redis = redis_client
    
    def should_cache(self, query: str, cost: float) -> bool:
        """Decide if query should be cached"""
        # Cache expensive queries
        if cost > 0.01:
            return True
        
        # Cache common queries
        query_frequency = self.get_query_frequency(query)
        if query_frequency > 5:  # Asked more than 5 times
            return True
        
        return False
    
    def get_cache_ttl(self, query: str) -> int:
        """Dynamic TTL based on query frequency"""
        frequency = self.get_query_frequency(query)
        
        if frequency > 100:
            return 86400  # 24 hours
        elif frequency > 10:
            return 3600   # 1 hour
        else:
            return 600    # 10 minutes
```

---

## Code Quality

### 1. Type Hints

```python
from typing import List, Dict, Optional, Union
from dataclasses import dataclass

@dataclass
class Document:
    id: str
    content: str
    metadata: Dict[str, any]
    relevance_score: Optional[float] = None

def retrieve_documents(
    query: str,
    top_k: int = 5,
    filters: Optional[Dict[str, any]] = None
) -> List[Document]:
    """Retrieve relevant documents"""
    pass
```

### 2. Error Handling

```python
from tenacity import retry, stop_after_attempt, wait_exponential

class RAGError(Exception):
    """Base exception for RAG errors"""
    pass

class RetrievalError(RAGError):
    """Retrieval failed"""
    pass

class GenerationError(RAGError):
    """Generation failed"""
    pass

@retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=4, max=10)
)
async def call_llm_with_retry(prompt: str) -> str:
    """Call LLM with automatic retries"""
    try:
        response = await llm.generate(prompt)
        return response
    except Exception as e:
        logger.error(f"LLM call failed: {e}")
        raise GenerationError(f"Failed to generate response: {e}")
```

### 3. Testing

```python
import pytest
from unittest.mock import Mock, patch

@pytest.fixture
def mock_llm():
    llm = Mock()
    llm.generate.return_value = "Test response"
    return llm

@pytest.fixture
def sample_documents():
    return [
        Document(id="1", content="Test content 1", metadata={}),
        Document(id="2", content="Test content 2", metadata={})
    ]

def test_rag_pipeline(mock_llm, sample_documents):
    """Test complete RAG pipeline"""
    rag = RAGSystem(llm=mock_llm)
    
    with patch.object(rag, 'retrieve') as mock_retrieve:
        mock_retrieve.return_value = sample_documents
        
        result = rag.query("test query")
        
        assert result is not None
        assert mock_llm.generate.called
        mock_retrieve.assert_called_once_with("test query")
```

---

## Performance Optimization

### 1. Batch Processing

```python
async def process_documents_batch(documents: List[Document], batch_size: int = 10):
    """Process documents in batches"""
    for i in range(0, len(documents), batch_size):
        batch = documents[i:i + batch_size]
        
        # Process batch in parallel
        tasks = [process_document(doc) for doc in batch]
        await asyncio.gather(*tasks)
        
        # Small delay to avoid rate limits
        await asyncio.sleep(0.1)
```

### 2. Lazy Loading

```python
class LazyVectorStore:
    def __init__(self, index_path: str):
        self.index_path = index_path
        self._index = None
    
    @property
    def index(self):
        """Lazy load index"""
        if self._index is None:
            self._index = faiss.read_index(self.index_path)
        return self._index
```

### 3. Query Optimization

```python
def optimize_vector_search(
    query_embedding: List[float],
    index: faiss.Index,
    initial_k: int = 100,
    final_k: int = 5
) -> List[Document]:
    """Two-stage retrieval for better performance"""
    # Stage 1: Fast approximate search
    distances, indices = index.search(
        query_embedding,
        initial_k
    )
    
    # Stage 2: Precise re-ranking
    candidates = [get_document(idx) for idx in indices[0]]
    reranked = rerank_documents(query, candidates)
    
    return reranked[:final_k]
```

---

[← Back to Resources](../README.md)
