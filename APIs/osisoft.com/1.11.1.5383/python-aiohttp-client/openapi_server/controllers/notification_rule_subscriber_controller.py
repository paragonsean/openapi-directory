from typing import List, Dict
from aiohttp import web

from openapi_server.models.items_notification_rule_subscriber import ItemsNotificationRuleSubscriber
from openapi_server.models.notification_rule_subscriber import NotificationRuleSubscriber
from openapi_server import util


async def notification_rule_subscriber_delete(request: web.Request, web_id) -> web.Response:
    """Delete a notification rule subscriber.

    

    :param web_id: The ID of the notification rule subscriber.
    :type web_id: str

    """
    return web.Response(status=200)


async def notification_rule_subscriber_get(request: web.Request, web_id, selected_fields=None, web_id_type=None) -> web.Response:
    """Retrieve a notification rule subscriber.

    

    :param web_id: The ID of the resource to use as the root of the search.
    :type web_id: str
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    return web.Response(status=200)


async def notification_rule_subscriber_get_by_path(request: web.Request, path, selected_fields=None, web_id_type=None) -> web.Response:
    """Retrieve a notification rule subscriber by path.

    This method returns a Notification Rule Subscriber based on the hierarchical path associated with it, and should be used when a path has been received from a separate part of the PI System for use in the PI Web API. Users should primarily search with the WebID when available.

    :param path: The path to the notification rule subscriber.
    :type path: str
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    return web.Response(status=200)


async def notification_rule_subscriber_get_notification_rule_subscribers(request: web.Request, web_id, selected_fields=None, web_id_type=None) -> web.Response:
    """Retrieve notification rule subscriber subscribers.

    

    :param web_id: The ID of the resource to use as the root of the search.
    :type web_id: str
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    return web.Response(status=200)


async def notification_rule_subscriber_update(request: web.Request, web_id, notification_rule_subscriber) -> web.Response:
    """Update a notification rule subscriber.

    

    :param web_id: The ID of the notification rule subscriber.
    :type web_id: str
    :param notification_rule_subscriber: A partial notification rule subscriber containing the desired changes.
    :type notification_rule_subscriber: dict | bytes

    """
    notification_rule_subscriber = NotificationRuleSubscriber.from_dict(notification_rule_subscriber)
    return web.Response(status=200)
