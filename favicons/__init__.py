"""Favicon generator for Python."""

# Project
from favicons._generate import Favicons
from favicons._exceptions import (
    FaviconsError,
    FaviconColorError,
    FaviconNotFoundError,
    FaviconNotSupportedError,
)

__all__ = (
    "Favicons",
    "FaviconsError",
    "FaviconNotFoundError",
    "FaviconColorError",
    "FaviconNotSupportedError",
)
