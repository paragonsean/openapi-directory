from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def keycloak_list(request: web.Request, ) -> web.Response:
    """keycloak_list

    serves keycloak config


    """
    return web.Response(status=200)
