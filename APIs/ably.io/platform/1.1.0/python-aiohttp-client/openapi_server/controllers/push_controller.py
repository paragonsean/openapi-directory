from typing import List, Dict
from aiohttp import web

from openapi_server.models.device_details import DeviceDetails
from openapi_server.models.error import Error
from openapi_server.models.publish_push_notification_to_devices_request import PublishPushNotificationToDevicesRequest
from openapi_server.models.subscribe_push_device_to_channel_request import SubscribePushDeviceToChannelRequest
from openapi_server import util


async def delete_push_device_details(request: web.Request, x_ably_version=None, format=None, channel=None, device_id=None, client_id=None) -> web.Response:
    """Delete a registered device&#39;s update token

    Delete a device details object.

    :param x_ably_version: The version of the API you wish to use.
    :type x_ably_version: str
    :param format: The response format you would like
    :type format: str
    :param channel: Filter to restrict to subscriptions associated with that channel.
    :type channel: str
    :param device_id: Must be set when clientId is empty, cannot be used with clientId.
    :type device_id: str
    :param client_id: Must be set when deviceId is empty, cannot be used with deviceId.
    :type client_id: str

    """
    return web.Response(status=200)


async def get_channels_with_push_subscribers(request: web.Request, x_ably_version=None, format=None) -> web.Response:
    """List all channels with at least one subscribed device

    Returns a paginated response of channel names.

    :param x_ably_version: The version of the API you wish to use.
    :type x_ably_version: str
    :param format: The response format you would like
    :type format: str

    """
    return web.Response(status=200)


async def get_push_device_details(request: web.Request, device_id, x_ably_version=None, format=None) -> web.Response:
    """Get a device registration

    Get the full details of a device.

    :param device_id: Device&#39;s ID.
    :type device_id: str
    :param x_ably_version: The version of the API you wish to use.
    :type x_ably_version: str
    :param format: The response format you would like
    :type format: str

    """
    return web.Response(status=200)


async def get_push_subscriptions_on_channels(request: web.Request, x_ably_version=None, format=None, channel=None, device_id=None, client_id=None, limit=None) -> web.Response:
    """List channel subscriptions

    Get a list of push notification subscriptions to channels.

    :param x_ably_version: The version of the API you wish to use.
    :type x_ably_version: str
    :param format: The response format you would like
    :type format: str
    :param channel: Filter to restrict to subscriptions associated with that channel.
    :type channel: str
    :param device_id: Optional filter to restrict to devices associated with that deviceId. Cannot be used with clientId.
    :type device_id: str
    :param client_id: Optional filter to restrict to devices associated with that clientId. Cannot be used with deviceId.
    :type client_id: str
    :param limit: The maximum number of records to return.
    :type limit: int

    """
    return web.Response(status=200)


async def get_registered_push_devices(request: web.Request, x_ably_version=None, format=None, device_id=None, client_id=None, limit=None) -> web.Response:
    """List devices registered for receiving push notifications

    List of device details of devices registed for push notifications.

    :param x_ably_version: The version of the API you wish to use.
    :type x_ably_version: str
    :param format: The response format you would like
    :type format: str
    :param device_id: Optional filter to restrict to devices associated with that deviceId.
    :type device_id: str
    :param client_id: Optional filter to restrict to devices associated with that clientId.
    :type client_id: str
    :param limit: The maximum number of records to return.
    :type limit: int

    """
    return web.Response(status=200)


async def patch_push_device_details(request: web.Request, device_id, x_ably_version=None, format=None, body=None) -> web.Response:
    """Update a device registration

    Specific attributes of an existing registration can be updated. Only clientId, metadata and push.recipient are mutable.

    :param device_id: Device&#39;s ID.
    :type device_id: str
    :param x_ably_version: The version of the API you wish to use.
    :type x_ably_version: str
    :param format: The response format you would like
    :type format: str
    :param body: 
    :type body: dict | bytes

    """
    body = DeviceDetails.from_dict(body)
    return web.Response(status=200)


async def publish_push_notification_to_devices(request: web.Request, x_ably_version=None, format=None, body=None) -> web.Response:
    """Publish a push notification to device(s)

    A convenience endpoint to deliver a push notification payload to a single device or set of devices identified by their client identifier.

    :param x_ably_version: The version of the API you wish to use.
    :type x_ably_version: str
    :param format: The response format you would like
    :type format: str
    :param body: 
    :type body: dict | bytes

    """
    body = PublishPushNotificationToDevicesRequest.from_dict(body)
    return web.Response(status=200)


async def put_push_device_details(request: web.Request, device_id, x_ably_version=None, format=None, body=None) -> web.Response:
    """Update a device registration

    Device registrations can be upserted (the existing registration is replaced entirely) with a PUT operation. Only clientId, metadata and push.recipient are mutable.

    :param device_id: Device&#39;s ID.
    :type device_id: str
    :param x_ably_version: The version of the API you wish to use.
    :type x_ably_version: str
    :param format: The response format you would like
    :type format: str
    :param body: 
    :type body: dict | bytes

    """
    body = DeviceDetails.from_dict(body)
    return web.Response(status=200)


async def register_push_device(request: web.Request, x_ably_version=None, format=None, body=None) -> web.Response:
    """Register a device for receiving push notifications

    Register a device’s details, including the information necessary to deliver push notifications to it. Requires \&quot;push-admin\&quot; capability.

    :param x_ably_version: The version of the API you wish to use.
    :type x_ably_version: str
    :param format: The response format you would like
    :type format: str
    :param body: 
    :type body: dict | bytes

    """
    body = DeviceDetails.from_dict(body)
    return web.Response(status=200)


async def subscribe_push_device_to_channel(request: web.Request, x_ably_version=None, format=None, body=None) -> web.Response:
    """Subscribe a device to a channel

    Subscribe either a single device or all devices associated with a client ID to receive push notifications from messages sent to a channel.

    :param x_ably_version: The version of the API you wish to use.
    :type x_ably_version: str
    :param format: The response format you would like
    :type format: str
    :param body: 
    :type body: dict | bytes

    """
    body = SubscribePushDeviceToChannelRequest.from_dict(body)
    return web.Response(status=200)


async def unregister_all_push_devices(request: web.Request, x_ably_version=None, format=None, device_id=None, client_id=None) -> web.Response:
    """Unregister matching devices for push notifications

    Unregisters devices. All their subscriptions for receiving push notifications through channels will also be deleted.

    :param x_ably_version: The version of the API you wish to use.
    :type x_ably_version: str
    :param format: The response format you would like
    :type format: str
    :param device_id: Optional filter to restrict to devices associated with that deviceId. Cannot be used with clientId.
    :type device_id: str
    :param client_id: Optional filter to restrict to devices associated with that clientId. Cannot be used with deviceId.
    :type client_id: str

    """
    return web.Response(status=200)


async def unregister_push_device(request: web.Request, device_id, x_ably_version=None, format=None) -> web.Response:
    """Unregister a single device for push notifications

    Unregisters a single device by its device ID. All its subscriptions for receiving push notifications through channels will also be deleted.

    :param device_id: Device&#39;s ID.
    :type device_id: str
    :param x_ably_version: The version of the API you wish to use.
    :type x_ably_version: str
    :param format: The response format you would like
    :type format: str

    """
    return web.Response(status=200)


async def update_push_device_details(request: web.Request, device_id, x_ably_version=None, format=None) -> web.Response:
    """Reset a registered device&#39;s update token

    Gets an updated device details object.

    :param device_id: Device&#39;s ID.
    :type device_id: str
    :param x_ably_version: The version of the API you wish to use.
    :type x_ably_version: str
    :param format: The response format you would like
    :type format: str

    """
    return web.Response(status=200)
