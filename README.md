# NLP RAG Medical Assistant

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![LangChain](https://img.shields.io/badge/LangChain-0.1.1-ff69b4.svg)](https://python.langchain.com/)

A Retrieval-Augmented Generation (RAG) system designed to assist healthcare professionals by providing accurate medical information from trusted sources. This AI-powered assistant can answer medical questions, provide diagnostic assistance, and offer treatment recommendations based on the Merck Manual of Diagnosis & Therapy.

## ✨ Features

- **Medical Knowledge Base**: Leverages the comprehensive Merck Manual as its primary knowledge source
- **Advanced NLP**: Utilizes Mistral-7B-Instruct model for understanding and generating medical responses
- **Vector Search**: Implements efficient semantic search over medical documents
- **Context-Aware Responses**: Provides relevant, cited medical information
- **Interactive Interface**: Easy-to-use Jupyter notebook interface for querying the system

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- GPU recommended for faster inference (CPU supported but slower)
- Git

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/mwill20/NLP_RAG_Medical_Assistant.git
   cd NLP_RAG_Medical_Assistant
   ```

2. Create and activate a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: .\venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## 🏃‍♂️ Usage

1. Launch Jupyter Notebook:
   ```bash
   jupyter notebook
   ```

2. Open `NLP_RAG_Project.ipynb`

3. Follow the notebook cells to:
   - Load the medical knowledge base
   - Initialize the RAG system
   - Ask medical questions and receive informed responses

## 📚 Example Queries

- "What is the protocol for managing sepsis in a critical care unit?"
- "What are the common symptoms and treatments for pulmonary embolism?"
- "Can you provide the trade names of medications used for treating hypertension?"
- "What are the first-line treatment options for rheumatoid arthritis?"

## 🛠️ Technical Details

### Architecture

The system follows a RAG (Retrieval-Augmented Generation) architecture:

1. **Document Processing**:
   - PDF parsing and text extraction
   - Document chunking with overlap
   - Text cleaning and normalization

2. **Vector Database**:
   - Uses ChromaDB for efficient vector storage and retrieval
   - Sentence Transformers for document embeddings

3. **LLM Integration**:
   - Mistral-7B-Instruct model for response generation
   - LangChain for orchestration
   - Custom prompt engineering for medical context

### Performance

- **Response Time**: ~5-15 seconds on GPU (varies by query complexity)
- **Knowledge Base**: Merck Manual of Diagnosis & Therapy, 19th Edition
- **Context Window**: 4096 tokens

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

## 📧 Contact

Michael Williams - [@your_twitter](https://twitter.com/your_twitter) - mwill.itmission@gmail.com

Project Link: [https://github.com/mwill20/NLP_RAG_Medical_Assistant](https://github.com/mwill20/NLP_RAG_Medical_Assistant)

## 🙏 Acknowledgments

- [Mistral AI](https://mistral.ai/) for the powerful language model
- [LangChain](https://python.langchain.com/) for the RAG framework
- [Merck Manual](https://www.merckmanuals.com/) for the medical reference material
- The open-source community for valuable tools and libraries
