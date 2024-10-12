from typing import List, Dict
from aiohttp import web

from openapi_server.models.container_service import ContainerService
from openapi_server.models.container_service_list_result import ContainerServiceListResult
from openapi_server import util


async def container_services_delete(request: web.Request, resource_group_name, container_service_name, api_version, subscription_id) -> web.Response:
    """Deletes the specified container service.

    Deletes the specified container service in the specified subscription and resource group. The operation does not delete other resources created as part of creating a container service, including storage accounts, VMs, and availability sets. All the other resources created with the container service are part of the same resource group and can be deleted individually.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param container_service_name: The name of the container service in the specified subscription and resource group.
    :type container_service_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def container_services_get(request: web.Request, resource_group_name, container_service_name, api_version, subscription_id) -> web.Response:
    """Gets the properties of the specified container service.

    Gets the properties of the specified container service in the specified subscription and resource group. The operation returns the properties including state, orchestrator, number of masters and agents, and FQDNs of masters and agents. 

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param container_service_name: The name of the container service in the specified subscription and resource group.
    :type container_service_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def container_services_list_by_resource_group(request: web.Request, resource_group_name, api_version, subscription_id) -> web.Response:
    """Gets a list of container services in the specified resource group.

    Gets a list of container services in the specified subscription and resource group. The operation returns properties of each container service including state, orchestrator, number of masters and agents, and FQDNs of masters and agents.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)
