# Full-Stack Data Science Template

🚀 A comprehensive DS / MLOps project template with modern tooling, CI/CD pipelines, and starter files using Copier.

## ⚠️ Important: GitHub Template + Codespaces Only

**This repository is designed exclusively as a GitHub template for use in GitHub Codespaces.**

- 🎯 **Use the "Use this template" button** on GitHub to create your project
- 💻 **Open in GitHub Codespaces** for automatic environment setup
- 🚫 **Do not use Copier directly** - use the GitHub template workflow instead

### Why This Approach?

This template uses a **hybrid approach** combining GitHub templates with Copier + initialization script because:

1. **GitHub Codespaces Integration**: Codespaces initializes with the main branch as root
2. **Clean Project Structure**: The `init_project.py` script transforms the template into a proper project structure
3. **Automated Setup**: Everything is configured automatically in the Codespaces environment
4. **No Manual Configuration**: Dependencies, tools, and environment are pre-configured

While it might seem redundant to use both Copier and an init script, this approach provides the cleanest development experience specifically for GitHub Codespaces users.

## 🚀 Quick Start

### 1. Create Your Project
1. Click **"Use this template"** on GitHub
2. Create your new repository
3. Open in **GitHub Codespaces**

### 2. Initialize Your Project
Once in Codespaces, run the initialization script:
```bash
python init_project.py
```

This script will:
- ✨ Create proper project structure using Copier
- 🧹 Clean up template artifacts
- 🔧 Set up development tools (Ruff, Pyright, pytest, pre-commit)
- 📁 Move all files to the correct locations
- 🗑️ Remove initialization files

### 3. Verify Setup
```bash
uv run make verify
```

## 📋 Prerequisites

- **GitHub account** with Codespaces access
- **Python 3.8+** (automatically available in Codespaces)
- [Copier](https://copier.readthedocs.io/) installed

> **Note**: All dependencies and tools are automatically installed during the initialization process.

### Template Features

This template includes:

- **Development Environment**: Pre-configured with Python 3.12, Poetry/pip, and development tools
- **Code Quality**: Ruff for linting and formatting, pre-commit hooks
- **Testing**: Pytest setup with coverage reporting
- **Feature Engineering**: Optional Hamilton-based pipeline
- **Model Training & Inference**: MLOps-ready structure
- **API Service**: Optional FastAPI service for model serving
- **Monitoring**: Optional model drift detection and monitoring
- **CI/CD**: GitHub Actions workflows (optional)
- **Deployment**: GCP deployment configurations (optional)
- **Documentation**: Auto-generated project README

### Updating an Existing Project

To update a project created from this template:

```bash
cd /path/to/your/project
copier update
```

This will apply any changes from the template while preserving your customizations.