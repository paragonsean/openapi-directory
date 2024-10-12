from typing import List, Dict
from aiohttp import web

from openapi_server.models.check_get_default_response import CheckGetDefaultResponse
from openapi_server import util


async def store_get(request: web.Request, ) -> web.Response:
    """Get Fortnite Store

    


    """
    return web.Response(status=200)
