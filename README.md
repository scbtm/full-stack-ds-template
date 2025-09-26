# full-stack-ds-template

A comprehensive MLOps template for full-stack data science projects using Copier.

## Getting Started

### Prerequisites

- Python 3.8 or higher
- [Copier](https://copier.readthedocs.io/) installed

Install Copier:
```bash
pip install copier
```

**Note**: Generated projects use `uv` for dependency management, which is automatically installed during project generation.

### Using the Template

1. **Generate a new project** from this template:
   ```bash
   copier copy https://github.com/your-org/full-stack-ds-template.git /path/to/new/project
   ```

   Or if using locally:
   ```bash
   copier copy . /path/to/new/project --trust
   ```

2. **Answer the simple setup prompts**:
   - **project_slug**: Repository/Docker image name (kebab-case, e.g., 'my-ml-project')
   - **package_name**: Python package name under src/ (snake_case, auto-generated from project_slug)

   > **Note**: All MLOps features are included by default - no need to choose components!

3. **Navigate to your new project** - dependencies are already installed!
   ```bash
   cd /path/to/new/project
   make verify  # Test that everything works
   ```

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