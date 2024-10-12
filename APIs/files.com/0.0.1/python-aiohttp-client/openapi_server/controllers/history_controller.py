from typing import List, Dict
from aiohttp import web

from openapi_server.models.action_entity import ActionEntity
from openapi_server import util


async def history_list(request: web.Request, start_at=None, end_at=None, display=None, cursor=None, per_page=None, sort_by=None, filter=None, filter_prefix=None) -> web.Response:
    """List site full action history.

    List site full action history.

    :param start_at: Leave blank or set to a date/time to filter earlier entries.
    :type start_at: str
    :param end_at: Leave blank or set to a date/time to filter later entries.
    :type end_at: str
    :param display: Display format. Leave blank or set to &#x60;full&#x60; or &#x60;parent&#x60;.
    :type display: str
    :param cursor: Used for pagination.  When a list request has more records available, cursors are provided in the response headers &#x60;X-Files-Cursor-Next&#x60; and &#x60;X-Files-Cursor-Prev&#x60;.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination.
    :type cursor: str
    :param per_page: Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended).
    :type per_page: int
    :param sort_by: If set, sort records by the specified field in either &#x60;asc&#x60; or &#x60;desc&#x60; direction (e.g. &#x60;sort_by[path]&#x3D;desc&#x60;). Valid fields are &#x60;path&#x60;, &#x60;folder&#x60;, &#x60;user_id&#x60; or &#x60;created_at&#x60;.
    :type sort_by: dict | bytes
    :param filter: If set, return records where the specified field is equal to the supplied value. Valid fields are &#x60;user_id&#x60;, &#x60;folder&#x60; or &#x60;path&#x60;.
    :type filter: dict | bytes
    :param filter_prefix: If set, return records where the specified field is prefixed by the supplied value. Valid fields are &#x60;path&#x60;.
    :type filter_prefix: dict | bytes

    """
    start_at = util.deserialize_datetime(start_at)
    end_at = util.deserialize_datetime(end_at)
    sort_by = .from_dict(sort_by)
    filter = .from_dict(filter)
    filter_prefix = .from_dict(filter_prefix)
    return web.Response(status=200)


async def history_list_for_file(request: web.Request, path, start_at=None, end_at=None, display=None, cursor=None, per_page=None, sort_by=None) -> web.Response:
    """List history for specific file.

    List history for specific file.

    :param path: Path to operate on.
    :type path: str
    :param start_at: Leave blank or set to a date/time to filter earlier entries.
    :type start_at: str
    :param end_at: Leave blank or set to a date/time to filter later entries.
    :type end_at: str
    :param display: Display format. Leave blank or set to &#x60;full&#x60; or &#x60;parent&#x60;.
    :type display: str
    :param cursor: Used for pagination.  When a list request has more records available, cursors are provided in the response headers &#x60;X-Files-Cursor-Next&#x60; and &#x60;X-Files-Cursor-Prev&#x60;.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination.
    :type cursor: str
    :param per_page: Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended).
    :type per_page: int
    :param sort_by: If set, sort records by the specified field in either &#x60;asc&#x60; or &#x60;desc&#x60; direction (e.g. &#x60;sort_by[user_id]&#x3D;desc&#x60;). Valid fields are &#x60;user_id&#x60; and &#x60;created_at&#x60;.
    :type sort_by: dict | bytes

    """
    start_at = util.deserialize_datetime(start_at)
    end_at = util.deserialize_datetime(end_at)
    sort_by = .from_dict(sort_by)
    return web.Response(status=200)


async def history_list_for_folder(request: web.Request, path, start_at=None, end_at=None, display=None, cursor=None, per_page=None, sort_by=None) -> web.Response:
    """List history for specific folder.

    List history for specific folder.

    :param path: Path to operate on.
    :type path: str
    :param start_at: Leave blank or set to a date/time to filter earlier entries.
    :type start_at: str
    :param end_at: Leave blank or set to a date/time to filter later entries.
    :type end_at: str
    :param display: Display format. Leave blank or set to &#x60;full&#x60; or &#x60;parent&#x60;.
    :type display: str
    :param cursor: Used for pagination.  When a list request has more records available, cursors are provided in the response headers &#x60;X-Files-Cursor-Next&#x60; and &#x60;X-Files-Cursor-Prev&#x60;.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination.
    :type cursor: str
    :param per_page: Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended).
    :type per_page: int
    :param sort_by: If set, sort records by the specified field in either &#x60;asc&#x60; or &#x60;desc&#x60; direction (e.g. &#x60;sort_by[user_id]&#x3D;desc&#x60;). Valid fields are &#x60;user_id&#x60; and &#x60;created_at&#x60;.
    :type sort_by: dict | bytes

    """
    start_at = util.deserialize_datetime(start_at)
    end_at = util.deserialize_datetime(end_at)
    sort_by = .from_dict(sort_by)
    return web.Response(status=200)


async def history_list_for_user(request: web.Request, user_id, start_at=None, end_at=None, display=None, cursor=None, per_page=None, sort_by=None) -> web.Response:
    """List history for specific user.

    List history for specific user.

    :param user_id: User ID.
    :type user_id: int
    :param start_at: Leave blank or set to a date/time to filter earlier entries.
    :type start_at: str
    :param end_at: Leave blank or set to a date/time to filter later entries.
    :type end_at: str
    :param display: Display format. Leave blank or set to &#x60;full&#x60; or &#x60;parent&#x60;.
    :type display: str
    :param cursor: Used for pagination.  When a list request has more records available, cursors are provided in the response headers &#x60;X-Files-Cursor-Next&#x60; and &#x60;X-Files-Cursor-Prev&#x60;.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination.
    :type cursor: str
    :param per_page: Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended).
    :type per_page: int
    :param sort_by: If set, sort records by the specified field in either &#x60;asc&#x60; or &#x60;desc&#x60; direction (e.g. &#x60;sort_by[user_id]&#x3D;desc&#x60;). Valid fields are &#x60;user_id&#x60; and &#x60;created_at&#x60;.
    :type sort_by: dict | bytes

    """
    start_at = util.deserialize_datetime(start_at)
    end_at = util.deserialize_datetime(end_at)
    sort_by = .from_dict(sort_by)
    return web.Response(status=200)


async def history_list_logins(request: web.Request, start_at=None, end_at=None, display=None, cursor=None, per_page=None, sort_by=None) -> web.Response:
    """List site login history.

    List site login history.

    :param start_at: Leave blank or set to a date/time to filter earlier entries.
    :type start_at: str
    :param end_at: Leave blank or set to a date/time to filter later entries.
    :type end_at: str
    :param display: Display format. Leave blank or set to &#x60;full&#x60; or &#x60;parent&#x60;.
    :type display: str
    :param cursor: Used for pagination.  When a list request has more records available, cursors are provided in the response headers &#x60;X-Files-Cursor-Next&#x60; and &#x60;X-Files-Cursor-Prev&#x60;.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination.
    :type cursor: str
    :param per_page: Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended).
    :type per_page: int
    :param sort_by: If set, sort records by the specified field in either &#x60;asc&#x60; or &#x60;desc&#x60; direction (e.g. &#x60;sort_by[user_id]&#x3D;desc&#x60;). Valid fields are &#x60;user_id&#x60; and &#x60;created_at&#x60;.
    :type sort_by: dict | bytes

    """
    start_at = util.deserialize_datetime(start_at)
    end_at = util.deserialize_datetime(end_at)
    sort_by = .from_dict(sort_by)
    return web.Response(status=200)
