from typing import List, Dict
from aiohttp import web

from openapi_server.models.metric_definition_list import MetricDefinitionList
from openapi_server.models.metric_list import MetricList
from openapi_server.models.volume import Volume
from openapi_server.models.volume_list import VolumeList
from openapi_server import util


async def volumes_create_or_update(request: web.Request, device_name, volume_container_name, volume_name, subscription_id, resource_group_name, manager_name, api_version, parameters) -> web.Response:
    """volumes_create_or_update

    Creates or updates the volume.

    :param device_name: The device name
    :type device_name: str
    :param volume_container_name: The volume container name.
    :type volume_container_name: str
    :param volume_name: The volume name.
    :type volume_name: str
    :param subscription_id: The subscription id
    :type subscription_id: str
    :param resource_group_name: The resource group name
    :type resource_group_name: str
    :param manager_name: The manager name
    :type manager_name: str
    :param api_version: The api version
    :type api_version: str
    :param parameters: Volume to be created or updated.
    :type parameters: dict | bytes

    """
    parameters = Volume.from_dict(parameters)
    return web.Response(status=200)


async def volumes_delete(request: web.Request, device_name, volume_container_name, volume_name, subscription_id, resource_group_name, manager_name, api_version) -> web.Response:
    """volumes_delete

    Deletes the volume.

    :param device_name: The device name
    :type device_name: str
    :param volume_container_name: The volume container name.
    :type volume_container_name: str
    :param volume_name: The volume name.
    :type volume_name: str
    :param subscription_id: The subscription id
    :type subscription_id: str
    :param resource_group_name: The resource group name
    :type resource_group_name: str
    :param manager_name: The manager name
    :type manager_name: str
    :param api_version: The api version
    :type api_version: str

    """
    return web.Response(status=200)


async def volumes_get(request: web.Request, device_name, volume_container_name, volume_name, subscription_id, resource_group_name, manager_name, api_version) -> web.Response:
    """volumes_get

    Returns the properties of the specified volume name.

    :param device_name: The device name
    :type device_name: str
    :param volume_container_name: The volume container name.
    :type volume_container_name: str
    :param volume_name: The volume name.
    :type volume_name: str
    :param subscription_id: The subscription id
    :type subscription_id: str
    :param resource_group_name: The resource group name
    :type resource_group_name: str
    :param manager_name: The manager name
    :type manager_name: str
    :param api_version: The api version
    :type api_version: str

    """
    return web.Response(status=200)


async def volumes_list_by_device(request: web.Request, device_name, subscription_id, resource_group_name, manager_name, api_version) -> web.Response:
    """volumes_list_by_device

    Retrieves all the volumes in a device.

    :param device_name: The device name
    :type device_name: str
    :param subscription_id: The subscription id
    :type subscription_id: str
    :param resource_group_name: The resource group name
    :type resource_group_name: str
    :param manager_name: The manager name
    :type manager_name: str
    :param api_version: The api version
    :type api_version: str

    """
    return web.Response(status=200)


async def volumes_list_by_volume_container(request: web.Request, device_name, volume_container_name, subscription_id, resource_group_name, manager_name, api_version) -> web.Response:
    """volumes_list_by_volume_container

    Retrieves all the volumes in a volume container.

    :param device_name: The device name
    :type device_name: str
    :param volume_container_name: The volume container name.
    :type volume_container_name: str
    :param subscription_id: The subscription id
    :type subscription_id: str
    :param resource_group_name: The resource group name
    :type resource_group_name: str
    :param manager_name: The manager name
    :type manager_name: str
    :param api_version: The api version
    :type api_version: str

    """
    return web.Response(status=200)


async def volumes_list_metric_definition(request: web.Request, device_name, volume_container_name, volume_name, subscription_id, resource_group_name, manager_name, api_version) -> web.Response:
    """volumes_list_metric_definition

    Gets the metric definitions for the specified volume.

    :param device_name: The device name
    :type device_name: str
    :param volume_container_name: The volume container name.
    :type volume_container_name: str
    :param volume_name: The volume name.
    :type volume_name: str
    :param subscription_id: The subscription id
    :type subscription_id: str
    :param resource_group_name: The resource group name
    :type resource_group_name: str
    :param manager_name: The manager name
    :type manager_name: str
    :param api_version: The api version
    :type api_version: str

    """
    return web.Response(status=200)


async def volumes_list_metrics(request: web.Request, device_name, volume_container_name, volume_name, subscription_id, resource_group_name, manager_name, api_version, filter) -> web.Response:
    """volumes_list_metrics

    Gets the metrics for the specified volume.

    :param device_name: The device name
    :type device_name: str
    :param volume_container_name: The volume container name.
    :type volume_container_name: str
    :param volume_name: The volume name.
    :type volume_name: str
    :param subscription_id: The subscription id
    :type subscription_id: str
    :param resource_group_name: The resource group name
    :type resource_group_name: str
    :param manager_name: The manager name
    :type manager_name: str
    :param api_version: The api version
    :type api_version: str
    :param filter: OData Filter options
    :type filter: str

    """
    return web.Response(status=200)
