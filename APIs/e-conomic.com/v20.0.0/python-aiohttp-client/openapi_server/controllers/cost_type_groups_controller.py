from typing import List, Dict
from aiohttp import web

from openapi_server.models.cost_type_group import CostTypeGroup
from openapi_server.models.cost_type_group_cursor_results import CostTypeGroupCursorResults
from openapi_server.models.error import Error
from openapi_server import util


async def get_all_cost_type_groups(request: web.Request, cursor=None, filter=None) -> web.Response:
    """Retrieve all Cost Type Groups

    Use this endpoint to retrieve all Cost Type Groups in bulk.  Max number of items returned in a single call is 1000. Use the continuation cursor parameter to set the continuation cursor for retrieval of next set of data. [pagination instructions](#section/Retrieving-data/Pagination)

    :param cursor: 
    :type cursor: str
    :param filter: 
    :type filter: str

    """
    return web.Response(status=200)


async def get_cost_type_group_by_id(request: web.Request, number) -> web.Response:
    """Retrieve single Cost Type Group

    Use this endpoint to load a single Cost Type Group by id/number.

    :param number: 
    :type number: int

    """
    return web.Response(status=200)


async def get_number_of_cost_type_groups(request: web.Request, filter=None) -> web.Response:
    """Retrieve the number of Cost Type Groups

    Call this endpoint to get the number of Cost Type Groups. You can use a filtering as well.

    :param filter: 
    :type filter: str

    """
    return web.Response(status=200)


async def get_page_of_cost_type_groups(request: web.Request, filter=None, sort=None, page_size=None, skip_pages=None) -> web.Response:
    """Retrieve a page of Cost Type Groups

    Use this endpoint to load a page of Cost Type Groups.

    :param filter: 
    :type filter: str
    :param sort: 
    :type sort: str
    :param page_size: 
    :type page_size: int
    :param skip_pages: 
    :type skip_pages: int

    """
    return web.Response(status=200)
