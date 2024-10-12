from typing import List, Dict
from aiohttp import web

from openapi_server.models.problem_details import ProblemDetails
from openapi_server.models.task_info import TaskInfo
from openapi_server.models.task_trigger_info import TaskTriggerInfo
from openapi_server import util


async def get_task(request: web.Request, task_id) -> web.Response:
    """Get task by id.

    

    :param task_id: Task Id.
    :type task_id: str

    """
    return web.Response(status=200)


async def get_tasks(request: web.Request, is_hidden=None, is_enabled=None) -> web.Response:
    """Get tasks.

    

    :param is_hidden: Optional filter tasks that are hidden, or not.
    :type is_hidden: bool
    :param is_enabled: Optional filter tasks that are enabled, or not.
    :type is_enabled: bool

    """
    return web.Response(status=200)


async def start_task(request: web.Request, task_id) -> web.Response:
    """Start specified task.

    

    :param task_id: Task Id.
    :type task_id: str

    """
    return web.Response(status=200)


async def stop_task(request: web.Request, task_id) -> web.Response:
    """Stop specified task.

    

    :param task_id: Task Id.
    :type task_id: str

    """
    return web.Response(status=200)


async def update_task(request: web.Request, task_id, body) -> web.Response:
    """Update specified task triggers.

    

    :param task_id: Task Id.
    :type task_id: str
    :param body: Triggers.
    :type body: list | bytes

    """
    body = [TaskTriggerInfo.from_dict(d) for d in body]
    return web.Response(status=200)
