from typing import List, Dict
from aiohttp import web

from openapi_server.models.private_endpoint_connection import PrivateEndpointConnection
from openapi_server.models.private_endpoint_connection_list_result import PrivateEndpointConnectionListResult
from openapi_server import util


async def private_endpoint_connections_create_or_update(request: web.Request, subscription_id, resource_group_name, api_version, scope_name, private_endpoint_connection_name, parameters) -> web.Response:
    """private_endpoint_connections_create_or_update

    Approve or reject a private endpoint connection with a given name.

    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param scope_name: Name of the Azure Monitor PrivateLinkScope that will contain the datasource
    :type scope_name: str
    :param private_endpoint_connection_name: The name of the private endpoint connection.
    :type private_endpoint_connection_name: str
    :param parameters: 
    :type parameters: dict | bytes

    """
    parameters = PrivateEndpointConnection.from_dict(parameters)
    return web.Response(status=200)


async def private_endpoint_connections_delete(request: web.Request, subscription_id, resource_group_name, api_version, scope_name, private_endpoint_connection_name) -> web.Response:
    """private_endpoint_connections_delete

    Deletes a private endpoint connection with a given name.

    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param scope_name: Name of the Azure Monitor PrivateLinkScope that will contain the datasource
    :type scope_name: str
    :param private_endpoint_connection_name: The name of the private endpoint connection.
    :type private_endpoint_connection_name: str

    """
    return web.Response(status=200)


async def private_endpoint_connections_get(request: web.Request, subscription_id, resource_group_name, api_version, scope_name, private_endpoint_connection_name) -> web.Response:
    """private_endpoint_connections_get

    Gets a private endpoint connection.

    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param scope_name: Name of the Azure Monitor PrivateLinkScope that will contain the datasource
    :type scope_name: str
    :param private_endpoint_connection_name: The name of the private endpoint connection.
    :type private_endpoint_connection_name: str

    """
    return web.Response(status=200)


async def private_endpoint_connections_list_by_private_link_scope(request: web.Request, subscription_id, resource_group_name, api_version, scope_name) -> web.Response:
    """private_endpoint_connections_list_by_private_link_scope

    Gets all private endpoint connections on a private link scope.

    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param scope_name: Name of the Azure Monitor PrivateLinkScope that will contain the datasource
    :type scope_name: str

    """
    return web.Response(status=200)
