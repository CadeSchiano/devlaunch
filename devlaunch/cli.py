import typer
import shutil
from pathlib import Path

app = typer.Typer(help="🚀 DevLaunch — Generate starter projects instantly")


@app.callback()
def main():
    pass


@app.command()
def create(template_name: str, project_name: str):
    template_dir_name = template_name.replace("-", "_")

    base_dir = Path(__file__).resolve().parent.parent
    template_path = base_dir / "templates" / template_dir_name
    project_path = base_dir / project_name

    # Template check
    if not template_path.exists():
        typer.echo(f"❌ Template '{template_name}' not found\n")
        typer.echo("👉 Run 'devlaunch list' to see available templates")
        return

    # Project exists check
    if project_path.exists():
        typer.echo("❌ Folder already exists")
        return

    # Copy files
    shutil.copytree(template_path, project_path)

    # Success output
    typer.echo(f"\n✅ Project created: {project_name}")
    typer.echo(f"📦 Template: {template_name}\n")

    typer.echo("👉 Next steps:")
    typer.echo(f"cd {project_name}")
    typer.echo("pip install -r requirements.txt")
    typer.echo("python main.py\n")


@app.command()
def list():
    base_dir = Path(__file__).resolve().parent.parent
    templates_path = base_dir / "templates"

    typer.echo("\n📦 Available templates:\n")

    for item in templates_path.iterdir():
        if item.is_dir():
            name = item.name.replace("_", "-")
            typer.echo(f"- {name}")

    typer.echo("")