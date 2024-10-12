from typing import List, Dict
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.server_key import ServerKey
from openapi_server.models.server_key_list_result import ServerKeyListResult
from openapi_server import util


async def server_keys_create_or_update(request: web.Request, resource_group_name, server_name, key_name, subscription_id, api_version, parameters) -> web.Response:
    """server_keys_create_or_update

    Creates or updates a MySQL Server key.

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param key_name: The name of the MySQL Server key to be operated on (updated or created).
    :type key_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str
    :param parameters: The requested MySQL Server key resource state.
    :type parameters: dict | bytes

    """
    parameters = ServerKey.from_dict(parameters)
    return web.Response(status=200)


async def server_keys_delete(request: web.Request, resource_group_name, server_name, key_name, subscription_id, api_version) -> web.Response:
    """server_keys_delete

    Deletes the MySQL Server key with the given name.

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param key_name: The name of the MySQL Server key to be deleted.
    :type key_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str

    """
    return web.Response(status=200)


async def server_keys_get(request: web.Request, resource_group_name, server_name, key_name, subscription_id, api_version) -> web.Response:
    """server_keys_get

    Gets a MySQL Server key.

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param key_name: The name of the MySQL Server key to be retrieved.
    :type key_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str

    """
    return web.Response(status=200)


async def server_keys_list_by_instance(request: web.Request, resource_group_name, server_name, subscription_id, api_version) -> web.Response:
    """server_keys_list_by_instance

    Gets a list of  Server keys.

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
