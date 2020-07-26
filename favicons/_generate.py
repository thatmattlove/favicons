"""Generate common favicon formats from a single source image."""

# Standard Library
import json as _json
import math
import asyncio
from typing import Any, Type, Tuple, Callable, Iterable, Generator
from pathlib import Path as _Path

# Third Party
from PIL import Image as PILImage

# Project
from favicons._util import validate_path
from favicons._types import Color, FaviconProperties
from favicons._constants import HTML_LINK, ICON_TYPES, SUPPORTED_FORMATS
from favicons.exceptions import FaviconNotSupported


class Favicons:
    """Generate common favicon formats from a single source image."""

    def __init__(
        self,
        source: _Path,
        output_directory: _Path,
        background_color: Color = "#000000",
        transparent: bool = True,
        base_url: str = "/",
        *args: Any,
        **kwargs: Any,
    ) -> None:
        """Initialize Favicons class."""
        self._validated = False
        self._source = source
        self._output_directory = output_directory
        self._formats = tuple(FaviconProperties(**f) for f in ICON_TYPES)
        self.background_color = Color(background_color)
        self.transparent = transparent
        self.base_url = base_url
        self.generate = self.sgenerate

    def _validate(self) -> None:

        self.source = validate_path(self._source)
        self.output_directory = validate_path(self._output_directory)

        if self.source.suffix.lower() not in SUPPORTED_FORMATS:
            raise FaviconNotSupported(self.source)

        self._validated = True

    def __enter__(self) -> Callable:
        """Enter Favicons context."""
        self._validate()
        self.generate = self.sgenerate
        return self

    def __exit__(
        self, exc_type: Type = None, exc_value: Any = None, traceback: str = None
    ):
        """Exit Favicons context."""
        pass

    async def __aenter__(self):
        """Enter Favicons context."""
        self._validate()
        self.generate = self.agenerate
        return self

    async def __aexit__(
        self, exc_type: Type = None, exc_value: Any = None, traceback: str = None
    ):
        """Exit Favicons context."""
        pass

    @staticmethod
    def _get_center_point(background: PILImage, foreground: PILImage) -> Tuple:
        """Generate a tuple of center points for PIL."""
        bg_x, bg_y = background.size[0:2]
        fg_x, fg_y = foreground.size[0:2]
        x1 = math.floor((bg_x / 2) - (fg_x / 2))
        y1 = math.floor((bg_y / 2) - (fg_y / 2))
        x2 = math.floor((bg_x / 2) + (fg_x / 2))
        y2 = math.floor((bg_y / 2) + (fg_y / 2))
        return (x1, y1, x2, y2)

    def _generate_single(self, format_properties: FaviconProperties) -> None:
        with PILImage.open(self.source) as src:
            output_file = self.output_directory / str(format_properties)
            bg = self.background_color.colors

            # If transparency is enabled, add alpha channel to color.
            if self.transparent:
                bg += (0,)

            # Create background.
            dst = PILImage.new("RGBA", format_properties.dimensions, bg)

            # Resize source image without changing aspect ratio.
            src.thumbnail(format_properties.dimensions)

            # Place source image on top of background image.
            dst.paste(src, box=self._get_center_point(dst, src))

            # Save new file.
            dst.save(output_file, format_properties.image_fmt)

    async def _agenerate_single(self, format_properties: FaviconProperties) -> None:
        """Awaitable version of _generate_single."""

        return self._generate_single(format_properties)

    def sgenerate(self) -> None:
        """Generate favicons."""
        if not self._validated:
            self._validate()

        for fmt in self._formats:
            self._generate_single(fmt)

    async def agenerate(self) -> None:
        """Generate favicons."""
        if not self._validated:
            self._validate()

        await asyncio.gather(*(self._agenerate_single(fmt) for fmt in self._formats))

    def html_gen(self) -> Generator:
        """Get generator of HTML strings."""
        for fmt in self._formats:
            yield HTML_LINK.format(
                rel=fmt.rel,
                type=f"image/{fmt.image_fmt}",
                href=self.base_url + str(fmt),
            )

    def html(self) -> Tuple:
        """Get tuple of HTML strings."""
        return tuple(self.html_gen())

    def formats(self) -> Iterable:
        """Get image formats as list."""
        return [f.dict() for f in self._formats]

    def json(self, *args: Any, **kwargs: Any) -> str:
        """Get image formats as JSON string."""
        return _json.dumps(self.formats(), *args, **kwargs)

    def filenames_gen(self, prefix: bool = False) -> Generator:
        """Get generator of favicon file names."""
        for fmt in self._formats:
            filename = str(fmt)
            if prefix:
                filename = self.base_url + filename
            yield filename

    def filenames(self, prefix: bool = False) -> Tuple:
        """Get tuple of favicon file names."""
        return tuple(self.filenames_gen(prefix=prefix))
