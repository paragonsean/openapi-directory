from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def health_check_ping_get(request: web.Request, ) -> web.Response:
    """Health check for API

    Provides a response for automatic checks that the API and load balancers are healthy


    """
    return web.Response(status=200)
