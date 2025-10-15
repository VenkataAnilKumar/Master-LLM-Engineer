# Master LLM Engineer - Assessments

Weekly assessments to validate your learning and progress.

---

## Assessment Overview

| Week | Topic | Format | Duration | Passing | Weight |
|------|-------|--------|----------|---------|--------|
| 1-2 | LLM Fundamentals | MC + Coding | 45 min | 70% | 10% |
| 3-4 | RAG Systems | MC + Coding | 45 min | 70% | 15% |
| 5 | Prompt Engineering | Practical | 30 min | 70% | 10% |
| 6-7 | LangChain & LlamaIndex | Coding | 60 min | 70% | 15% |
| 8 | Backend Development | API Build | 45 min | 70% | 10% |
| 9 | Evaluation | Analysis | 45 min | 70% | 10% |
| 10 | Capstone Project | Final | Week | 70% | 30% |

**Total**: 100% (must achieve ≥70% overall to earn certificate)

---

## Week 1-2: LLM Fundamentals Assessment

### Part A: Multiple Choice (40 points)

1. **Which component allows transformers to process sequences in parallel?**
   - A) Recurrent connections
   - B) Self-attention mechanism ✓
   - C) LSTM cells
   - D) Convolutional layers

2. **What is the approximate ratio of characters to tokens in English text?**
   - A) 1:1
   - B) 2:1
   - C) 4:1 ✓
   - D) 10:1

3. **Which temperature setting produces the most deterministic outputs?**
   - A) 0.0 ✓
   - B) 0.7
   - C) 1.0
   - D) 2.0

[... 7 more questions]

### Part B: Coding Challenge (60 points)

**Task**: Build a multi-model comparison tool

Requirements:
1. Implement functions to call GPT-4, Claude, and Gemini
2. Calculate token usage and cost for each
3. Compare response times
4. Compute semantic similarity between responses
5. Generate comparison report

**Evaluation Criteria:**
- Functionality (30 points)
- Code quality (15 points)
- Error handling (10 points)
- Documentation (5 points)

---

## Week 3-4: RAG Systems Assessment

### Part A: Multiple Choice (30 points)

1. **What is the primary advantage of RAG over fine-tuning?**
   - A) Lower cost
   - B) Up-to-date information ✓
   - C) Faster inference
   - D) Smaller model size

2. **Which retrieval technique combines semantic and keyword search?**
   - A) Dense retrieval
   - B) Sparse retrieval
   - C) Hybrid search ✓
   - D) MMR

[... 8 more questions]

### Part B: Implementation (70 points)

**Task**: Build a RAG system for a document collection

Requirements:
1. Load 10+ documents (PDFs or text)
2. Implement chunking strategy (justify choice)
3. Create vector store (FAISS or ChromaDB)
4. Implement hybrid search
5. Evaluate with RAGAS
6. Document performance metrics

**Evaluation Criteria:**
- RAG implementation (40 points)
- Chunking strategy (10 points)
- Evaluation (10 points)
- Code quality (10 points)

---

## Week 5: Prompt Engineering Assessment

### Practical Prompting Challenge (100 points)

**Task**: Create prompt templates for 5 scenarios

Scenarios:
1. Customer support chatbot
2. Code documentation generator
3. Data extraction from text
4. Creative content writer
5. Math problem solver

For each:
- Design optimal prompt template
- Implement few-shot examples
- Test and refine
- Document effectiveness

**Evaluation:**
- Prompt effectiveness (50 points)
- Template reusability (20 points)
- Few-shot quality (15 points)
- Documentation (15 points)

---

## Week 6-7: LangChain & LlamaIndex Assessment

### Coding Challenge (100 points)

**Task**: Build an agent-based research assistant

Requirements:
1. Create agent with 3+ custom tools:
   - Web search
   - Calculator
   - Document retrieval
2. Implement conversation memory
3. Handle multi-turn conversations
4. Add error recovery
5. Log agent decisions

**Evaluation:**
- Agent functionality (40 points)
- Tool implementation (25 points)
- Memory management (15 points)
- Error handling (10 points)
- Code quality (10 points)

---

## Week 8: Backend Development Assessment

### API Implementation (100 points)

**Task**: Build production-ready RAG API

Requirements:
1. FastAPI with async endpoints
2. Authentication (JWT)
3. Rate limiting
4. Redis caching
5. Streaming responses
6. API documentation

**Evaluation:**
- API functionality (35 points)
- Authentication (15 points)
- Performance features (20 points)
- Error handling (10 points)
- Documentation (10 points)
- Code quality (10 points)

---

## Week 9: Evaluation & Testing Assessment

### Analysis & Implementation (100 points)

**Task**: Evaluate and optimize a RAG system

Given: Pre-built RAG system with known issues

Requirements:
1. Evaluate with RAGAS
2. Identify performance bottlenecks
3. Implement improvements
4. Write unit and integration tests
5. Add monitoring
6. Document findings

**Evaluation:**
- RAGAS implementation (25 points)
- Problem identification (20 points)
- Improvements (25 points)
- Testing (20 points)
- Documentation (10 points)

---

## Week 10: Capstone Project Assessment

### Comprehensive Evaluation (100 points)

See [Capstone Guidelines](../modules/module-07-capstone/project-guidelines.md) for full requirements.

**Scoring Breakdown:**

1. **Functionality (30 points)**
   - All features implemented
   - Works as specified
   - Robust error handling

2. **Code Quality (20 points)**
   - Clean, modular code
   - Best practices followed
   - Well-documented

3. **Architecture (15 points)**
   - Well-designed system
   - Scalable
   - Appropriate tech choices

4. **Testing (10 points)**
   - Unit tests (>80% coverage)
   - Integration tests
   - Evaluation metrics

5. **Security (10 points)**
   - Secure key management
   - Input validation
   - Rate limiting

6. **Documentation (10 points)**
   - Clear README
   - API docs
   - Architecture diagrams

7. **Presentation (5 points)**
   - Demo video quality
   - Slides clarity
   - Communication

---

## Grading Scale

| Score | Grade | Status |
|-------|-------|--------|
| 90-100% | A | Excellent |
| 80-89% | B | Good |
| 70-79% | C | Pass |
| 60-69% | D | Needs Improvement |
| <60% | F | Fail |

---

## Retake Policy

- **Weekly Assessments**: 1 retake allowed within 1 week
- **Projects**: Can resubmit once with feedback applied
- **Capstone**: No retakes (must meet minimum requirements)

---

## Academic Integrity

- All work must be your own
- Collaboration allowed for learning, not for assessments
- Use of AI tools: Allowed for research, not for answers
- Plagiarism results in automatic failure
- Code must be original (cite external libraries/code)

---

## Submission Guidelines

### Format:
- Code: GitHub repository link
- Documentation: Markdown files in repo
- Answers: Submit via assessment platform

### Deadline:
- Weekly assessments: End of respective week
- Projects: 2 weeks after module completion
- Capstone: End of Week 10

### Late Policy:
- -10% per day late (max 3 days)
- After 3 days: 0 points
- Extensions for emergencies (request in advance)

---

## Assessment Schedule

```
Week 1: Setup and learning
Week 2: LLM Fundamentals Assessment
Week 3-4: Learning RAG
Week 4: RAG Systems Assessment
Week 5: Prompt Engineering Assessment
Week 6-7: Learning Frameworks
Week 7: LangChain Assessment
Week 8: Backend Assessment
Week 9: Evaluation Assessment
Week 10: Capstone Submission
Week 11: Capstone Presentation
```

---

## Support During Assessments

- **Questions**: Use discussion board (no solution sharing)
- **Technical Issues**: Report immediately
- **Clarifications**: Allowed, cheating is not
- **Resources**: All course materials + documentation

---

## Certificate Requirements

To earn the **Master LLM Engineer Certificate**:

1. ✅ Pass all weekly assessments (≥70%)
2. ✅ Submit all 3 projects (≥70% each)
3. ✅ Complete capstone project (≥70%)
4. ✅ Overall program score ≥70%
5. ✅ Participate in peer reviews (5+)
6. ✅ Complete exit survey

---

## After Completion

- Certificates issued within 2 weeks
- Digital badge for LinkedIn
- Access to alumni network
- Lifetime access to course materials
- Priority for advanced courses

---

**Good luck with your assessments! Study hard and build amazing things! 🚀**

Questions? Open an issue or discussion.
