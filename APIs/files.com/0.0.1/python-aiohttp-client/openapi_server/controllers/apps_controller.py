from typing import List, Dict
from aiohttp import web

from openapi_server.models.app_entity import AppEntity
from openapi_server import util


async def get_apps(request: web.Request, cursor=None, per_page=None, sort_by=None, filter=None, filter_prefix=None) -> web.Response:
    """List Apps

    List Apps

    :param cursor: Used for pagination.  When a list request has more records available, cursors are provided in the response headers &#x60;X-Files-Cursor-Next&#x60; and &#x60;X-Files-Cursor-Prev&#x60;.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination.
    :type cursor: str
    :param per_page: Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended).
    :type per_page: int
    :param sort_by: If set, sort records by the specified field in either &#x60;asc&#x60; or &#x60;desc&#x60; direction (e.g. &#x60;sort_by[name]&#x3D;desc&#x60;). Valid fields are &#x60;name&#x60; and &#x60;app_type&#x60;.
    :type sort_by: dict | bytes
    :param filter: If set, return records where the specified field is equal to the supplied value. Valid fields are &#x60;name&#x60; and &#x60;app_type&#x60;. Valid field combinations are &#x60;[ name, app_type ]&#x60; and &#x60;[ app_type, name ]&#x60;.
    :type filter: dict | bytes
    :param filter_prefix: If set, return records where the specified field is prefixed by the supplied value. Valid fields are &#x60;name&#x60;.
    :type filter_prefix: dict | bytes

    """
    sort_by = .from_dict(sort_by)
    filter = .from_dict(filter)
    filter_prefix = .from_dict(filter_prefix)
    return web.Response(status=200)
