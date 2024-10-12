from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_server_health200_response import GetServerHealth200Response
from openapi_server import util


async def get_heartbeat(request: web.Request, ) -> web.Response:
    """Ping the server for liveness

    


    """
    return web.Response(status=200)


async def get_server_health(request: web.Request, ) -> web.Response:
    """Get state of the server and its dependencies.

    


    """
    return web.Response(status=200)
