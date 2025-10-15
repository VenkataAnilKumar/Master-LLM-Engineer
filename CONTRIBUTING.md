# Contributing to Master LLM Engineer

Thank you for your interest in contributing to the Master LLM Engineer program! This document provides guidelines for contributing.

## Ways to Contribute

### 1. Content Improvements
- Fix typos and grammatical errors
- Improve explanations and examples
- Add additional resources and references
- Update outdated information

### 2. Code Examples
- Add working code examples
- Improve existing implementations
- Add test cases
- Optimize performance

### 3. New Content
- Create additional tutorials
- Add video content
- Write blog posts
- Translate content to other languages

### 4. Bug Reports
- Report broken links
- Identify errors in code
- Flag confusing content
- Report technical issues

### 5. Project Solutions
- Share your project implementations (in separate branches)
- Provide alternative approaches
- Create example projects

## Getting Started

### 1. Fork the Repository

Click the "Fork" button at the top right of the repository page.

### 2. Clone Your Fork

```bash
git clone https://github.com/YOUR-USERNAME/Master-LLM-Engineer.git
cd Master-LLM-Engineer
```

### 3. Create a Branch

```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/your-bug-fix
```

### 4. Make Your Changes

Follow the style guidelines below.

### 5. Commit Your Changes

```bash
git add .
git commit -m "Description of your changes"
```

**Commit Message Format:**
```
type: brief description

Detailed explanation if needed.

Fixes #issue-number (if applicable)
```

**Types:**
- `docs`: Documentation changes
- `feat`: New feature or content
- `fix`: Bug fix
- `style`: Formatting changes
- `refactor`: Code restructuring
- `test`: Adding tests
- `chore`: Maintenance tasks

### 6. Push to Your Fork

```bash
git push origin feature/your-feature-name
```

### 7. Create a Pull Request

1. Go to the original repository
2. Click "New Pull Request"
3. Select your fork and branch
4. Fill in the PR template
5. Submit the PR

## Pull Request Guidelines

### PR Title Format
```
[Type] Brief description
```

Examples:
- `[Docs] Fix typo in Week 1 README`
- `[Feat] Add Python async example`
- `[Fix] Correct FAISS implementation`

### PR Description Template

```markdown
## Description
Brief description of your changes.

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Code improvement

## Checklist
- [ ] My code follows the style guidelines
- [ ] I have tested my changes
- [ ] Documentation has been updated
- [ ] No merge conflicts

## Related Issues
Fixes #issue-number
```

## Style Guidelines

### Markdown

- Use proper heading hierarchy (# → ## → ###)
- Include blank lines between sections
- Use code blocks with language specification
- Keep line length reasonable (<120 characters)
- Use bullet points for lists

### Code Examples

```python
# Good: Well-documented, type-hinted, clear
from typing import List

def process_documents(documents: List[str]) -> List[dict]:
    """
    Process a list of documents.
    
    Args:
        documents: List of document texts
        
    Returns:
        List of processed document dictionaries
    """
    results = []
    
    for doc in documents:
        processed = clean_text(doc)
        results.append({"text": processed, "length": len(processed)})
    
    return results
```

```python
# Bad: No documentation, unclear variable names
def proc(d):
    r = []
    for x in d:
        r.append({"t": x.strip(), "l": len(x)})
    return r
```

### Python Code Style

- Follow PEP 8
- Use type hints
- Write docstrings
- Include error handling
- Add comments for complex logic
- Use meaningful variable names

### Documentation

- Be clear and concise
- Include examples
- Provide context
- Link to relevant resources
- Use proper grammar and spelling

## Content Guidelines

### Adding Tutorials

1. Create a new markdown file in appropriate week folder
2. Follow the template structure:
   ```markdown
   # Tutorial Title
   
   ## Overview
   Brief description
   
   ## Prerequisites
   What you need to know
   
   ## Step-by-Step Guide
   Detailed instructions
   
   ## Complete Example
   Full working code
   
   ## Exercises
   Practice problems
   ```

### Adding Code Examples

1. Ensure code is tested and working
2. Include necessary imports
3. Add comments explaining key parts
4. Provide expected output
5. Include error handling

### Adding Resources

1. Verify links are working
2. Provide context for each resource
3. Categorize appropriately
4. Include publication date if relevant

## Review Process

### What We Look For

- **Accuracy**: Information is correct and up-to-date
- **Clarity**: Content is easy to understand
- **Completeness**: No missing steps or information
- **Quality**: Well-written and properly formatted
- **Value**: Adds meaningful content

### Review Timeline

- Initial review: Within 3-5 days
- Feedback provided if changes needed
- Merge after approval from maintainers

## Community Guidelines

### Code of Conduct

- Be respectful and professional
- Welcome newcomers
- Provide constructive feedback
- Focus on the content, not the person
- Help others learn and grow

### Communication

- Use clear, professional language
- Be patient with learners
- Provide helpful feedback
- Ask questions when unsure
- Share knowledge generously

## Project-Specific Guidelines

### Submitting Project Solutions

**Important:** Do not submit complete project solutions to the main branch!

Instead:
1. Create a separate branch: `solutions/your-name/project-X`
2. Add your solution to `examples/` directory
3. Include a disclaimer that this is one possible approach
4. Provide explanation of your design decisions

### Example Structure

```
examples/
└── project-01-solutions/
    └── your-name/
        ├── README.md
        ├── src/
        └── tests/
```

## Recognition

Contributors will be:
- Listed in CONTRIBUTORS.md
- Mentioned in release notes
- Thanked in the community

Top contributors may be invited to:
- Become repository maintainers
- Present in community sessions
- Write official tutorials

## Questions?

- **General Questions**: Open a [GitHub Discussion](../../discussions)
- **Bug Reports**: Create an [Issue](../../issues)
- **Feature Requests**: Create an [Issue](../../issues) with [Feature Request] tag
- **Security Issues**: Email [security@example.com]

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

## Quick Reference

### Common Tasks

**Fix a typo:**
```bash
git checkout -b fix/typo-week-2
# Make changes
git commit -m "fix: correct typo in Week 2 README"
git push origin fix/typo-week-2
# Create PR
```

**Add a code example:**
```bash
git checkout -b feat/add-rag-example
# Add example
git commit -m "feat: add complete RAG implementation example"
git push origin feat/add-rag-example
# Create PR
```

**Update documentation:**
```bash
git checkout -b docs/improve-setup-guide
# Improve documentation
git commit -m "docs: clarify environment setup instructions"
git push origin docs/improve-setup-guide
# Create PR
```

---

Thank you for contributing to Master LLM Engineer! 🚀

Your contributions help make this program better for everyone.

[← Back to Main README](README.md)
