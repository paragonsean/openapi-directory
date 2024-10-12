from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.private_endpoint_connection import PrivateEndpointConnection
from openapi_server.models.private_endpoint_connection_list_result import PrivateEndpointConnectionListResult
from openapi_server import util


async def private_endpoint_connections_create_or_update(request: web.Request, subscription_id, resource_group_name, config_store_name, api_version, private_endpoint_connection_name, private_endpoint_connection) -> web.Response:
    """private_endpoint_connections_create_or_update

    Update the state of the specified private endpoint connection associated with the configuration store.

    :param subscription_id: The Microsoft Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group to which the container registry belongs.
    :type resource_group_name: str
    :param config_store_name: The name of the configuration store.
    :type config_store_name: str
    :param api_version: The client API version.
    :type api_version: str
    :param private_endpoint_connection_name: Private endpoint connection name
    :type private_endpoint_connection_name: str
    :param private_endpoint_connection: The private endpoint connection properties.
    :type private_endpoint_connection: dict | bytes

    """
    private_endpoint_connection = PrivateEndpointConnection.from_dict(private_endpoint_connection)
    return web.Response(status=200)


async def private_endpoint_connections_delete(request: web.Request, subscription_id, resource_group_name, config_store_name, api_version, private_endpoint_connection_name) -> web.Response:
    """private_endpoint_connections_delete

    Deletes a private endpoint connection.

    :param subscription_id: The Microsoft Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group to which the container registry belongs.
    :type resource_group_name: str
    :param config_store_name: The name of the configuration store.
    :type config_store_name: str
    :param api_version: The client API version.
    :type api_version: str
    :param private_endpoint_connection_name: Private endpoint connection name
    :type private_endpoint_connection_name: str

    """
    return web.Response(status=200)


async def private_endpoint_connections_get(request: web.Request, subscription_id, resource_group_name, config_store_name, api_version, private_endpoint_connection_name) -> web.Response:
    """private_endpoint_connections_get

    Gets the specified private endpoint connection associated with the configuration store.

    :param subscription_id: The Microsoft Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group to which the container registry belongs.
    :type resource_group_name: str
    :param config_store_name: The name of the configuration store.
    :type config_store_name: str
    :param api_version: The client API version.
    :type api_version: str
    :param private_endpoint_connection_name: Private endpoint connection name
    :type private_endpoint_connection_name: str

    """
    return web.Response(status=200)


async def private_endpoint_connections_list_by_configuration_store(request: web.Request, subscription_id, resource_group_name, config_store_name, api_version) -> web.Response:
    """private_endpoint_connections_list_by_configuration_store

    Lists all private endpoint connections for a configuration store.

    :param subscription_id: The Microsoft Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group to which the container registry belongs.
    :type resource_group_name: str
    :param config_store_name: The name of the configuration store.
    :type config_store_name: str
    :param api_version: The client API version.
    :type api_version: str

    """
    return web.Response(status=200)
