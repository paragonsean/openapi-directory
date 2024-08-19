from typing import List, Dict
from aiohttp import web

from openapi_server.models.created_result import CreatedResult
from openapi_server.models.error import Error
from openapi_server.models.project_employee_group import ProjectEmployeeGroup
from openapi_server.models.project_employee_group_cursor_results import ProjectEmployeeGroupCursorResults
from openapi_server import util


async def create_project_employee_group(request: web.Request, body=None) -> web.Response:
    """Create a single Project employee group

    Use this endpoint to create a single Project employee group.

    :param body: 
    :type body: dict | bytes

    """
    body = ProjectEmployeeGroup.from_dict(body)
    return web.Response(status=200)


async def delete_project_employee_group_by_id(request: web.Request, number) -> web.Response:
    """Delete single Project employee group

    Use this endpoint to delete a single Project employee group by id/number.

    :param number: 
    :type number: int

    """
    return web.Response(status=200)


async def get_all_project_employee_groups(request: web.Request, cursor=None, filter=None) -> web.Response:
    """Retrieve all Project employee groups

    Use this endpoint to retrieve all Project employee groups in bulk.  Max number of items returned in a single call is 1000. Use the continuation cursor parameter to set the continuation cursor for retrieval of next set of data. [pagination instructions](#section/Retrieving-data/Pagination)

    :param cursor: 
    :type cursor: str
    :param filter: 
    :type filter: str

    """
    return web.Response(status=200)


async def get_number_of_project_employee_groups(request: web.Request, filter=None) -> web.Response:
    """Retrieve the number of Project employee groups

    Call this endpoint to get the number of Project employee groups. You can use a filtering as well.

    :param filter: 
    :type filter: str

    """
    return web.Response(status=200)


async def get_page_of_project_employee_groups(request: web.Request, filter=None, sort=None, page_size=None, skip_pages=None) -> web.Response:
    """Retrieve a page of Project employee groups

    Use this endpoint to load a page of Project employee groups.

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


async def get_project_employee_group_by_id(request: web.Request, number) -> web.Response:
    """Retrieve single Project employee group

    Use this endpoint to load a single Project employee group by id/number.

    :param number: 
    :type number: int

    """
    return web.Response(status=200)


async def update_project_employee_group(request: web.Request, body=None) -> web.Response:
    """Update a single Project employee group

    Use this endpoint to update a single Project employee group.

    :param body: 
    :type body: dict | bytes

    """
    body = ProjectEmployeeGroup.from_dict(body)
    return web.Response(status=200)
