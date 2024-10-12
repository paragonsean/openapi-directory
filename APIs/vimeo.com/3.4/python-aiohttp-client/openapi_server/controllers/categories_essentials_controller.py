from typing import List, Dict
from aiohttp import web

from openapi_server.models.category import Category
from openapi_server.models.legacy_error import LegacyError
from openapi_server import util


async def get_categories(request: web.Request, direction=None, page=None, per_page=None, sort=None) -> web.Response:
    """Get all categories

    This method gets all existing categories.

    :param direction: The sort direction of the results.
    :type direction: str
    :param page: The page number of the results to show.
    :type page: 
    :param per_page: The number of items to show on each page of results, up to a maximum of 100.
    :type per_page: 
    :param sort: The way to sort the results.
    :type sort: str

    """
    return web.Response(status=200)


async def get_category(request: web.Request, category) -> web.Response:
    """Get a specific category

    

    :param category: The name of the category.
    :type category: str

    """
    return web.Response(status=200)
