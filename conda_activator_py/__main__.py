# type: ignore[attr-defined]

from typing import Optional

import random
from enum import Enum

import typer
from conda_activator_py import __version__
from conda_activator_py.example import activate_conda
from rich.console import Console

app = typer.Typer(
    name="conda-activator-py",
    help="Awesome `conda-activator-py` is a Python cli/package created with https://github.com/TezRomacH/python-package-template",
    add_completion=False,
)
console = Console()


def version_callback(value: bool):
    """Prints the version of the package."""
    if value:
        console.print(
            f"[yellow]conda-activator-py[/] version: [bold blue]{__version__}[/]"
        )
        raise typer.Exit()


@app.command()
def main(
    conda: Optional[str] = typer.Option(
        None,
        "-c",
        "--conda",
        case_sensitive=False,
        help=".conda_ac file",
    ),
    version: bool = typer.Option(
        None,
        "-v",
        "--version",
        callback=version_callback,
        is_eager=True,
        help="Prints the version of the conda-activator-py package.",
    ),
):
    """Prints a greeting for a giving name."""
    if conda:
        pass

    activate_conda()
