from typing import List, Dict
from aiohttp import web

from openapi_server.models.page_bean_issue_security_level_member import PageBeanIssueSecurityLevelMember
from openapi_server.models.security_level import SecurityLevel
from openapi_server import util


async def get_issue_security_level(request: web.Request, id) -> web.Response:
    """Get issue security level

    Returns details of an issue security level.  Use [Get issue security scheme](#api-rest-api-3-issuesecurityschemes-id-get) to obtain the IDs of issue security levels associated with the issue security scheme.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:** None.

    :param id: The ID of the issue security level.
    :type id: str

    """
    return web.Response(status=200)


async def get_issue_security_level_members(request: web.Request, issue_security_scheme_id, start_at=None, max_results=None, issue_security_level_id=None, expand=None) -> web.Response:
    """Get issue security level members

    Returns issue security level members.  Only issue security level members in context of classic projects are returned.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param issue_security_scheme_id: The ID of the issue security scheme. Use the [Get issue security schemes](#api-rest-api-3-issuesecurityschemes-get) operation to get a list of issue security scheme IDs.
    :type issue_security_scheme_id: int
    :param start_at: The index of the first item to return in a page of results (page offset).
    :type start_at: int
    :param max_results: The maximum number of items to return per page.
    :type max_results: int
    :param issue_security_level_id: The list of issue security level IDs. To include multiple issue security levels separate IDs with ampersand: &#x60;issueSecurityLevelId&#x3D;10000&amp;issueSecurityLevelId&#x3D;10001&#x60;.
    :type issue_security_level_id: List[int]
    :param expand: Use expand to include additional information in the response. This parameter accepts a comma-separated list. Expand options include:   *  &#x60;all&#x60; Returns all expandable information.  *  &#x60;field&#x60; Returns information about the custom field granted the permission.  *  &#x60;group&#x60; Returns information about the group that is granted the permission.  *  &#x60;projectRole&#x60; Returns information about the project role granted the permission.  *  &#x60;user&#x60; Returns information about the user who is granted the permission.
    :type expand: str

    """
    return web.Response(status=200)
