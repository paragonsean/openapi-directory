from typing import List, Dict
from aiohttp import web

from openapi_server.models.fetch_health_check200_response import FetchHealthCheck200Response
from openapi_server import util


async def fetch_health_check(request: web.Request, ) -> web.Response:
    """fetch_health_check

    API HealthCheck


    """
    return web.Response(status=200)
