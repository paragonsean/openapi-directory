from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def favico_favicon_ico_get(request: web.Request, ) -> web.Response:
    """Favico

    


    """
    return web.Response(status=200)


async def pong_ping_get(request: web.Request, ) -> web.Response:
    """Pong

    Sanity check. This will let the user know that the service is operational. And this path operation will: * show a lifesign


    """
    return web.Response(status=200)
