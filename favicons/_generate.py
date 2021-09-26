"""Generate common favicon formats from a single source image."""

# Standard Library
import json as _json
import math
import asyncio
from typing import (
    Any,
    Type,
    Tuple,
    Union,
    Callable,
    Optional,
    Coroutine,
    Generator,
    Collection,
)
from pathlib import Path

# Third Party
from PIL import Image as PILImage

# Project
from favicons._util import svg_to_png, validate_path, generate_icon_types
from favicons._types import Color, FaviconProperties
from favicons._constants import HTML_LINK, SUPPORTED_FORMATS
from favicons._exceptions import FaviconNotSupported

LoosePath = Union[Path, str]
LooseColor = Union[Collection[int], str]


class Favicons:
    """Generate common favicon formats from a single source image."""

    def __init__(
        self,
        source: LoosePath,
        output_directory: LoosePath,
        background_color: LooseColor = "#000000",
        transparent: bool = True,
        base_url: str = "/",
        *args: Any,
        **kwargs: Any,
    ) -> None:
        """Initialize Favicons class."""
        self._validated = False
        self._output_directory = output_directory
        self._formats = tuple(generate_icon_types())
        self.transparent = transparent
        self.base_url = base_url
        self.background_color: Color = Color(background_color)
        self.generate: Union[Callable, Coroutine] = self.sgenerate
        self.completed: int = 0
        self._temp_source: Optional[Path] = None

        if isinstance(source, str):
            source = Path(source)

        self._source = source

        self._check_source_format()

    def _validate(self) -> None:

        self.source = validate_path(self._source)
        self.output_directory = validate_path(self._output_directory, create=True)

        if self.source.suffix.lower() not in SUPPORTED_FORMATS:
            raise FaviconNotSupported(self.source)

        self._validated = True

    def __enter__(self) -> "Favicons":
        """Enter Favicons context."""
        self._validate()
        self.generate = self.sgenerate
        return self

    def __exit__(self, exc_type: Type = None, exc_value: Any = None, traceback: str = None) -> None:
        """Exit Favicons context."""
        self._close_temp_source()
        pass

    async def __aenter__(self) -> "Favicons":
        """Enter Favicons context."""
        self._validate()
        self.generate = self.agenerate
        return self

    async def __aexit__(
        self, exc_type: Type = None, exc_value: Any = None, traceback: str = None
    ) -> None:
        """Exit Favicons context."""
        self._close_temp_source()
        pass

    def _close_temp_source(self) -> None:
        """Close temporary file if it exists."""
        if self._temp_source is not None:
            try:
                self._temp_source.unlink()
            except FileNotFoundError:
                pass

    def _check_source_format(self) -> None:
        """Convert source image to PNG if it's in SVG format."""
        if self._source.suffix == ".svg":
            self._source = svg_to_png(self._source, self.background_color)

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
            bg: Tuple[int, ...] = self.background_color.colors

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

            self.completed += 1

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
                rel=fmt.rel, type=f"image/{fmt.image_fmt}", href=self.base_url + str(fmt),
            )

    def html(self) -> Tuple:
        """Get tuple of HTML strings."""
        return tuple(self.html_gen())

    def formats(self) -> Tuple:
        """Get image formats as list."""
        return tuple(f.dict() for f in self._formats)

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
