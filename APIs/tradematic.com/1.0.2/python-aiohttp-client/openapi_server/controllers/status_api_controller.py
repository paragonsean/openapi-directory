from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.time_get200_response import TimeGet200Response
from openapi_server import util


async def ping_get(request: web.Request, ) -> web.Response:
    """Ping

    Ping


    """
    return web.Response(status=200)


async def time_get(request: web.Request, ) -> web.Response:
    """Get current server time

    Get current server time


    """
    return web.Response(status=200)
