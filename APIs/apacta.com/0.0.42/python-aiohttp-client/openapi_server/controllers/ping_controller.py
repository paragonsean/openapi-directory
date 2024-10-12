from typing import List, Dict
from aiohttp import web

from openapi_server.models.ping_get200_response import PingGet200Response
from openapi_server import util


async def ping_get(request: web.Request, ) -> web.Response:
    """Check if API is up and API key works

    


    """
    return web.Response(status=200)
