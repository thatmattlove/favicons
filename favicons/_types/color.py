"""Custom Validation & Conversion for Color."""

# Standard Library
import re
from typing import Tuple, Union, Pattern, Generator, Collection

# Project
from favicons._exceptions import FaviconsError, FaviconColorError

_RGB_STR_PATTERN = re.compile(r"^rgb\((\d+),\s?(\d+),\s?(\d+)\)$")
_HEX_STR_PATTERN3 = re.compile(r"^\#?([A-Fa-f0-9])([A-Fa-f0-9])([A-Fa-f0-9])$")
_HEX_STR_PATTERN6 = re.compile(r"^\#?([A-Fa-f0-9]{2})([A-Fa-f0-9]{2})([A-Fa-f0-9]{2})$")

Rgb = Tuple[int, int, int]


def get_matches(pattern: Pattern, search: str) -> Generator[str, None, None]:
    """Get capture group matches as a tuple."""
    matches = pattern.search(search)
    if matches is not None:
        for match in matches.groups():
            yield match
    else:
        raise FaviconsError(f"Pattern {repr(pattern)} did not match anything in {repr(search)}")


class Color:
    """Validate & Transform Color Representations."""

    red: int
    green: int
    blue: int

    def __init__(self, color: Union[str, Collection]) -> None:
        """Validate & parse input color."""
        rgb = None
        if isinstance(color, str):
            rgb = self._validate_str(color)
        elif isinstance(color, Collection):
            rgb = self._validate_rgb_iter(color)
        else:
            raise FaviconColorError(color)
        if rgb is None:
            raise FaviconColorError(color)

        color_names = ("red", "green", "blue")
        for i, color_num in enumerate(rgb):
            setattr(self, color_names[i], color_num)

    def as_hex(self) -> str:
        """Represent color as hex value."""

        def hexstr(num: int) -> str:
            return hex(num).replace("0x", "").zfill(2)

        colors = (hexstr(c) for c in (self.red, self.green, self.blue))

        return "#" + "".join(colors)

    def as_rgb(self) -> str:
        """Represent color as RGB string in rgb(x, y, z) format."""
        return f"rgb({', '.join(str(c) for c in (self.red, self.green, self.blue))})"

    @property
    def colors(self) -> Rgb:
        """Represent color as tuple of RGB values."""
        return (self.red, self.green, self.blue)

    def _validate_str(self, colorstr: str) -> Generator:
        """Validate & parse input string."""
        rgb = None

        if _RGB_STR_PATTERN.match(colorstr):
            rgb = self._parse_rgbstr(colorstr)

        elif _HEX_STR_PATTERN3.match(colorstr):
            rgb = self._parse_hex(colorstr, 3)

        elif _HEX_STR_PATTERN6.match(colorstr):
            rgb = self._parse_hex(colorstr, 6)

        if rgb is None:
            raise FaviconColorError(colorstr)

        return rgb

    @staticmethod
    def _validate_rgb_iter(rgb_iter: Collection) -> Generator:
        """Validate & parse color iterable of RGB values."""

        if not len(rgb_iter) == 3:
            raise FaviconColorError(rgb_iter)

        for i in rgb_iter:
            try:
                num = int(i)
                if num not in range(0, 256):
                    raise FaviconColorError(rgb_iter)
                yield num
            except TypeError:
                raise FaviconColorError(rgb_iter)

    @staticmethod
    def _parse_rgbstr(rgbstr: str) -> Generator:
        """Validate & parse color string in rgb(x, y, z) format."""
        for digit in get_matches(_RGB_STR_PATTERN, rgbstr):
            num = int(digit)
            if num not in range(0, 256):
                raise FaviconColorError(rgbstr)
            yield num

    @staticmethod
    def _parse_hex(hexstr: str, length: int) -> Generator[int, None, None]:
        """Validate & parse color string in hex format."""
        rgb = None

        if length == 3:
            rgb = (s + s for s in get_matches(_HEX_STR_PATTERN3, hexstr))
        elif length == 6:
            rgb = get_matches(_HEX_STR_PATTERN6, hexstr)

        if rgb is None:
            raise FaviconColorError(hexstr)

        for c in rgb:
            yield int(c, 16)

    def __str__(self) -> str:
        """Represent instance as string."""
        return self.as_hex()

    def __repr__(self) -> str:
        """Represent instance & values."""
        colors = (f"{c}={getattr(self, c)}" for c in ("red", "green", "blue"))
        return f"{self.__class__.__name__}({', '.join(colors)})"
