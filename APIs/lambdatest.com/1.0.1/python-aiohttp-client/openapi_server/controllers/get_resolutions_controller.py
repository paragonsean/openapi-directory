from typing import List, Dict
from aiohttp import web

from openapi_server.models.access_denied import AccessDenied
from openapi_server.models.resolutions import Resolutions
from openapi_server import util


async def resolutions(request: web.Request, ) -> web.Response:
    """Fetch all available resolution on different OS

    Fetch all available resolution on different OS


    """
    return web.Response(status=200)
