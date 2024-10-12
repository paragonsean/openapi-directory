from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.source import Source
from openapi_server import util


async def list(request: web.Request, ) -> web.Response:
    """list

    Returns list of sources


    """
    return web.Response(status=200)
