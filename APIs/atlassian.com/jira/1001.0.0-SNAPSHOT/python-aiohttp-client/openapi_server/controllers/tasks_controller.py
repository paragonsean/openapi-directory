from typing import List, Dict
from aiohttp import web

from openapi_server.models.task_progress_bean_object import TaskProgressBeanObject
from openapi_server import util


async def cancel_task(request: web.Request, task_id) -> web.Response:
    """Cancel task

    Cancels a task.  **[Permissions](#permissions) required:** either of:   *  *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).  *  Creator of the task.

    :param task_id: The ID of the task.
    :type task_id: str

    """
    return web.Response(status=200)


async def get_task(request: web.Request, task_id) -> web.Response:
    """Get task

    Returns the status of a [long-running asynchronous task](#async).  When a task has finished, this operation returns the JSON blob applicable to the task. See the documentation of the operation that created the task for details. Task details are not permanently retained. As of September 2019, details are retained for 14 days although this period may change without notice.  **[Permissions](#permissions) required:** either of:   *  *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).  *  Creator of the task.

    :param task_id: The ID of the task.
    :type task_id: str

    """
    return web.Response(status=200)
