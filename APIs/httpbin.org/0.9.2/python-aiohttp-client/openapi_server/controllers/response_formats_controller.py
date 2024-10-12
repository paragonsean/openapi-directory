from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def brotli_get(request: web.Request, ) -> web.Response:
    """Returns Brotli-encoded data.

    


    """
    return web.Response(status=200)


async def deflate_get(request: web.Request, ) -> web.Response:
    """Returns Deflate-encoded data.

    


    """
    return web.Response(status=200)


async def deny_get(request: web.Request, ) -> web.Response:
    """Returns page denied by robots.txt rules.

    


    """
    return web.Response(status=200)


async def encoding_utf8_get(request: web.Request, ) -> web.Response:
    """Returns a UTF-8 encoded body.

    


    """
    return web.Response(status=200)


async def gzip_get(request: web.Request, ) -> web.Response:
    """Returns GZip-encoded data.

    


    """
    return web.Response(status=200)


async def html_get(request: web.Request, ) -> web.Response:
    """Returns a simple HTML document.

    


    """
    return web.Response(status=200)


async def json_get(request: web.Request, ) -> web.Response:
    """Returns a simple JSON document.

    


    """
    return web.Response(status=200)


async def robots_txt_get(request: web.Request, ) -> web.Response:
    """Returns some robots.txt rules.

    


    """
    return web.Response(status=200)


async def xml_get(request: web.Request, ) -> web.Response:
    """Returns a simple XML document.

    


    """
    return web.Response(status=200)
