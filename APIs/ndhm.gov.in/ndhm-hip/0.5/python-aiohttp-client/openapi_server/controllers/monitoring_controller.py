from typing import List, Dict
from aiohttp import web

from openapi_server.models.heartbeat_response import HeartbeatResponse
from openapi_server import util


async def v05_heartbeat_get(request: web.Request, ) -> web.Response:
    """Get consent request status

    


    """
    return web.Response(status=200)
