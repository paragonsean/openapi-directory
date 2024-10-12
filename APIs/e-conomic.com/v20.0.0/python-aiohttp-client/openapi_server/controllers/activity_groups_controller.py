from typing import List, Dict
from aiohttp import web

from openapi_server.models.activity_group import ActivityGroup
from openapi_server.models.activity_group_cursor_results import ActivityGroupCursorResults
from openapi_server.models.created_result import CreatedResult
from openapi_server.models.error import Error
from openapi_server import util


async def create_activity_group(request: web.Request, body=None) -> web.Response:
    """Create a single Activity Group

    Use this endpoint to create a single Activity Group.

    :param body: 
    :type body: dict | bytes

    """
    body = ActivityGroup.from_dict(body)
    return web.Response(status=200)


async def get_activity_group_by_id(request: web.Request, number) -> web.Response:
    """Retrieve single Activity Group

    Use this endpoint to load a single Activity Group by id/number.

    :param number: 
    :type number: int

    """
    return web.Response(status=200)


async def get_all_activity_groups(request: web.Request, cursor=None, filter=None) -> web.Response:
    """Retrieve all Activity Groups

    Use this endpoint to retrieve all Activity Groups in bulk.  Max number of items returned in a single call is 1000. Use the continuation cursor parameter to set the continuation cursor for retrieval of next set of data. [pagination instructions](#section/Retrieving-data/Pagination)

    :param cursor: 
    :type cursor: str
    :param filter: 
    :type filter: str

    """
    return web.Response(status=200)


async def get_number_of_activity_groups(request: web.Request, filter=None) -> web.Response:
    """Retrieve the number of Activity Groups

    Call this endpoint to get the number of Activity Groups. You can use a filtering as well.

    :param filter: 
    :type filter: str

    """
    return web.Response(status=200)


async def get_page_of_activity_groups(request: web.Request, filter=None, sort=None, page_size=None, skip_pages=None) -> web.Response:
    """Retrieve a page of Activity Groups

    Use this endpoint to load a page of Activity Groups.

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
