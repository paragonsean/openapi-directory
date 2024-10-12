from typing import List, Dict
from aiohttp import web

from openapi_server.models.backup_storage_config import BackupStorageConfig
from openapi_server import util


async def backup_storage_configs_get(request: web.Request, subscription_id, api_version, resource_group_name, vault_name) -> web.Response:
    """backup_storage_configs_get

    Fetches resource storage config.

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


async def backup_storage_configs_update(request: web.Request, subscription_id, api_version, resource_group_name, vault_name, backup_storage_config) -> web.Response:
    """backup_storage_configs_update

    Updates vault storage model type.

    :param subscription_id: The subscription Id.
    :type subscription_id: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param resource_group_name: The name of the resource group where the recovery services vault is present.
    :type resource_group_name: str
    :param vault_name: The name of the recovery services vault.
    :type vault_name: str
    :param backup_storage_config: Backup storage config.
    :type backup_storage_config: dict | bytes

    """
    backup_storage_config = BackupStorageConfig.from_dict(backup_storage_config)
    return web.Response(status=200)
