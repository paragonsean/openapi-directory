from typing import List, Dict
from aiohttp import web

from openapi_server.models.health_response import HealthResponse
from openapi_server import util


async def api_health_read(request: web.Request, ) -> web.Response:
    """api_health_read

    Get the IX-API service health status.


    """
    return web.Response(status=200)
