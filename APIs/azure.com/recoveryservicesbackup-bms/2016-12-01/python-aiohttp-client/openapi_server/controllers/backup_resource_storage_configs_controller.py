from typing import List, Dict
from aiohttp import web

from openapi_server.models.backup_resource_config_resource import BackupResourceConfigResource
from openapi_server import util


async def backup_resource_storage_configs_get(request: web.Request, api_version, vault_name, resource_group_name, subscription_id) -> web.Response:
    """backup_resource_storage_configs_get

    Fetches resource storage config.

    :param api_version: Client Api Version.
    :type api_version: str
    :param vault_name: The name of the recovery services vault.
    :type vault_name: str
    :param resource_group_name: The name of the resource group where the recovery services vault is present.
    :type resource_group_name: str
    :param subscription_id: The subscription Id.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def backup_resource_storage_configs_patch(request: web.Request, api_version, vault_name, resource_group_name, subscription_id, parameters) -> web.Response:
    """backup_resource_storage_configs_patch

    Updates vault storage model type.

    :param api_version: Client Api Version.
    :type api_version: str
    :param vault_name: The name of the recovery services vault.
    :type vault_name: str
    :param resource_group_name: The name of the resource group where the recovery services vault is present.
    :type resource_group_name: str
    :param subscription_id: The subscription Id.
    :type subscription_id: str
    :param parameters: Vault storage config request
    :type parameters: dict | bytes

    """
    parameters = BackupResourceConfigResource.from_dict(parameters)
    return web.Response(status=200)


async def backup_resource_storage_configs_update(request: web.Request, api_version, vault_name, resource_group_name, subscription_id, parameters) -> web.Response:
    """backup_resource_storage_configs_update

    Updates vault storage model type.

    :param api_version: Client Api Version.
    :type api_version: str
    :param vault_name: The name of the recovery services vault.
    :type vault_name: str
    :param resource_group_name: The name of the resource group where the recovery services vault is present.
    :type resource_group_name: str
    :param subscription_id: The subscription Id.
    :type subscription_id: str
    :param parameters: Vault storage config request
    :type parameters: dict | bytes

    """
    parameters = BackupResourceConfigResource.from_dict(parameters)
    return web.Response(status=200)
