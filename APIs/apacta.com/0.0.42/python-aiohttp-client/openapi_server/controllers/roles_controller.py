from typing import List, Dict
from aiohttp import web

from openapi_server.models.roles_get200_response import RolesGet200Response
from openapi_server import util


async def roles_get(request: web.Request, ) -> web.Response:
    """Get a list of roles

    


    """
    return web.Response(status=200)
