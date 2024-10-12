from typing import List, Dict
from aiohttp import web

from openapi_server.models.server_key import ServerKey
from openapi_server.models.server_key_list_result import ServerKeyListResult
from openapi_server import util


async def server_keys_create_or_update(request: web.Request, resource_group_name, server_name, key_name, subscription_id, api_version, parameters) -> web.Response:
    """server_keys_create_or_update

    Creates or updates a server key.

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param key_name: The name of the server key to be operated on (updated or created). The key name is required to be in the format of &#39;vault_key_version&#39;. For example, if the keyId is https://YourVaultName.vault.azure.net/keys/YourKeyName/01234567890123456789012345678901, then the server key name should be formatted as: YourVaultName_YourKeyName_01234567890123456789012345678901
    :type key_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str
    :param parameters: The requested server key resource state.
    :type parameters: dict | bytes

    """
    parameters = ServerKey.from_dict(parameters)
    return web.Response(status=200)


async def server_keys_delete(request: web.Request, resource_group_name, server_name, key_name, subscription_id, api_version) -> web.Response:
    """server_keys_delete

    Deletes the server key with the given name.

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param key_name: The name of the server key to be deleted.
    :type key_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str

    """
    return web.Response(status=200)


async def server_keys_get(request: web.Request, resource_group_name, server_name, key_name, subscription_id, api_version) -> web.Response:
    """server_keys_get

    Gets a server key.

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param key_name: The name of the server key to be retrieved.
    :type key_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str

    """
    return web.Response(status=200)


async def server_keys_list_by_server(request: web.Request, resource_group_name, server_name, subscription_id, api_version) -> web.Response:
    """server_keys_list_by_server

    Gets a list of server keys.

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
