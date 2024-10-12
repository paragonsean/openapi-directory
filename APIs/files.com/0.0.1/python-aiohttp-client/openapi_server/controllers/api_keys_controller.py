from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_key_entity import ApiKeyEntity
from openapi_server import util


async def delete_api_keys_id(request: web.Request, id) -> web.Response:
    """Delete Api Key

    Delete Api Key

    :param id: Api Key ID.
    :type id: int

    """
    return web.Response(status=200)


async def get_api_keys(request: web.Request, user_id=None, cursor=None, per_page=None, sort_by=None, filter=None, filter_gt=None, filter_gteq=None, filter_lt=None, filter_lteq=None) -> web.Response:
    """List Api Keys

    List Api Keys

    :param user_id: User ID.  Provide a value of &#x60;0&#x60; to operate the current session&#39;s user.
    :type user_id: int
    :param cursor: Used for pagination.  When a list request has more records available, cursors are provided in the response headers &#x60;X-Files-Cursor-Next&#x60; and &#x60;X-Files-Cursor-Prev&#x60;.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination.
    :type cursor: str
    :param per_page: Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended).
    :type per_page: int
    :param sort_by: If set, sort records by the specified field in either &#x60;asc&#x60; or &#x60;desc&#x60; direction (e.g. &#x60;sort_by[expires_at]&#x3D;desc&#x60;). Valid fields are &#x60;expires_at&#x60;.
    :type sort_by: dict | bytes
    :param filter: If set, return records where the specified field is equal to the supplied value. Valid fields are &#x60;expires_at&#x60;.
    :type filter: dict | bytes
    :param filter_gt: If set, return records where the specified field is greater than the supplied value. Valid fields are &#x60;expires_at&#x60;.
    :type filter_gt: dict | bytes
    :param filter_gteq: If set, return records where the specified field is greater than or equal the supplied value. Valid fields are &#x60;expires_at&#x60;.
    :type filter_gteq: dict | bytes
    :param filter_lt: If set, return records where the specified field is less than the supplied value. Valid fields are &#x60;expires_at&#x60;.
    :type filter_lt: dict | bytes
    :param filter_lteq: If set, return records where the specified field is less than or equal the supplied value. Valid fields are &#x60;expires_at&#x60;.
    :type filter_lteq: dict | bytes

    """
    sort_by = .from_dict(sort_by)
    filter = .from_dict(filter)
    filter_gt = .from_dict(filter_gt)
    filter_gteq = .from_dict(filter_gteq)
    filter_lt = .from_dict(filter_lt)
    filter_lteq = .from_dict(filter_lteq)
    return web.Response(status=200)


async def get_api_keys_id(request: web.Request, id) -> web.Response:
    """Show Api Key

    Show Api Key

    :param id: Api Key ID.
    :type id: int

    """
    return web.Response(status=200)


async def patch_api_keys_id(request: web.Request, id, description=None, expires_at=None, name=None, permission_set=None) -> web.Response:
    """Update Api Key

    Update Api Key

    :param id: Api Key ID.
    :type id: int
    :param description: User-supplied description of API key.
    :type description: str
    :param expires_at: API Key expiration date
    :type expires_at: str
    :param name: Internal name for the API Key.  For your use.
    :type name: str
    :param permission_set: Permissions for this API Key.  Keys with the &#x60;desktop_app&#x60; permission set only have the ability to do the functions provided in our Desktop App (File and Share Link operations).  Additional permission sets may become available in the future, such as for a Site Admin to give a key with no administrator privileges.  If you have ideas for permission sets, please let us know.
    :type permission_set: str

    """
    expires_at = util.deserialize_datetime(expires_at)
    return web.Response(status=200)


async def post_api_keys(request: web.Request, description=None, expires_at=None, name=None, path=None, permission_set=None, user_id=None) -> web.Response:
    """Create Api Key

    Create Api Key

    :param description: User-supplied description of API key.
    :type description: str
    :param expires_at: API Key expiration date
    :type expires_at: str
    :param name: Internal name for the API Key.  For your use.
    :type name: str
    :param path: Folder path restriction for this api key.
    :type path: str
    :param permission_set: Permissions for this API Key.  Keys with the &#x60;desktop_app&#x60; permission set only have the ability to do the functions provided in our Desktop App (File and Share Link operations).  Additional permission sets may become available in the future, such as for a Site Admin to give a key with no administrator privileges.  If you have ideas for permission sets, please let us know.
    :type permission_set: str
    :param user_id: User ID.  Provide a value of &#x60;0&#x60; to operate the current session&#39;s user.
    :type user_id: int

    """
    expires_at = util.deserialize_datetime(expires_at)
    return web.Response(status=200)
