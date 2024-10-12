from typing import List, Dict
from aiohttp import web

from openapi_server.models.avatar import Avatar
from openapi_server.models.issue_type_create_bean import IssueTypeCreateBean
from openapi_server.models.issue_type_details import IssueTypeDetails
from openapi_server.models.issue_type_update_bean import IssueTypeUpdateBean
from openapi_server import util


async def create_issue_type(request: web.Request, body) -> web.Response:
    """Create issue type

    Creates an issue type and adds it to the default issue type scheme.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param body: 
    :type body: dict | bytes

    """
    body = IssueTypeCreateBean.from_dict(body)
    return web.Response(status=200)


async def create_issue_type_avatar(request: web.Request, id, size, body, x=None, y=None) -> web.Response:
    """Load issue type avatar

    Loads an avatar for the issue type.  Specify the avatar&#39;s local file location in the body of the request. Also, include the following headers:   *  &#x60;X-Atlassian-Token: no-check&#x60; To prevent XSRF protection blocking the request, for more information see [Special Headers](#special-request-headers).  *  &#x60;Content-Type: image/image type&#x60; Valid image types are JPEG, GIF, or PNG.  For example:   &#x60;curl --request POST \\ --user email@example.com:&lt;api_token&gt; \\ --header &#39;X-Atlassian-Token: no-check&#39; \\ --header &#39;Content-Type: image/&lt; image_type&gt;&#39; \\ --data-binary \&quot;&lt;@/path/to/file/with/your/avatar&gt;\&quot; \\ --url &#39;https://your-domain.atlassian.net/rest/api/3/issuetype/{issueTypeId}&#39;This&#x60;  The avatar is cropped to a square. If no crop parameters are specified, the square originates at the top left of the image. The length of the square&#39;s sides is set to the smaller of the height or width of the image.  The cropped image is then used to create avatars of 16x16, 24x24, 32x32, and 48x48 in size.  After creating the avatar, use [ Update issue type](#api-rest-api-3-issuetype-id-put) to set it as the issue type&#39;s displayed avatar.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param id: The ID of the issue type.
    :type id: str
    :param size: The length of each side of the crop region.
    :type size: int
    :param body: 
    :type body: 
    :param x: The X coordinate of the top-left corner of the crop region.
    :type x: int
    :param y: The Y coordinate of the top-left corner of the crop region.
    :type y: int

    """
    return web.Response(status=200)


async def delete_issue_type(request: web.Request, id, alternative_issue_type_id=None) -> web.Response:
    """Delete issue type

    Deletes the issue type. If the issue type is in use, all uses are updated with the alternative issue type (&#x60;alternativeIssueTypeId&#x60;). A list of alternative issue types are obtained from the [Get alternative issue types](#api-rest-api-3-issuetype-id-alternatives-get) resource.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param id: The ID of the issue type.
    :type id: str
    :param alternative_issue_type_id: The ID of the replacement issue type.
    :type alternative_issue_type_id: str

    """
    return web.Response(status=200)


async def get_alternative_issue_types(request: web.Request, id) -> web.Response:
    """Get alternative issue types

    Returns a list of issue types that can be used to replace the issue type. The alternative issue types are those assigned to the same workflow scheme, field configuration scheme, and screen scheme.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:** None.

    :param id: The ID of the issue type.
    :type id: str

    """
    return web.Response(status=200)


async def get_issue_all_types(request: web.Request, ) -> web.Response:
    """Get all issue types for user

    Returns all issue types.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:** Issue types are only returned as follows:   *  if the user has the *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg), all issue types are returned.  *  if the user has the *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for one or more projects, the issue types associated with the projects the user has permission to browse are returned.


    """
    return web.Response(status=200)


async def get_issue_type(request: web.Request, id) -> web.Response:
    """Get issue type

    Returns an issue type.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:** *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) in a project the issue type is associated with or *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param id: The ID of the issue type.
    :type id: str

    """
    return web.Response(status=200)


async def get_issue_types_for_project(request: web.Request, project_id, level=None) -> web.Response:
    """Get issue types for project

    Returns issue types for a project.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:** *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) in the relevant project or *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param project_id: The ID of the project.
    :type project_id: int
    :param level: The level of the issue type to filter by. Use:   *  &#x60;-1&#x60; for Subtask.  *  &#x60;0&#x60; for Base.  *  &#x60;1&#x60; for Epic.
    :type level: int

    """
    return web.Response(status=200)


async def update_issue_type(request: web.Request, id, body) -> web.Response:
    """Update issue type

    Updates the issue type.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param id: The ID of the issue type.
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = IssueTypeUpdateBean.from_dict(body)
    return web.Response(status=200)
