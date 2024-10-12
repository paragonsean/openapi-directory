from typing import List, Dict
from aiohttp import web

from openapi_server.models.health_check_read import HealthCheckRead
from openapi_server import util


async def get_health_check(request: web.Request, ) -> web.Response:
    """Health Check

    


    """
    return web.Response(status=200)
