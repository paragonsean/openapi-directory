from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.token_response_if import TokenResponseIF
from openapi_server import util


async def post_oauth_v1_token_create(request: web.Request, client_id=None, client_secret=None, code=None, grant_type=None, redirect_uri=None, refresh_token=None) -> web.Response:
    """post_oauth_v1_token_create

    

    :param client_id: 
    :type client_id: str
    :param client_secret: 
    :type client_secret: str
    :param code: 
    :type code: str
    :param grant_type: 
    :type grant_type: str
    :param redirect_uri: 
    :type redirect_uri: str
    :param refresh_token: 
    :type refresh_token: str

    """
    return web.Response(status=200)
