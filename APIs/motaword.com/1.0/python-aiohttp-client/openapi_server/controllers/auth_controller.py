from typing import List, Dict
from aiohttp import web

from openapi_server.models.token import Token
from openapi_server.models.token_error import TokenError
from openapi_server.models.token_request import TokenRequest
from openapi_server import util


async def get_access_token(request: web.Request, body=None) -> web.Response:
    """Retrieve an access token

    MotaWord API is using OAuth2 procedures when authenticating or authorizing your API call. 

    :param body: 
    :type body: dict | bytes

    """
    body = TokenRequest.from_dict(body)
    return web.Response(status=200)
