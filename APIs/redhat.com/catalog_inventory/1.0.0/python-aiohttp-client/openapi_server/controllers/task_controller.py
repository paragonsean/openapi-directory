from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_not_found import ErrorNotFound
from openapi_server.models.task import Task
from openapi_server.models.tasks_collection import TasksCollection
from openapi_server import util


async def list_tasks(request: web.Request, limit=None, offset=None, filter=None, sort_by=None) -> web.Response:
    """List Tasks

    Returns an array of Task objects

    :param limit: The numbers of items to return per page.
    :type limit: int
    :param offset: The number of items to skip before starting to collect the result set.
    :type offset: int
    :param filter: Filter for querying collections.
    :type filter: dict | bytes
    :type filter: Dict[str, ]
    :param sort_by: The list of attribute and order to sort the result set by.
    :type sort_by: dict | bytes
    :type sort_by: Dict[str, ]

    """
    filter = .from_dict(filter)
    sort_by = .from_dict(sort_by)
    return web.Response(status=200)


async def show_task(request: web.Request, id) -> web.Response:
    """Show an existing Task

    Returns a Task object

    :param id: UUID of task
    :type id: str

    """
    return web.Response(status=200)


async def update_task(request: web.Request, id, body) -> web.Response:
    """Update an existing Task

    Updates a Task object

    :param id: UUID of task
    :type id: str
    :param body: Task attributes to update
    :type body: dict | bytes

    """
    body = Task.from_dict(body)
    return web.Response(status=200)
