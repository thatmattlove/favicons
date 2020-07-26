"""Custom excpetions for favicons."""

# Standard Library
import json as _json
from typing import Any, Dict, Union, Iterable, Generator
from pathlib import Path

# Project
from favicons._constants import SUPPORTED_FORMATS


class FaviconsError(Exception):
    """Raise an error while running favicons."""

    def __init__(self, message: str, *args: Any, **kwargs: Any):
        """Favicons Base Exception."""
        self._message = message
        self._args = args
        self._kwargs = kwargs

    @property
    def message(self) -> str:
        """Format message with args & kwargs."""
        return self._message.format(*self._args, **self._kwargs)

    @property
    def kwargs(self) -> Dict:
        """Keyword arguments as a dict."""
        return dict(self._kwargs)

    def __repr__(self) -> str:
        """Representation of exception."""
        attrs = (
            f"message='{self.message}'",
            *(repr(a) for a in self.args),
            *(f"{k}={repr(v)}" for k, v in self.kwargs.items()),
        )

        return f"{self.__class__.__name__}({', '.join(attrs)})"

    def __str__(self) -> str:
        """Represent exception as string."""
        return self.message

    def dict(self) -> Dict:
        """Represent exception as dict."""
        return {
            "message": self.message,
            "arguments": list(self.args),
            "keyword_arguments": self.kwargs,
        }

    def json(self) -> str:
        """Represent exception as JSON string."""
        return _json.dumps(self.dict())


class FaviconNotFound(FaviconsError):
    """Raised if the source favicon doesn't exist."""

    def __init__(self, file: Path) -> None:
        """Set message."""
        super().__init__("{} does not exit.", str(file))


class FaviconNotSupported(FaviconsError):
    """Raised if the source favicon file format is not supported."""

    def __init__(self, file: Path) -> None:
        """Set message."""
        one_of = ", ".join(f"'{f}'" for f in SUPPORTED_FORMATS)
        super().__init__(
            "Extension {extension} is not supported ({file}). Must be one of {one_of}.",
            extension=file.suffix,
            file=str(file),
            one_of=one_of,
        )


class FaviconColorError(FaviconsError):
    """Raised if an input color is invalid."""

    def __init__(
        self,
        color: Union[str, Iterable, Generator],
        message: str = "Color '{color}' is not a valid color.",
    ) -> None:
        """Set message."""
        if isinstance(color, Iterable):
            color = str(color)
        elif isinstance(color, Generator):
            color = ",".join(color)
        super().__init__(message, color=color)
