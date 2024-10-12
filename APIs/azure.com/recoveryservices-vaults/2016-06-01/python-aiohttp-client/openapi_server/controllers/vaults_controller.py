from typing import List, Dict
from aiohttp import web

from openapi_server.models.patch_vault import PatchVault
from openapi_server.models.vault import Vault
from openapi_server.models.vault_list import VaultList
from openapi_server import util


async def vaults_create_or_update(request: web.Request, subscription_id, api_version, resource_group_name, vault_name, vault) -> web.Response:
    """vaults_create_or_update

    Creates or updates a Recovery Services vault.

    :param subscription_id: The subscription Id.
    :type subscription_id: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param resource_group_name: The name of the resource group where the recovery services vault is present.
    :type resource_group_name: str
    :param vault_name: The name of the recovery services vault.
    :type vault_name: str
    :param vault: Recovery Services Vault to be created.
    :type vault: dict | bytes

    """
    vault = Vault.from_dict(vault)
    return web.Response(status=200)


async def vaults_delete(request: web.Request, subscription_id, api_version, resource_group_name, vault_name) -> web.Response:
    """vaults_delete

    Deletes a vault.

    :param subscription_id: The subscription Id.
    :type subscription_id: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param resource_group_name: The name of the resource group where the recovery services vault is present.
    :type resource_group_name: str
    :param vault_name: The name of the recovery services vault.
    :type vault_name: str

    """
    return web.Response(status=200)


async def vaults_get(request: web.Request, subscription_id, api_version, resource_group_name, vault_name) -> web.Response:
    """vaults_get

    Get the Vault details.

    :param subscription_id: The subscription Id.
    :type subscription_id: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param resource_group_name: The name of the resource group where the recovery services vault is present.
    :type resource_group_name: str
    :param vault_name: The name of the recovery services vault.
    :type vault_name: str

    """
    return web.Response(status=200)


async def vaults_list_by_resource_group(request: web.Request, subscription_id, api_version, resource_group_name) -> web.Response:
    """vaults_list_by_resource_group

    Retrieve a list of Vaults.

    :param subscription_id: The subscription Id.
    :type subscription_id: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param resource_group_name: The name of the resource group where the recovery services vault is present.
    :type resource_group_name: str

    """
    return web.Response(status=200)


async def vaults_list_by_subscription_id(request: web.Request, subscription_id, api_version) -> web.Response:
    """vaults_list_by_subscription_id

    Fetches all the resources of the specified type in the subscription.

    :param subscription_id: The subscription Id.
    :type subscription_id: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def vaults_update(request: web.Request, subscription_id, api_version, resource_group_name, vault_name, vault) -> web.Response:
    """vaults_update

    Updates the vault.

    :param subscription_id: The subscription Id.
    :type subscription_id: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param resource_group_name: The name of the resource group where the recovery services vault is present.
    :type resource_group_name: str
    :param vault_name: The name of the recovery services vault.
    :type vault_name: str
    :param vault: Recovery Services Vault to be created.
    :type vault: dict | bytes

    """
    vault = PatchVault.from_dict(vault)
    return web.Response(status=200)
