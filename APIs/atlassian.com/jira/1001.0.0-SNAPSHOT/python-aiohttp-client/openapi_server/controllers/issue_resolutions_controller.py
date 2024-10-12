from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_resolution_details import CreateResolutionDetails
from openapi_server.models.error_collection import ErrorCollection
from openapi_server.models.page_bean_resolution_json_bean import PageBeanResolutionJsonBean
from openapi_server.models.reorder_issue_resolutions_request import ReorderIssueResolutionsRequest
from openapi_server.models.resolution import Resolution
from openapi_server.models.resolution_id import ResolutionId
from openapi_server.models.set_default_resolution_request import SetDefaultResolutionRequest
from openapi_server.models.task_progress_bean_object import TaskProgressBeanObject
from openapi_server.models.update_resolution_details import UpdateResolutionDetails
from openapi_server import util


async def create_resolution(request: web.Request, body) -> web.Response:
    """Create resolution

    Creates an issue resolution.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param body: 
    :type body: dict | bytes

    """
    body = CreateResolutionDetails.from_dict(body)
    return web.Response(status=200)


async def delete_resolution(request: web.Request, id, replace_with) -> web.Response:
    """Delete resolution

    Deletes an issue resolution.  This operation is [asynchronous](#async). Follow the &#x60;location&#x60; link in the response to determine the status of the task and use [Get task](#api-rest-api-3-task-taskId-get) to obtain subsequent updates.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param id: The ID of the issue resolution.
    :type id: str
    :param replace_with: The ID of the issue resolution that will replace the currently selected resolution.
    :type replace_with: str

    """
    return web.Response(status=200)


async def get_resolution(request: web.Request, id) -> web.Response:
    """Get resolution

    Returns an issue resolution value.  **[Permissions](#permissions) required:** Permission to access Jira.

    :param id: The ID of the issue resolution value.
    :type id: str

    """
    return web.Response(status=200)


async def get_resolutions(request: web.Request, ) -> web.Response:
    """Get resolutions

    Returns a list of all issue resolution values.  **[Permissions](#permissions) required:** Permission to access Jira.


    """
    return web.Response(status=200)


async def move_resolutions(request: web.Request, body) -> web.Response:
    """Move resolutions

    Changes the order of issue resolutions.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param body: 
    :type body: dict | bytes

    """
    body = ReorderIssueResolutionsRequest.from_dict(body)
    return web.Response(status=200)


async def search_resolutions(request: web.Request, start_at=None, max_results=None, id=None, only_default=None) -> web.Response:
    """Search resolutions

    Returns a [paginated](#pagination) list of resolutions. The list can contain all resolutions or a subset determined by any combination of these criteria:   *  a list of resolutions IDs.  *  whether the field configuration is a default. This returns resolutions from company-managed (classic) projects only, as there is no concept of default resolutions in team-managed projects.  **[Permissions](#permissions) required:** Permission to access Jira.

    :param start_at: The index of the first item to return in a page of results (page offset).
    :type start_at: str
    :param max_results: The maximum number of items to return per page.
    :type max_results: str
    :param id: The list of resolutions IDs to be filtered out
    :type id: List[str]
    :param only_default: When set to true, return default only, when IDs provided, if none of them is default, return empty page. Default value is false
    :type only_default: bool

    """
    return web.Response(status=200)


async def set_default_resolution(request: web.Request, body) -> web.Response:
    """Set default resolution

    Sets default issue resolution.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param body: 
    :type body: dict | bytes

    """
    body = SetDefaultResolutionRequest.from_dict(body)
    return web.Response(status=200)


async def update_resolution(request: web.Request, id, body) -> web.Response:
    """Update resolution

    Updates an issue resolution.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param id: The ID of the issue resolution.
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateResolutionDetails.from_dict(body)
    return web.Response(status=200)
