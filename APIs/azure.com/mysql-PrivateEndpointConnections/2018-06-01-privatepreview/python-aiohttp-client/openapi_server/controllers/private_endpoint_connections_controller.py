from typing import List, Dict
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.private_endpoint_connection import PrivateEndpointConnection
from openapi_server.models.private_endpoint_connection_list_result import PrivateEndpointConnectionListResult
from openapi_server.models.tags_object import TagsObject
from openapi_server import util


async def private_endpoint_connections_create_or_update(request: web.Request, resource_group_name, server_name, private_endpoint_connection_name, subscription_id, api_version, parameters) -> web.Response:
    """private_endpoint_connections_create_or_update

    Approve or reject a private endpoint connection with a given name.

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param private_endpoint_connection_name: 
    :type private_endpoint_connection_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str
    :param parameters: 
    :type parameters: dict | bytes

    """
    parameters = PrivateEndpointConnection.from_dict(parameters)
    return web.Response(status=200)


async def private_endpoint_connections_delete(request: web.Request, resource_group_name, server_name, private_endpoint_connection_name, subscription_id, api_version) -> web.Response:
    """private_endpoint_connections_delete

    Deletes a private endpoint connection with a given name.

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param private_endpoint_connection_name: 
    :type private_endpoint_connection_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str

    """
    return web.Response(status=200)


async def private_endpoint_connections_get(request: web.Request, resource_group_name, server_name, private_endpoint_connection_name, subscription_id, api_version) -> web.Response:
    """private_endpoint_connections_get

    Gets a private endpoint connection.

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param private_endpoint_connection_name: The name of the private endpoint connection.
    :type private_endpoint_connection_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str

    """
    return web.Response(status=200)


async def private_endpoint_connections_list_by_server(request: web.Request, resource_group_name, server_name, subscription_id, api_version) -> web.Response:
    """private_endpoint_connections_list_by_server

    Gets all private endpoint connections on a server.

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str

    """
    return web.Response(status=200)


async def private_endpoint_connections_update_tags(request: web.Request, api_version, subscription_id, resource_group_name, server_name, private_endpoint_connection_name, parameters) -> web.Response:
    """Updates tags on private endpoint connection.

    Updates private endpoint connection with the specified tags.

    :param api_version: The API version to use for the request.
    :type api_version: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param private_endpoint_connection_name: 
    :type private_endpoint_connection_name: str
    :param parameters: Parameters supplied to the Update private endpoint connection Tags operation.
    :type parameters: dict | bytes

    """
    parameters = TagsObject.from_dict(parameters)
    return web.Response(status=200)
