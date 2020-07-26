"""Common utility functions used throughout Favicons."""

# Standard Library
from typing import Any
from pathlib import Path

# Project
from favicons.exceptions import FaviconsError, FaviconNotFound


def validate_path(path: Any, must_exist: bool = True) -> Path:
    """Validate a path and ensure it's a Path object."""
    valid_path = path
    if not isinstance(path, Path):
        try:
            valid_path = Path(path)
        except TypeError:
            raise FaviconsError("{path} is not a valid path.", path=path)

    if must_exist and not valid_path.exists():
        raise FaviconNotFound(valid_path)

    return valid_path
