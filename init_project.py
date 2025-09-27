import shutil
import subprocess
from pathlib import Path
import sys

"""
Data Science/MLOps Project Template Initializer

A clean, user-friendly script that transforms this template into a personalized
ML project with proper tooling and structure. Designed for one-time execution
with robust error handling and clear progress feedback.

Usage:
    python init_project.py

The script will:
1. Validate your environment and gather project information
2. Create proper project structure with src/ and tests/ directories using Copier
4. Configure development tools (Ruff, Pyright, pytest, pre-commit)
5. Clean up template artifacts

After completion, use 'uv run make verify' to test your setup.
"""

# ============================================================================
# FILE SYSTEM UTILITIES
# ============================================================================

def run_command(cmd: list[str], description: str, timeout: int = 360) -> subprocess.CompletedProcess:
    """
    Run a command with proper error handling and informative output.

    Args:
        cmd: Command and arguments as a list
        description: Human-readable description of what the command does
        timeout: Maximum time to wait for command completion (seconds)

    Returns:
        CompletedProcess object with result

    Raises:
        subprocess.CalledProcessError: If command fails
        subprocess.TimeoutExpired: If command times out
        FileNotFoundError: If command is not found
    """
    try:
        result = subprocess.run(
            cmd,
            check=True,
            text=True,
            stdin=sys.stdin,
            stdout=sys.stdout,
            stderr=sys.stderr,
            timeout=timeout,
        )
        return result
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to {description}")
        print(f"   Command: {' '.join(cmd)}")
        print(f"   Error: {e.stderr.strip() if e.stderr else 'No error output'}")
        raise
    except subprocess.TimeoutExpired:
        print(f"❌ Timeout while trying to {description}")
        raise
    except FileNotFoundError:
        print(f"❌ Command not found: {cmd[0]}")
        raise

def safe_remove(path: Path, description: str = "") -> bool:
    """
    Safely remove a file or directory with error handling.

    Args:
        path: Path to remove
        description: Optional description for logging

    Returns:
        True if removal was successful, False otherwise
    """
    try:
        if path.exists():
            if path.is_dir():
                shutil.rmtree(path)
            else:
                path.unlink()
            desc = description or str(path)
            print(f"   Removed {desc}")
            return True
        return True  # Already doesn't exist
    except Exception as e:
        print(f"⚠️  Failed to remove {path}: {e}")
        return False


def rollback_changes(created_files: list[Path]) -> None:
    """
    Roll back changes by removing created files in reverse order.

    Args:
        created_files: List of paths that were created during initialization
    """
    print("🔄 Rolling back changes...")
    for file_path in reversed(created_files):
        safe_remove(file_path, f"rollback: {file_path}")


def ensure_directory_exists(path: Path) -> Path:
    """
    Ensure a directory exists, creating it if necessary.

    Args:
        path: Directory path to ensure exists

    Returns:
        The same path (for chaining)
    """
    path.mkdir(parents=True, exist_ok=True)
    return path

def create_project_structure() -> list[Path]:
    """Create the main project structure using Copier."""
    print("🏗️  Creating project structure...")
    created_files: list[Path] = []

    # Project name derived from directory name
    project_slug = Path.cwd().name.lower()
    package_name = project_slug.replace("-", "_")

    # Initialize project, pass package_name to Copier as flag
    run_command([
        "copier",
        "copy",
        ".",
        project_slug,
        "--trust",
        "--force",
        "--d",
        f"project_slug={project_slug}",
        "--d",
        f"package_name={package_name}",
        ], "initialize project structure with Copier")
    created_files.append(Path(project_slug))

    return created_files

def cleanup_template_readme():
    """Remove template README if it hasn't been customized."""
    readme = Path("Template_README.md")
    if not readme.exists():
        return

    try:
        content = readme.read_text()
        if "projects using Copier" in content:
            safe_remove(readme, "template README.md")
            print("   💡 You can create a new README.md for your project")
    except Exception:
        pass  # If we can't read it, leave it alone

def cleanup_initialization_script():
    """Remove the initialization script and utilities."""
    print("   🗑️  Removing initialization files...")

    # Remove utilities first
    utils_file = Path("init_utils.py")
    if utils_file.exists():
        try:
            utils_file.unlink()
            print(f"   Removed {utils_file}")
        except Exception as e:
            print(f"   ⚠️  Could not remove {utils_file}: {e}")

    # Remove this script (final step)
    script_file = Path(__file__)
    if script_file.exists():
        try:
            script_file.unlink()
            print(f"   Removed {script_file}")
        except Exception as e:
            print(f"   ⚠️  Could not remove {script_file}: {e}")
            print("   You can manually delete it after initialization")

def cleanup_template_artifacts():
    """Clean up template files and temporary artifacts."""
    print("🧹 Cleaning up template artifacts...")

    # Remove temporary directories
    temp_items = [
        Path(".venv"),           # Temporary virtual environment
        Path(".ruff_cache"),     # Ruff cache
        Path("template"),        # Copier template directory
        Path("copier.yml"),      # Copier configuration file
    ]

    for item in temp_items:
        safe_remove(item, f"temporary: {item.name}")

    # Remove __pycache__ directories from src/
    if Path("src").exists():
        for pycache in Path("src").rglob("__pycache__"):
            safe_remove(pycache, f"cache: {pycache}")

    # Remove this initialization script (final step)
    cleanup_initialization_script()

    # Remove template README if it's still the original
    cleanup_template_readme()


def display_success_message():
    """Display success message with next steps."""
    project_name = Path.cwd().name.lower().replace("-", "_")
    print("\n" + "=" * 60)
    print(f"\n🎉 Success! '{project_name}' is ready for development!")
    print("=" * 60)
    print("\n📋 Next Steps:")
    print("   1. Run 'uv run make verify' to test everything")
    print("   2. Check your main file: src/{}/main.py".format(project_name))
    print("   3. Start building your ML project!")
    print("\n💡 Useful Commands:")
    print("   • uv run make verify    - Run all quality checks")
    print("   • uv run make test      - Run tests")
    print("   • uv add <package>      - Add new dependencies")
    print("   • uv run <command>      - Run commands in the environment")
    print("\n📚 Documentation:")
    print("   • UV: https://docs.astral.sh/uv/")
    print("   • Ruff: https://docs.astral.sh/ruff/")
    print("   • Pytest: https://docs.pytest.org/")
    print()

def display_troubleshooting_help():
    """Display troubleshooting information for common issues."""
    print("\n🔧 Troubleshooting:")
    print("   • Ensure UV is installed: https://docs.astral.sh/uv/getting-started/installation/")
    print("   • Check Python version compatibility (>= 3.9)")
    print("   • Verify network connectivity for package downloads")
    print("   • Try running in a fresh directory")
    print()

# ============================================================================
# MAIN WORKFLOW
# ============================================================================

def main():
    """
    Main initialization workflow.

    Orchestrates the entire template-to-project transformation process
    with proper error handling and rollback capability.
    """
    print("🚀 Full-Stack Data Science Project Template Initializer")
    print("=" * 50)
    print("Transforming template into your personalized ML project...")
    print()

    created_files: list[Path] = []  # Track files for potential rollback

    try:
        # Phase 1: Copy from template
        print("\n🏗️  Phase 1: Building Project Structure")
        print("-" * 40)
        
        created_files.extend(create_project_structure())

        # Phase 2: Cleanup
        print("\n🧹 Phase 2: Cleaning Up Template Files")
        print("-" * 41)
        cleanup_template_artifacts()

        # Phase 3: Move the created project files to current directory
        print("\n🚚 Phase 3: Finalizing Project Setup")
        print("-" * 40)

        project_dir = created_files[0]
        for item in project_dir.iterdir():
            target = Path.cwd() / item.name
            if target.exists():
                print(f"⚠️  Conflict: {target} already exists. Skipping.")
            else:
                shutil.move(str(item), str(target))
                print(f"   Moved {item.name} to current directory")

        # Success!
        display_success_message()

    except KeyboardInterrupt:
        print("\n\n⏹️  Initialization cancelled by user.")
        if created_files:
            rollback_changes(created_files)
        sys.exit(1)

    except Exception as e:
        print(f"\n❌ Initialization failed: {e}")
        if created_files:
            rollback_changes(created_files)
        display_troubleshooting_help()
        sys.exit(1)

# ============================================================================
# SCRIPT ENTRY POINT
# ============================================================================

if __name__ == "__main__":
    main()