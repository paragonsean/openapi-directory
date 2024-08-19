from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_health import ApiHealth
from openapi_server.models.error import Error
from openapi_server import util


async def payments_health_get(request: web.Request, ) -> web.Response:
    """Returns the status of each connectivity provider

    Returns the status of each connectivity provider


    """
    return web.Response(status=200)
