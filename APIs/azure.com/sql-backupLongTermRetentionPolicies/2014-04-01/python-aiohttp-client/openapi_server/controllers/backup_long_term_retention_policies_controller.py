from typing import List, Dict
from aiohttp import web

from openapi_server.models.backup_long_term_retention_policy import BackupLongTermRetentionPolicy
from openapi_server.models.backup_long_term_retention_policy_list_result import BackupLongTermRetentionPolicyListResult
from openapi_server import util


async def backup_long_term_retention_policies_create_or_update(request: web.Request, api_version, subscription_id, resource_group_name, server_name, database_name, backup_long_term_retention_policy_name, parameters) -> web.Response:
    """backup_long_term_retention_policies_create_or_update

    Creates or updates a database backup long term retention policy

    :param api_version: The API version to use for the request.
    :type api_version: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param database_name: The name of the database
    :type database_name: str
    :param backup_long_term_retention_policy_name: The name of the backup long term retention policy
    :type backup_long_term_retention_policy_name: str
    :param parameters: The required parameters to update a backup long term retention policy
    :type parameters: dict | bytes

    """
    parameters = BackupLongTermRetentionPolicy.from_dict(parameters)
    return web.Response(status=200)


async def backup_long_term_retention_policies_get(request: web.Request, api_version, subscription_id, resource_group_name, server_name, database_name, backup_long_term_retention_policy_name) -> web.Response:
    """backup_long_term_retention_policies_get

    Returns a database backup long term retention policy

    :param api_version: The API version to use for the request.
    :type api_version: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param database_name: The name of the database.
    :type database_name: str
    :param backup_long_term_retention_policy_name: The name of the backup long term retention policy
    :type backup_long_term_retention_policy_name: str

    """
    return web.Response(status=200)


async def backup_long_term_retention_policies_list_by_database(request: web.Request, api_version, subscription_id, resource_group_name, server_name, database_name) -> web.Response:
    """backup_long_term_retention_policies_list_by_database

    Returns a database backup long term retention policy

    :param api_version: The API version to use for the request.
    :type api_version: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param database_name: The name of the database.
    :type database_name: str

    """
    return web.Response(status=200)
