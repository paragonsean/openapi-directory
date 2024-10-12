from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def backend_module_service_v1_get_modules_get(request: web.Request, ) -> web.Response:
    """modules

    Returns an array of enabled modules


    """
    return web.Response(status=200)
