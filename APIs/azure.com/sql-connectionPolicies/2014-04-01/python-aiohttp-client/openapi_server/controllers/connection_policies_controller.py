from typing import List, Dict
from aiohttp import web

from openapi_server.models.server_connection_policy import ServerConnectionPolicy
from openapi_server import util


async def server_connection_policies_create_or_update(request: web.Request, api_version, subscription_id, resource_group_name, server_name, connection_policy_name, parameters) -> web.Response:
    """server_connection_policies_create_or_update

    Creates or updates the server&#39;s connection policy.

    :param api_version: The API version to use for the request.
    :type api_version: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param connection_policy_name: The name of the connection policy.
    :type connection_policy_name: str
    :param parameters: The required parameters for updating a secure connection policy.
    :type parameters: dict | bytes

    """
    parameters = ServerConnectionPolicy.from_dict(parameters)
    return web.Response(status=200)


async def server_connection_policies_get(request: web.Request, api_version, subscription_id, resource_group_name, server_name, connection_policy_name) -> web.Response:
    """server_connection_policies_get

    Gets the server&#39;s secure connection policy.

    :param api_version: The API version to use for the request.
    :type api_version: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param connection_policy_name: The name of the connection policy.
    :type connection_policy_name: str

    """
    return web.Response(status=200)
