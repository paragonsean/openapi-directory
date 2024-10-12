from typing import List, Dict
from aiohttp import web

from openapi_server.models.permission_entity import PermissionEntity
from openapi_server import util


async def delete_permissions_id(request: web.Request, id) -> web.Response:
    """Delete Permission

    Delete Permission

    :param id: Permission ID.
    :type id: int

    """
    return web.Response(status=200)


async def get_permissions(request: web.Request, cursor=None, per_page=None, sort_by=None, filter=None, filter_prefix=None, path=None, group_id=None, user_id=None, include_groups=None) -> web.Response:
    """List Permissions

    List Permissions

    :param cursor: Used for pagination.  When a list request has more records available, cursors are provided in the response headers &#x60;X-Files-Cursor-Next&#x60; and &#x60;X-Files-Cursor-Prev&#x60;.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination.
    :type cursor: str
    :param per_page: Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended).
    :type per_page: int
    :param sort_by: If set, sort records by the specified field in either &#x60;asc&#x60; or &#x60;desc&#x60; direction (e.g. &#x60;sort_by[group_id]&#x3D;desc&#x60;). Valid fields are &#x60;group_id&#x60;, &#x60;path&#x60;, &#x60;user_id&#x60; or &#x60;permission&#x60;.
    :type sort_by: dict | bytes
    :param filter: If set, return records where the specified field is equal to the supplied value. Valid fields are &#x60;group_id&#x60;, &#x60;user_id&#x60; or &#x60;path&#x60;. Valid field combinations are &#x60;[ group_id, path ]&#x60; and &#x60;[ user_id, path ]&#x60;.
    :type filter: dict | bytes
    :param filter_prefix: If set, return records where the specified field is prefixed by the supplied value. Valid fields are &#x60;path&#x60;.
    :type filter_prefix: dict | bytes
    :param path: DEPRECATED: Permission path.  If provided, will scope permissions to this path. Use &#x60;filter[path]&#x60; instead.
    :type path: str
    :param group_id: DEPRECATED: Group ID.  If provided, will scope permissions to this group. Use &#x60;filter[group_id]&#x60; instead.&#x60;
    :type group_id: str
    :param user_id: DEPRECATED: User ID.  If provided, will scope permissions to this user. Use &#x60;filter[user_id]&#x60; instead.&#x60;
    :type user_id: str
    :param include_groups: If searching by user or group, also include user&#39;s permissions that are inherited from its groups?
    :type include_groups: bool

    """
    sort_by = .from_dict(sort_by)
    filter = .from_dict(filter)
    filter_prefix = .from_dict(filter_prefix)
    return web.Response(status=200)


async def post_permissions(request: web.Request, group_id=None, path=None, permission=None, recursive=None, user_id=None, username=None) -> web.Response:
    """Create Permission

    Create Permission

    :param group_id: Group ID
    :type group_id: int
    :param path: Folder path
    :type path: str
    :param permission:  Permission type.  Can be &#x60;admin&#x60;, &#x60;full&#x60;, &#x60;readonly&#x60;, &#x60;writeonly&#x60;, &#x60;list&#x60;, or &#x60;history&#x60;
    :type permission: str
    :param recursive: Apply to subfolders recursively?
    :type recursive: bool
    :param user_id: User ID.  Provide &#x60;username&#x60; or &#x60;user_id&#x60;
    :type user_id: int
    :param username: User username.  Provide &#x60;username&#x60; or &#x60;user_id&#x60;
    :type username: str

    """
    return web.Response(status=200)
