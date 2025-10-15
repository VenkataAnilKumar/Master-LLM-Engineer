# Module 05: Backend & LLM API Development

**Duration:** Week 8 | **Level:** Advanced

## FastAPI for LLM Services

### 1. Basic API Structure
```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="LLM API")

class QueryRequest(BaseModel):
    query: str
    model: str = "gpt-4"
    temperature: float = 0.7

class QueryResponse(BaseModel):
    response: str
    model: str
    tokens_used: int

@app.post("/query", response_model=QueryResponse)
async def query_llm(request: QueryRequest):
    # Implementation
    pass
```

### 2. Async Processing
```python
import asyncio
from concurrent.futures import ThreadPoolExecutor

@app.post("/batch-query")
async def batch_query(queries: List[str]):
    tasks = [call_llm_async(q) for q in queries]
    results = await asyncio.gather(*tasks)
    return results
```

### 3. Streaming Responses
```python
from fastapi.responses import StreamingResponse

@app.post("/stream")
async def stream_response(request: QueryRequest):
    async def generate():
        for chunk in llm.stream(request.query):
            yield f"data: {chunk}\n\n"
    
    return StreamingResponse(generate(), media_type="text/event-stream")
```

### 4. Authentication & Rate Limiting
```python
from fastapi.security import HTTPBearer
from slowapi import Limiter

security = HTTPBearer()
limiter = Limiter(key_func=lambda: "user")

@app.post("/query")
@limiter.limit("10/minute")
async def query_llm(request: QueryRequest, token=Depends(security)):
    # Verify token, process request
    pass
```

### 5. Caching
```python
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend

@app.post("/query")
@cache(expire=3600)
async def query_llm(request: QueryRequest):
    # Response cached for 1 hour
    pass
```

### 6. Background Tasks
```python
from fastapi import BackgroundTasks

def log_usage(user_id: str, tokens: int):
    # Log to database
    pass

@app.post("/query")
async def query_llm(request: QueryRequest, background_tasks: BackgroundTasks):
    response = await process_query(request)
    background_tasks.add_task(log_usage, user_id, response.tokens)
    return response
```

## Best Practices

1. **Error Handling:** Comprehensive try-except, user-friendly messages
2. **Validation:** Pydantic models for all inputs
3. **Monitoring:** Prometheus metrics, structured logging
4. **Documentation:** Auto-generated with OpenAPI/Swagger
5. **Testing:** Unit + integration tests with pytest
6. **Deployment:** Docker, Kubernetes, CI/CD

## Practice: Build production-ready RAG API

➡️ [Next: Module 06](../module-06-evaluation/notes.md)
