from typing import List, Dict
from aiohttp import web

from openapi_server.models.container_service import ContainerService
from openapi_server.models.container_service_list_result import ContainerServiceListResult
from openapi_server import util


async def container_service_create_or_update(request: web.Request, resource_group_name, container_service_name, api_version, subscription_id, parameters) -> web.Response:
    """container_service_create_or_update

    The operation to create or update a container service.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param container_service_name: The name of the container service within the given subscription and resource group.
    :type container_service_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters supplied to the Create Container Service operation.
    :type parameters: dict | bytes

    """
    parameters = ContainerService.from_dict(parameters)
    return web.Response(status=200)


async def container_service_delete(request: web.Request, resource_group_name, container_service_name, api_version, subscription_id) -> web.Response:
    """container_service_delete

    The operation to delete a container service.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param container_service_name: The name of the container service within the given subscription and resource group.
    :type container_service_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def container_service_get(request: web.Request, resource_group_name, container_service_name, api_version, subscription_id) -> web.Response:
    """container_service_get

    The operation to get a container service.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param container_service_name: The name of the container service within the given subscription and resource group.
    :type container_service_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def container_service_list_by_resource_group(request: web.Request, resource_group_name, api_version, subscription_id) -> web.Response:
    """container_service_list_by_resource_group

    The operation to list container services.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)
