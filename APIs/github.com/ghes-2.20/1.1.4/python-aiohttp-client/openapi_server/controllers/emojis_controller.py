from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def emojis_get(request: web.Request, ) -> web.Response:
    """Get emojis

    Lists all the emojis available to use on GitHub Enterprise Server.


    """
    return web.Response(status=200)
