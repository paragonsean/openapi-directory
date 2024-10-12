from typing import List, Dict
from aiohttp import web

from openapi_server.models.channel import Channel
from openapi_server.models.legacy_error import LegacyError
from openapi_server import util


async def get_category_channels(request: web.Request, category, direction=None, page=None, per_page=None, query=None, sort=None) -> web.Response:
    """Get all the channels in a category

    

    :param category: The name of the category.
    :type category: str
    :param direction: The sort direction of the results.
    :type direction: str
    :param page: The page number of the results to show.
    :type page: 
    :param per_page: The number of items to show on each page of results, up to a maximum of 100.
    :type per_page: 
    :param query: The search query to use to filter the results.
    :type query: str
    :param sort: The way to sort the results.
    :type sort: str

    """
    return web.Response(status=200)
