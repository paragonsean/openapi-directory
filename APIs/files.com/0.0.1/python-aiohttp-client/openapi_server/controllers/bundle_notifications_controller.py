from typing import List, Dict
from aiohttp import web

from openapi_server.models.bundle_notification_entity import BundleNotificationEntity
from openapi_server import util


async def delete_bundle_notifications_id(request: web.Request, id) -> web.Response:
    """Delete Bundle Notification

    Delete Bundle Notification

    :param id: Bundle Notification ID.
    :type id: int

    """
    return web.Response(status=200)


async def get_bundle_notifications(request: web.Request, user_id=None, cursor=None, per_page=None, sort_by=None, bundle_id=None, filter=None) -> web.Response:
    """List Bundle Notifications

    List Bundle Notifications

    :param user_id: User ID.  Provide a value of &#x60;0&#x60; to operate the current session&#39;s user.
    :type user_id: int
    :param cursor: Used for pagination.  When a list request has more records available, cursors are provided in the response headers &#x60;X-Files-Cursor-Next&#x60; and &#x60;X-Files-Cursor-Prev&#x60;.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination.
    :type cursor: str
    :param per_page: Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended).
    :type per_page: int
    :param sort_by: If set, sort records by the specified field in either &#x60;asc&#x60; or &#x60;desc&#x60; direction (e.g. &#x60;sort_by[bundle_id]&#x3D;desc&#x60;). Valid fields are &#x60;bundle_id&#x60;.
    :type sort_by: dict | bytes
    :param bundle_id: If set, return records where the specified field is equal to the supplied value.
    :type bundle_id: str
    :param filter: If set, return records where the specified field is equal to the supplied value. Valid fields are &#x60;bundle_id&#x60;.
    :type filter: dict | bytes

    """
    sort_by = .from_dict(sort_by)
    filter = .from_dict(filter)
    return web.Response(status=200)


async def get_bundle_notifications_id(request: web.Request, id) -> web.Response:
    """Show Bundle Notification

    Show Bundle Notification

    :param id: Bundle Notification ID.
    :type id: int

    """
    return web.Response(status=200)


async def patch_bundle_notifications_id(request: web.Request, id, notify_on_registration=None, notify_on_upload=None) -> web.Response:
    """Update Bundle Notification

    Update Bundle Notification

    :param id: Bundle Notification ID.
    :type id: int
    :param notify_on_registration: Triggers bundle notification when a registration action occurs for it.
    :type notify_on_registration: bool
    :param notify_on_upload: Triggers bundle notification when a upload action occurs for it.
    :type notify_on_upload: bool

    """
    return web.Response(status=200)


async def post_bundle_notifications(request: web.Request, bundle_id, notify_on_registration=None, notify_on_upload=None, user_id=None) -> web.Response:
    """Create Bundle Notification

    Create Bundle Notification

    :param bundle_id: Bundle ID to notify on
    :type bundle_id: int
    :param notify_on_registration: Triggers bundle notification when a registration action occurs for it.
    :type notify_on_registration: bool
    :param notify_on_upload: Triggers bundle notification when a upload action occurs for it.
    :type notify_on_upload: bool
    :param user_id: The id of the user to notify.
    :type user_id: int

    """
    return web.Response(status=200)
