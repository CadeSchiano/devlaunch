import typer
import os
import shutil
from pathlib import Path

app = typer.Typer()

@app.callback()
def main():
    """DevLaunch CLI"""
    pass

@app.command()
def create(template_name: str, project_name: str):
    # Normalize template name (python-api → python_api)
    template_dir_name = template_name.replace("-", "_")

    # Get paths
    base_dir = Path(__file__).resolve().parent.parent
    template_path = base_dir / "templates" / template_dir_name
    project_path = base_dir / project_name

    # Check if template exists
    if not template_path.exists():
        print(f"Template '{template_name}' not found.")
        return

    # Check if project already exists
    if project_path.exists():
        print("Folder already exists")
        return

    # Copy template → project folder
    shutil.copytree(template_path, project_path)

    print(f"Project '{project_name}' created using '{template_name}' template.")