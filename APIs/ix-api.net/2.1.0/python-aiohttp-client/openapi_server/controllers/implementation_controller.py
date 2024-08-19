from typing import List, Dict
from aiohttp import web

from openapi_server.models.implementation_response import ImplementationResponse
from openapi_server import util


async def api_implementation_read(request: web.Request, ) -> web.Response:
    """api_implementation_read

    Get the API implementation details.


    """
    return web.Response(status=200)
