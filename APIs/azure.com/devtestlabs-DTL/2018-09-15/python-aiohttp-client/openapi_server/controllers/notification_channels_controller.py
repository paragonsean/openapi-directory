from typing import List, Dict
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.notification_channel import NotificationChannel
from openapi_server.models.notification_channel_fragment import NotificationChannelFragment
from openapi_server.models.notification_channel_list import NotificationChannelList
from openapi_server.models.notify_parameters import NotifyParameters
from openapi_server import util


async def notification_channels_create_or_update(request: web.Request, subscription_id, resource_group_name, lab_name, name, api_version, notification_channel) -> web.Response:
    """notification_channels_create_or_update

    Create or replace an existing notification channel.

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param lab_name: The name of the lab.
    :type lab_name: str
    :param name: The name of the notification channel.
    :type name: str
    :param api_version: Client API version.
    :type api_version: str
    :param notification_channel: A notification.
    :type notification_channel: dict | bytes

    """
    notification_channel = NotificationChannel.from_dict(notification_channel)
    return web.Response(status=200)


async def notification_channels_delete(request: web.Request, subscription_id, resource_group_name, lab_name, name, api_version) -> web.Response:
    """notification_channels_delete

    Delete notification channel.

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param lab_name: The name of the lab.
    :type lab_name: str
    :param name: The name of the notification channel.
    :type name: str
    :param api_version: Client API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def notification_channels_get(request: web.Request, subscription_id, resource_group_name, lab_name, name, api_version, expand=None) -> web.Response:
    """notification_channels_get

    Get notification channel.

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param lab_name: The name of the lab.
    :type lab_name: str
    :param name: The name of the notification channel.
    :type name: str
    :param api_version: Client API version.
    :type api_version: str
    :param expand: Specify the $expand query. Example: &#39;properties($select&#x3D;webHookUrl)&#39;
    :type expand: str

    """
    return web.Response(status=200)


async def notification_channels_list(request: web.Request, subscription_id, resource_group_name, lab_name, api_version, expand=None, filter=None, top=None, orderby=None) -> web.Response:
    """notification_channels_list

    List notification channels in a given lab.

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param lab_name: The name of the lab.
    :type lab_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param expand: Specify the $expand query. Example: &#39;properties($select&#x3D;webHookUrl)&#39;
    :type expand: str
    :param filter: The filter to apply to the operation. Example: &#39;$filter&#x3D;contains(name,&#39;myName&#39;)
    :type filter: str
    :param top: The maximum number of resources to return from the operation. Example: &#39;$top&#x3D;10&#39;
    :type top: int
    :param orderby: The ordering expression for the results, using OData notation. Example: &#39;$orderby&#x3D;name desc&#39;
    :type orderby: str

    """
    return web.Response(status=200)


async def notification_channels_notify(request: web.Request, subscription_id, resource_group_name, lab_name, name, api_version, notify_parameters) -> web.Response:
    """notification_channels_notify

    Send notification to provided channel.

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param lab_name: The name of the lab.
    :type lab_name: str
    :param name: The name of the notification channel.
    :type name: str
    :param api_version: Client API version.
    :type api_version: str
    :param notify_parameters: Properties for generating a Notification.
    :type notify_parameters: dict | bytes

    """
    notify_parameters = NotifyParameters.from_dict(notify_parameters)
    return web.Response(status=200)


async def notification_channels_update(request: web.Request, subscription_id, resource_group_name, lab_name, name, api_version, notification_channel) -> web.Response:
    """notification_channels_update

    Allows modifying tags of notification channels. All other properties will be ignored.

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param lab_name: The name of the lab.
    :type lab_name: str
    :param name: The name of the notification channel.
    :type name: str
    :param api_version: Client API version.
    :type api_version: str
    :param notification_channel: A notification.
    :type notification_channel: dict | bytes

    """
    notification_channel = NotificationChannelFragment.from_dict(notification_channel)
    return web.Response(status=200)
