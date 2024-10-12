from typing import List, Dict
from aiohttp import web

from openapi_server.models.backup_long_term_retention_policy import BackupLongTermRetentionPolicy
from openapi_server import util


async def backup_long_term_retention_policies_create_or_update(request: web.Request, resource_group_name, server_name, database_name, policy_name, subscription_id, api_version, parameters) -> web.Response:
    """backup_long_term_retention_policies_create_or_update

    Sets a database&#39;s long term retention policy.

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param database_name: The name of the database.
    :type database_name: str
    :param policy_name: The policy name. Should always be Default.
    :type policy_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str
    :param parameters: The long term retention policy info.
    :type parameters: dict | bytes

    """
    parameters = BackupLongTermRetentionPolicy.from_dict(parameters)
    return web.Response(status=200)


async def backup_long_term_retention_policies_get(request: web.Request, resource_group_name, server_name, database_name, policy_name, subscription_id, api_version) -> web.Response:
    """backup_long_term_retention_policies_get

    Gets a database&#39;s long term retention policy.

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param database_name: The name of the database.
    :type database_name: str
    :param policy_name: The policy name. Should always be Default.
    :type policy_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str

    """
    return web.Response(status=200)


async def backup_long_term_retention_policies_list_by_database(request: web.Request, resource_group_name, server_name, database_name, subscription_id, api_version) -> web.Response:
    """backup_long_term_retention_policies_list_by_database

    Gets a database&#39;s long term retention policy.

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param database_name: The name of the database.
    :type database_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str

    """
    return web.Response(status=200)
