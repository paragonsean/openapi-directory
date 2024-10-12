from typing import List, Dict
from aiohttp import web

from openapi_server.models.container_service import ContainerService
from openapi_server.models.container_service_list_result import ContainerServiceListResult
from openapi_server import util


async def container_services_create_or_update(request: web.Request, resource_group_name, container_service_name, api_version, subscription_id, parameters) -> web.Response:
    """Creates or updates a container service.

    Creates or updates a container service with the specified configuration of orchestrator, masters, and agents.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param container_service_name: The name of the container service in the specified subscription and resource group.
    :type container_service_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters supplied to the Create or Update a Container Service operation.
    :type parameters: dict | bytes

    """
    parameters = ContainerService.from_dict(parameters)
    return web.Response(status=200)


async def container_services_list(request: web.Request, api_version, subscription_id) -> web.Response:
    """Gets a list of container services in the specified subscription.

    Gets a list of container services in the specified subscription. The operation returns properties of each container service including state, orchestrator, number of masters and agents, and FQDNs of masters and agents.

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)
