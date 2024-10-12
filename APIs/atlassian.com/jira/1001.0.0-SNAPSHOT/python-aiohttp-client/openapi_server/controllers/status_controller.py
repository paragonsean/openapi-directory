from typing import List, Dict
from aiohttp import web

from openapi_server.models.jira_status import JiraStatus
from openapi_server.models.page_of_statuses import PageOfStatuses
from openapi_server.models.status_create_request import StatusCreateRequest
from openapi_server.models.status_update_request import StatusUpdateRequest
from openapi_server import util


async def create_statuses(request: web.Request, body) -> web.Response:
    """Bulk create statuses

    Creates statuses for a global or project scope.  **[Permissions](#permissions) required:**   *  *Administer projects* [project permission.](https://confluence.atlassian.com/x/yodKLg)  *  *Administer Jira* [project permission.](https://confluence.atlassian.com/x/yodKLg)

    :param body: Details of the statuses being created and their scope.
    :type body: dict | bytes

    """
    body = StatusCreateRequest.from_dict(body)
    return web.Response(status=200)


async def delete_statuses_by_id(request: web.Request, id=None) -> web.Response:
    """Bulk delete Statuses

    Deletes statuses by ID.  **[Permissions](#permissions) required:**   *  *Administer projects* [project permission.](https://confluence.atlassian.com/x/yodKLg)  *  *Administer Jira* [project permission.](https://confluence.atlassian.com/x/yodKLg)

    :param id: The list of status IDs. To include multiple IDs, provide an ampersand-separated list. For example, id&#x3D;10000&amp;id&#x3D;10001.  Min items &#x60;1&#x60;, Max items &#x60;50&#x60;
    :type id: List[str]

    """
    return web.Response(status=200)


async def get_statuses_by_id(request: web.Request, expand=None, id=None) -> web.Response:
    """Bulk get statuses

    Returns a list of the statuses specified by one or more status IDs.  **[Permissions](#permissions) required:**   *  *Administer projects* [project permission.](https://confluence.atlassian.com/x/yodKLg)  *  *Administer Jira* [project permission.](https://confluence.atlassian.com/x/yodKLg)

    :param expand: Use [expand](#expansion) to include additional information in the response. This parameter accepts a comma-separated list. Expand options include:   *  &#x60;usages&#x60; Returns the project and issue types that use the status in their workflow.
    :type expand: str
    :param id: The list of status IDs. To include multiple IDs, provide an ampersand-separated list. For example, id&#x3D;10000&amp;id&#x3D;10001.  Min items &#x60;1&#x60;, Max items &#x60;50&#x60;
    :type id: List[str]

    """
    return web.Response(status=200)


async def search(request: web.Request, expand=None, project_id=None, start_at=None, max_results=None, search_string=None, status_category=None) -> web.Response:
    """Search statuses paginated

    Returns a [paginated](https://developer.atlassian.com/cloud/jira/platform/rest/v3/intro/#pagination) list of statuses that match a search on name or project.  **[Permissions](#permissions) required:**   *  *Administer projects* [project permission.](https://confluence.atlassian.com/x/yodKLg)  *  *Administer Jira* [project permission.](https://confluence.atlassian.com/x/yodKLg)

    :param expand: Use [expand](#expansion) to include additional information in the response. This parameter accepts a comma-separated list. Expand options include:   *  &#x60;usages&#x60; Returns the project and issue types that use the status in their workflow.
    :type expand: str
    :param project_id: The project the status is part of or null for global statuses.
    :type project_id: str
    :param start_at: The index of the first item to return in a page of results (page offset).
    :type start_at: int
    :param max_results: The maximum number of items to return per page.
    :type max_results: int
    :param search_string: Term to match status names against or null to search for all statuses in the search scope.
    :type search_string: str
    :param status_category: Category of the status to filter by. The supported values are: &#x60;TODO&#x60;, &#x60;IN_PROGRESS&#x60;, and &#x60;DONE&#x60;.
    :type status_category: str

    """
    return web.Response(status=200)


async def update_statuses(request: web.Request, body) -> web.Response:
    """Bulk update statuses

    Updates statuses by ID.  **[Permissions](#permissions) required:**   *  *Administer projects* [project permission.](https://confluence.atlassian.com/x/yodKLg)  *  *Administer Jira* [project permission.](https://confluence.atlassian.com/x/yodKLg)

    :param body: The list of statuses that will be updated.
    :type body: dict | bytes

    """
    body = StatusUpdateRequest.from_dict(body)
    return web.Response(status=200)
