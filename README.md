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

### Using the Template

1. **Generate a new project** from this template:
   ```bash
   copier copy https://github.com/your-org/full-stack-ds-template.git /path/to/new/project
   ```

   Or if using locally:
   ```bash
   copier copy . /path/to/new/project
   ```

2. **Answer the prompts** to customize your project:
   - **project_slug**: Repository/Docker image name (kebab-case, e.g., 'my-ml-project')
   - **package_name**: Python package name under src/ (snake_case, auto-generated from project_slug)
   - **org_name**: Organization/Weights & Biases entity name
   - **include_sample_code**: Choose between 'minimal' or 'starter' code
   - **include_feature_engineering**: Include Hamilton-based feature engineering pipeline
   - **ci_provider**: Choose CI provider (github_actions or none)
   - **cloud_provider**: Choose cloud provider (gcp or none)
   - **include_monitoring**: Include model monitoring pipeline with drift detection
   - **api_framework**: Choose API framework (fastapi or none)

3. **Navigate to your new project** and install dependencies:
   ```bash
   cd /path/to/new/project
   make install
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