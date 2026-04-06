import typer
import os

app = typer.Typer()

@app.callback()
def main():
    """DevLaunch CLI"""
    pass

@app.command()
def create(template_name: str, project_name: str):
    print("Creating project...")
    print(f"Template: {template_name}")
    print(f"Project Name: {project_name}")

    if os.path.exists(project_name):
        print("Folder already exists")
        return
    else:
        os.mkdir(project_name)
    