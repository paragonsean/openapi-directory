from typing import List, Dict
from aiohttp import web

from openapi_server.models.categories_response import CategoriesResponse
from openapi_server.models.category_error_response import CategoryErrorResponse
from openapi_server import util


async def categories_get(request: web.Request, x_api_key, kind=None) -> web.Response:
    """List of categories

    Retrieve Categories 

    :param x_api_key: API_KEY
    :type x_api_key: str
    :param kind: Filter by provided query. E.g. &#39;promoted&#39; returns promoted categories
    :type kind: str

    """
    return web.Response(status=200)


async def categories_id_get(request: web.Request, x_api_key, id) -> web.Response:
    """Category by ID

    Retrieve Categories by ID 

    :param x_api_key: API_KEY
    :type x_api_key: str
    :param id: Retrieve information about the category. E.g. &#39;sport-football-europeanchampionship&#39;
    :type id: str

    """
    return web.Response(status=200)
