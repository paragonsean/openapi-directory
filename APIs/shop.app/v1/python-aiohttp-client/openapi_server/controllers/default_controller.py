from typing import List, Dict
from aiohttp import web

from openapi_server.models.search_response import SearchResponse
from openapi_server import util


async def details(request: web.Request, ids) -> web.Response:
    """Return more details about a list of products.

    

    :param ids: Comma separated list of product ids
    :type ids: str

    """
    return web.Response(status=200)


async def search(request: web.Request, query=None, price_min=None, price_max=None, similar_to_id=None, num_results=None) -> web.Response:
    """Search for products

    

    :param query: Query string to search for items.
    :type query: str
    :param price_min: The minimum price to filter by.
    :type price_min: 
    :param price_max: The maximum price to filter by.
    :type price_max: 
    :param similar_to_id: A product id that you want to find similar products for. (Only include one)
    :type similar_to_id: str
    :param num_results: How many results to return. Defaults to 5. It can be a number between 1 and 10.
    :type num_results: str

    """
    return web.Response(status=200)
