from typing import List, Dict
from aiohttp import web

from openapi_server.models.metric_definition_list import MetricDefinitionList
from openapi_server.models.metric_list import MetricList
from openapi_server.models.volume_container import VolumeContainer
from openapi_server.models.volume_container_list import VolumeContainerList
from openapi_server import util


async def volume_containers_create_or_update(request: web.Request, device_name, volume_container_name, subscription_id, resource_group_name, manager_name, api_version, parameters) -> web.Response:
    """volume_containers_create_or_update

    Creates or updates the volume container.

    :param device_name: The device name
    :type device_name: str
    :param volume_container_name: The name of the volume container.
    :type volume_container_name: str
    :param subscription_id: The subscription id
    :type subscription_id: str
    :param resource_group_name: The resource group name
    :type resource_group_name: str
    :param manager_name: The manager name
    :type manager_name: str
    :param api_version: The api version
    :type api_version: str
    :param parameters: The volume container to be added or updated.
    :type parameters: dict | bytes

    """
    parameters = VolumeContainer.from_dict(parameters)
    return web.Response(status=200)


async def volume_containers_delete(request: web.Request, device_name, volume_container_name, subscription_id, resource_group_name, manager_name, api_version) -> web.Response:
    """volume_containers_delete

    Deletes the volume container.

    :param device_name: The device name
    :type device_name: str
    :param volume_container_name: The name of the volume container.
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


async def volume_containers_get(request: web.Request, device_name, volume_container_name, subscription_id, resource_group_name, manager_name, api_version) -> web.Response:
    """volume_containers_get

    Gets the properties of the specified volume container name.

    :param device_name: The device name
    :type device_name: str
    :param volume_container_name: The name of the volume container.
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


async def volume_containers_list_by_device(request: web.Request, device_name, subscription_id, resource_group_name, manager_name, api_version) -> web.Response:
    """volume_containers_list_by_device

    Gets all the volume containers in a device.

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


async def volume_containers_list_metric_definition(request: web.Request, device_name, volume_container_name, subscription_id, resource_group_name, manager_name, api_version) -> web.Response:
    """volume_containers_list_metric_definition

    Gets the metric definitions for the specified volume container.

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


async def volume_containers_list_metrics(request: web.Request, device_name, volume_container_name, subscription_id, resource_group_name, manager_name, api_version, filter) -> web.Response:
    """volume_containers_list_metrics

    Gets the metrics for the specified volume container.

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
    :param filter: OData Filter options
    :type filter: str

    """
    return web.Response(status=200)
