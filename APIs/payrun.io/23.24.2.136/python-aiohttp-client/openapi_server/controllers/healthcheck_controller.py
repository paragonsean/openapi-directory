from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_model import ErrorModel
from openapi_server.models.health_check import HealthCheck
from openapi_server import util


async def get_health_check(request: web.Request, ) -> web.Response:
    """Get health check status

    Returns the health status of the application


    """
    return web.Response(status=200)
