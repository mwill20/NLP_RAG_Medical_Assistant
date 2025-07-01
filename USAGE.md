# NLP RAG Medical Assistant - Usage Guide

This guide provides detailed instructions on how to use the NLP RAG Medical Assistant, including setup, configuration, and example queries.

## Table of Contents

- [Quick Start](#quick-start)
- [Detailed Usage](#detailed-usage)
  - [Loading the Knowledge Base](#loading-the-knowledge-base)
  - [Asking Questions](#asking-questions)
  - [Advanced Configuration](#advanced-configuration)
- [Example Queries](#example-queries)
- [Troubleshooting](#troubleshooting)
- [FAQs](#faqs)

## Quick Start

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Launch Jupyter Notebook**
   ```bash
   jupyter notebook
   ```

3. **Open and Run the Notebook**
   - Open `NLP_RAG_Project.ipynb`
   - Run all cells (Kernel > Restart & Run All)

4. **Start Querying**
   - Use the provided functions to ask medical questions
   - View and analyze the responses

## Detailed Usage

### Loading the Knowledge Base

The system uses the Merck Manual as its primary knowledge source. The notebook includes code to:

1. Load the PDF document
2. Process and chunk the content
3. Create embeddings
4. Set up the vector store

```python
# Example: Loading the knowledge base
from document_processor import load_and_process_documents

# Initialize the document processor
docs = load_and_process_documents("path/to/merck_manual.pdf")
```

### Asking Questions

Use the `get_medical_response` function to ask questions:

```python
from assistant import get_medical_response

# Ask a medical question
question = "What are the symptoms of diabetes?"
response = get_medical_response(question)
print(response)
```

### Advanced Configuration

You can customize various parameters for the RAG system:

```python
response = get_medical_response(
    question="What is the treatment for hypertension?",
    temperature=0.7,       # Controls randomness (0.0 to 1.0)
    max_tokens=500,       # Maximum length of the response
    top_k=50,             # Number of documents to retrieve
    top_p=0.95,           # Nucleus sampling parameter
    system_prompt=SYSTEM_PROMPT  # Custom system prompt
)
```

## Example Queries

### Diagnostic Questions
- "What are the common symptoms of myocardial infarction?"
- "How is rheumatoid arthritis diagnosed?"
- "What are the differential diagnoses for chronic fatigue?"

### Treatment Information
- "What are the first-line treatments for type 2 diabetes?"
- "What are the surgical options for severe osteoarthritis?"
- "What is the recommended antibiotic regimen for community-acquired pneumonia?"

### Drug Information
- "What are the side effects of metformin?"
- "What is the mechanism of action of beta blockers?"
- "Are there any drug interactions between warfarin and NSAIDs?"

## Troubleshooting

### Common Issues

1. **Memory Errors**
   - Reduce the chunk size when processing documents
   - Close other memory-intensive applications
   - Consider using a machine with more RAM

2. **Slow Performance**
   - Use a GPU if available
   - Reduce the number of retrieved documents (`top_k`)
   - Lower the `max_tokens` parameter

3. **Poor Quality Responses**
   - Try adjusting the temperature (lower for more focused, higher for more creative)
   - Modify the system prompt to be more specific
   - Ensure the knowledge base contains relevant information

### Error Messages

- **"CUDA out of memory"**: Reduce batch size or use CPU
- "Module not found": Install missing dependencies with `pip install -r requirements.txt`
- "Invalid PDF": Ensure the PDF is not password protected and is not corrupted

## FAQs

### Q: Can I use my own medical documents?
A: Yes! Simply replace the default PDF with your document and reprocess it using the provided functions.

### Q: How accurate are the responses?
A: The system provides information based on the provided medical manual. Always verify critical medical information with a healthcare professional.

### Q: Is my data private?
A: All processing is done locally by default. No data is sent to external servers unless you configure it to do so.

### Q: How can I improve response quality?
A: Try these tips:
- Be specific with your questions
- Use medical terminology when possible
- Break complex questions into simpler ones
- Adjust the temperature parameter (lower for more factual responses)

## Support

For additional help, please [open an issue](https://github.com/mwill20/NLP_RAG_Medical_Assistant/issues) on GitHub.
