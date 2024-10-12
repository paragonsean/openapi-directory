from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.update_user_request import UpdateUserRequest
from openapi_server.models.user import User
from openapi_server import util


async def get_authenticated_user(request: web.Request, ) -> web.Response:
    """Get the authenticated user

    


    """
    return web.Response(status=200)


async def update_user(request: web.Request, body) -> web.Response:
    """Update a user

    

    :param body: User body
    :type body: dict | bytes

    """
    body = UpdateUserRequest.from_dict(body)
    return web.Response(status=200)
