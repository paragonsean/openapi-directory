from typing import List, Dict
from aiohttp import web

from openapi_server.models.token_request import TokenRequest
from openapi_server.models.token_response import TokenResponse
from openapi_server import util


async def auth_token(request: web.Request, body=None) -> web.Response:
    """Get token for accessing APIs

    

    :param body: 
    :type body: dict | bytes

    """
    body = TokenRequest.from_dict(body)
    return web.Response(status=200)
