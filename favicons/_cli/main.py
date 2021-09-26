"""Favicons CLI Commands."""

# Standard Library
from pathlib import Path

# Third Party
from typer import Typer, Option
from rich.panel import Panel
from rich.columns import Columns
from rich.console import Console
from rich.progress import track

# Project
from favicons._generate import Favicons
from favicons._types.properties import FaviconProperties

cli = Typer(name="Favicons", add_completion=False)
console = Console()


def item_name(item: FaviconProperties) -> str:
    """Format favicon name."""
    return f"[bold green]{str(item)}[/bold green]"


DEFAULT_SOURCE = Option(..., help="Source Image")
DEFAULT_OUTPUT_DIR = Option(..., help="Output Directory")
DEFAULT_BG = Option("#000000", help="Background Color")
DEFAULT_TRANSPARENT = Option(True, help="Transparent Background")
DEFAULT_BASE_URL = Option("/", help="Base URL for HTML output")


@cli.command()
def generate(
    source: Path = DEFAULT_SOURCE,
    output_directory: Path = DEFAULT_OUTPUT_DIR,
    background_color: str = DEFAULT_BG,
    transparent: bool = DEFAULT_TRANSPARENT,
    base_url: str = DEFAULT_BASE_URL,
) -> None:
    """Generate Favicons"""  # noqa: D400

    favicons = Favicons(
        source=source,
        output_directory=output_directory,
        background_color=background_color,
        transparent=transparent,
        base_url=base_url,
    )

    favicons._validate()
    for fmt in track(
        favicons._formats,
        description="Generating Favicons...",
        total=len(favicons._formats),
        console=console,
    ):
        favicons._generate_single(fmt)

    generated = [Panel(item_name(f), expand=True) for f in favicons._formats]

    console.print(f"\n[green]Generated [b]{favicons.completed}[/b] icons:[/green]\n")
    console.print(Columns(generated))


@cli.command()
def json(
    source: Path = DEFAULT_SOURCE,
    output_directory: Path = DEFAULT_OUTPUT_DIR,
    background_color: str = DEFAULT_BG,
    transparent: bool = DEFAULT_TRANSPARENT,
    base_url: str = DEFAULT_BASE_URL,
) -> None:
    """Get favicons as JSON."""
    with Favicons(
        source=source,
        output_directory=output_directory,
        background_color=background_color,
        transparent=transparent,
        base_url=base_url,
    ) as favicons:
        console.print(favicons.json(indent=2))


@cli.command()
def names(
    source: Path = DEFAULT_SOURCE,
    output_directory: Path = DEFAULT_OUTPUT_DIR,
    background_color: str = DEFAULT_BG,
    transparent: bool = DEFAULT_TRANSPARENT,
    base_url: str = DEFAULT_BASE_URL,
) -> None:
    """Get favicon file names."""
    with Favicons(
        source=source,
        output_directory=output_directory,
        background_color=background_color,
        transparent=transparent,
        base_url=base_url,
    ) as favicons:
        for icon in favicons.filenames_gen():
            fname, ext = icon.split(".")
            console.print(f"[bold yellow]{fname}[/bold yellow].[bold blue]{ext}[/bold blue]")


@cli.command()
def html(
    source: Path = DEFAULT_SOURCE,
    output_directory: Path = DEFAULT_OUTPUT_DIR,
    background_color: str = DEFAULT_BG,
    transparent: bool = DEFAULT_TRANSPARENT,
    base_url: str = DEFAULT_BASE_URL,
) -> None:
    """Get favicons as HTML."""
    with Favicons(
        source=source,
        output_directory=output_directory,
        background_color=background_color,
        transparent=transparent,
        base_url=base_url,
    ) as favicons:
        console.print("\n".join(favicons.html_gen()))
