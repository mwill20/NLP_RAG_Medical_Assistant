from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="nlp-rag-medical-assistant",
    version="0.1.0",
    author="Michael Williams",
    author_email="mwill.itmission@gmail.com",
    description="A Retrieval-Augmented Generation (RAG) system for medical information retrieval and question answering",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mwill20/NLP_RAG_Medical_Assistant",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Healthcare Industry",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: Medical Science Apps.",
    ],
    python_requires=">=3.8",
    install_requires=[
        "numpy>=1.26.4",
        "pandas>=1.5.3",
        "transformers>=4.40.0",
        "sentence-transformers>=2.7.0",
        "torch>=2.0.0",
        "accelerate>=0.20.0",
        "pymupdf>=1.24.1",
        "python-dotenv>=1.0.0",
        "chromadb>=0.4.0",
        "langchain>=0.1.1",
        "langchain-community>=0.0.13",
        "llama-cpp-python>=0.1.85",
        "jupyter>=1.0.0",
        "ipykernel>=6.0.0",
        "tqdm>=4.66.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.4.0",
            "pytest-cov>=4.1.0",
            "black>=23.0.0",
            "isort>=5.12.0",
            "mypy>=1.0.0",
            "pre-commit>=3.5.0",
        ],
        "docs": [
            "sphinx>=7.0.0",
            "sphinx-rtd-theme>=1.3.0",
            "sphinx-copybutton>=0.5.2",
            "myst-parser>=2.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "rag-medical-assist=nlp_rag_medical_assistant.cli:main",
        ],
    },
    include_package_data=True,
    package_data={
        "nlp_rag_medical_assistant": ["data/*.pdf", "data/*.json"],
    },
    project_urls={
        "Bug Reports": "https://github.com/mwill20/NLP_RAG_Medical_Assistant/issues",
        "Source": "https://github.com/mwill20/NLP_RAG_Medical_Assistant",
    },
)
