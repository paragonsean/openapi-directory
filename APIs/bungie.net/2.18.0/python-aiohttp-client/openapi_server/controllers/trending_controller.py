from typing import List, Dict
from aiohttp import web

from openapi_server.models.trending_get_trending_categories200_response import TrendingGetTrendingCategories200Response
from openapi_server.models.trending_get_trending_category200_response import TrendingGetTrendingCategory200Response
from openapi_server.models.trending_get_trending_entry_detail200_response import TrendingGetTrendingEntryDetail200Response
from openapi_server import util


async def trending_get_trending_categories(request: web.Request, ) -> web.Response:
    """trending_get_trending_categories

    Returns trending items for Bungie.net, collapsed into the first page of items per category. For pagination within a category, call GetTrendingCategory.


    """
    return web.Response(status=200)


async def trending_get_trending_category(request: web.Request, category_id, page_number) -> web.Response:
    """trending_get_trending_category

    Returns paginated lists of trending items for a category.

    :param category_id: The ID of the category for whom you want additional results.
    :type category_id: str
    :param page_number: The page # of results to return.
    :type page_number: int

    """
    return web.Response(status=200)


async def trending_get_trending_entry_detail(request: web.Request, identifier, trending_entry_type) -> web.Response:
    """trending_get_trending_entry_detail

    Returns the detailed results for a specific trending entry. Note that trending entries are uniquely identified by a combination of *both* the TrendingEntryType *and* the identifier: the identifier alone is not guaranteed to be globally unique.

    :param identifier: The identifier for the entity to be returned.
    :type identifier: str
    :param trending_entry_type: The type of entity to be returned.
    :type trending_entry_type: int

    """
    return web.Response(status=200)
