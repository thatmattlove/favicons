"""Static values for one way import."""

SUPPORTED_FORMATS = (".svg", ".jpeg", ".jpg", ".png", ".tiff", ".tif")

HTML_LINK = '<link rel="{rel}" type="{type}" href="{href}" />'

ICON_TYPES = (
    {"image_fmt": "ico", "rel": None, "dimensions": (64, 64), "prefix": "favicon"},
    {"image_fmt": "png", "rel": "icon", "dimensions": (16, 16), "prefix": "favicon"},
    {"image_fmt": "png", "rel": "icon", "dimensions": (32, 32), "prefix": "favicon"},
    {"image_fmt": "png", "rel": "icon", "dimensions": (64, 64), "prefix": "favicon"},
    {"image_fmt": "png", "rel": "icon", "dimensions": (96, 96), "prefix": "favicon"},
    {"image_fmt": "png", "rel": "icon", "dimensions": (180, 180), "prefix": "favicon"},
    {
        "image_fmt": "png",
        "rel": "apple-touch-icon",
        "dimensions": (57, 57),
        "prefix": "apple-touch-icon",
    },
    {
        "image_fmt": "png",
        "rel": "apple-touch-icon",
        "dimensions": (60, 60),
        "prefix": "apple-touch-icon",
    },
    {
        "image_fmt": "png",
        "rel": "apple-touch-icon",
        "dimensions": (72, 72),
        "prefix": "apple-touch-icon",
    },
    {
        "image_fmt": "png",
        "rel": "apple-touch-icon",
        "dimensions": (76, 76),
        "prefix": "apple-touch-icon",
    },
    {
        "image_fmt": "png",
        "rel": "apple-touch-icon",
        "dimensions": (114, 114),
        "prefix": "apple-touch-icon",
    },
    {
        "image_fmt": "png",
        "rel": "apple-touch-icon",
        "dimensions": (120, 120),
        "prefix": "apple-touch-icon",
    },
    {
        "image_fmt": "png",
        "rel": "apple-touch-icon",
        "dimensions": (144, 144),
        "prefix": "apple-touch-icon",
    },
    {
        "image_fmt": "png",
        "rel": "apple-touch-icon",
        "dimensions": (152, 152),
        "prefix": "apple-touch-icon",
    },
    {
        "image_fmt": "png",
        "rel": "apple-touch-icon",
        "dimensions": (167, 167),
        "prefix": "apple-touch-icon",
    },
    {
        "image_fmt": "png",
        "rel": "apple-touch-icon",
        "dimensions": (180, 180),
        "prefix": "apple-touch-icon",
    },
    {"image_fmt": "png", "rel": None, "dimensions": (70, 70), "prefix": "mstile"},
    {"image_fmt": "png", "rel": None, "dimensions": (270, 270), "prefix": "mstile"},
    {"image_fmt": "png", "rel": None, "dimensions": (310, 310), "prefix": "mstile"},
    {"image_fmt": "png", "rel": None, "dimensions": (310, 150), "prefix": "mstile"},
    {"image_fmt": "png", "rel": "shortcut icon", "dimensions": (196, 196), "prefix": "favicon"},
)
