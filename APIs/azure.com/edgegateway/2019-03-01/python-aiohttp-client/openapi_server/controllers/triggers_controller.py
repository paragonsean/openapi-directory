from typing import List, Dict
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.trigger import Trigger
from openapi_server.models.trigger_list import TriggerList
from openapi_server import util


async def triggers_create_or_update(request: web.Request, device_name, name, subscription_id, resource_group_name, api_version, trigger) -> web.Response:
    """triggers_create_or_update

    Creates or updates a trigger.

    :param device_name: Creates or updates a trigger
    :type device_name: str
    :param name: The trigger name.
    :type name: str
    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param api_version: The API version.
    :type api_version: str
    :param trigger: The trigger.
    :type trigger: dict | bytes

    """
    trigger = Trigger.from_dict(trigger)
    return web.Response(status=200)


async def triggers_delete(request: web.Request, device_name, name, subscription_id, resource_group_name, api_version) -> web.Response:
    """triggers_delete

    Deletes the trigger on the gateway device.

    :param device_name: The device name.
    :type device_name: str
    :param name: The trigger name.
    :type name: str
    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param api_version: The API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def triggers_get(request: web.Request, device_name, name, subscription_id, resource_group_name, api_version) -> web.Response:
    """triggers_get

    Get a specific trigger by name.

    :param device_name: The device name.
    :type device_name: str
    :param name: The trigger name.
    :type name: str
    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param api_version: The API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def triggers_list_by_data_box_edge_device(request: web.Request, device_name, subscription_id, resource_group_name, api_version, expand=None) -> web.Response:
    """triggers_list_by_data_box_edge_device

    Lists all the triggers configured in the device.

    :param device_name: The device name.
    :type device_name: str
    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param api_version: The API version.
    :type api_version: str
    :param expand: Specify $filter&#x3D;&#39;CustomContextTag eq &lt;tag&gt;&#39; to filter on custom context tag property
    :type expand: str

    """
    return web.Response(status=200)
