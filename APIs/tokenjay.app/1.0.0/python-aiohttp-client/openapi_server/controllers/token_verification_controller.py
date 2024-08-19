from typing import List, Dict
from aiohttp import web

from openapi_server.models.check_response import CheckResponse
from openapi_server.models.genuine_token import GenuineToken
from openapi_server import util


async def check_token(request: web.Request, token_id, token_name) -> web.Response:
    """Check a token verification

    

    :param token_id: 
    :type token_id: str
    :param token_name: 
    :type token_name: str

    """
    return web.Response(status=200)


async def list_blocked(request: web.Request, ) -> web.Response:
    """Lists all blocked tokens

    


    """
    return web.Response(status=200)


async def list_genuine(request: web.Request, ) -> web.Response:
    """Lists all genuine tokens known

    


    """
    return web.Response(status=200)
