from typing import List, Dict
from aiohttp import web

from openapi_server.models.settings_change_entity import SettingsChangeEntity
from openapi_server import util


async def get_settings_changes(request: web.Request, cursor=None, per_page=None, sort_by=None, api_key_id=None, user_id=None, filter=None) -> web.Response:
    """List Settings Changes

    List Settings Changes

    :param cursor: Used for pagination.  When a list request has more records available, cursors are provided in the response headers &#x60;X-Files-Cursor-Next&#x60; and &#x60;X-Files-Cursor-Prev&#x60;.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination.
    :type cursor: str
    :param per_page: Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended).
    :type per_page: int
    :param sort_by: If set, sort records by the specified field in either &#x60;asc&#x60; or &#x60;desc&#x60; direction (e.g. &#x60;sort_by[api_key_id]&#x3D;desc&#x60;). Valid fields are &#x60;api_key_id&#x60;, &#x60;created_at&#x60; or &#x60;user_id&#x60;.
    :type sort_by: dict | bytes
    :param api_key_id: If set, return records where the specified field is equal to the supplied value.
    :type api_key_id: str
    :param user_id: If set, return records where the specified field is equal to the supplied value.
    :type user_id: str
    :param filter: If set, return records where the specified field is equal to the supplied value. Valid fields are &#x60;api_key_id&#x60; and &#x60;user_id&#x60;.
    :type filter: dict | bytes

    """
    sort_by = .from_dict(sort_by)
    filter = .from_dict(filter)
    return web.Response(status=200)
