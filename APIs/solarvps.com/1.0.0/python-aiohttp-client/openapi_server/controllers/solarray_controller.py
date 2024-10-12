from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def solarray_critical_get(request: web.Request, ) -> web.Response:
    """View all your critical notifications

    Shows all your critical notifications


    """
    return web.Response(status=200)


async def solarray_get(request: web.Request, ) -> web.Response:
    """View all your monitors

    Shows all your monitors


    """
    return web.Response(status=200)
