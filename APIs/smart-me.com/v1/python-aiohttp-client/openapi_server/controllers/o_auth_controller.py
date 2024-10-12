from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def api_oauth_authorize_post(request: web.Request, client_id, redirect_uri, state, scope=None, client_secret=None) -> web.Response:
    """api_oauth_authorize_post

    

    :param client_id: 
    :type client_id: str
    :param redirect_uri: 
    :type redirect_uri: str
    :param state: 
    :type state: str
    :param scope: 
    :type scope: str
    :param client_secret: 
    :type client_secret: str

    """
    return web.Response(status=200)


async def o_auth_authorize(request: web.Request, client_id, redirect_uri, state, scope=None, client_secret=None) -> web.Response:
    """o_auth_authorize

    

    :param client_id: 
    :type client_id: str
    :param redirect_uri: 
    :type redirect_uri: str
    :param state: 
    :type state: str
    :param scope: 
    :type scope: str
    :param client_secret: 
    :type client_secret: str

    """
    return web.Response(status=200)
