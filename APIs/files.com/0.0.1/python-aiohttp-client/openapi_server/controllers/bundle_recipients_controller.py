from typing import List, Dict
from aiohttp import web

from openapi_server.models.bundle_recipient_entity import BundleRecipientEntity
from openapi_server import util


async def get_bundle_recipients(request: web.Request, bundle_id, user_id=None, cursor=None, per_page=None, sort_by=None, filter=None) -> web.Response:
    """List Bundle Recipients

    List Bundle Recipients

    :param bundle_id: List recipients for the bundle with this ID.
    :type bundle_id: int
    :param user_id: User ID.  Provide a value of &#x60;0&#x60; to operate the current session&#39;s user.
    :type user_id: int
    :param cursor: Used for pagination.  When a list request has more records available, cursors are provided in the response headers &#x60;X-Files-Cursor-Next&#x60; and &#x60;X-Files-Cursor-Prev&#x60;.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination.
    :type cursor: str
    :param per_page: Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended).
    :type per_page: int
    :param sort_by: If set, sort records by the specified field in either &#x60;asc&#x60; or &#x60;desc&#x60; direction (e.g. &#x60;sort_by[has_registrations]&#x3D;desc&#x60;). Valid fields are &#x60;has_registrations&#x60;.
    :type sort_by: dict | bytes
    :param filter: If set, return records where the specified field is equal to the supplied value. Valid fields are &#x60;has_registrations&#x60;.
    :type filter: dict | bytes

    """
    sort_by = .from_dict(sort_by)
    filter = .from_dict(filter)
    return web.Response(status=200)


async def post_bundle_recipients(request: web.Request, bundle_id, recipient, company=None, name=None, note=None, share_after_create=None, user_id=None) -> web.Response:
    """Create Bundle Recipient

    Create Bundle Recipient

    :param bundle_id: Bundle to share.
    :type bundle_id: int
    :param recipient: Email addresses to share this bundle with.
    :type recipient: str
    :param company: Company of recipient.
    :type company: str
    :param name: Name of recipient.
    :type name: str
    :param note: Note to include in email.
    :type note: str
    :param share_after_create: Set to true to share the link with the recipient upon creation.
    :type share_after_create: bool
    :param user_id: User ID.  Provide a value of &#x60;0&#x60; to operate the current session&#39;s user.
    :type user_id: int

    """
    return web.Response(status=200)
