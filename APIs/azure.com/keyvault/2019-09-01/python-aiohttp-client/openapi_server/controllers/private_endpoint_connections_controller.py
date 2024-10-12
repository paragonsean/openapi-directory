from typing import List, Dict
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.private_endpoint_connection import PrivateEndpointConnection
from openapi_server import util


async def private_endpoint_connections_delete(request: web.Request, subscription_id, resource_group_name, vault_name, private_endpoint_connection_name, api_version) -> web.Response:
    """private_endpoint_connections_delete

    Deletes the specified private endpoint connection associated with the key vault.

    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: Name of the resource group that contains the key vault.
    :type resource_group_name: str
    :param vault_name: The name of the key vault.
    :type vault_name: str
    :param private_endpoint_connection_name: Name of the private endpoint connection associated with the key vault.
    :type private_endpoint_connection_name: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def private_endpoint_connections_get(request: web.Request, subscription_id, resource_group_name, vault_name, private_endpoint_connection_name, api_version) -> web.Response:
    """private_endpoint_connections_get

    Gets the specified private endpoint connection associated with the key vault.

    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: Name of the resource group that contains the key vault.
    :type resource_group_name: str
    :param vault_name: The name of the key vault.
    :type vault_name: str
    :param private_endpoint_connection_name: Name of the private endpoint connection associated with the key vault.
    :type private_endpoint_connection_name: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def private_endpoint_connections_put(request: web.Request, subscription_id, resource_group_name, vault_name, private_endpoint_connection_name, api_version, properties) -> web.Response:
    """private_endpoint_connections_put

    Updates the specified private endpoint connection associated with the key vault.

    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: Name of the resource group that contains the key vault.
    :type resource_group_name: str
    :param vault_name: The name of the key vault.
    :type vault_name: str
    :param private_endpoint_connection_name: Name of the private endpoint connection associated with the key vault.
    :type private_endpoint_connection_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param properties: The intended state of private endpoint connection.
    :type properties: dict | bytes

    """
    properties = PrivateEndpointConnection.from_dict(properties)
    return web.Response(status=200)
