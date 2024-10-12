from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.refresh_token_info_response import RefreshTokenInfoResponse
from openapi_server import util


async def delete_oauth_v1_refresh_tokens_token_archive(request: web.Request, token) -> web.Response:
    """delete_oauth_v1_refresh_tokens_token_archive

    

    :param token: 
    :type token: str

    """
    return web.Response(status=200)


async def get_oauth_v1_refresh_tokens_token_get(request: web.Request, token) -> web.Response:
    """get_oauth_v1_refresh_tokens_token_get

    

    :param token: 
    :type token: str

    """
    return web.Response(status=200)
