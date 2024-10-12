from typing import List, Dict
from aiohttp import web

from openapi_server.models.notification_collection import NotificationCollection
from openapi_server.models.notification_contract import NotificationContract
from openapi_server.models.notification_get_default_response import NotificationGetDefaultResponse
from openapi_server.models.recipient_user_collection import RecipientUserCollection
from openapi_server import util


async def notification_create_or_update(request: web.Request, resource_group_name, service_name, notification_name, api_version, subscription_id, if_match=None) -> web.Response:
    """notification_create_or_update

    Updates an Notification.

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
    :param if_match: ETag of the Entity. Not required when creating an entity, but required when updating an entity.
    :type if_match: str

    """
    return web.Response(status=200)


async def notification_get(request: web.Request, resource_group_name, service_name, notification_name, api_version, subscription_id) -> web.Response:
    """notification_get

    Gets the details of the Notification specified by its identifier.

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


async def notification_list_by_service(request: web.Request, resource_group_name, service_name, api_version, subscription_id, top=None, skip=None) -> web.Response:
    """notification_list_by_service

    Lists a collection of properties defined within a service instance.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param top: Number of records to return.
    :type top: int
    :param skip: Number of records to skip.
    :type skip: int

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
