# DevLaunch

![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![CLI](https://img.shields.io/badge/type-CLI-orange)
![Status](https://img.shields.io/badge/status-active-success)

**Generate starter projects instantly from your terminal.**

DevLaunch is a simple CLI tool that lets you create clean, ready-to-run project templates in seconds.

---

## Quick Start

```bash
pip install -e .
devlaunch create python-api my_project
```

## Available Templates

```bash
devlaunch list
```

Current templates:

- `python-api` -> Basic API starter
- `cli-tool` -> Command-line tool starter
- `python-script` -> Script with config structure

## Usage

```bash
devlaunch create <template> <project_name>
```

Example:

```bash
devlaunch create cli-tool my_cli
```

## What You Get

Each template includes:

- Clean project structure
- Ready-to-run code
- Minimal setup required

## Example Output

```text
Project created: my_cli
Template: cli-tool

Next steps:
cd my_cli
pip install -r requirements.txt
python main.py
```

## Why DevLaunch?

- Fast project setup
- Clean, simple templates
- Designed for real use, not just demos
- Easy to extend with new templates

## Roadmap

- More templates (web apps, games, tools)
- Better customization options
- Publish to PyPI

## Contributing

Want to add a template or improve existing ones?

Feel free to open a pull request or suggestion.

## Support

If you find this useful, consider starring the repo.
