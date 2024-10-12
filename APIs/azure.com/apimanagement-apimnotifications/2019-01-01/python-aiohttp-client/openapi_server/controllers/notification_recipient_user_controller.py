from typing import List, Dict
from aiohttp import web

from openapi_server.models.notification_list_by_service_default_response import NotificationListByServiceDefaultResponse
from openapi_server.models.notification_recipient_user_create_or_update200_response import NotificationRecipientUserCreateOrUpdate200Response
from openapi_server.models.notification_recipient_user_list_by_notification200_response import NotificationRecipientUserListByNotification200Response
from openapi_server import util


async def notification_recipient_user_check_entity_exists(request: web.Request, resource_group_name, service_name, notification_name, user_id, api_version, subscription_id) -> web.Response:
    """notification_recipient_user_check_entity_exists

    Determine if the Notification Recipient User is subscribed to the notification.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param notification_name: Notification Name Identifier.
    :type notification_name: str
    :param user_id: User identifier. Must be unique in the current API Management service instance.
    :type user_id: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def notification_recipient_user_create_or_update(request: web.Request, resource_group_name, service_name, notification_name, user_id, api_version, subscription_id) -> web.Response:
    """notification_recipient_user_create_or_update

    Adds the API Management User to the list of Recipients for the Notification.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param notification_name: Notification Name Identifier.
    :type notification_name: str
    :param user_id: User identifier. Must be unique in the current API Management service instance.
    :type user_id: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def notification_recipient_user_delete(request: web.Request, resource_group_name, service_name, notification_name, user_id, api_version, subscription_id) -> web.Response:
    """notification_recipient_user_delete

    Removes the API Management user from the list of Notification.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param notification_name: Notification Name Identifier.
    :type notification_name: str
    :param user_id: User identifier. Must be unique in the current API Management service instance.
    :type user_id: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def notification_recipient_user_list_by_notification(request: web.Request, resource_group_name, service_name, notification_name, api_version, subscription_id) -> web.Response:
    """notification_recipient_user_list_by_notification

    Gets the list of the Notification Recipient User subscribed to the notification.

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
