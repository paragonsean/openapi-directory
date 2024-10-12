from typing import List, Dict
from aiohttp import web

from openapi_server.models.activity import Activity
from openapi_server.models.activity_cursor_results import ActivityCursorResults
from openapi_server.models.created_result import CreatedResult
from openapi_server.models.error import Error
from openapi_server import util


async def create_activity(request: web.Request, body=None) -> web.Response:
    """Create a single Activity

    Use this endpoint to create a single Activity.

    :param body: 
    :type body: dict | bytes

    """
    body = Activity.from_dict(body)
    return web.Response(status=200)


async def get_activity_by_id(request: web.Request, number) -> web.Response:
    """Retrieve single Activity

    Use this endpoint to load a single Activity by id/number.

    :param number: 
    :type number: int

    """
    return web.Response(status=200)


async def get_all_activities(request: web.Request, cursor=None, filter=None) -> web.Response:
    """Retrieve all Activities

    Use this endpoint to retrieve all Activities in bulk.  Max number of items returned in a single call is 1000. Use the continuation cursor parameter to set the continuation cursor for retrieval of next set of data. [pagination instructions](#section/Retrieving-data/Pagination)

    :param cursor: 
    :type cursor: str
    :param filter: 
    :type filter: str

    """
    return web.Response(status=200)


async def get_allowed_activities(request: web.Request, employee_number, project_number) -> web.Response:
    """Retrieve allowed activities

    Use this endpoint to get all the activities that the employee is allowed to register an entry on for a given project. Potential restrictions of registration are based on recording rules in the UI, which cannot be modified through the API. Add the employee number and project to your query parameter to obtain the allowed activities for registrations.

    :param employee_number: The employee number.
    :type employee_number: int
    :param project_number: The project number.
    :type project_number: int

    """
    return web.Response(status=200)


async def get_number_of_activities(request: web.Request, filter=None) -> web.Response:
    """Retrieve the number of Activities

    Call this endpoint to get the number of Activities. You can use a filtering as well.

    :param filter: 
    :type filter: str

    """
    return web.Response(status=200)


async def get_page_of_activities(request: web.Request, filter=None, sort=None, page_size=None, skip_pages=None) -> web.Response:
    """Retrieve a page of Activities

    Use this endpoint to load a page of Activities.

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


async def update_activity(request: web.Request, body=None) -> web.Response:
    """Update a single Activity

    Use this endpoint to update a single Activity.

    :param body: 
    :type body: dict | bytes

    """
    body = Activity.from_dict(body)
    return web.Response(status=200)
