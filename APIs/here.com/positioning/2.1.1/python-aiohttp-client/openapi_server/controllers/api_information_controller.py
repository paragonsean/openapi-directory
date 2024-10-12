from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_health_status import ApiHealthStatus
from openapi_server.models.api_version import ApiVersion
from openapi_server import util


async def get_api_version(request: web.Request, ) -> web.Response:
    """API version

    Retrieves API Specification version information


    """
    return web.Response(status=200)


async def get_health(request: web.Request, ) -> web.Response:
    """Service health

    Tests basic health of the service


    """
    return web.Response(status=200)
