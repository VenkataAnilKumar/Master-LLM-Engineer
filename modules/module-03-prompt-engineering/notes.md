# Module 03: Prompt Engineering

**Duration:** Week 5 | **Level:** Intermediate

## Key Topics

### 1. Prompt Design Principles
- Clear, specific instructions
- Context and examples (few-shot learning)
- Output format specification
- Constraints and guardrails

### 2. Prompting Techniques
- **Zero-shot:** Direct instruction
- **Few-shot:** Provide examples
- **Chain-of-Thought (CoT):** Step-by-step reasoning
- **Tree of Thoughts:** Explore multiple reasoning paths
- **ReAct:** Reasoning + Action
- **Self-Consistency:** Multiple reasoning paths, majority vote

### 3. Prompt Templates
```python
from langchain import PromptTemplate

template = """You are a {role}. 
Task: {task}
Context: {context}
Format: {format}

Answer:"""

prompt = PromptTemplate(
    input_variables=["role", "task", "context", "format"],
    template=template
)
```

### 4. Prompt Optimization
- A/B testing different formulations
- Iterative refinement based on outputs
- Automated prompt optimization (DSPy, PromptPerfect)

### 5. Common Patterns
- **Summarization:** "Summarize in X words focusing on..."
- **Extraction:** "Extract all {entities} in JSON format"
- **Classification:** "Classify into categories: ..."
- **Translation:** "Translate while preserving tone..."
- **Code Generation:** "Write Python function that..."

## Practice: Build a prompt toolkit with templates for common tasks

➡️ [Next: Module 04](../module-04-langchain-llamaindex/notes.md)
