from typing import List, Dict
from aiohttp import web

from openapi_server.models.component_issues_count import ComponentIssuesCount
from openapi_server.models.page_bean_component_with_issue_count import PageBeanComponentWithIssueCount
from openapi_server.models.project_component import ProjectComponent
from openapi_server import util


async def create_component(request: web.Request, body) -> web.Response:
    """Create component

    Creates a component. Use components to provide containers for issues within a project.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:** *Administer projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project in which the component is created or *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param body: 
    :type body: dict | bytes

    """
    body = ProjectComponent.from_dict(body)
    return web.Response(status=200)


async def delete_component(request: web.Request, id, move_issues_to=None) -> web.Response:
    """Delete component

    Deletes a component.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:** *Administer projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project containing the component or *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param id: The ID of the component.
    :type id: str
    :param move_issues_to: The ID of the component to replace the deleted component. If this value is null no replacement is made.
    :type move_issues_to: str

    """
    return web.Response(status=200)


async def get_component(request: web.Request, id) -> web.Response:
    """Get component

    Returns a component.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:** *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for project containing the component.

    :param id: The ID of the component.
    :type id: str

    """
    return web.Response(status=200)


async def get_component_related_issues(request: web.Request, id) -> web.Response:
    """Get component issues count

    Returns the counts of issues assigned to the component.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:** None.

    :param id: The ID of the component.
    :type id: str

    """
    return web.Response(status=200)


async def get_project_components(request: web.Request, project_id_or_key) -> web.Response:
    """Get project components

    Returns all components in a project. See the [Get project components paginated](#api-rest-api-3-project-projectIdOrKey-component-get) resource if you want to get a full list of components with pagination.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:** *Browse Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.

    :param project_id_or_key: The project ID or project key (case sensitive).
    :type project_id_or_key: str

    """
    return web.Response(status=200)


async def get_project_components_paginated(request: web.Request, project_id_or_key, start_at=None, max_results=None, order_by=None, query=None) -> web.Response:
    """Get project components paginated

    Returns a [paginated](#pagination) list of all components in a project. See the [Get project components](#api-rest-api-3-project-projectIdOrKey-components-get) resource if you want to get a full list of versions without pagination.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:** *Browse Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.

    :param project_id_or_key: The project ID or project key (case sensitive).
    :type project_id_or_key: str
    :param start_at: The index of the first item to return in a page of results (page offset).
    :type start_at: int
    :param max_results: The maximum number of items to return per page.
    :type max_results: int
    :param order_by: [Order](#ordering) the results by a field:   *  &#x60;description&#x60; Sorts by the component description.  *  &#x60;issueCount&#x60; Sorts by the count of issues associated with the component.  *  &#x60;lead&#x60; Sorts by the user key of the component&#39;s project lead.  *  &#x60;name&#x60; Sorts by component name.
    :type order_by: str
    :param query: Filter the results using a literal string. Components with a matching &#x60;name&#x60; or &#x60;description&#x60; are returned (case insensitive).
    :type query: str

    """
    return web.Response(status=200)


async def update_component(request: web.Request, id, body) -> web.Response:
    """Update component

    Updates a component. Any fields included in the request are overwritten. If &#x60;leadAccountId&#x60; is an empty string (\&quot;\&quot;) the component lead is removed.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:** *Administer projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project containing the component or *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param id: The ID of the component.
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = ProjectComponent.from_dict(body)
    return web.Response(status=200)
