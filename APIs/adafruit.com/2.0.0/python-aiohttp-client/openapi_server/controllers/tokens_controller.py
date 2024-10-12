from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_token_request import CreateTokenRequest
from openapi_server.models.token import Token
from openapi_server import util


async def all_tokens(request: web.Request, username) -> web.Response:
    """All tokens for current user

    The Tokens endpoint returns information about the user&#39;s tokens. 

    :param username: a valid username string
    :type username: str

    """
    return web.Response(status=200)


async def create_token(request: web.Request, username, token) -> web.Response:
    """Create a new Token

    

    :param username: a valid username string
    :type username: str
    :param token: 
    :type token: dict | bytes

    """
    token = CreateTokenRequest.from_dict(token)
    return web.Response(status=200)


async def destroy_token(request: web.Request, username, id) -> web.Response:
    """Delete an existing Token

    

    :param username: a valid username string
    :type username: str
    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def get_token(request: web.Request, username, id) -> web.Response:
    """Returns Token based on ID

    

    :param username: a valid username string
    :type username: str
    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def replace_token(request: web.Request, username, id, token) -> web.Response:
    """Replace an existing Token

    

    :param username: a valid username string
    :type username: str
    :param id: 
    :type id: str
    :param token: 
    :type token: dict | bytes

    """
    token = CreateTokenRequest.from_dict(token)
    return web.Response(status=200)


async def update_token(request: web.Request, username, id, token) -> web.Response:
    """Update properties of an existing Token

    

    :param username: a valid username string
    :type username: str
    :param id: 
    :type id: str
    :param token: 
    :type token: dict | bytes

    """
    token = CreateTokenRequest.from_dict(token)
    return web.Response(status=200)
