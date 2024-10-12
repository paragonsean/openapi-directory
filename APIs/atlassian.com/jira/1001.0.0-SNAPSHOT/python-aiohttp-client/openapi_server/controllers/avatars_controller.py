from typing import List, Dict
from aiohttp import web

from openapi_server.models.avatar import Avatar
from openapi_server.models.avatars import Avatars
from openapi_server.models.error_collection import ErrorCollection
from openapi_server.models.system_avatars import SystemAvatars
from openapi_server import util


async def delete_avatar(request: web.Request, type, owning_object_id, id) -> web.Response:
    """Delete avatar

    Deletes an avatar from a project or issue type.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param type: The avatar type.
    :type type: str
    :param owning_object_id: The ID of the item the avatar is associated with.
    :type owning_object_id: str
    :param id: The ID of the avatar.
    :type id: int

    """
    return web.Response(status=200)


async def get_all_system_avatars(request: web.Request, type) -> web.Response:
    """Get system avatars by type

    Returns a list of system avatar details by owner type, where the owner types are issue type, project, or user.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:** None.

    :param type: The avatar type.
    :type type: str

    """
    return web.Response(status=200)


async def get_avatar_image_by_id(request: web.Request, type, id, size=None, format=None) -> web.Response:
    """Get avatar image by ID

    Returns a project or issue type avatar image by ID.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:**   *  For system avatars, none.  *  For custom project avatars, *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project the avatar belongs to.  *  For custom issue type avatars, *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for at least one project the issue type is used in.

    :param type: The icon type of the avatar.
    :type type: str
    :param id: The ID of the avatar.
    :type id: int
    :param size: The size of the avatar image. If not provided the default size is returned.
    :type size: str
    :param format: The format to return the avatar image in. If not provided the original content format is returned.
    :type format: str

    """
    return web.Response(status=200)


async def get_avatar_image_by_owner(request: web.Request, type, entity_id, size=None, format=None) -> web.Response:
    """Get avatar image by owner

    Returns the avatar image for a project or issue type.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:**   *  For system avatars, none.  *  For custom project avatars, *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project the avatar belongs to.  *  For custom issue type avatars, *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for at least one project the issue type is used in.

    :param type: The icon type of the avatar.
    :type type: str
    :param entity_id: The ID of the project or issue type the avatar belongs to.
    :type entity_id: str
    :param size: The size of the avatar image. If not provided the default size is returned.
    :type size: str
    :param format: The format to return the avatar image in. If not provided the original content format is returned.
    :type format: str

    """
    return web.Response(status=200)


async def get_avatar_image_by_type(request: web.Request, type, size=None, format=None) -> web.Response:
    """Get avatar image by type

    Returns the default project or issue type avatar image.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:** None.

    :param type: The icon type of the avatar.
    :type type: str
    :param size: The size of the avatar image. If not provided the default size is returned.
    :type size: str
    :param format: The format to return the avatar image in. If not provided the original content format is returned.
    :type format: str

    """
    return web.Response(status=200)


async def get_avatars(request: web.Request, type, entity_id) -> web.Response:
    """Get avatars

    Returns the system and custom avatars for a project or issue type.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:**   *  for custom project avatars, *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project the avatar belongs to.  *  for custom issue type avatars, *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for at least one project the issue type is used in.  *  for system avatars, none.

    :param type: The avatar type.
    :type type: str
    :param entity_id: The ID of the item the avatar is associated with.
    :type entity_id: str

    """
    return web.Response(status=200)


async def store_avatar(request: web.Request, type, entity_id, size, body, x=None, y=None) -> web.Response:
    """Load avatar

    Loads a custom avatar for a project or issue type.  Specify the avatar&#39;s local file location in the body of the request. Also, include the following headers:   *  &#x60;X-Atlassian-Token: no-check&#x60; To prevent XSRF protection blocking the request, for more information see [Special Headers](#special-request-headers).  *  &#x60;Content-Type: image/image type&#x60; Valid image types are JPEG, GIF, or PNG.  For example:   &#x60;curl --request POST &#x60;  &#x60;--user email@example.com:&lt;api_token&gt; &#x60;  &#x60;--header &#39;X-Atlassian-Token: no-check&#39; &#x60;  &#x60;--header &#39;Content-Type: image/&lt; image_type&gt;&#39; &#x60;  &#x60;--data-binary \&quot;&lt;@/path/to/file/with/your/avatar&gt;\&quot; &#x60;  &#x60;--url &#39;https://your-domain.atlassian.net/rest/api/3/universal_avatar/type/{type}/owner/{entityId}&#39;&#x60;  The avatar is cropped to a square. If no crop parameters are specified, the square originates at the top left of the image. The length of the square&#39;s sides is set to the smaller of the height or width of the image.  The cropped image is then used to create avatars of 16x16, 24x24, 32x32, and 48x48 in size.  After creating the avatar use:   *  [Update issue type](#api-rest-api-3-issuetype-id-put) to set it as the issue type&#39;s displayed avatar.  *  [Set project avatar](#api-rest-api-3-project-projectIdOrKey-avatar-put) to set it as the project&#39;s displayed avatar.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param type: The avatar type.
    :type type: str
    :param entity_id: The ID of the item the avatar is associated with.
    :type entity_id: str
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
