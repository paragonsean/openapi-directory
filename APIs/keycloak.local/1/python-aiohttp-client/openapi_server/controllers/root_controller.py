from typing import List, Dict
from aiohttp import web

from openapi_server.models.server_info_representation import ServerInfoRepresentation
from openapi_server import util


async def root_get(request: web.Request, ) -> web.Response:
    """Get themes, social providers, auth providers, and event listeners available on this server

    


    """
    return web.Response(status=200)
