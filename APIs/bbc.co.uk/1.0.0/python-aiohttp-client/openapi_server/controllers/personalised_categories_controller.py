from typing import List, Dict
from aiohttp import web

from openapi_server.models.body import Body
from openapi_server.models.body1 import Body1
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.personalised_categories_response import PersonalisedCategoriesResponse
from openapi_server import util


async def my_categories_follows_delete(request: web.Request, authorization, x_api_key, body) -> web.Response:
    """Unfollow category

    

    :param authorization: Bearer OAUTH_TOKEN
    :type authorization: str
    :param x_api_key: API_KEY
    :type x_api_key: str
    :param body: 
    :type body: dict | bytes

    """
    body = Body1.from_dict(body)
    return web.Response(status=200)


async def my_categories_follows_get(request: web.Request, authorization, x_api_key, offset=None, limit=None) -> web.Response:
    """List of followed categories

    List of followed categories for a given user. 

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


async def my_categories_follows_post(request: web.Request, authorization, x_api_key, body) -> web.Response:
    """Follow category

    

    :param authorization: Bearer OAUTH_TOKEN
    :type authorization: str
    :param x_api_key: API_KEY
    :type x_api_key: str
    :param body: 
    :type body: dict | bytes

    """
    body = Body.from_dict(body)
    return web.Response(status=200)
