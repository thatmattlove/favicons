"""Common utility functions used throughout Favicons."""

# Standard Library
from typing import Union, Mapping, Generator
from pathlib import Path
from tempfile import mkstemp

# Project
from favicons._types import Color, FaviconProperties
from favicons._constants import ICON_TYPES
from favicons._exceptions import FaviconsError, FaviconNotFound


def validate_path(path: Union[Path, str], must_exist: bool = True, create: bool = False) -> Path:
    """Validate a path and ensure it's a Path object."""

    if isinstance(path, str):
        try:
            path = Path(path)
        except TypeError:
            raise FaviconsError("{path} is not a valid path.", path=path)

    if create:
        if path.is_dir() and not path.exists():
            path.mkdir(parents=True)
        elif not path.is_dir() and not path.parent.exists():
            path.parent.mkdir(parents=True)

    if must_exist and not path.exists():
        raise FaviconNotFound(path)

    return path


def generate_icon_types() -> Generator[FaviconProperties, None, None]:
    """Get icon type objects."""
    for icon_type in ICON_TYPES:
        if isinstance(icon_type, Mapping):
            yield FaviconProperties(**icon_type)


def svg_to_png(svg_path: Path, background_color: Color) -> Path:
    """Convert an SVG vector to a PNG file."""
    from svglib.svglib import svg2rlg
    from reportlab.graphics import renderPM
    from reportlab.lib.colors import transparent

    _, png_path = mkstemp(suffix=".tiff")

    png = Path(png_path)

    drawing = svg2rlg(str(svg_path))
    renderPM.drawToFile(
        drawing,
        str(png),
        fmt="TIFF",
        bg=int(background_color.as_hex().replace("#", ""), 16),
        configPIL={"transparent": transparent},
    )

    return png
