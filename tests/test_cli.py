import typer

app = typer.Typer()

@app.callback()
def main():
    """DevLaunch CLI"""
    pass

@app.command()
def create():
    print("Creating project...")

if __name__ == "__main__":
    app()