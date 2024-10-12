from typing import List, Dict
from aiohttp import web

from openapi_server.models.access_token_info_response import AccessTokenInfoResponse
from openapi_server.models.error import Error
from openapi_server import util


async def get_oauth_v1_access_tokens_token_get(request: web.Request, token) -> web.Response:
    """get_oauth_v1_access_tokens_token_get

    

    :param token: 
    :type token: str

    """
    return web.Response(status=200)
