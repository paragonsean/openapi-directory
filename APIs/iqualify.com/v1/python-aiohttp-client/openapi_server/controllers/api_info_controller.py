from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def root_get(request: web.Request, ) -> web.Response:
    """List supported endpoints URLs

    Responds with all supported endpoints URLs for v2 version.


    """
    return web.Response(status=200)
