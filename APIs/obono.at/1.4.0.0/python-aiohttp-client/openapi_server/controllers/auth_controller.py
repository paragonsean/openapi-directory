from typing import List, Dict
from aiohttp import web

from openapi_server.models.auth_result import AuthResult
from openapi_server import util


async def auth_get(request: web.Request, ) -> web.Response:
    """auth_get

    Request a JWT access token using your obono username and password.


    """
    return web.Response(status=200)
