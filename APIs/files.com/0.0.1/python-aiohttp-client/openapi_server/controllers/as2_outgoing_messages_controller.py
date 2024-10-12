from typing import List, Dict
from aiohttp import web

from openapi_server.models.as2_outgoing_message_entity import As2OutgoingMessageEntity
from openapi_server import util


async def get_as2_outgoing_messages(request: web.Request, cursor=None, per_page=None, sort_by=None, filter=None, filter_gt=None, filter_gteq=None, filter_lt=None, filter_lteq=None, as2_partner_id=None) -> web.Response:
    """List As2 Outgoing Messages

    List As2 Outgoing Messages

    :param cursor: Used for pagination.  When a list request has more records available, cursors are provided in the response headers &#x60;X-Files-Cursor-Next&#x60; and &#x60;X-Files-Cursor-Prev&#x60;.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination.
    :type cursor: str
    :param per_page: Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended).
    :type per_page: int
    :param sort_by: If set, sort records by the specified field in either &#x60;asc&#x60; or &#x60;desc&#x60; direction (e.g. &#x60;sort_by[created_at]&#x3D;desc&#x60;). Valid fields are &#x60;created_at&#x60; and &#x60;as2_partner_id&#x60;.
    :type sort_by: dict | bytes
    :param filter: If set, return records where the specified field is equal to the supplied value. Valid fields are &#x60;created_at&#x60;.
    :type filter: dict | bytes
    :param filter_gt: If set, return records where the specified field is greater than the supplied value. Valid fields are &#x60;created_at&#x60;.
    :type filter_gt: dict | bytes
    :param filter_gteq: If set, return records where the specified field is greater than or equal the supplied value. Valid fields are &#x60;created_at&#x60;.
    :type filter_gteq: dict | bytes
    :param filter_lt: If set, return records where the specified field is less than the supplied value. Valid fields are &#x60;created_at&#x60;.
    :type filter_lt: dict | bytes
    :param filter_lteq: If set, return records where the specified field is less than or equal the supplied value. Valid fields are &#x60;created_at&#x60;.
    :type filter_lteq: dict | bytes
    :param as2_partner_id: As2 Partner ID.  If provided, will return message specific to that partner.
    :type as2_partner_id: int

    """
    sort_by = .from_dict(sort_by)
    filter = .from_dict(filter)
    filter_gt = .from_dict(filter_gt)
    filter_gteq = .from_dict(filter_gteq)
    filter_lt = .from_dict(filter_lt)
    filter_lteq = .from_dict(filter_lteq)
    return web.Response(status=200)
