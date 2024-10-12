from typing import List, Dict
from aiohttp import web

from openapi_server.models.id_bean import IdBean
from openapi_server.models.permission_scheme import PermissionScheme
from openapi_server.models.project_issue_security_levels import ProjectIssueSecurityLevels
from openapi_server.models.security_scheme import SecurityScheme
from openapi_server import util


async def assign_permission_scheme(request: web.Request, project_key_or_id, body, expand=None) -> web.Response:
    """Assign permission scheme

    Assigns a permission scheme with a project. See [Managing project permissions](https://confluence.atlassian.com/x/yodKLg) for more information about permission schemes.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg)

    :param project_key_or_id: The project ID or project key (case sensitive).
    :type project_key_or_id: str
    :param body: 
    :type body: dict | bytes
    :param expand: Use [expand](#expansion) to include additional information in the response. This parameter accepts a comma-separated list. Note that permissions are included when you specify any value. Expand options include:   *  &#x60;all&#x60; Returns all expandable information.  *  &#x60;field&#x60; Returns information about the custom field granted the permission.  *  &#x60;group&#x60; Returns information about the group that is granted the permission.  *  &#x60;permissions&#x60; Returns all permission grants for each permission scheme.  *  &#x60;projectRole&#x60; Returns information about the project role granted the permission.  *  &#x60;user&#x60; Returns information about the user who is granted the permission.
    :type expand: str

    """
    body = IdBean.from_dict(body)
    return web.Response(status=200)


async def get_assigned_permission_scheme(request: web.Request, project_key_or_id, expand=None) -> web.Response:
    """Get assigned permission scheme

    Gets the [permission scheme](https://confluence.atlassian.com/x/yodKLg) associated with the project.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg) or *Administer projects* [project permission](https://confluence.atlassian.com/x/yodKLg).

    :param project_key_or_id: The project ID or project key (case sensitive).
    :type project_key_or_id: str
    :param expand: Use [expand](#expansion) to include additional information in the response. This parameter accepts a comma-separated list. Note that permissions are included when you specify any value. Expand options include:   *  &#x60;all&#x60; Returns all expandable information.  *  &#x60;field&#x60; Returns information about the custom field granted the permission.  *  &#x60;group&#x60; Returns information about the group that is granted the permission.  *  &#x60;permissions&#x60; Returns all permission grants for each permission scheme.  *  &#x60;projectRole&#x60; Returns information about the project role granted the permission.  *  &#x60;user&#x60; Returns information about the user who is granted the permission.
    :type expand: str

    """
    return web.Response(status=200)


async def get_project_issue_security_scheme(request: web.Request, project_key_or_id) -> web.Response:
    """Get project issue security scheme

    Returns the [issue security scheme](https://confluence.atlassian.com/x/J4lKLg) associated with the project.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg) or the *Administer Projects* [project permission](https://confluence.atlassian.com/x/yodKLg).

    :param project_key_or_id: The project ID or project key (case sensitive).
    :type project_key_or_id: str

    """
    return web.Response(status=200)


async def get_security_levels_for_project(request: web.Request, project_key_or_id) -> web.Response:
    """Get project issue security levels

    Returns all [issue security](https://confluence.atlassian.com/x/J4lKLg) levels for the project that the user has access to.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:** *Browse projects* [global permission](https://confluence.atlassian.com/x/x4dKLg) for the project, however, issue security levels are only returned for authenticated user with *Set Issue Security* [global permission](https://confluence.atlassian.com/x/x4dKLg) for the project.

    :param project_key_or_id: The project ID or project key (case sensitive).
    :type project_key_or_id: str

    """
    return web.Response(status=200)
