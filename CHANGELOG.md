# Changelog

All notable changes to the NLP RAG Medical Assistant project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Initial project setup with Jupyter notebook implementation
- Basic RAG functionality with Mistral-7B-Instruct
- Document processing pipeline for medical PDFs
- Vector search capabilities with ChromaDB
- Example queries and response generation

### Changed
- Updated README with comprehensive documentation
- Added contribution guidelines and code of conduct
- Improved error handling and logging

### Fixed
- Memory optimization for large document processing
- Fixed issues with special characters in text extraction
- Improved handling of medical terminology

## [0.1.0] - 2025-07-01

### Added
- Initial release of NLP RAG Medical Assistant
- Core functionality for medical information retrieval
- Basic documentation and setup instructions

## Future Improvements

### Planned Features
- Web interface for easier interaction
- Support for multiple medical knowledge sources
- Fine-tuned medical language model
- API for integration with other applications
- Docker container for easy deployment
- More comprehensive testing suite

### Known Issues
- Processing very large documents may require significant memory
- Response quality depends on the source material quality
- Limited support for non-English medical terminology

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/mwill20/NLP_RAG_Medical_Assistant/tags).

## Authors

- **Michael Williams** - Initial work - [mwill20](https://github.com/mwill20)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Mistral AI](https://mistral.ai/) for the language model
- [LangChain](https://python.langchain.com/) for the RAG framework
- [ChromaDB](https://www.trychroma.com/) for vector storage
- [Merck Manual](https://www.merckmanuals.com/) for the medical reference material
