from typing import List, Dict
from aiohttp import web

from openapi_server.models.server import Server
from openapi_server import util


async def server_get(request: web.Request, ) -> web.Response:
    """Fetch Server information

    


    """
    return web.Response(status=200)


async def server_put(request: web.Request, body) -> web.Response:
    """Update Server information

    

    :param body: 
    :type body: dict | bytes

    """
    body = Server.from_dict(body)
    return web.Response(status=200)
