from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def api_plugins_get(request: web.Request, ) -> web.Response:
    """api_plugins_get

    Returns a list of Wellknown ai-plugins json objects from the Wellknown ai-plugins registry.


    """
    return web.Response(status=200)
