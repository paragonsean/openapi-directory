from typing import List, Dict
from aiohttp import web

from openapi_server.models.cost_type import CostType
from openapi_server.models.cost_type_cursor_results import CostTypeCursorResults
from openapi_server.models.error import Error
from openapi_server import util


async def get_all_cost_types(request: web.Request, cursor=None, filter=None) -> web.Response:
    """Retrieve all Cost Types

    Use this endpoint to retrieve all Cost Types in bulk.  Max number of items returned in a single call is 1000. Use the continuation cursor parameter to set the continuation cursor for retrieval of next set of data. [pagination instructions](#section/Retrieving-data/Pagination)

    :param cursor: 
    :type cursor: str
    :param filter: 
    :type filter: str

    """
    return web.Response(status=200)


async def get_cost_type_by_id(request: web.Request, number) -> web.Response:
    """Retrieve single Cost Type

    Use this endpoint to load a single Cost Type by id/number.

    :param number: 
    :type number: int

    """
    return web.Response(status=200)


async def get_number_of_cost_types(request: web.Request, filter=None) -> web.Response:
    """Retrieve the number of Cost Types

    Call this endpoint to get the number of Cost Types. You can use a filtering as well.

    :param filter: 
    :type filter: str

    """
    return web.Response(status=200)


async def get_page_of_cost_types(request: web.Request, filter=None, sort=None, page_size=None, skip_pages=None) -> web.Response:
    """Retrieve a page of Cost Types

    Use this endpoint to load a page of Cost Types.

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
