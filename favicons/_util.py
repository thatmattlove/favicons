"""Common utility functions used throughout Favicons."""

# Standard Library
from typing import Union, Mapping, Generator
from pathlib import Path

# Project
from favicons._types import FaviconProperties
from favicons._constants import ICON_TYPES
from favicons._exceptions import FaviconsError, FaviconNotFound


def validate_path(path: Union[Path, str], must_exist: bool = True) -> Path:
    """Validate a path and ensure it's a Path object."""

    if isinstance(path, str):
        try:
            path = Path(path)
        except TypeError:
            raise FaviconsError("{path} is not a valid path.", path=path)

    if must_exist and not path.exists():
        raise FaviconNotFound(path)

    return path


def generate_icon_types() -> Generator[FaviconProperties, None, None]:
    """Get icon type objects."""
    for icon_type in ICON_TYPES:
        if isinstance(icon_type, Mapping):
            yield FaviconProperties(**icon_type)
