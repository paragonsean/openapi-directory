from typing import List, Dict
from aiohttp import web

from openapi_server.models.notification_get_default_response import NotificationGetDefaultResponse
from openapi_server.models.recipient_email_collection import RecipientEmailCollection
from openapi_server.models.recipient_email_contract import RecipientEmailContract
from openapi_server import util


async def notification_recipient_email_create_or_update(request: web.Request, resource_group_name, service_name, notification_name, email, api_version, subscription_id) -> web.Response:
    """notification_recipient_email_create_or_update

    Adds the Email address to the list of Recipients for the Notification.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param notification_name: Notification Name Identifier.
    :type notification_name: str
    :param email: Email identifier.
    :type email: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def notification_recipient_email_delete(request: web.Request, resource_group_name, service_name, notification_name, email, api_version, subscription_id) -> web.Response:
    """notification_recipient_email_delete

    Removes the email from the list of Notification.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param notification_name: Notification Name Identifier.
    :type notification_name: str
    :param email: Email identifier.
    :type email: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def notification_recipient_email_get(request: web.Request, resource_group_name, service_name, notification_name, email, api_version, subscription_id) -> web.Response:
    """notification_recipient_email_get

    Determine if Notification Recipient Email subscribed to the notification.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param notification_name: Notification Name Identifier.
    :type notification_name: str
    :param email: Email identifier.
    :type email: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def notification_recipient_email_list_by_notification(request: web.Request, resource_group_name, service_name, notification_name, api_version, subscription_id) -> web.Response:
    """notification_recipient_email_list_by_notification

    Gets the list of the Notification Recipient Emails subscribed to a notification.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param notification_name: Notification Name Identifier.
    :type notification_name: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)
