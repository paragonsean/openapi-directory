from typing import List, Dict
from aiohttp import web

from openapi_server.models.action_notification_export_entity import ActionNotificationExportEntity
from openapi_server import util


async def get_action_notification_exports_id(request: web.Request, id) -> web.Response:
    """Show Action Notification Export

    Show Action Notification Export

    :param id: Action Notification Export ID.
    :type id: int

    """
    return web.Response(status=200)


async def post_action_notification_exports(request: web.Request, end_at=None, query_folder=None, query_message=None, query_path=None, query_request_method=None, query_request_url=None, query_status=None, query_success=None, start_at=None, user_id=None) -> web.Response:
    """Create Action Notification Export

    Create Action Notification Export

    :param end_at: End date/time of export range.
    :type end_at: str
    :param query_folder: Return notifications that were triggered by actions in this folder.
    :type query_folder: str
    :param query_message: Error message associated with the request, if any.
    :type query_message: str
    :param query_path: Return notifications that were triggered by actions on this specific path.
    :type query_path: str
    :param query_request_method: The HTTP request method used by the webhook.
    :type query_request_method: str
    :param query_request_url: The target webhook URL.
    :type query_request_url: str
    :param query_status: The HTTP status returned from the server in response to the webhook request.
    :type query_status: str
    :param query_success: true if the webhook request succeeded (i.e. returned a 200 or 204 response status). false otherwise.
    :type query_success: bool
    :param start_at: Start date/time of export range.
    :type start_at: str
    :param user_id: User ID.  Provide a value of &#x60;0&#x60; to operate the current session&#39;s user.
    :type user_id: int

    """
    end_at = util.deserialize_datetime(end_at)
    start_at = util.deserialize_datetime(start_at)
    return web.Response(status=200)
