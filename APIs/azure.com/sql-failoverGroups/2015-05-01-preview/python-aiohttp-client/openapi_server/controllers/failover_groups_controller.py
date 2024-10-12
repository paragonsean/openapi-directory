from typing import List, Dict
from aiohttp import web

from openapi_server.models.failover_group import FailoverGroup
from openapi_server.models.failover_group_list_result import FailoverGroupListResult
from openapi_server.models.failover_group_update import FailoverGroupUpdate
from openapi_server import util


async def failover_groups_create_or_update(request: web.Request, resource_group_name, server_name, failover_group_name, subscription_id, api_version, parameters) -> web.Response:
    """failover_groups_create_or_update

    Creates or updates a failover group.

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server containing the failover group.
    :type server_name: str
    :param failover_group_name: The name of the failover group.
    :type failover_group_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str
    :param parameters: The failover group parameters.
    :type parameters: dict | bytes

    """
    parameters = FailoverGroup.from_dict(parameters)
    return web.Response(status=200)


async def failover_groups_delete(request: web.Request, resource_group_name, server_name, failover_group_name, subscription_id, api_version) -> web.Response:
    """failover_groups_delete

    Deletes a failover group.

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server containing the failover group.
    :type server_name: str
    :param failover_group_name: The name of the failover group.
    :type failover_group_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str

    """
    return web.Response(status=200)


async def failover_groups_failover(request: web.Request, resource_group_name, server_name, failover_group_name, subscription_id, api_version) -> web.Response:
    """failover_groups_failover

    Fails over from the current primary server to this server.

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server containing the failover group.
    :type server_name: str
    :param failover_group_name: The name of the failover group.
    :type failover_group_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str

    """
    return web.Response(status=200)


async def failover_groups_force_failover_allow_data_loss(request: web.Request, resource_group_name, server_name, failover_group_name, subscription_id, api_version) -> web.Response:
    """failover_groups_force_failover_allow_data_loss

    Fails over from the current primary server to this server. This operation might result in data loss.

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server containing the failover group.
    :type server_name: str
    :param failover_group_name: The name of the failover group.
    :type failover_group_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str

    """
    return web.Response(status=200)


async def failover_groups_get(request: web.Request, resource_group_name, server_name, failover_group_name, subscription_id, api_version) -> web.Response:
    """failover_groups_get

    Gets a failover group.

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server containing the failover group.
    :type server_name: str
    :param failover_group_name: The name of the failover group.
    :type failover_group_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str

    """
    return web.Response(status=200)


async def failover_groups_list_by_server(request: web.Request, resource_group_name, server_name, subscription_id, api_version) -> web.Response:
    """failover_groups_list_by_server

    Lists the failover groups in a server.

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server containing the failover group.
    :type server_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str

    """
    return web.Response(status=200)


async def failover_groups_update(request: web.Request, resource_group_name, server_name, failover_group_name, subscription_id, api_version, parameters) -> web.Response:
    """failover_groups_update

    Updates a failover group.

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server containing the failover group.
    :type server_name: str
    :param failover_group_name: The name of the failover group.
    :type failover_group_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str
    :param parameters: The failover group parameters.
    :type parameters: dict | bytes

    """
    parameters = FailoverGroupUpdate.from_dict(parameters)
    return web.Response(status=200)
