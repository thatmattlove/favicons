<div align="center">
  <h1>Favicons</h1>
  <h3>Favicon generator for Python 3 with strongly typed sync & async APIs, CLI, & HTML generation.</h3>
</div>

<hr/>

<div align="center">

[![PyPI](https://img.shields.io/pypi/v/favicons?style=for-the-badge)](https://pypi.org/project/favicons/)
![PyPI - Downloads](https://img.shields.io/pypi/dm/favicons?style=for-the-badge)
[![GitHub Workflow Status](https://img.shields.io/github/workflow/status/thatmattlove/favicons/Tests?style=for-the-badge)](https://github.com/thatmattlove/favicons/actions/workflows/ci.yml)

[![GitHub Contributors](https://img.shields.io/github/contributors/thatmattlove/favicons?style=for-the-badge&color=blueviolet)](https://github.com/thatmattlove/favicons)


<br/>

### [Changelog](https://github.com/thatmattlove/favicons/blob/master/CHANGELOG.md)

</div>

- [Installation](#installation)
- [Documentation](#documentation)
  - [Supported Formats](#supported-formats)
  - [CLI](#cli)
    - [`generate`](#generate)
    - [`html`](#html)
    - [`json`](#json)
    - [`names`](#names)
  - [Python Sync API](#python-sync-api)
  - [Python Async API](#python-async-api)
  - [HTML](#html-1)
  - [Tuple](#tuple)
  - [JSON](#json-1)
- [License](#license)

## Installation

```shell
pip3 install favicons
```

## Documentation

*More docs are coming. Remember, this is a work in progress.*

### Supported Formats
- SVG
- PNG
- JPEG
- TIFF

### CLI

```console
$ favicons --help

Usage: favicons [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  generate  Generate Favicons
  html      Get favicons as HTML.
  json      Get favicons as JSON.
  names     Get favicon file names.
```

#### `generate`

Generate Favicons from the command line:

```console
Usage: favicons generate [OPTIONS]

  Generate Favicons

Options:
  --source PATH                    Source Image  [required]
  --output-directory PATH          Output Directory  [required]
  --background-color TEXT          Background Color  [default: #000000]
  --transparent / --no-transparent Transparent Background  [default: True]
  --base-url TEXT                  Base URL for HTML output  [default: /]
  --help                           Show this message and exit.
```

#### `html`

Generate HTML elements (same options as `generate`).

#### `json`

Generate JSON array of favicon objects (same options as `generate`).

#### `names`

Generate list of favicon file names (same options as `generate`).

### Python Sync API

```python
from favicons import Favicons

YOUR_ICON = "/home/user/icon.jpg"
WEB_SERVER_ROOT = "/var/www/html"

with Favicons(YOUR_ICON, WEB_SERVER_ROOT) as favicons:
    favicons.generate()
    for icon in favicons.filenames():
        print(icon)

# favicon.ico
# favicon-16x16.png
# favicon-32x32.png
# favicon-64x64.png
# favicon-96x96.png
# favicon-180x180.png
# apple-touch-icon-57x57.png
# apple-touch-icon-60x60.png
# apple-touch-icon-72x72.png
# apple-touch-icon-76x76.png
# apple-touch-icon-114x114.png
# apple-touch-icon-120x120.png
# apple-touch-icon-144x144.png
# apple-touch-icon-152x152.png
# apple-touch-icon-167x167.png
# apple-touch-icon-180x180.png
# mstile-70x70.png
# mstile-270x270.png
# mstile-310x310.png
# mstile-310x150.png
# favicon-196x196.png
```

### Python Async API

```python
from favicons import Favicons

YOUR_ICON = "/home/user/icon.jpg"
WEB_SERVER_ROOT = "/var/www/html"

async with Favicons(YOUR_ICON, WEB_SERVER_ROOT) as favicons:
    await favicons.generate()
    for icon in favicons.filenames():
        print(icon)

# favicon.ico
# favicon-16x16.png
# favicon-32x32.png
# favicon-64x64.png
# favicon-96x96.png
# favicon-180x180.png
# apple-touch-icon-57x57.png
# apple-touch-icon-60x60.png
# apple-touch-icon-72x72.png
# apple-touch-icon-76x76.png
# apple-touch-icon-114x114.png
# apple-touch-icon-120x120.png
# apple-touch-icon-144x144.png
# apple-touch-icon-152x152.png
# apple-touch-icon-167x167.png
# apple-touch-icon-180x180.png
# mstile-70x70.png
# mstile-270x270.png
# mstile-310x310.png
# mstile-310x150.png
# favicon-196x196.png
```

### HTML
Get HTML elements for each generated favicon:

```python
from favicons import Favicons

YOUR_ICON = "/home/user/icon.jpg"
WEB_SERVER_ROOT = "/var/www/html"

async with Favicons(YOUR_ICON, WEB_SERVER_ROOT) as favicons:
    await favicons.generate()
    # As generator
    html = favicons.html_gen()
    # As tuple
    html = favicons.html()

print(html)
# (
#   '<link rel="None" type="image/ico" href="/favicon.ico" />',
#   '<link rel="icon" type="image/png" href="/favicon-16x16.png" />',
#   '<link rel="icon" type="image/png" href="/favicon-32x32.png" />',
#   '<link rel="icon" type="image/png" href="/favicon-64x64.png" />',
#   '<link rel="icon" type="image/png" href="/favicon-96x96.png" />',
#   '<link rel="icon" type="image/png" href="/favicon-180x180.png" />',
#   '<link rel="apple-touch-icon" type="image/png" '
#   'href="/apple-touch-icon-57x57.png" />',
#   '<link rel="apple-touch-icon" type="image/png" '
#   'href="/apple-touch-icon-60x60.png" />',
#   '<link rel="apple-touch-icon" type="image/png" '
#   'href="/apple-touch-icon-72x72.png" />',
#   '<link rel="apple-touch-icon" type="image/png" '
#   'href="/apple-touch-icon-76x76.png" />',
#   '<link rel="apple-touch-icon" type="image/png" '
#   'href="/apple-touch-icon-114x114.png" />',
#   '<link rel="apple-touch-icon" type="image/png" '
#   'href="/apple-touch-icon-120x120.png" />',
#   '<link rel="apple-touch-icon" type="image/png" '
#   'href="/apple-touch-icon-144x144.png" />',
#   '<link rel="apple-touch-icon" type="image/png" '
#   'href="/apple-touch-icon-152x152.png" />',
#   '<link rel="apple-touch-icon" type="image/png" '
#   'href="/apple-touch-icon-167x167.png" />',
#   '<link rel="apple-touch-icon" type="image/png" '
#   'href="/apple-touch-icon-180x180.png" />',
#   '<link rel="None" type="image/png" href="/mstile-70x70.png" />',
#   '<link rel="None" type="image/png" href="/mstile-270x270.png" />',
#   '<link rel="None" type="image/png" href="/mstile-310x310.png" />',
#   '<link rel="None" type="image/png" href="/mstile-310x150.png" />',
#   '<link rel="shortcut icon" type="image/png" href="/favicon-196x196.png" />'
# )
```

### Tuple
Get a Python tuple containing each generated favicon's properties:

```python
from favicons import Favicons

YOUR_ICON = "/home/user/icon.jpg"
WEB_SERVER_ROOT = "/var/www/html"

async with Favicons(YOUR_ICON, WEB_SERVER_ROOT) as favicons:
    await favicons.generate()
    as_tuple = favicons.formats()
    print(as_tuple)
# (
#   {
#     'dimensions': (64, 64),
#     'image_format': 'ico',
#     'prefix': 'favicon',
#     'rel': None
#   },
#   {
#     'dimensions': (16, 16),
#     'image_format': 'png',
#     'prefix': 'favicon',
#     'rel': 'icon'
#   },
#   {
#     'dimensions': (32, 32),
#     'image_format': 'png',
#     'prefix': 'favicon',
#     'rel': 'icon'
#   },
#   {
#     'dimensions': (64, 64),
#     'image_format': 'png',
#     'prefix': 'favicon',
#     'rel': 'icon'
#   },
#   {
#     'dimensions': (96, 96),
#     'image_format': 'png',
#     'prefix': 'favicon',
#     'rel': 'icon'
#   },
#   {
#     'dimensions': (180, 180),
#     'image_format': 'png',
#     'prefix': 'favicon',
#     'rel': 'icon'
#   },
#   {
#     'dimensions': (57, 57),
#     'image_format': 'png',
#     'prefix': 'apple-touch-icon',
#     'rel': 'apple-touch-icon'
#   },
#   {
#     'dimensions': (60, 60),
#     'image_format': 'png',
#     'prefix': 'apple-touch-icon',
#     'rel': 'apple-touch-icon'
#   },
#   {
#     'dimensions': (72, 72),
#     'image_format': 'png',
#     'prefix': 'apple-touch-icon',
#     'rel': 'apple-touch-icon'
#   },
#   {
#     'dimensions': (76, 76),
#     'image_format': 'png',
#     'prefix': 'apple-touch-icon',
#     'rel': 'apple-touch-icon'
#   },
#   {
#     'dimensions': (114, 114),
#     'image_format': 'png',
#     'prefix': 'apple-touch-icon',
#     'rel': 'apple-touch-icon'
#   },
#   {
#     'dimensions': (120, 120),
#     'image_format': 'png',
#     'prefix': 'apple-touch-icon',
#     'rel': 'apple-touch-icon'
#   },
#   {
#     'dimensions': (144, 144),
#     'image_format': 'png',
#     'prefix': 'apple-touch-icon',
#     'rel': 'apple-touch-icon'
#   },
#   {
#     'dimensions': (152, 152),
#     'image_format': 'png',
#     'prefix': 'apple-touch-icon',
#     'rel': 'apple-touch-icon'
#   },
#   {
#     'dimensions': (167, 167),
#     'image_format': 'png',
#     'prefix': 'apple-touch-icon',
#     'rel': 'apple-touch-icon'
#   },
#   {
#     'dimensions': (180, 180),
#     'image_format': 'png',
#     'prefix': 'apple-touch-icon',
#     'rel': 'apple-touch-icon'
#   },
#   {
#     'dimensions': (70, 70),
#     'image_format': 'png',
#     'prefix': 'mstile',
#     'rel': None
#   },
#   {
#     'dimensions': (270, 270),
#     'image_format': 'png',
#     'prefix': 'mstile',
#     'rel': None
#   },
#   {
#     'dimensions': (310, 310),
#     'image_format': 'png',
#     'prefix': 'mstile',
#     'rel': None
#   },
#   {
#     'dimensions': (310, 150),
#     'image_format': 'png',
#     'prefix': 'mstile',
#     'rel': None
#   },
#   {
#     'dimensions': (196, 196),
#     'image_format': 'png',
#     'prefix': 'favicon',
#     'rel': 'shortcut icon'
#   }
# )
```

### JSON
Get a JSON array containing each generated favicon's properties:

```python
from favicons import Favicons

YOUR_ICON = "/home/user/icon.jpg"
WEB_SERVER_ROOT = "/var/www/html"

async with Favicons(YOUR_ICON, WEB_SERVER_ROOT) as favicons:
    await favicons.generate()
    as_json = favicons.json(indent=2)
    print(as_json)

# [
#   {
#     "image_format": "ico",
#     "dimensions": [
#       64,
#       64
#     ],
#     "prefix": "favicon",
#     "rel": null
#   },
#   {
#     "image_format": "png",
#     "dimensions": [
#       16,
#       16
#     ],
#     "prefix": "favicon",
#     "rel": "icon"
#   },
#   {
#     "image_format": "png",
#     "dimensions": [
#       32,
#       32
#     ],
#     "prefix": "favicon",
#     "rel": "icon"
#   },
#   {
#     "image_format": "png",
#     "dimensions": [
#       64,
#       64
#     ],
#     "prefix": "favicon",
#     "rel": "icon"
#   },
#   {
#     "image_format": "png",
#     "dimensions": [
#       96,
#       96
#     ],
#     "prefix": "favicon",
#     "rel": "icon"
#   },
#   {
#     "image_format": "png",
#     "dimensions": [
#       180,
#       180
#     ],
#     "prefix": "favicon",
#     "rel": "icon"
#   },
#   {
#     "image_format": "png",
#     "dimensions": [
#       57,
#       57
#     ],
#     "prefix": "apple-touch-icon",
#     "rel": "apple-touch-icon"
#   },
#   {
#     "image_format": "png",
#     "dimensions": [
#       60,
#       60
#     ],
#     "prefix": "apple-touch-icon",
#     "rel": "apple-touch-icon"
#   },
#   {
#     "image_format": "png",
#     "dimensions": [
#       72,
#       72
#     ],
#     "prefix": "apple-touch-icon",
#     "rel": "apple-touch-icon"
#   },
#   {
#     "image_format": "png",
#     "dimensions": [
#       76,
#       76
#     ],
#     "prefix": "apple-touch-icon",
#     "rel": "apple-touch-icon"
#   },
#   {
#     "image_format": "png",
#     "dimensions": [
#       114,
#       114
#     ],
#     "prefix": "apple-touch-icon",
#     "rel": "apple-touch-icon"
#   },
#   {
#     "image_format": "png",
#     "dimensions": [
#       120,
#       120
#     ],
#     "prefix": "apple-touch-icon",
#     "rel": "apple-touch-icon"
#   },
#   {
#     "image_format": "png",
#     "dimensions": [
#       144,
#       144
#     ],
#     "prefix": "apple-touch-icon",
#     "rel": "apple-touch-icon"
#   },
#   {
#     "image_format": "png",
#     "dimensions": [
#       152,
#       152
#     ],
#     "prefix": "apple-touch-icon",
#     "rel": "apple-touch-icon"
#   },
#   {
#     "image_format": "png",
#     "dimensions": [
#       167,
#       167
#     ],
#     "prefix": "apple-touch-icon",
#     "rel": "apple-touch-icon"
#   },
#   {
#     "image_format": "png",
#     "dimensions": [
#       180,
#       180
#     ],
#     "prefix": "apple-touch-icon",
#     "rel": "apple-touch-icon"
#   },
#   {
#     "image_format": "png",
#     "dimensions": [
#       70,
#       70
#     ],
#     "prefix": "mstile",
#     "rel": null
#   },
#   {
#     "image_format": "png",
#     "dimensions": [
#       270,
#       270
#     ],
#     "prefix": "mstile",
#     "rel": null
#   },
#   {
#     "image_format": "png",
#     "dimensions": [
#       310,
#       310
#     ],
#     "prefix": "mstile",
#     "rel": null
#   },
#   {
#     "image_format": "png",
#     "dimensions": [
#       310,
#       150
#     ],
#     "prefix": "mstile",
#     "rel": null
#   },
#   {
#     "image_format": "png",
#     "dimensions": [
#       196,
#       196
#     ],
#     "prefix": "favicon",
#     "rel": "shortcut icon"
#   }
# ]
```

## License

[Clear BSD License](https://github.com/thatmattlove/blob/favicons/master/LICENSE)
