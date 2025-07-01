# Contributing to NLP RAG Medical Assistant

First off, thank you for considering contributing to the NLP RAG Medical Assistant project! We appreciate your time and effort in making this project better.

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [How to Contribute](#how-to-contribute)
  - [Reporting Bugs](#reporting-bugs)
  - [Suggesting Enhancements](#suggesting-enhancements)
  - [Your First Code Contribution](#your-first-code-contribution)
  - [Pull Request Process](#pull-request-process)
- [Development Setup](#development-setup)
- [Style Guide](#style-guide)
- [License](#license)

## Code of Conduct

This project and everyone participating in it is governed by our [Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code.

## Getting Started

1. **Fork** the repository on GitHub
2. **Clone** the project to your own machine
3. **Commit** changes to your own branch
4. **Push** your work back up to your fork
5. Submit a **Pull Request** so that we can review your changes

## How to Contribute

### Reporting Bugs

Bugs are tracked as [GitHub issues](https://github.com/mwill20/NLP_RAG_Medical_Assistant/issues). When creating a bug report, please include:

- A clear title and description
- Steps to reproduce the issue
- Expected vs. actual behavior
- Any relevant screenshots or logs
- Your environment details (OS, Python version, etc.)

### Suggesting Enhancements

We welcome suggestions for new features and improvements. When suggesting an enhancement:

- Use a clear and descriptive title
- Explain the current behavior and why it's not ideal
- Describe the proposed solution
- Include any alternative solutions you've considered

### Your First Code Contribution

1. Look through the GitHub issues for items labeled "good first issue" or "help wanted"
2. Comment on the issue to express your interest
3. Follow the development setup instructions below
4. Make your changes and submit a pull request

### Pull Request Process

1. Ensure any install or build dependencies are removed before the end of the layer when doing a build
2. Update the README.md with details of changes to the interface, including new environment variables, exposed ports, useful file locations, and container parameters
3. Increase the version numbers in any examples files and the README.md to the new version that this Pull Request would represent
4. You may merge the Pull Request in once you have the sign-off of two other developers, or if you do not have permission to do that, you may request the second reviewer to merge it for you

## Development Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/mwill20/NLP_RAG_Medical_Assistant.git
   cd NLP_RAG_Medical_Assistant
   ```

2. **Set up a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: .\venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements-dev.txt
   ```

4. **Set up pre-commit hooks**
   ```bash
   pre-commit install
   ```

5. **Run tests**
   ```bash
   pytest
   ```

## Style Guide

- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) for Python code
- Use type hints for all function signatures
- Include docstrings for all public functions and classes following the [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings)
- Keep lines under 100 characters when possible
- Use absolute imports
- Write tests for new functionality

## License

By contributing, you agree that your contributions will be licensed under its MIT License.
