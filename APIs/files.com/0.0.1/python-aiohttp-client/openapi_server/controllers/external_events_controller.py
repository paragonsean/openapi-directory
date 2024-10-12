from typing import List, Dict
from aiohttp import web

from openapi_server.models.external_event_entity import ExternalEventEntity
from openapi_server import util


async def get_external_events(request: web.Request, cursor=None, per_page=None, sort_by=None, filter=None, filter_gt=None, filter_gteq=None, filter_prefix=None, filter_lt=None, filter_lteq=None) -> web.Response:
    """List External Events

    List External Events

    :param cursor: Used for pagination.  When a list request has more records available, cursors are provided in the response headers &#x60;X-Files-Cursor-Next&#x60; and &#x60;X-Files-Cursor-Prev&#x60;.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination.
    :type cursor: str
    :param per_page: Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended).
    :type per_page: int
    :param sort_by: If set, sort records by the specified field in either &#x60;asc&#x60; or &#x60;desc&#x60; direction (e.g. &#x60;sort_by[remote_server_type]&#x3D;desc&#x60;). Valid fields are &#x60;remote_server_type&#x60;, &#x60;site_id&#x60;, &#x60;folder_behavior_id&#x60;, &#x60;event_type&#x60;, &#x60;created_at&#x60; or &#x60;status&#x60;.
    :type sort_by: dict | bytes
    :param filter: If set, return records where the specified field is equal to the supplied value. Valid fields are &#x60;created_at&#x60;, &#x60;event_type&#x60;, &#x60;remote_server_type&#x60;, &#x60;status&#x60; or &#x60;folder_behavior_id&#x60;. Valid field combinations are &#x60;[ event_type, status, created_at ]&#x60;, &#x60;[ event_type, created_at ]&#x60; or &#x60;[ status, created_at ]&#x60;.
    :type filter: dict | bytes
    :param filter_gt: If set, return records where the specified field is greater than the supplied value. Valid fields are &#x60;created_at&#x60;.
    :type filter_gt: dict | bytes
    :param filter_gteq: If set, return records where the specified field is greater than or equal the supplied value. Valid fields are &#x60;created_at&#x60;.
    :type filter_gteq: dict | bytes
    :param filter_prefix: If set, return records where the specified field is prefixed by the supplied value. Valid fields are &#x60;remote_server_type&#x60;.
    :type filter_prefix: dict | bytes
    :param filter_lt: If set, return records where the specified field is less than the supplied value. Valid fields are &#x60;created_at&#x60;.
    :type filter_lt: dict | bytes
    :param filter_lteq: If set, return records where the specified field is less than or equal the supplied value. Valid fields are &#x60;created_at&#x60;.
    :type filter_lteq: dict | bytes

    """
    sort_by = .from_dict(sort_by)
    filter = .from_dict(filter)
    filter_gt = .from_dict(filter_gt)
    filter_gteq = .from_dict(filter_gteq)
    filter_prefix = .from_dict(filter_prefix)
    filter_lt = .from_dict(filter_lt)
    filter_lteq = .from_dict(filter_lteq)
    return web.Response(status=200)


async def get_external_events_id(request: web.Request, id) -> web.Response:
    """Show External Event

    Show External Event

    :param id: External Event ID.
    :type id: int

    """
    return web.Response(status=200)


async def post_external_events(request: web.Request, body, status) -> web.Response:
    """Create External Event

    Create External Event

    :param body: Event body
    :type body: str
    :param status: Status of event.
    :type status: str

    """
    return web.Response(status=200)
