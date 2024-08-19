from typing import List, Dict
from aiohttp import web

from openapi_server.models.container_group import ContainerGroup
from openapi_server.models.container_group_list_result import ContainerGroupListResult
from openapi_server.models.logs import Logs
from openapi_server.models.usage_list_result import UsageListResult
from openapi_server import util


async def container_group_usage_list(request: web.Request, subscription_id, location, api_version) -> web.Response:
    """container_group_usage_list

    Get the usage for a subscription

    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param location: The identifier for the physical azure location.
    :type location: str
    :param api_version: Client API version
    :type api_version: str

    """
    return web.Response(status=200)


async def container_groups_create_or_update(request: web.Request, subscription_id, api_version, resource_group_name, container_group_name, container_group) -> web.Response:
    """Create or update container groups.

    Create or update container groups with specified configurations.

    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client API version
    :type api_version: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param container_group_name: The name of the container group.
    :type container_group_name: str
    :param container_group: The properties of the container group to be created or updated.
    :type container_group: dict | bytes

    """
    container_group = ContainerGroup.from_dict(container_group)
    return web.Response(status=200)


async def container_groups_delete(request: web.Request, subscription_id, api_version, resource_group_name, container_group_name) -> web.Response:
    """Delete the specified container group.

    Delete the specified container group in the specified subscription and resource group. The operation does not delete other resources provided by the user, such as volumes.

    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client API version
    :type api_version: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param container_group_name: The name of the container group.
    :type container_group_name: str

    """
    return web.Response(status=200)


async def container_groups_get(request: web.Request, subscription_id, api_version, resource_group_name, container_group_name) -> web.Response:
    """Get the properties of the specified container group.

    Gets the properties of the specified container group in the specified subscription and resource group. The operation returns the properties of each container group including containers, image registry credentials, restart policy, IP address type, OS type, state, and volumes.

    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client API version
    :type api_version: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param container_group_name: The name of the container group.
    :type container_group_name: str

    """
    return web.Response(status=200)


async def container_groups_list(request: web.Request, subscription_id, api_version) -> web.Response:
    """Get a list of container groups in the specified subscription.

    Get a list of container groups in the specified subscription. This operation returns properties of each container group including containers, image registry credentials, restart policy, IP address type, OS type, state, and volumes.

    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client API version
    :type api_version: str

    """
    return web.Response(status=200)


async def container_groups_list_by_resource_group(request: web.Request, subscription_id, api_version, resource_group_name) -> web.Response:
    """Get a list of container groups in the specified subscription and resource group.

    Get a list of container groups in a specified subscription and resource group. This operation returns properties of each container group including containers, image registry credentials, restart policy, IP address type, OS type, state, and volumes.

    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client API version
    :type api_version: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str

    """
    return web.Response(status=200)


async def container_logs_list(request: web.Request, subscription_id, api_version, resource_group_name, container_group_name, container_name, tail=None) -> web.Response:
    """Get the logs for a specified container instance.

    Get the logs for a specified container instance in a specified resource group and container group.

    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client API version
    :type api_version: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param container_group_name: The name of the container group.
    :type container_group_name: str
    :param container_name: The name of the container instance.
    :type container_name: str
    :param tail: The number of lines to show from the tail of the container instance log. If not provided, all available logs are shown up to 4mb.
    :type tail: int

    """
    return web.Response(status=200)
