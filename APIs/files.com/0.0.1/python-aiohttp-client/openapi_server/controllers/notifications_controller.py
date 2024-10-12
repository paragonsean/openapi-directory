from typing import List, Dict
from aiohttp import web

from openapi_server.models.notification_entity import NotificationEntity
from openapi_server import util


async def delete_notifications_id(request: web.Request, id) -> web.Response:
    """Delete Notification

    Delete Notification

    :param id: Notification ID.
    :type id: int

    """
    return web.Response(status=200)


async def get_notifications(request: web.Request, user_id=None, cursor=None, per_page=None, sort_by=None, group_id=None, filter=None, filter_prefix=None, path=None, include_ancestors=None) -> web.Response:
    """List Notifications

    List Notifications

    :param user_id: DEPRECATED: Show notifications for this User ID. Use &#x60;filter[user_id]&#x60; instead.
    :type user_id: int
    :param cursor: Used for pagination.  When a list request has more records available, cursors are provided in the response headers &#x60;X-Files-Cursor-Next&#x60; and &#x60;X-Files-Cursor-Prev&#x60;.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination.
    :type cursor: str
    :param per_page: Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended).
    :type per_page: int
    :param sort_by: If set, sort records by the specified field in either &#x60;asc&#x60; or &#x60;desc&#x60; direction (e.g. &#x60;sort_by[path]&#x3D;desc&#x60;). Valid fields are &#x60;path&#x60;, &#x60;user_id&#x60; or &#x60;group_id&#x60;.
    :type sort_by: dict | bytes
    :param group_id: If set, return records where the specified field is equal to the supplied value.
    :type group_id: str
    :param filter: If set, return records where the specified field is equal to the supplied value. Valid fields are &#x60;path&#x60;, &#x60;user_id&#x60; or &#x60;group_id&#x60;.
    :type filter: dict | bytes
    :param filter_prefix: If set, return records where the specified field is prefixed by the supplied value. Valid fields are &#x60;path&#x60;.
    :type filter_prefix: dict | bytes
    :param path: Show notifications for this Path.
    :type path: str
    :param include_ancestors: If &#x60;include_ancestors&#x60; is &#x60;true&#x60; and &#x60;path&#x60; is specified, include notifications for any parent paths. Ignored if &#x60;path&#x60; is not specified.
    :type include_ancestors: bool

    """
    sort_by = .from_dict(sort_by)
    filter = .from_dict(filter)
    filter_prefix = .from_dict(filter_prefix)
    return web.Response(status=200)


async def get_notifications_id(request: web.Request, id) -> web.Response:
    """Show Notification

    Show Notification

    :param id: Notification ID.
    :type id: int

    """
    return web.Response(status=200)


async def patch_notifications_id(request: web.Request, id, message=None, notify_on_copy=None, notify_on_delete=None, notify_on_download=None, notify_on_move=None, notify_on_upload=None, notify_user_actions=None, recursive=None, send_interval=None, trigger_by_share_recipients=None, triggering_filenames=None, triggering_group_ids=None, triggering_user_ids=None) -> web.Response:
    """Update Notification

    Update Notification

    :param id: Notification ID.
    :type id: int
    :param message: Custom message to include in notification emails.
    :type message: str
    :param notify_on_copy: If &#x60;true&#x60;, copying or moving resources into this path will trigger a notification, in addition to just uploads.
    :type notify_on_copy: bool
    :param notify_on_delete: Triggers notification when deleting files from this path
    :type notify_on_delete: bool
    :param notify_on_download: Triggers notification when downloading files from this path
    :type notify_on_download: bool
    :param notify_on_move: Triggers notification when moving files to this path
    :type notify_on_move: bool
    :param notify_on_upload: Triggers notification when uploading new files to this path
    :type notify_on_upload: bool
    :param notify_user_actions: If &#x60;true&#x60; actions initiated by the user will still result in a notification
    :type notify_user_actions: bool
    :param recursive: If &#x60;true&#x60;, enable notifications for each subfolder in this path
    :type recursive: bool
    :param send_interval: The time interval that notifications are aggregated by.  Can be &#x60;five_minutes&#x60;, &#x60;fifteen_minutes&#x60;, &#x60;hourly&#x60;, or &#x60;daily&#x60;.
    :type send_interval: str
    :param trigger_by_share_recipients: Notify when actions are performed by a share recipient?
    :type trigger_by_share_recipients: bool
    :param triggering_filenames: Array of filenames (possibly with wildcards) to match for action path
    :type triggering_filenames: List[str]
    :param triggering_group_ids: Only notify on actions made by a member of one of the specified groups
    :type triggering_group_ids: List[int]
    :param triggering_user_ids: Only notify on actions made one of the specified users
    :type triggering_user_ids: List[int]

    """
    return web.Response(status=200)


async def post_notifications(request: web.Request, group_id=None, message=None, notify_on_copy=None, notify_on_delete=None, notify_on_download=None, notify_on_move=None, notify_on_upload=None, notify_user_actions=None, path=None, recursive=None, send_interval=None, trigger_by_share_recipients=None, triggering_filenames=None, triggering_group_ids=None, triggering_user_ids=None, user_id=None, username=None) -> web.Response:
    """Create Notification

    Create Notification

    :param group_id: The ID of the group to notify.  Provide &#x60;user_id&#x60;, &#x60;username&#x60; or &#x60;group_id&#x60;.
    :type group_id: int
    :param message: Custom message to include in notification emails.
    :type message: str
    :param notify_on_copy: If &#x60;true&#x60;, copying or moving resources into this path will trigger a notification, in addition to just uploads.
    :type notify_on_copy: bool
    :param notify_on_delete: Triggers notification when deleting files from this path
    :type notify_on_delete: bool
    :param notify_on_download: Triggers notification when downloading files from this path
    :type notify_on_download: bool
    :param notify_on_move: Triggers notification when moving files to this path
    :type notify_on_move: bool
    :param notify_on_upload: Triggers notification when uploading new files to this path
    :type notify_on_upload: bool
    :param notify_user_actions: If &#x60;true&#x60; actions initiated by the user will still result in a notification
    :type notify_user_actions: bool
    :param path: Path
    :type path: str
    :param recursive: If &#x60;true&#x60;, enable notifications for each subfolder in this path
    :type recursive: bool
    :param send_interval: The time interval that notifications are aggregated by.  Can be &#x60;five_minutes&#x60;, &#x60;fifteen_minutes&#x60;, &#x60;hourly&#x60;, or &#x60;daily&#x60;.
    :type send_interval: str
    :param trigger_by_share_recipients: Notify when actions are performed by a share recipient?
    :type trigger_by_share_recipients: bool
    :param triggering_filenames: Array of filenames (possibly with wildcards) to match for action path
    :type triggering_filenames: List[str]
    :param triggering_group_ids: Only notify on actions made by a member of one of the specified groups
    :type triggering_group_ids: List[int]
    :param triggering_user_ids: Only notify on actions made one of the specified users
    :type triggering_user_ids: List[int]
    :param user_id: The id of the user to notify. Provide &#x60;user_id&#x60;, &#x60;username&#x60; or &#x60;group_id&#x60;.
    :type user_id: int
    :param username: The username of the user to notify.  Provide &#x60;user_id&#x60;, &#x60;username&#x60; or &#x60;group_id&#x60;.
    :type username: str

    """
    return web.Response(status=200)
