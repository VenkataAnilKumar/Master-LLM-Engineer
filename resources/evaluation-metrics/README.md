# Evaluation Metrics for LLM Applications

Comprehensive guide to measuring and evaluating LLM application performance.

## Table of Contents

1. [RAG Evaluation Metrics](#rag-evaluation-metrics)
2. [LLM Response Quality Metrics](#llm-response-quality-metrics)
3. [Performance Metrics](#performance-metrics)
4. [Cost Metrics](#cost-metrics)
5. [Evaluation Frameworks](#evaluation-frameworks)
6. [Best Practices](#best-practices)

---

## RAG Evaluation Metrics

### 1. Retrieval Metrics

#### Precision
Measures the proportion of retrieved documents that are relevant.

```python
precision = relevant_retrieved / total_retrieved
```

**Example:**
- Retrieved: 10 documents
- Relevant: 7 documents
- Precision = 7/10 = 0.7 (70%)

**Target:** >0.7 for production systems

#### Recall
Measures the proportion of relevant documents that were retrieved.

```python
recall = relevant_retrieved / total_relevant
```

**Example:**
- Total relevant in corpus: 15 documents
- Retrieved relevant: 7 documents
- Recall = 7/15 = 0.47 (47%)

**Target:** >0.6 for production systems

#### F1 Score
Harmonic mean of precision and recall.

```python
f1 = 2 * (precision * recall) / (precision + recall)
```

**Target:** >0.65

#### Mean Reciprocal Rank (MRR)
Measures how high the first relevant document appears.

```python
MRR = 1 / rank_of_first_relevant_doc
```

**Example:**
- First relevant doc at position 3
- MRR = 1/3 = 0.33

**Target:** >0.5

#### NDCG (Normalized Discounted Cumulative Gain)
Measures ranking quality considering position.

```python
def dcg(relevances):
    return sum(rel / log2(i + 2) for i, rel in enumerate(relevances))

ndcg = dcg(retrieved) / dcg(ideal_ranking)
```

**Target:** >0.7

### 2. Retrieval Quality Code Examples

```python
from ragas.metrics import (
    context_precision,
    context_recall,
    context_relevancy
)
from ragas import evaluate

# Prepare evaluation dataset
data = {
    "question": ["What is RAG?", ...],
    "contexts": [[retrieved_docs], ...],
    "ground_truth": ["RAG is...", ...],
}

# Evaluate
results = evaluate(
    data,
    metrics=[
        context_precision,
        context_recall,
        context_relevancy
    ]
)

print(results)
```

---

## LLM Response Quality Metrics

### 1. Faithfulness
Measures if the answer is grounded in the provided context.

**Calculation:**
- Extract claims from answer
- Verify each claim against context
- Faithfulness = verified_claims / total_claims

```python
from ragas.metrics import faithfulness

score = faithfulness.score(
    question="What is the capital of France?",
    answer="Paris is the capital of France",
    contexts=["Paris is the capital and largest city of France"]
)
```

**Target:** >0.85

### 2. Answer Relevancy
Measures how well the answer addresses the question.

**Calculation:**
- Generate questions from the answer
- Measure similarity to original question

```python
from ragas.metrics import answer_relevancy

score = answer_relevancy.score(
    question="What is RAG?",
    answer="RAG stands for Retrieval Augmented Generation...",
    contexts=[...]
)
```

**Target:** >0.8

### 3. Answer Correctness
Compares generated answer to ground truth.

**Combines:**
- Semantic similarity
- Factual overlap

```python
from ragas.metrics import answer_correctness

score = answer_correctness.score(
    question="What is the capital of France?",
    answer="Paris",
    ground_truth="Paris is the capital of France"
)
```

**Target:** >0.75

### 4. Context Relevancy
Measures if retrieved context is relevant to the question.

```python
from ragas.metrics import context_relevancy

score = context_relevancy.score(
    question="What is machine learning?",
    contexts=[
        "Machine learning is a subset of AI...",
        "Python is a programming language..."  # Less relevant
    ]
)
```

**Target:** >0.7

### 5. Hallucination Detection

```python
def detect_hallucination(answer: str, contexts: List[str]) -> float:
    """
    Returns score between 0 (no hallucination) and 1 (complete hallucination)
    """
    # Extract claims from answer
    claims = extract_claims(answer)
    
    # Verify each claim
    verified = 0
    for claim in claims:
        if is_supported_by_context(claim, contexts):
            verified += 1
    
    # Return hallucination rate
    return 1 - (verified / len(claims))
```

**Target:** <0.15 (less than 15% hallucination)

---

## Performance Metrics

### 1. Latency Metrics

#### Response Time Percentiles
```python
import numpy as np

latencies = [...]  # List of response times in seconds

p50 = np.percentile(latencies, 50)  # Median
p95 = np.percentile(latencies, 95)
p99 = np.percentile(latencies, 99)

print(f"P50: {p50:.2f}s")
print(f"P95: {p95:.2f}s")
print(f"P99: {p99:.2f}s")
```

**Targets:**
- P50: <2 seconds
- P95: <3 seconds
- P99: <5 seconds

#### Component Breakdown
```python
metrics = {
    "retrieval_time": 0.5,  # seconds
    "rerank_time": 0.2,
    "llm_time": 1.8,
    "total_time": 2.5
}

# Identify bottlenecks
bottleneck = max(metrics.items(), key=lambda x: x[1])
print(f"Bottleneck: {bottleneck[0]} ({bottleneck[1]}s)")
```

### 2. Throughput Metrics

#### Queries Per Second (QPS)
```python
total_queries = 1000
total_time = 500  # seconds

qps = total_queries / total_time
print(f"QPS: {qps:.2f}")
```

**Target:** >10 QPS for production

#### Concurrent Request Handling
```python
import asyncio
import time

async def measure_concurrent_capacity():
    tasks = []
    for i in range(100):  # 100 concurrent requests
        tasks.append(make_request())
    
    start = time.time()
    results = await asyncio.gather(*tasks)
    duration = time.time() - start
    
    success_rate = sum(1 for r in results if r.success) / len(results)
    
    return {
        "concurrent_requests": 100,
        "duration": duration,
        "success_rate": success_rate
    }
```

**Target:** Handle 50+ concurrent requests

### 3. Resource Utilization

```python
import psutil

def get_resource_metrics():
    return {
        "cpu_percent": psutil.cpu_percent(),
        "memory_mb": psutil.virtual_memory().used / 1024 / 1024,
        "memory_percent": psutil.virtual_memory().percent
    }
```

**Targets:**
- CPU: <70% average
- Memory: <80% of available

---

## Cost Metrics

### 1. Token Usage Tracking

```python
class TokenTracker:
    def __init__(self):
        self.prompt_tokens = 0
        self.completion_tokens = 0
        self.total_tokens = 0
    
    def track(self, response):
        self.prompt_tokens += response.usage.prompt_tokens
        self.completion_tokens += response.usage.completion_tokens
        self.total_tokens += response.usage.total_tokens
    
    def calculate_cost(self, model="gpt-4"):
        prices = {
            "gpt-4": {"prompt": 0.03, "completion": 0.06},
            "gpt-3.5-turbo": {"prompt": 0.0005, "completion": 0.0015}
        }
        
        price = prices.get(model, prices["gpt-3.5-turbo"])
        
        prompt_cost = (self.prompt_tokens / 1000) * price["prompt"]
        completion_cost = (self.completion_tokens / 1000) * price["completion"]
        
        return {
            "prompt_cost": prompt_cost,
            "completion_cost": completion_cost,
            "total_cost": prompt_cost + completion_cost
        }
```

### 2. Cost Per Query

```python
def calculate_cost_per_query(
    prompt_tokens: int,
    completion_tokens: int,
    model: str = "gpt-4"
) -> float:
    """Calculate cost for a single query"""
    
    # Prices per 1K tokens (as of 2024)
    prices = {
        "gpt-4": {"prompt": 0.03, "completion": 0.06},
        "gpt-4-turbo": {"prompt": 0.01, "completion": 0.03},
        "gpt-3.5-turbo": {"prompt": 0.0005, "completion": 0.0015},
        "claude-3-opus": {"prompt": 0.015, "completion": 0.075},
        "claude-3-sonnet": {"prompt": 0.003, "completion": 0.015},
    }
    
    model_price = prices.get(model, prices["gpt-3.5-turbo"])
    
    cost = (
        (prompt_tokens / 1000) * model_price["prompt"] +
        (completion_tokens / 1000) * model_price["completion"]
    )
    
    return cost
```

### 3. Monthly Cost Projection

```python
def project_monthly_cost(
    daily_queries: int,
    avg_prompt_tokens: int,
    avg_completion_tokens: int,
    model: str
) -> dict:
    """Project monthly costs"""
    
    cost_per_query = calculate_cost_per_query(
        avg_prompt_tokens,
        avg_completion_tokens,
        model
    )
    
    daily_cost = cost_per_query * daily_queries
    monthly_cost = daily_cost * 30
    
    return {
        "cost_per_query": cost_per_query,
        "daily_cost": daily_cost,
        "monthly_cost": monthly_cost,
        "queries_per_day": daily_queries
    }

# Example
projection = project_monthly_cost(
    daily_queries=1000,
    avg_prompt_tokens=500,
    avg_completion_tokens=200,
    model="gpt-4"
)

print(f"Monthly cost: ${projection['monthly_cost']:.2f}")
```

---

## Evaluation Frameworks

### 1. RAGAs (RAG Assessment)

```python
from ragas import evaluate
from ragas.metrics import (
    faithfulness,
    answer_relevancy,
    context_relevancy,
    context_precision,
    context_recall
)

# Prepare dataset
data = {
    "question": questions,
    "answer": generated_answers,
    "contexts": retrieved_contexts,
    "ground_truth": reference_answers
}

# Run evaluation
result = evaluate(
    data,
    metrics=[
        faithfulness,
        answer_relevancy,
        context_relevancy,
        context_precision,
        context_recall
    ]
)

print(result)
```

### 2. DeepEval

```python
from deepeval.metrics import AnswerRelevancyMetric, FaithfulnessMetric
from deepeval.test_case import LLMTestCase

# Create test case
test_case = LLMTestCase(
    input="What is RAG?",
    actual_output="RAG is Retrieval Augmented Generation...",
    expected_output="RAG stands for...",
    context=["RAG is a technique..."]
)

# Define metrics
relevancy_metric = AnswerRelevancyMetric(threshold=0.7)
faithfulness_metric = FaithfulnessMetric(threshold=0.8)

# Evaluate
relevancy_metric.measure(test_case)
faithfulness_metric.measure(test_case)

print(f"Relevancy: {relevancy_metric.score}")
print(f"Faithfulness: {faithfulness_metric.score}")
```

### 3. Custom Evaluation Pipeline

```python
class RAGEvaluator:
    def __init__(self, llm, embeddings):
        self.llm = llm
        self.embeddings = embeddings
    
    def evaluate_rag_system(
        self,
        test_queries: List[str],
        ground_truth: List[str],
        rag_system
    ) -> dict:
        """Comprehensive RAG evaluation"""
        
        results = {
            "retrieval_metrics": [],
            "generation_metrics": [],
            "performance_metrics": []
        }
        
        for query, truth in zip(test_queries, ground_truth):
            # Get RAG response
            start_time = time.time()
            response = rag_system.query(query)
            latency = time.time() - start_time
            
            # Retrieval metrics
            retrieval = self.evaluate_retrieval(
                query, response.source_documents
            )
            
            # Generation metrics
            generation = self.evaluate_generation(
                query, response.answer, truth, response.source_documents
            )
            
            # Performance
            performance = {
                "latency": latency,
                "tokens": response.token_usage
            }
            
            results["retrieval_metrics"].append(retrieval)
            results["generation_metrics"].append(generation)
            results["performance_metrics"].append(performance)
        
        # Aggregate
        return self.aggregate_results(results)
    
    def aggregate_results(self, results):
        """Calculate average metrics"""
        return {
            "avg_precision": np.mean([r["precision"] for r in results["retrieval_metrics"]]),
            "avg_recall": np.mean([r["recall"] for r in results["retrieval_metrics"]]),
            "avg_faithfulness": np.mean([r["faithfulness"] for r in results["generation_metrics"]]),
            "avg_relevancy": np.mean([r["relevancy"] for r in results["generation_metrics"]]),
            "avg_latency": np.mean([r["latency"] for r in results["performance_metrics"]]),
            "p95_latency": np.percentile([r["latency"] for r in results["performance_metrics"]], 95)
        }
```

---

## Best Practices

### 1. Create Evaluation Datasets

```python
# evaluation_dataset.json
{
    "test_cases": [
        {
            "id": "001",
            "question": "What is RAG?",
            "ground_truth": "RAG is Retrieval Augmented Generation...",
            "relevant_doc_ids": ["doc_123", "doc_456"],
            "category": "definitions"
        },
        ...
    ]
}
```

### 2. Continuous Evaluation

```python
class ContinuousEvaluator:
    def __init__(self, eval_dataset, rag_system):
        self.eval_dataset = eval_dataset
        self.rag_system = rag_system
        self.history = []
    
    def run_evaluation(self) -> dict:
        """Run evaluation and track over time"""
        
        results = evaluate_system(
            self.rag_system,
            self.eval_dataset
        )
        
        results["timestamp"] = datetime.now()
        self.history.append(results)
        
        # Check for regressions
        if len(self.history) > 1:
            self.check_regression()
        
        return results
    
    def check_regression(self):
        """Alert if metrics degrade"""
        current = self.history[-1]
        previous = self.history[-2]
        
        for metric in ["precision", "faithfulness", "relevancy"]:
            if current[metric] < previous[metric] - 0.1:  # 10% drop
                print(f"⚠️ Regression detected in {metric}")
                print(f"  Previous: {previous[metric]:.2f}")
                print(f"  Current: {current[metric]:.2f}")
```

### 3. A/B Testing

```python
def ab_test_rag_systems(
    system_a,
    system_b,
    test_queries: List[str],
    ground_truth: List[str]
) -> dict:
    """Compare two RAG systems"""
    
    results_a = evaluate_system(system_a, test_queries, ground_truth)
    results_b = evaluate_system(system_b, test_queries, ground_truth)
    
    # Statistical significance test
    from scipy import stats
    
    t_stat, p_value = stats.ttest_ind(
        results_a["scores"],
        results_b["scores"]
    )
    
    winner = "A" if np.mean(results_a["scores"]) > np.mean(results_b["scores"]) else "B"
    significant = p_value < 0.05
    
    return {
        "system_a_avg": np.mean(results_a["scores"]),
        "system_b_avg": np.mean(results_b["scores"]),
        "winner": winner,
        "statistically_significant": significant,
        "p_value": p_value
    }
```

### 4. Real-User Feedback

```python
class FeedbackTracker:
    def __init__(self):
        self.feedback = []
    
    def record_feedback(
        self,
        query_id: str,
        rating: int,  # 1-5 stars
        feedback_text: str = None
    ):
        """Track user feedback"""
        self.feedback.append({
            "query_id": query_id,
            "rating": rating,
            "feedback": feedback_text,
            "timestamp": datetime.now()
        })
    
    def get_satisfaction_score(self) -> float:
        """Calculate average user satisfaction"""
        if not self.feedback:
            return 0.0
        
        return np.mean([f["rating"] for f in self.feedback]) / 5.0
```

---

## Evaluation Dashboard Example

```python
import streamlit as st
import plotly.graph_objects as go

def create_evaluation_dashboard(metrics: dict):
    st.title("RAG System Evaluation Dashboard")
    
    # Metrics overview
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Precision", f"{metrics['precision']:.2f}", 
                 delta=f"{metrics['precision_change']:+.2f}")
    
    with col2:
        st.metric("Faithfulness", f"{metrics['faithfulness']:.2f}",
                 delta=f"{metrics['faithfulness_change']:+.2f}")
    
    with col3:
        st.metric("Avg Latency", f"{metrics['avg_latency']:.2f}s",
                 delta=f"{metrics['latency_change']:+.2f}s", delta_color="inverse")
    
    with col4:
        st.metric("Cost/Query", f"${metrics['cost_per_query']:.4f}",
                 delta=f"${metrics['cost_change']:+.4f}", delta_color="inverse")
    
    # Detailed charts
    st.subheader("Metrics Over Time")
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=metrics['timestamps'],
        y=metrics['precision_history'],
        name="Precision"
    ))
    fig.add_trace(go.Scatter(
        x=metrics['timestamps'],
        y=metrics['faithfulness_history'],
        name="Faithfulness"
    ))
    
    st.plotly_chart(fig)
```

---

## Summary Table

| Metric | Target | Good | Needs Improvement |
|--------|--------|------|-------------------|
| Precision | >0.7 | >0.75 | <0.6 |
| Recall | >0.6 | >0.7 | <0.5 |
| Faithfulness | >0.85 | >0.9 | <0.8 |
| Relevancy | >0.8 | >0.85 | <0.75 |
| Latency (P95) | <3s | <2s | >5s |
| Cost per Query | <$0.05 | <$0.02 | >$0.10 |
| User Satisfaction | >4.0/5 | >4.5/5 | <3.5/5 |

---

[← Back to Resources](../README.md)
