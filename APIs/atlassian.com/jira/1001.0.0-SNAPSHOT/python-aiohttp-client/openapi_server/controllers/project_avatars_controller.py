from typing import List, Dict
from aiohttp import web

from openapi_server.models.avatar import Avatar
from openapi_server.models.project_avatars import ProjectAvatars
from openapi_server import util


async def create_project_avatar(request: web.Request, project_id_or_key, body, x=None, y=None, size=None) -> web.Response:
    """Load project avatar

    Loads an avatar for a project.  Specify the avatar&#39;s local file location in the body of the request. Also, include the following headers:   *  &#x60;X-Atlassian-Token: no-check&#x60; To prevent XSRF protection blocking the request, for more information see [Special Headers](#special-request-headers).  *  &#x60;Content-Type: image/image type&#x60; Valid image types are JPEG, GIF, or PNG.  For example:   &#x60;curl --request POST &#x60;  &#x60;--user email@example.com:&lt;api_token&gt; &#x60;  &#x60;--header &#39;X-Atlassian-Token: no-check&#39; &#x60;  &#x60;--header &#39;Content-Type: image/&lt; image_type&gt;&#39; &#x60;  &#x60;--data-binary \&quot;&lt;@/path/to/file/with/your/avatar&gt;\&quot; &#x60;  &#x60;--url &#39;https://your-domain.atlassian.net/rest/api/3/project/{projectIdOrKey}/avatar2&#39;&#x60;  The avatar is cropped to a square. If no crop parameters are specified, the square originates at the top left of the image. The length of the square&#39;s sides is set to the smaller of the height or width of the image.  The cropped image is then used to create avatars of 16x16, 24x24, 32x32, and 48x48 in size.  After creating the avatar use [Set project avatar](#api-rest-api-3-project-projectIdOrKey-avatar-put) to set it as the project&#39;s displayed avatar.  **[Permissions](#permissions) required:** *Administer projects* [project permission](https://confluence.atlassian.com/x/yodKLg).

    :param project_id_or_key: The ID or (case-sensitive) key of the project.
    :type project_id_or_key: str
    :param body: 
    :type body: 
    :param x: The X coordinate of the top-left corner of the crop region.
    :type x: int
    :param y: The Y coordinate of the top-left corner of the crop region.
    :type y: int
    :param size: The length of each side of the crop region.
    :type size: int

    """
    return web.Response(status=200)


async def delete_project_avatar(request: web.Request, project_id_or_key, id) -> web.Response:
    """Delete project avatar

    Deletes a custom avatar from a project. Note that system avatars cannot be deleted.  **[Permissions](#permissions) required:** *Administer projects* [project permission](https://confluence.atlassian.com/x/yodKLg).

    :param project_id_or_key: The project ID or (case-sensitive) key.
    :type project_id_or_key: str
    :param id: The ID of the avatar.
    :type id: int

    """
    return web.Response(status=200)


async def get_all_project_avatars(request: web.Request, project_id_or_key) -> web.Response:
    """Get all project avatars

    Returns all project avatars, grouped by system and custom avatars.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:** *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.

    :param project_id_or_key: The ID or (case-sensitive) key of the project.
    :type project_id_or_key: str

    """
    return web.Response(status=200)


async def update_project_avatar(request: web.Request, project_id_or_key, body) -> web.Response:
    """Set project avatar

    Sets the avatar displayed for a project.  Use [Load project avatar](#api-rest-api-3-project-projectIdOrKey-avatar2-post) to store avatars against the project, before using this operation to set the displayed avatar.  **[Permissions](#permissions) required:** *Administer projects* [project permission](https://confluence.atlassian.com/x/yodKLg).

    :param project_id_or_key: The ID or (case-sensitive) key of the project.
    :type project_id_or_key: str
    :param body: 
    :type body: dict | bytes

    """
    body = Avatar.from_dict(body)
    return web.Response(status=200)
