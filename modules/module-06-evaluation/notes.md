# Module 06: Evaluation & Testing

**Duration:** Week 9 | **Level:** Advanced

## Evaluation Frameworks

### 1. RAGAS (RAG Assessment)
```python
from ragas import evaluate
from ragas.metrics import (
    faithfulness,
    answer_relevancy,
    context_precision,
    context_recall,
    answer_similarity,
    answer_correctness
)

results = evaluate(
    dataset=test_dataset,
    metrics=[
        faithfulness,
        answer_relevancy,
        context_precision,
        context_recall
    ]
)

print(results.to_pandas())
```

### 2. DeepEval
```python
from deepeval import evaluate
from deepeval.metrics import AnswerRelevancyMetric, FaithfulnessMetric
from deepeval.test_case import LLMTestCase

test_case = LLMTestCase(
    input="What is machine learning?",
    actual_output=model_response,
    expected_output=reference_answer,
    retrieval_context=retrieved_docs
)

metric = AnswerRelevancyMetric(threshold=0.7)
evaluate([test_case], [metric])
```

### 3. LangSmith
```python
from langsmith import Client

client = Client()

# Log runs
with client.start_run(name="rag-query") as run:
    response = rag_chain.invoke(query)
    run.log_outputs({"response": response})
    run.log_metrics({"latency": latency, "tokens": tokens})
```

## Key Metrics

### RAG-Specific
- **Faithfulness:** 0-1, response grounded in context
- **Answer Relevancy:** 0-1, addresses the query
- **Context Precision:** Relevant docs in top-k
- **Context Recall:** All needed info retrieved

### General LLM
- **BLEU/ROUGE:** Lexical overlap with reference
- **BERTScore:** Semantic similarity
- **Perplexity:** Language model quality

### Performance
- **Latency:** P50, P95, P99 response times
- **Throughput:** Queries per second
- **Token Usage:** Input + output tokens
- **Cost:** $ per query

## Testing Strategies

### 1. Unit Tests
```python
import pytest

def test_retriever():
    retriever = build_retriever()
    results = retriever.get_relevant_documents("test query")
    assert len(results) > 0
    assert "expected_keyword" in results[0].page_content
```

### 2. Integration Tests
```python
def test_rag_pipeline():
    query = "What is RAG?"
    response = rag_system.query(query)
    assert response is not None
    assert len(response) > 50
    assert "retrieval" in response.lower()
```

### 3. A/B Testing
```python
def ab_test_prompts(test_queries, prompt_a, prompt_b, eval_func):
    results_a = [eval_func(llm.predict(prompt_a.format(q=q))) for q in test_queries]
    results_b = [eval_func(llm.predict(prompt_b.format(q=q))) for q in test_queries]
    
    print(f"Prompt A avg score: {np.mean(results_a)}")
    print(f"Prompt B avg score: {np.mean(results_b)}")
```

### 4. Regression Testing
```python
# golden_dataset.json contains expected outputs
def test_regression():
    with open("golden_dataset.json") as f:
        test_cases = json.load(f)
    
    for case in test_cases:
        output = system.process(case["input"])
        similarity = compute_similarity(output, case["expected"])
        assert similarity > 0.8, f"Regression on: {case['input']}"
```

## Monitoring in Production

### 1. Metrics Collection
```python
from prometheus_client import Counter, Histogram

query_counter = Counter('llm_queries_total', 'Total queries')
latency_histogram = Histogram('llm_latency_seconds', 'Query latency')

@latency_histogram.time()
def process_query(query):
    query_counter.inc()
    return llm.predict(query)
```

### 2. Alerting
- Latency > P95 threshold
- Error rate > 1%
- Cost anomalies
- Quality score drop

## Practice: Build comprehensive evaluation pipeline

➡️ [Next: Module 07](../module-07-capstone/project-guidelines.md)
