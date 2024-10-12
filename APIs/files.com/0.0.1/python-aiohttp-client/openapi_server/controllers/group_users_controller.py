from typing import List, Dict
from aiohttp import web

from openapi_server.models.group_user_entity import GroupUserEntity
from openapi_server import util


async def delete_group_users_id(request: web.Request, id, group_id, user_id) -> web.Response:
    """Delete Group User

    Delete Group User

    :param id: Group User ID.
    :type id: int
    :param group_id: Group ID from which to remove user.
    :type group_id: int
    :param user_id: User ID to remove from group.
    :type user_id: int

    """
    return web.Response(status=200)


async def get_group_users(request: web.Request, user_id=None, cursor=None, per_page=None, group_id=None) -> web.Response:
    """List Group Users

    List Group Users

    :param user_id: User ID.  If provided, will return group_users of this user.
    :type user_id: int
    :param cursor: Used for pagination.  When a list request has more records available, cursors are provided in the response headers &#x60;X-Files-Cursor-Next&#x60; and &#x60;X-Files-Cursor-Prev&#x60;.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination.
    :type cursor: str
    :param per_page: Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended).
    :type per_page: int
    :param group_id: Group ID.  If provided, will return group_users of this group.
    :type group_id: int

    """
    return web.Response(status=200)


async def patch_group_users_id(request: web.Request, id, group_id, user_id, admin=None) -> web.Response:
    """Update Group User

    Update Group User

    :param id: Group User ID.
    :type id: int
    :param group_id: Group ID to add user to.
    :type group_id: int
    :param user_id: User ID to add to group.
    :type user_id: int
    :param admin: Is the user a group administrator?
    :type admin: bool

    """
    return web.Response(status=200)


async def post_group_users(request: web.Request, group_id, user_id, admin=None) -> web.Response:
    """Create Group User

    Create Group User

    :param group_id: Group ID to add user to.
    :type group_id: int
    :param user_id: User ID to add to group.
    :type user_id: int
    :param admin: Is the user a group administrator?
    :type admin: bool

    """
    return web.Response(status=200)
