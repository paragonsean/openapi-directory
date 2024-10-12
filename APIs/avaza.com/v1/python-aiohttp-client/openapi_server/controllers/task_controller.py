from typing import List, Dict
from aiohttp import web

from openapi_server.models.new_task import NewTask
from openapi_server.models.task_details import TaskDetails
from openapi_server.models.task_dropdown_list import TaskDropdownList
from openapi_server.models.task_list import TaskList
from openapi_server.models.update_task import UpdateTask
from openapi_server import util


async def task_delete(request: web.Request, task_id) -> web.Response:
    """Delete a Task

    

    :param task_id: 
    :type task_id: int

    """
    return web.Response(status=200)


async def task_get(request: web.Request, updated_after=None, page_size=None, page_number=None, sort=None, is_complete=None, project_id=None) -> web.Response:
    """Gets list of Tasks

    

    :param updated_after: Optional filter to records updated after a specific date.
    :type updated_after: str
    :param page_size: Number of items per page. Defaults to 20.
    :type page_size: int
    :param page_number: Page to display. Starts from 1. Defaults to 1
    :type page_number: int
    :param sort: Optional sorting instruction. Currently possible values: \&quot;DateUpdated\&quot;, \&quot;DateCreated\&quot;, \&quot;DateUpdated desc\&quot;, \&quot;DateCreated desc\&quot;, \&quot;SectionTitle\&quot;, \&quot;Title\&quot;
    :type sort: str
    :param is_complete: Optional filter to only display tasks linked to a Task Status where isComplete&#x3D;false, or where isComplete&#x3D;true
    :type is_complete: bool
    :param project_id: Optional filter to only display tasks belonging to a specific ProjectID
    :type project_id: int

    """
    updated_after = util.deserialize_datetime(updated_after)
    return web.Response(status=200)


async def task_get_by_id(request: web.Request, id) -> web.Response:
    """Gets Task by Task ID

    

    :param id: Task ID number
    :type id: int

    """
    return web.Response(status=200)


async def task_lookup(request: web.Request, project_id, page_size=None, page_number=None, hide_completed=None, search=None) -> web.Response:
    """Gets minimal list of Tasks for the current user

    Groups Tasks by Section. Default sort is by Section Title followed by Task Title

    :param project_id: (required) The ProjectID to use when filtering Tasks
    :type project_id: int
    :param page_size: Number of items per page (max 1000)
    :type page_size: int
    :param page_number: Page to display. Starts from 1.
    :type page_number: int
    :param hide_completed: (optional) true/false to hide completed tasks. Defaults false
    :type hide_completed: bool
    :param search: (optional) Search string to match against Task title. Performs begins-with match
    :type search: str

    """
    return web.Response(status=200)


async def task_post(request: web.Request, model) -> web.Response:
    """Create a Task

    

    :param model: 
    :type model: dict | bytes

    """
    model = NewTask.from_dict(model)
    return web.Response(status=200)


async def task_put(request: web.Request, model) -> web.Response:
    """Update a Task.

    Requires TaskID and a list of field names to update. The FieldsToUpdate field accepts a string array containing field names that should be updated.

    :param model: 
    :type model: dict | bytes

    """
    model = UpdateTask.from_dict(model)
    return web.Response(status=200)
