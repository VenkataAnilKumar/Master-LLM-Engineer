# Assessment Framework

Comprehensive evaluation framework for the Master LLM Engineer program.

## Overview

This framework provides structured assessments to evaluate your progress throughout the program. Each week includes quizzes, assignments, and project evaluations.

## Assessment Components

| Component | Weight | Description |
|-----------|--------|-------------|
| Weekly Quizzes | 20% | Test theoretical understanding |
| Lab Assignments | 20% | Hands-on coding exercises |
| Project 1 | 10% | Prompt Engineering Toolkit |
| Project 2 | 15% | Multi-Source RAG System |
| Capstone Project | 30% | Enterprise AI Knowledge Assistant |
| Final Assessment | 5% | Comprehensive final quiz |

---

## Weekly Quizzes

### Week 1: LLM Foundations

**Quiz Format:** 20 multiple choice and short answer questions  
**Time Limit:** 30 minutes  
**Passing Score:** 70%

**Sample Questions:**

1. **What is the primary innovation of the Transformer architecture?**
   - a) Recurrent connections
   - b) Self-attention mechanism ✓
   - c) Convolutional layers
   - d) Pooling layers

2. **Explain the purpose of positional encoding in Transformers.**
   - _Answer: Positional encoding adds information about the position of tokens in a sequence since the attention mechanism itself has no inherent notion of order._

3. **If a model has a context window of 8K tokens and uses BPE tokenization, approximately how many words can it process?**
   - a) 2,000 words
   - b) 4,000 words
   - c) 6,000 words ✓
   - d) 8,000 words

4. **What is the relationship between embedding dimensions and model capability?**
   - _Answer: Higher embedding dimensions generally allow the model to capture more nuanced semantic relationships, but also increase computational cost and memory requirements._

5. **Calculate token count:**
   ```
   Text: "The quick brown fox jumps over the lazy dog"
   Using GPT-4 tokenizer, this is approximately:
   a) 8 tokens
   b) 10 tokens ✓
   c) 12 tokens
   d) 15 tokens
   ```

---

### Week 2: Prompt Engineering

**Quiz Format:** 25 questions (15 multiple choice, 10 practical)  
**Time Limit:** 40 minutes  
**Passing Score:** 70%

**Sample Questions:**

1. **What is Chain-of-Thought prompting?**
   - a) Linking multiple prompts together
   - b) Making the model explain its reasoning step-by-step ✓
   - c) Using chains in the prompt
   - d) Sequential API calls

2. **Which temperature setting is best for creative writing tasks?**
   - a) 0.0
   - b) 0.3
   - c) 0.7-0.9 ✓
   - d) 2.0

3. **Write a few-shot prompt for email classification.**
   ```
   Expected format:
   Email: [example 1]
   Category: Spam
   
   Email: [example 2]
   Category: Important
   
   Email: [new email]
   Category: ?
   ```

4. **What is the purpose of the presence_penalty parameter?**
   - _Answer: Presence penalty encourages the model to talk about new topics by penalizing tokens that have already appeared in the text._

5. **Practical: Debug this prompt**
   ```
   Bad prompt: "Tell me about AI"
   
   Improved prompt should:
   - Be specific
   - Provide context
   - Set constraints
   - Specify format
   ```

---

### Week 3: RAG Fundamentals

**Quiz Format:** 20 questions + 1 coding exercise  
**Time Limit:** 45 minutes  
**Passing Score:** 70%

**Sample Questions:**

1. **What are the three main phases of RAG?**
   - _Answer: 1) Indexing (document processing and embedding), 2) Retrieval (finding relevant documents), 3) Generation (creating response with context)_

2. **Why is chunking necessary in RAG systems?**
   - a) To reduce storage costs
   - b) To fit within model context windows ✓
   - c) To improve search speed
   - d) To organize documents

3. **What is the purpose of chunk overlap?**
   - _Answer: Chunk overlap ensures that information spanning chunk boundaries is not lost and provides context continuity._

4. **Calculate optimal chunk size:**
   ```
   Model context: 8K tokens
   Query + prompt: 500 tokens
   Number of retrieved chunks: 5
   Max tokens for generation: 1000 tokens
   
   Maximum chunk size = ?
   Answer: (8000 - 500 - 1000) / 5 = 1,300 tokens per chunk
   ```

5. **Coding Exercise: Implement a simple chunker**
   ```python
   def chunk_text(text: str, chunk_size: int, overlap: int) -> List[str]:
       """
       Split text into chunks with overlap.
       
       Args:
           text: Input text
           chunk_size: Size of each chunk in characters
           overlap: Overlap between chunks in characters
       
       Returns:
           List of text chunks
       """
       # Your implementation here
       pass
   ```

---

### Week 4: Vector Databases

**Quiz Format:** 25 questions  
**Time Limit:** 40 minutes  
**Passing Score:** 70%

**Sample Questions:**

1. **What is the purpose of HNSW indexing?**
   - a) Exact nearest neighbor search
   - b) Approximate nearest neighbor search ✓
   - c) Full-text search
   - d) Graph traversal

2. **Compare FAISS, ChromaDB, and Pinecone:**
   | Feature | FAISS | ChromaDB | Pinecone |
   |---------|-------|----------|----------|
   | Deployment | Local | Local/Cloud | Cloud |
   | Scalability | Medium | Medium | High |
   | Ease of use | Low | High | High |

3. **What is cosine similarity and when should it be used?**
   - _Answer: Cosine similarity measures the cosine of the angle between two vectors, ranging from -1 to 1. It's ideal for comparing document embeddings because it focuses on direction rather than magnitude._

4. **Calculate similarity:**
   ```
   Vector A: [0.5, 0.3, 0.8]
   Vector B: [0.6, 0.4, 0.7]
   
   Cosine similarity = ?
   ```

5. **What is the trade-off in hybrid search?**
   - _Answer: Hybrid search trades increased computational cost for better retrieval quality by combining semantic understanding with exact keyword matching._

---

### Week 5-6: Advanced RAG & LangChain

**Quiz Format:** 30 questions  
**Time Limit:** 50 minutes  
**Passing Score:** 75%

**Sample Questions:**

1. **Explain HyDE (Hypothetical Document Embeddings):**
   - _Answer: HyDE generates a hypothetical answer to the query and uses its embedding for retrieval, improving semantic matching._

2. **What is the difference between LangChain Chains and Agents?**
   - _Answer: Chains follow a predetermined sequence of operations, while Agents can dynamically decide which tools to use based on the input._

3. **Implement a simple LangChain chain:**
   ```python
   from langchain import PromptTemplate, LLMChain
   
   # Create a chain that:
   # 1. Takes a topic as input
   # 2. Generates 3 questions about the topic
   # 3. Answers each question
   
   # Your implementation here
   ```

4. **What are the key components of ReAct agents?**
   - _Answer: Thought (reasoning), Action (tool to use), Observation (result of action)_

5. **When should you use ConversationBufferMemory vs. ConversationSummaryMemory?**
   - _Answer: Use BufferMemory for short conversations when you need complete history. Use SummaryMemory for long conversations to stay within token limits._

---

## Lab Assignments

### Week 1 Assignment: LLM Comparison

**Objective:** Compare responses from different LLM providers

**Requirements:**
- Test same prompt on GPT-4, Claude 3, and Gemini
- Document response quality, latency, and cost
- Analyze token usage
- Submit comparison report

**Evaluation Criteria:**
- [ ] All three models tested (30%)
- [ ] Detailed comparison table (30%)
- [ ] Cost analysis included (20%)
- [ ] Insights and recommendations (20%)

---

### Week 2 Assignment: Prompt Template Library

**Objective:** Create a library of 10 prompt templates

**Requirements:**
- At least 10 different use cases
- Each template with variations
- Test each template
- Document effectiveness

**Templates to include:**
1. Text summarization
2. Code generation
3. Data extraction
4. Question answering
5. Creative writing
6. Translation
7. Classification
8. Sentiment analysis
9. Instruction following
10. Chain-of-thought reasoning

**Evaluation Criteria:**
- [ ] 10+ templates created (40%)
- [ ] Templates are reusable (20%)
- [ ] Tested with examples (20%)
- [ ] Documentation quality (20%)

---

### Week 3 Assignment: RAG System Prototype

**Objective:** Build a basic RAG system from scratch

**Requirements:**
- Document loading and processing
- Chunking implementation
- Embedding generation
- Vector storage
- Basic retrieval
- Response generation

**Evaluation Criteria:**
- [ ] Loads multiple file formats (15%)
- [ ] Implements smart chunking (20%)
- [ ] Embeddings generated correctly (15%)
- [ ] Retrieval works (25%)
- [ ] Response includes sources (15%)
- [ ] Code quality (10%)

---

### Week 4 Assignment: Vector Database Comparison

**Objective:** Implement and compare three vector databases

**Requirements:**
- Implement FAISS, ChromaDB, Pinecone
- Use same dataset for all
- Benchmark performance
- Compare features

**Metrics to measure:**
- Indexing time
- Query latency
- Memory usage
- Retrieval quality (precision@k)
- Ease of implementation

**Evaluation Criteria:**
- [ ] All three DBs implemented (30%)
- [ ] Comprehensive benchmarks (30%)
- [ ] Fair comparison (20%)
- [ ] Recommendations (20%)

---

### Week 5 Assignment: Advanced RAG Features

**Objective:** Enhance RAG with advanced techniques

**Requirements:**
- Implement query expansion
- Add re-ranking
- Implement hybrid search
- Add metadata filtering
- Evaluate improvements

**Evaluation Criteria:**
- [ ] Query expansion working (20%)
- [ ] Re-ranking implemented (20%)
- [ ] Hybrid search functional (25%)
- [ ] Metadata filtering (15%)
- [ ] Evaluation shows improvement (20%)

---

## Project Evaluation Rubrics

### Project 1: Prompt Engineering Toolkit (100 points)

| Criteria | Excellent (90-100) | Good (75-89) | Satisfactory (60-74) | Needs Work (<60) |
|----------|-------------------|--------------|---------------------|------------------|
| **Functionality** (30pts) | All features work perfectly | Minor bugs | Some features incomplete | Major features missing |
| **Code Quality** (25pts) | Clean, documented, modular | Mostly clean | Some issues | Poor quality |
| **Documentation** (20pts) | Comprehensive and clear | Good coverage | Basic docs | Minimal docs |
| **Testing** (15pts) | >80% coverage | 60-80% coverage | 40-60% coverage | <40% coverage |
| **Innovation** (10pts) | Creative features beyond requirements | Some innovation | Meets requirements | Basic implementation |

---

### Project 2: Multi-Source RAG (150 points)

| Criteria | Weight | Excellent | Good | Satisfactory | Needs Work |
|----------|--------|-----------|------|--------------|------------|
| **Multi-format Processing** | 20pts | Handles all formats flawlessly | Most formats work | Basic support | Limited support |
| **RAG Pipeline** | 30pts | Advanced implementation | Solid implementation | Basic working | Incomplete |
| **API Design** | 20pts | Professional, well-documented | Good structure | Functional | Basic |
| **Code Architecture** | 25pts | Excellent design | Good structure | Acceptable | Poor design |
| **Testing & Evaluation** | 20pts | Comprehensive | Good coverage | Basic tests | Minimal |
| **Documentation** | 20pts | Complete and professional | Well documented | Basic docs | Incomplete |
| **Performance** | 15pts | Exceeds targets | Meets targets | Close to targets | Below targets |

---

### Capstone Project: Enterprise AI Assistant (300 points)

| Criteria | Weight | Description |
|----------|--------|-------------|
| **Feature Completeness** | 75pts | All required features implemented and working |
| **System Architecture** | 60pts | Well-designed, scalable, production-ready |
| **Code Quality** | 60pts | Clean, maintainable, well-documented code |
| **Documentation** | 45pts | Comprehensive docs (README, Architecture, API, Deployment) |
| **Testing** | 30pts | >80% coverage, all tests passing |
| **Security** | 20pts | Security best practices implemented |
| **Performance** | 10pts | Meets performance targets |

**Scoring:**
- 270-300: Excellent (A)
- 240-269: Very Good (B+)
- 210-239: Good (B)
- 180-209: Satisfactory (C)
- <180: Needs Improvement

---

## Final Assessment

**Format:** Comprehensive 50-question quiz  
**Time Limit:** 90 minutes  
**Passing Score:** 80%

**Topics Covered:**
- LLM fundamentals (10%)
- Prompt engineering (15%)
- RAG architecture (20%)
- Vector databases (10%)
- LangChain/LlamaIndex (15%)
- Production systems (15%)
- Security & scaling (10%)
- Best practices (5%)

**Question Types:**
- Multiple choice (25 questions)
- Short answer (15 questions)
- Code analysis (5 questions)
- System design (5 questions)

---

## Grading Scale

| Grade | Score Range | Description |
|-------|-------------|-------------|
| A | 90-100% | Excellent - Deep understanding and mastery |
| B+ | 85-89% | Very Good - Strong understanding |
| B | 80-84% | Good - Solid understanding |
| C+ | 75-79% | Satisfactory - Adequate understanding |
| C | 70-74% | Passing - Minimum competency |
| F | <70% | Failing - Needs significant improvement |

---

## Certification Requirements

To earn the Master LLM Engineer certificate:

- [ ] Complete all 10 weeks of curriculum
- [ ] Pass all weekly quizzes (>70%)
- [ ] Submit all lab assignments
- [ ] Complete Project 1 (score >75%)
- [ ] Complete Project 2 (score >75%)
- [ ] Complete Capstone Project (score >75%)
- [ ] Pass Final Assessment (>80%)
- [ ] Overall grade: B (80%) or higher

---

## Self-Assessment Tools

### Knowledge Check Questions

After each module, ask yourself:

1. Can I explain this concept to someone else?
2. Can I implement this from scratch?
3. Do I know when to use this technique?
4. Can I debug issues related to this?
5. Do I understand the trade-offs?

### Skill Progression Matrix

| Skill Level | Description | Actions |
|-------------|-------------|---------|
| **Beginner** | Aware of concept | Read documentation, watch tutorials |
| **Intermediate** | Can use with examples | Implement with guidance, practice |
| **Advanced** | Can implement independently | Build projects, solve problems |
| **Expert** | Can teach and optimize | Mentor others, contribute to field |

---

## Feedback & Improvement

### Weekly Reflection Template

```markdown
## Week X Reflection

### What I Learned
- Key concept 1
- Key concept 2
- Key concept 3

### Challenges Faced
- Challenge 1 and how I overcame it
- Challenge 2 and what I'm still working on

### Questions I Have
1. Question about concept X
2. Question about implementation Y

### Next Steps
- [ ] Practice skill A
- [ ] Review concept B
- [ ] Build mini-project C
```

---

## Additional Resources

### Practice Problems

Access additional practice problems at:
- [LeetCode (AI/ML track)](https://leetcode.com/)
- [HackerRank (AI section)](https://www.hackerrank.com/)
- Custom problem sets in `/assessments/practice/`

### Mock Interviews

Prepare for LLM Engineer interviews:
- System design scenarios
- Coding challenges
- Theoretical questions
- Project walkthroughs

---

## Support

- **Office Hours:** Weekly Q&A sessions
- **Discussion Forum:** Ask questions, share solutions
- **Peer Review:** Exchange feedback on assignments
- **1-on-1 Help:** Available for struggling students

---

[← Back to Main README](../../README.md)
