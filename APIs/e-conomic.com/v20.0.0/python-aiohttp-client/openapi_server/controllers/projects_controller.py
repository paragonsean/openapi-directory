from typing import List, Dict
from aiohttp import web

from openapi_server.models.created_result import CreatedResult
from openapi_server.models.error import Error
from openapi_server.models.project import Project
from openapi_server.models.project_cursor_results import ProjectCursorResults
from openapi_server import util


async def create_project(request: web.Request, body=None) -> web.Response:
    """Create a single Project

    Use this endpoint to create a single Project.

    :param body: 
    :type body: dict | bytes

    """
    body = Project.from_dict(body)
    return web.Response(status=200)


async def delete_project_by_id(request: web.Request, number) -> web.Response:
    """Delete single Project

    Use this endpoint to delete a single Project by id/number.

    :param number: 
    :type number: int

    """
    return web.Response(status=200)


async def get_all_projects(request: web.Request, cursor=None, filter=None) -> web.Response:
    """Retrieve all Projects

    Use this endpoint to retrieve all Projects in bulk.  Max number of items returned in a single call is 1000. Use the continuation cursor parameter to set the continuation cursor for retrieval of next set of data. [pagination instructions](#section/Retrieving-data/Pagination)

    :param cursor: 
    :type cursor: str
    :param filter: 
    :type filter: str

    """
    return web.Response(status=200)


async def get_number_of_projects(request: web.Request, filter=None) -> web.Response:
    """Retrieve the number of Projects

    Call this endpoint to get the number of Projects. You can use a filtering as well.

    :param filter: 
    :type filter: str

    """
    return web.Response(status=200)


async def get_page_of_projects(request: web.Request, filter=None, sort=None, page_size=None, skip_pages=None) -> web.Response:
    """Retrieve a page of Projects

    Use this endpoint to load a page of Projects.

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


async def get_paged_list_of_project_under_employee(request: web.Request, employee_number) -> web.Response:
    """Retrieve the allowed projects that employee can register an entry on.

    Use this endpoint to get all the projects that the employee is allowed to register an entry on. Potential restrictions of registration are based on recording rules in the UI, which cannot be modified through the API. Add the employee number to your query parameter to obtain the allowed projects for registrations.

    :param employee_number: The employee number.
    :type employee_number: int

    """
    return web.Response(status=200)


async def get_project_by_id(request: web.Request, number) -> web.Response:
    """Retrieve single Project

    Use this endpoint to load a single Project by id/number.

    :param number: 
    :type number: int

    """
    return web.Response(status=200)


async def update_project(request: web.Request, body=None) -> web.Response:
    """Update a single Project

    Use this endpoint to update a single Project.

    :param body: 
    :type body: dict | bytes

    """
    body = Project.from_dict(body)
    return web.Response(status=200)
