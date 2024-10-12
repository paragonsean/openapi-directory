from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_user_in_group_request import CreateUserInGroupRequest
from openapi_server import util


async def create_user_in_group(request: web.Request, activate=None, body=None) -> web.Response:
    """Create User in Group

    Create User in Group

    :param activate: 
    :type activate: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateUserInGroupRequest.from_dict(body)
    return web.Response(status=200)
