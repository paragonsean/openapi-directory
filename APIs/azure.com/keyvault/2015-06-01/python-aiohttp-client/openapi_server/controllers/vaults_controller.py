from typing import List, Dict
from aiohttp import web

from openapi_server.models.resource_list_result import ResourceListResult
from openapi_server.models.vault import Vault
from openapi_server.models.vault_create_or_update_parameters import VaultCreateOrUpdateParameters
from openapi_server.models.vault_list_result import VaultListResult
from openapi_server import util


async def vaults_create_or_update(request: web.Request, resource_group_name, vault_name, api_version, subscription_id, parameters) -> web.Response:
    """vaults_create_or_update

    Create or update a key vault in the specified subscription.

    :param resource_group_name: The name of the Resource Group to which the server belongs.
    :type resource_group_name: str
    :param vault_name: Name of the vault
    :type vault_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters to create or update the vault
    :type parameters: dict | bytes

    """
    parameters = VaultCreateOrUpdateParameters.from_dict(parameters)
    return web.Response(status=200)


async def vaults_delete(request: web.Request, resource_group_name, vault_name, api_version, subscription_id) -> web.Response:
    """vaults_delete

    Deletes the specified Azure key vault.

    :param resource_group_name: The name of the Resource Group to which the vault belongs.
    :type resource_group_name: str
    :param vault_name: The name of the vault to delete
    :type vault_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def vaults_get(request: web.Request, resource_group_name, vault_name, api_version, subscription_id) -> web.Response:
    """vaults_get

    Gets the specified Azure key vault.

    :param resource_group_name: The name of the Resource Group to which the vault belongs.
    :type resource_group_name: str
    :param vault_name: The name of the vault.
    :type vault_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def vaults_list(request: web.Request, filter, api_version, subscription_id, top=None) -> web.Response:
    """vaults_list

    The List operation gets information about the vaults associated with the subscription.

    :param filter: The filter to apply on the operation.
    :type filter: str
    :param api_version: Azure Resource Manager Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param top: Maximum number of results to return.
    :type top: int

    """
    return web.Response(status=200)


async def vaults_list_by_resource_group(request: web.Request, resource_group_name, api_version, subscription_id, top=None) -> web.Response:
    """vaults_list_by_resource_group

    The List operation gets information about the vaults associated with the subscription and within the specified resource group.

    :param resource_group_name: The name of the Resource Group to which the vault belongs.
    :type resource_group_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param top: Maximum number of results to return.
    :type top: int

    """
    return web.Response(status=200)
