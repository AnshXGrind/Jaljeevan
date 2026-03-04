# Contributing to JalJeevan 🐬

Thank you for your interest in contributing! This document will help you get started.

---

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
- [Development Setup](#development-setup)
- [Pull Request Process](#pull-request-process)
- [Style Guide](#style-guide)
- [Commit Message Convention](#commit-message-convention)

---

## Code of Conduct

This project follows the [Contributor Covenant](https://www.contributor-covenant.org/). By participating, you are expected to be respectful and constructive. Harassment of any kind is not tolerated.

---

## How Can I Contribute?

### 🐛 Reporting Bugs

Before filing a bug, check [existing issues](https://github.com/AnshXGrind/Jaljeevan/issues). If it's new:
1. Use the **Bug Report** issue template
2. Include your OS, Python version, and steps to reproduce
3. Attach relevant logs from `app_out.txt` or `pipeline_err.txt`

### 💡 Suggesting Features

Open a [Feature Request](https://github.com/AnshXGrind/Jaljeevan/issues/new) and describe:
- The problem you're solving
- Your proposed solution
- Why it benefits the project

### 🔧 Code Contributions

Look for issues tagged:
- `good first issue` – Great for new contributors
- `help wanted` – Needs community input
- `roadmap` – Planned features you can claim

---

## Development Setup

```bash
# Fork and clone
git clone https://github.com/<your-username>/Jaljeevan.git
cd Jaljeevan

# Create virtual environment
python -m venv venv
source venv/bin/activate

# Install dev dependencies
pip install -r requirements.txt
pip install pytest black flake8

# Run tests
pytest tests/
```

---

## Pull Request Process

1. **Branch** off `main`: `git checkout -b feature/your-feature`
2. **Write tests** for new functionality in `tests/`
3. **Run tests** before submitting: `pytest tests/`
4. **Format code**: `black .`
5. **Lint**: `flake8 . --max-line-length=100`
6. **Update** `README.md` if your change adds/removes functionality
7. Open your PR against the `main` branch with a clear description

PRs will be reviewed within 48–72 hours.

---

## Style Guide

- Python: Follow [PEP 8](https://pep8.org/), max line length 100
- Use **type hints** for all function signatures
- Docstrings: Google style
- Avoid hardcoded paths or credentials — use `config.py` or `.env`

```python
# Good
def compute_score(zone: str, window_hours: int = 48) -> float:
    """
    Compute dolphin health score for a zone.

    Args:
        zone: River zone identifier (e.g. 'UP-001')
        window_hours: Rolling window in hours.

    Returns:
        Health score between 0.0 and 1.0
    """
    ...
```

---

## Commit Message Convention

Follow [Conventional Commits](https://www.conventionalcommits.org/):

```
feat: add WhatsApp alert integration
fix: correct dolphin count aggregation in 48h window
docs: update quickstart for Windows WSL
chore: upgrade Pathway to 0.14
test: add unit tests for causal chain analyser
```

---

## Questions?

Open a [Discussion](https://github.com/AnshXGrind/Jaljeevan/discussions) or tag the maintainer in an issue.
