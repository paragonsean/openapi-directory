from typing import List, Dict
from aiohttp import web

from openapi_server.models.login_dto import LoginDTO
from openapi_server import util


async def auth_login(request: web.Request, body) -> web.Response:
    """Authenticate and provide token for autherizations.             

    

    :param body: Login Credentials
    :type body: dict | bytes

    """
    body = LoginDTO.from_dict(body)
    return web.Response(status=200)
