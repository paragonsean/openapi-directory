from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.private_endpoint_connection import PrivateEndpointConnection
from openapi_server import util


async def private_endpoint_connections_delete(request: web.Request, resource_group_name, account_name, api_version, subscription_id, private_endpoint_connection_name) -> web.Response:
    """private_endpoint_connections_delete

    Deletes the specified private endpoint connection associated with the storage account.

    :param resource_group_name: The name of the resource group within the user&#39;s subscription. The name is case insensitive.
    :type resource_group_name: str
    :param account_name: The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.
    :type account_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param private_endpoint_connection_name: The name of the private endpoint connection associated with the Storage Account
    :type private_endpoint_connection_name: str

    """
    return web.Response(status=200)


async def private_endpoint_connections_get(request: web.Request, resource_group_name, account_name, api_version, subscription_id, private_endpoint_connection_name) -> web.Response:
    """private_endpoint_connections_get

    Gets the specified private endpoint connection associated with the storage account.

    :param resource_group_name: The name of the resource group within the user&#39;s subscription. The name is case insensitive.
    :type resource_group_name: str
    :param account_name: The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.
    :type account_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param private_endpoint_connection_name: The name of the private endpoint connection associated with the Storage Account
    :type private_endpoint_connection_name: str

    """
    return web.Response(status=200)


async def private_endpoint_connections_put(request: web.Request, resource_group_name, account_name, api_version, subscription_id, private_endpoint_connection_name, properties) -> web.Response:
    """private_endpoint_connections_put

    Update the state of specified private endpoint connection associated with the storage account.

    :param resource_group_name: The name of the resource group within the user&#39;s subscription. The name is case insensitive.
    :type resource_group_name: str
    :param account_name: The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.
    :type account_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param private_endpoint_connection_name: The name of the private endpoint connection associated with the Storage Account
    :type private_endpoint_connection_name: str
    :param properties: The private endpoint connection properties.
    :type properties: dict | bytes

    """
    properties = PrivateEndpointConnection.from_dict(properties)
    return web.Response(status=200)
