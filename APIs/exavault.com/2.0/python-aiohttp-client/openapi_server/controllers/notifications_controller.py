from typing import List, Dict
from aiohttp import web

from openapi_server.models.add_notification_request_body import AddNotificationRequestBody
from openapi_server.models.empty_response import EmptyResponse
from openapi_server.models.notification_collection_response import NotificationCollectionResponse
from openapi_server.models.notification_response import NotificationResponse
from openapi_server.models.update_notification_by_id_request_body import UpdateNotificationByIdRequestBody
from openapi_server import util


async def add_notification(request: web.Request, ev_api_key, ev_access_token, body=None) -> web.Response:
    """Create a new notification

    Create a new notification for a [resource](#section/Identifying-Resources) in your account. Notifications can be sent via email or webhook;  - To enable email, pass an array of email addresses to the &#x60;recipients&#x60; parameter of this call.  - To enable webhooks, setup the webhook callback URL in your account settings via [PATCH /account](#operation/updateAccount).   **Notes:**   - Authenticated user should have [notifications permission](/docs/account/04-users/00-introduction#managing-user-roles-and-permissions) 

    :param ev_api_key: API Key required to make API call. 
    :type ev_api_key: str
    :param ev_access_token: Access token required to make the API call.
    :type ev_access_token: str
    :param body: 
    :type body: dict | bytes

    """
    body = AddNotificationRequestBody.from_dict(body)
    return web.Response(status=200)


async def delete_notification_by_id(request: web.Request, ev_api_key, ev_access_token, id) -> web.Response:
    """Delete a notification

    Deletes a notification. Note that deleting a notification _only_ deletes the notification &amp;ndash; it does not delete any underlying files or folders.  **Notes:**  - You need to have the [notifications permission](/docs/account/04-users/00-introduction#managing-user-roles-and-permissions) to update a notification. - You can only delete notifications owned by your user account.

    :param ev_api_key: API Key required to make the API call.
    :type ev_api_key: str
    :param ev_access_token: Access token required to make the API call.
    :type ev_access_token: str
    :param id: ID of the notification. Use [GET /notifications](#operation/listNotifications) if you need to lookup an ID.
    :type id: int

    """
    return web.Response(status=200)


async def get_notification_by_id(request: web.Request, ev_api_key, ev_access_token, id, include=None) -> web.Response:
    """Get notification details

    Get the details for a notification with a specific ID number. You&#39;ll be able to review its path, triggers and who&#39;s getting the notification.   **Notes**  - You need to have the [notifications permission](/docs/account/04-users/00-introduction#managing-user-roles-and-permissions) to view the detail for a notification. - You can only retrieve notifications owned by your user account.

    :param ev_api_key: API Key required to make the API call.
    :type ev_api_key: str
    :param ev_access_token: Access token required to make the API call.
    :type ev_access_token: str
    :param id: ID of the notification. Use [GET /notifications](#operation/listNotifications) if you need to lookup an ID.
    :type id: int
    :param include: Related record types to include in the response. You can include multiple types by separating them with commas. Valid options are **ownerUser**, **resource**, and **share**.
    :type include: str

    """
    return web.Response(status=200)


async def list_notifications(request: web.Request, ev_api_key, ev_access_token, type=None, offset=None, sort=None, limit=None, include=None, action=None) -> web.Response:
    """Get a list of notifications

    Get a list of all the [notifications](/docs/account/06-notifications) you have access to. You can use sorting and filtering to limit the returned list.  **Notes:**   - Authenticated user should have [notifications permission](/docs/account/04-users/00-introduction#managing-user-roles-and-permissions)

    :param ev_api_key: API Key required to make the API call. 
    :type ev_api_key: str
    :param ev_access_token: Access token required to make the API call.
    :type ev_access_token: str
    :param type: Type of notification include in the list. Valid options are **file**, **folder**, **send_receipt**, **share_receipt**, **file_drop**  If this parameter is not used, only **file** and **folder** type notifications are included in the list.
    :type type: str
    :param offset: Starting notification record in the result set. Can be used for pagination.
    :type offset: int
    :param sort: What order the list of matches should be in. Valid sort fields are **resourcename**, **date**, **action** and **type**. The sort order for each sort field is ascending unless it is prefixed with a minus (“-“), in which case it will be descending.  You can chose multiple options for the sort by separating them with commmas, such as \&quot;type,-date\&quot; to sort by type, then most recent.
    :type sort: str
    :param limit: Number of notification records to return. Can be used for pagination.
    :type limit: int
    :param include: Related records to include in the response. Valid options are **ownerUser**, **resource**, **share**
    :type include: str
    :param action: The kind of action which triggers the notification. Valid choices are **connect** (only for delivery receipts), **download**, **upload**, **delete**, or **all**   **Note** The **all** action matches notifications set to \&quot;all\&quot;, not all notifications. For example, notifications set to trigger only on delete are not included if you filter for action&#x3D;all
    :type action: str

    """
    return web.Response(status=200)


async def update_notification_by_id(request: web.Request, ev_api_key, ev_access_token, id, body=None) -> web.Response:
    """Update a notification

    Update an existing notification. You can add additional emails or change the action or users that cause a notification to trigger.   When updating recipient emails, make sure your &#x60;recipients&#x60; parameter contains the full list of people who should be included on the notification. If you resend the list without an existing recipient, they will be deleted from the notification emails.   **Notes:**  - You need to have the [notifications permission](/docs/account/04-users/00-introduction#managing-user-roles-and-permissions) to update a notification. - You can only change notifications owned by your user account.

    :param ev_api_key: API Key required to make the API call.
    :type ev_api_key: str
    :param ev_access_token: Access token required to make the API call.
    :type ev_access_token: str
    :param id: ID of the notification. Use [GET /notifications](#operation/listNotifications) if you need to lookup an ID.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNotificationByIdRequestBody.from_dict(body)
    return web.Response(status=200)
