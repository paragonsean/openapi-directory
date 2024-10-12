from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def image_get(request: web.Request, ) -> web.Response:
    """Returns a simple image of the type suggest by the Accept header.

    


    """
    return web.Response(status=200)


async def image_jpeg_get(request: web.Request, ) -> web.Response:
    """Returns a simple JPEG image.

    


    """
    return web.Response(status=200)


async def image_png_get(request: web.Request, ) -> web.Response:
    """Returns a simple PNG image.

    


    """
    return web.Response(status=200)


async def image_svg_get(request: web.Request, ) -> web.Response:
    """Returns a simple SVG image.

    


    """
    return web.Response(status=200)


async def image_webp_get(request: web.Request, ) -> web.Response:
    """Returns a simple WEBP image.

    


    """
    return web.Response(status=200)
