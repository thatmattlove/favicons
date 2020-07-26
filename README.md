<div align="center">
  <h1>Favicons</h1>
  <h3>Favicon generator for Python 3 with sync & async APIs, CLI, & HTML generation.</h3>
</div>

<hr/>

<div align="center">

[![PyPI](https://img.shields.io/pypi/v/favicons?style=for-the-badge)](https://pypi.org/project/favicons/)
![PyPI - Downloads](https://img.shields.io/pypi/dm/favicons?style=for-the-badge)
[![CI](https://img.shields.io/travis/com/checktheroads/favicons?style=for-the-badge)](https://travis-ci.com/github/checktheroads/favicons)

[![GitHub Contributors](https://img.shields.io/github/contributors/checktheroads/favicons?style=for-the-badge&color=blueviolet)](https://github.com/checktheroads/favicons)


<br/>

⚠️ *This library is brand new, and is still in progress. I would strongly suggest not using it in production until this message disappears.*

</div>

### [Changelog](https://github.com/checktheroads/favicons/blob/master/CHANGELOG.md)

## Installation

```console
$ pip3 install favicons
```

## Usage

*More docs are coming. Remember, this is a work in progress.*

### CLI

*Coming soon*

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

## License

[Clear BSD License](https://github.com/checktheroads/blob/favicons/master/LICENSE)
