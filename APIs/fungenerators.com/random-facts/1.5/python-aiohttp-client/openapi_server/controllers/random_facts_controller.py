from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def fact_categories_get(request: web.Request, start=None) -> web.Response:
    """fact_categories_get

    Get a random Fact.

    :param start: start
    :type start: int

    """
    return web.Response(status=200)


async def fact_get(request: web.Request, id=None) -> web.Response:
    """fact_get

    Get a Fact belonging to the id.

    :param id: ID of the fact to fetch
    :type id: str

    """
    return web.Response(status=200)


async def fact_random_get(request: web.Request, category=None, subcategory=None) -> web.Response:
    """fact_random_get

    Get a random Fact for a given category(optional) and subcategory(optional).

    :param category: Category to get the fact from
    :type category: str
    :param subcategory: Sub Category to get the fact from
    :type subcategory: str

    """
    return web.Response(status=200)


async def fact_search_get(request: web.Request, query=None, category=None, subcategory=None) -> web.Response:
    """fact_search_get

    Search for random Fact which has the text in the query, for a given category(optional) and subcategory(optional).

    :param query: Text to search for in the facts
    :type query: str
    :param category: Category to get the fact from
    :type category: str
    :param subcategory: Sub Category to get the fact from
    :type subcategory: str

    """
    return web.Response(status=200)
