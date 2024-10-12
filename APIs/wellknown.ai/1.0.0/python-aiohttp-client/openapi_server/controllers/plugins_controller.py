from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def get_provider(request: web.Request, ) -> web.Response:
    """List all the Wellknown AI Plugins.

    List all the Wellknown AI Plugins. Returns ai-plugin.json objects in an array


    """
    return web.Response(status=200)
