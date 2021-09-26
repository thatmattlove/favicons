"""Custom data model for favicon properties."""

# Standard Library
import json as _json
from typing import Tuple, Mapping, Optional


class FaviconProperties:
    """Data Model for Favicon Properties."""

    def __init__(
        self, image_fmt: str, dimensions: Tuple[int, int], prefix: str, rel: Optional[str] = None,
    ) -> None:
        """Set properties."""

        self.image_fmt = image_fmt
        self.rel = rel
        self.dimensions = dimensions
        self.prefix = prefix

    @property
    def width(self) -> int:
        """Width from dimensions."""
        return self.dimensions[0]

    @property
    def height(self) -> int:
        """Height from dimensions."""
        return self.dimensions[1]

    def __repr__(self) -> str:
        """Representation of instance."""
        attr_names = (a for a in self.__dir__() if not a.startswith("_"))
        attrs = (f"{a}={getattr(self, a)}" for a in attr_names)
        return f"{self.__class__.__name__}({', '.join(attrs)})"

    def __str__(self) -> str:
        """Represent instance as string."""
        return self._get_filename_parts()

    def dict(self) -> Mapping:
        """Represent instance as dict."""
        return {
            "image_format": self.image_fmt,
            "dimensions": self.dimensions,
            "prefix": self.prefix,
            "rel": self.rel,
        }

    def json(self) -> str:
        """Represent instance as JSON string."""
        return _json.dumps(self.dict())

    def _get_filename_parts(self) -> str:
        """Don't add dimensions to favicon.ico."""
        parts: Tuple[str, ...] = (self.prefix,)

        if self.image_fmt == "ico":
            parts += (
                ".",
                self.image_fmt,
            )
        else:
            parts += (
                "-",
                "x".join(str(d) for d in self.dimensions),
                ".",
                self.image_fmt,
            )
        return "".join(parts)
