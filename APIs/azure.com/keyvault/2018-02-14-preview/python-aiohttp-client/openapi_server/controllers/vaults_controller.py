from typing import List, Dict
from aiohttp import web

from openapi_server.models.check_name_availability_result import CheckNameAvailabilityResult
from openapi_server.models.deleted_vault import DeletedVault
from openapi_server.models.deleted_vault_list_result import DeletedVaultListResult
from openapi_server.models.resource_list_result import ResourceListResult
from openapi_server.models.vault import Vault
from openapi_server.models.vault_access_policy_parameters import VaultAccessPolicyParameters
from openapi_server.models.vault_check_name_availability_parameters import VaultCheckNameAvailabilityParameters
from openapi_server.models.vault_create_or_update_parameters import VaultCreateOrUpdateParameters
from openapi_server.models.vault_list_result import VaultListResult
from openapi_server.models.vault_patch_parameters import VaultPatchParameters
from openapi_server import util


async def vaults_check_name_availability(request: web.Request, api_version, subscription_id, vault_name) -> web.Response:
    """vaults_check_name_availability

    Checks that the vault name is valid and is not already in use.

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param vault_name: The name of the vault.
    :type vault_name: dict | bytes

    """
    vault_name = VaultCheckNameAvailabilityParameters.from_dict(vault_name)
    return web.Response(status=200)


async def vaults_create_or_update(request: web.Request, resource_group_name, vault_name, api_version, subscription_id, parameters) -> web.Response:
    """vaults_create_or_update

    Create or update a key vault in the specified subscription.

    :param resource_group_name: The name of the Resource Group to which the server belongs.
    :type resource_group_name: str
    :param vault_name: Name of the vault
    :type vault_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
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
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
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
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def vaults_get_deleted(request: web.Request, vault_name, location, api_version, subscription_id) -> web.Response:
    """vaults_get_deleted

    Gets the deleted Azure key vault.

    :param vault_name: The name of the vault.
    :type vault_name: str
    :param location: The location of the deleted vault.
    :type location: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
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
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
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
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param top: Maximum number of results to return.
    :type top: int

    """
    return web.Response(status=200)


async def vaults_list_by_subscription(request: web.Request, api_version, subscription_id, top=None) -> web.Response:
    """vaults_list_by_subscription

    The List operation gets information about the vaults associated with the subscription.

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param top: Maximum number of results to return.
    :type top: int

    """
    return web.Response(status=200)


async def vaults_list_deleted(request: web.Request, api_version, subscription_id) -> web.Response:
    """vaults_list_deleted

    Gets information about the deleted vaults in a subscription.

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def vaults_purge_deleted(request: web.Request, vault_name, location, api_version, subscription_id) -> web.Response:
    """vaults_purge_deleted

    Permanently deletes the specified vault. aka Purges the deleted Azure key vault.

    :param vault_name: The name of the soft-deleted vault.
    :type vault_name: str
    :param location: The location of the soft-deleted vault.
    :type location: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def vaults_update(request: web.Request, resource_group_name, vault_name, api_version, subscription_id, parameters) -> web.Response:
    """vaults_update

    Update a key vault in the specified subscription.

    :param resource_group_name: The name of the Resource Group to which the server belongs.
    :type resource_group_name: str
    :param vault_name: Name of the vault
    :type vault_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters to patch the vault
    :type parameters: dict | bytes

    """
    parameters = VaultPatchParameters.from_dict(parameters)
    return web.Response(status=200)


async def vaults_update_access_policy(request: web.Request, resource_group_name, vault_name, operation_kind, api_version, subscription_id, parameters) -> web.Response:
    """vaults_update_access_policy

    Update access policies in a key vault in the specified subscription.

    :param resource_group_name: The name of the Resource Group to which the vault belongs.
    :type resource_group_name: str
    :param vault_name: Name of the vault
    :type vault_name: str
    :param operation_kind: Name of the operation
    :type operation_kind: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Access policy to merge into the vault
    :type parameters: dict | bytes

    """
    parameters = VaultAccessPolicyParameters.from_dict(parameters)
    return web.Response(status=200)
