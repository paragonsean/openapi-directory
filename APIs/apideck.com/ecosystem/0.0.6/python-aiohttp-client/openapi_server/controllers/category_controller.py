from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_categories_response import GetCategoriesResponse
from openapi_server.models.get_category_response import GetCategoryResponse
from openapi_server.models.get_listings_response import GetListingsResponse
from openapi_server import util


async def categories_all(request: web.Request, ecosystem_id, cursor=None, limit=None) -> web.Response:
    """List categories

    List categories

    :param ecosystem_id: 
    :type ecosystem_id: str
    :param cursor: Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.
    :type cursor: str
    :param limit: Number of records to return
    :type limit: int

    """
    return web.Response(status=200)


async def categories_one(request: web.Request, ecosystem_id, id) -> web.Response:
    """Get category

    Get category

    :param ecosystem_id: 
    :type ecosystem_id: str
    :param id: ID of the record you are acting upon.
    :type id: str

    """
    return web.Response(status=200)


async def category_listings_all(request: web.Request, ecosystem_id, id, cursor=None, limit=None) -> web.Response:
    """List category listings

    List category listings

    :param ecosystem_id: 
    :type ecosystem_id: str
    :param id: ID of the record you are acting upon.
    :type id: str
    :param cursor: Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.
    :type cursor: str
    :param limit: Number of records to return
    :type limit: int

    """
    return web.Response(status=200)
