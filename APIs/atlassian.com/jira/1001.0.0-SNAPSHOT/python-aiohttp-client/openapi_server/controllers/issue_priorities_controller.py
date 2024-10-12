from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_priority_details import CreatePriorityDetails
from openapi_server.models.error_collection import ErrorCollection
from openapi_server.models.page_bean_priority import PageBeanPriority
from openapi_server.models.priority import Priority
from openapi_server.models.priority_id import PriorityId
from openapi_server.models.reorder_issue_priorities import ReorderIssuePriorities
from openapi_server.models.set_default_priority_request import SetDefaultPriorityRequest
from openapi_server.models.task_progress_bean_object import TaskProgressBeanObject
from openapi_server.models.update_priority_details import UpdatePriorityDetails
from openapi_server import util


async def create_priority(request: web.Request, body) -> web.Response:
    """Create priority

    Creates an issue priority.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param body: 
    :type body: dict | bytes

    """
    body = CreatePriorityDetails.from_dict(body)
    return web.Response(status=200)


async def delete_priority(request: web.Request, id, replace_with) -> web.Response:
    """Delete priority

    Deletes an issue priority.  This operation is [asynchronous](#async). Follow the &#x60;location&#x60; link in the response to determine the status of the task and use [Get task](#api-rest-api-3-task-taskId-get) to obtain subsequent updates.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param id: The ID of the issue priority.
    :type id: str
    :param replace_with: The ID of the issue priority that will replace the currently selected resolution.
    :type replace_with: str

    """
    return web.Response(status=200)


async def get_priorities(request: web.Request, ) -> web.Response:
    """Get priorities

    Returns the list of all issue priorities.  **[Permissions](#permissions) required:** Permission to access Jira.


    """
    return web.Response(status=200)


async def get_priority(request: web.Request, id) -> web.Response:
    """Get priority

    Returns an issue priority.  **[Permissions](#permissions) required:** Permission to access Jira.

    :param id: The ID of the issue priority.
    :type id: str

    """
    return web.Response(status=200)


async def move_priorities(request: web.Request, body) -> web.Response:
    """Move priorities

    Changes the order of issue priorities.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param body: 
    :type body: dict | bytes

    """
    body = ReorderIssuePriorities.from_dict(body)
    return web.Response(status=200)


async def search_priorities(request: web.Request, start_at=None, max_results=None, id=None, only_default=None) -> web.Response:
    """Search priorities

    Returns a [paginated](#pagination) list of priorities. The list can contain all priorities or a subset determined by any combination of these criteria:   *  a list of priority IDs. Any invalid priority IDs are ignored.  *  whether the field configuration is a default. This returns priorities from company-managed (classic) projects only, as there is no concept of default priorities in team-managed projects.  **[Permissions](#permissions) required:** Permission to access Jira.

    :param start_at: The index of the first item to return in a page of results (page offset).
    :type start_at: str
    :param max_results: The maximum number of items to return per page.
    :type max_results: str
    :param id: The list of priority IDs. To include multiple IDs, provide an ampersand-separated list. For example, &#x60;id&#x3D;2&amp;id&#x3D;3&#x60;.
    :type id: List[str]
    :param only_default: Whether only the default priority is returned.
    :type only_default: bool

    """
    return web.Response(status=200)


async def set_default_priority(request: web.Request, body) -> web.Response:
    """Set default priority

    Sets default issue priority.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param body: 
    :type body: dict | bytes

    """
    body = SetDefaultPriorityRequest.from_dict(body)
    return web.Response(status=200)


async def update_priority(request: web.Request, id, body) -> web.Response:
    """Update priority

    Updates an issue priority.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param id: The ID of the issue priority.
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdatePriorityDetails.from_dict(body)
    return web.Response(status=200)
