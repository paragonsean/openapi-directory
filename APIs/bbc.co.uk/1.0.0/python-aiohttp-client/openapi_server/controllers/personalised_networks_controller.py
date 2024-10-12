from typing import List, Dict
from aiohttp import web

from openapi_server.models.body2 import Body2
from openapi_server.models.body3 import Body3
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.personalised_networks_response import PersonalisedNetworksResponse
from openapi_server import util


async def my_networks_follows_delete(request: web.Request, authorization, x_api_key, body, offset=None, limit=None) -> web.Response:
    """Unfollow network

    

    :param authorization: Bearer OAUTH_TOKEN
    :type authorization: str
    :param x_api_key: API_KEY
    :type x_api_key: str
    :param body: 
    :type body: dict | bytes
    :param offset: Paginated results offset
    :type offset: int
    :param limit: Paginated results limit
    :type limit: int

    """
    body = Body3.from_dict(body)
    return web.Response(status=200)


async def my_networks_follows_get(request: web.Request, authorization, x_api_key, offset=None, limit=None) -> web.Response:
    """List of followed networks

    List of followed networks for a given user. 

    :param authorization: Bearer OAUTH_TOKEN
    :type authorization: str
    :param x_api_key: API_KEY
    :type x_api_key: str
    :param offset: Paginated results offset
    :type offset: int
    :param limit: Paginated results limit
    :type limit: int

    """
    return web.Response(status=200)


async def my_networks_follows_post(request: web.Request, authorization, x_api_key, body, offset=None, limit=None) -> web.Response:
    """Follow network

    

    :param authorization: Bearer OAUTH_TOKEN
    :type authorization: str
    :param x_api_key: API_KEY
    :type x_api_key: str
    :param body: 
    :type body: dict | bytes
    :param offset: Paginated results offset
    :type offset: int
    :param limit: Paginated results limit
    :type limit: int

    """
    body = Body2.from_dict(body)
    return web.Response(status=200)
