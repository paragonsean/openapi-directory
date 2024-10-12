from typing import List, Dict
from aiohttp import web

from openapi_server.models.backup_long_term_retention_vault import BackupLongTermRetentionVault
from openapi_server.models.backup_long_term_retention_vault_list_result import BackupLongTermRetentionVaultListResult
from openapi_server import util


async def backup_long_term_retention_vaults_create_or_update(request: web.Request, api_version, subscription_id, resource_group_name, server_name, backup_long_term_retention_vault_name, parameters) -> web.Response:
    """backup_long_term_retention_vaults_create_or_update

    Updates a server backup long term retention vault

    :param api_version: The API version to use for the request.
    :type api_version: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param backup_long_term_retention_vault_name: The name of the backup long term retention vault
    :type backup_long_term_retention_vault_name: str
    :param parameters: The required parameters to update a backup long term retention vault
    :type parameters: dict | bytes

    """
    parameters = BackupLongTermRetentionVault.from_dict(parameters)
    return web.Response(status=200)


async def backup_long_term_retention_vaults_get(request: web.Request, api_version, subscription_id, resource_group_name, server_name, backup_long_term_retention_vault_name) -> web.Response:
    """backup_long_term_retention_vaults_get

    Gets a server backup long term retention vault

    :param api_version: The API version to use for the request.
    :type api_version: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param backup_long_term_retention_vault_name: The name of the Azure SQL Server backup LongTermRetention vault
    :type backup_long_term_retention_vault_name: str

    """
    return web.Response(status=200)


async def backup_long_term_retention_vaults_list_by_server(request: web.Request, api_version, subscription_id, resource_group_name, server_name) -> web.Response:
    """backup_long_term_retention_vaults_list_by_server

    Gets server backup long term retention vaults in a server

    :param api_version: The API version to use for the request.
    :type api_version: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str

    """
    return web.Response(status=200)
