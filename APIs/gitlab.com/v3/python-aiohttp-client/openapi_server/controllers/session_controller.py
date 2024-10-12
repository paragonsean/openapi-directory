from typing import List, Dict
from aiohttp import web

from openapi_server.models.post_v3_session_request import PostV3SessionRequest
from openapi_server.models.user_with_private_token import UserWithPrivateToken
from openapi_server import util


async def post_v3_session(request: web.Request, body) -> web.Response:
    """Login to get token

    Login to get token

    :param body: 
    :type body: dict | bytes

    """
    body = PostV3SessionRequest.from_dict(body)
    return web.Response(status=200)
