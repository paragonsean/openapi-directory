from typing import List, Dict
from aiohttp import web

from openapi_server.models.bandwidth_schedule import BandwidthSchedule
from openapi_server.models.bandwidth_schedules_list import BandwidthSchedulesList
from openapi_server.models.cloud_error import CloudError
from openapi_server import util


async def bandwidth_schedules_create_or_update(request: web.Request, device_name, name, subscription_id, resource_group_name, api_version, parameters) -> web.Response:
    """bandwidth_schedules_create_or_update

    Creates or updates a bandwidth schedule.

    :param device_name: The device name.
    :type device_name: str
    :param name: The bandwidth schedule name which needs to be added/updated.
    :type name: str
    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param api_version: The API version.
    :type api_version: str
    :param parameters: The bandwidth schedule to be added or updated.
    :type parameters: dict | bytes

    """
    parameters = BandwidthSchedule.from_dict(parameters)
    return web.Response(status=200)


async def bandwidth_schedules_delete(request: web.Request, device_name, name, subscription_id, resource_group_name, api_version) -> web.Response:
    """bandwidth_schedules_delete

    Deletes the specified bandwidth schedule.

    :param device_name: The device name.
    :type device_name: str
    :param name: The bandwidth schedule name.
    :type name: str
    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param api_version: The API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def bandwidth_schedules_get(request: web.Request, device_name, name, subscription_id, resource_group_name, api_version) -> web.Response:
    """bandwidth_schedules_get

    Gets the properties of the specified bandwidth schedule.

    :param device_name: The device name.
    :type device_name: str
    :param name: The bandwidth schedule name.
    :type name: str
    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param api_version: The API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def bandwidth_schedules_list_by_data_box_edge_device(request: web.Request, device_name, subscription_id, resource_group_name, api_version) -> web.Response:
    """bandwidth_schedules_list_by_data_box_edge_device

    Gets all the bandwidth schedules for a data box edge/gateway device.

    :param device_name: The device name.
    :type device_name: str
    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param api_version: The API version.
    :type api_version: str

    """
    return web.Response(status=200)
