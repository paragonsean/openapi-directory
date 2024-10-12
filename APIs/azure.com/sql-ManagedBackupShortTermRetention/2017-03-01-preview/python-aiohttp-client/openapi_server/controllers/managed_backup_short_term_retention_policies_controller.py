from typing import List, Dict
from aiohttp import web

from openapi_server.models.managed_backup_short_term_retention_policy import ManagedBackupShortTermRetentionPolicy
from openapi_server.models.managed_backup_short_term_retention_policy_list_result import ManagedBackupShortTermRetentionPolicyListResult
from openapi_server import util


async def managed_backup_short_term_retention_policies_create_or_update(request: web.Request, resource_group_name, managed_instance_name, database_name, policy_name, subscription_id, api_version, parameters) -> web.Response:
    """managed_backup_short_term_retention_policies_create_or_update

    Updates a managed database&#39;s short term retention policy.

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param managed_instance_name: The name of the managed instance.
    :type managed_instance_name: str
    :param database_name: The name of the database.
    :type database_name: str
    :param policy_name: The policy name. Should always be \&quot;default\&quot;.
    :type policy_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str
    :param parameters: The short term retention policy info.
    :type parameters: dict | bytes

    """
    parameters = ManagedBackupShortTermRetentionPolicy.from_dict(parameters)
    return web.Response(status=200)


async def managed_backup_short_term_retention_policies_get(request: web.Request, resource_group_name, managed_instance_name, database_name, policy_name, subscription_id, api_version) -> web.Response:
    """managed_backup_short_term_retention_policies_get

    Gets a managed database&#39;s short term retention policy.

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param managed_instance_name: The name of the managed instance.
    :type managed_instance_name: str
    :param database_name: The name of the database.
    :type database_name: str
    :param policy_name: The policy name.
    :type policy_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str

    """
    return web.Response(status=200)


async def managed_backup_short_term_retention_policies_list_by_database(request: web.Request, resource_group_name, managed_instance_name, database_name, subscription_id, api_version) -> web.Response:
    """managed_backup_short_term_retention_policies_list_by_database

    Gets a managed database&#39;s short term retention policy list.

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param managed_instance_name: The name of the managed instance.
    :type managed_instance_name: str
    :param database_name: The name of the database.
    :type database_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str

    """
    return web.Response(status=200)


async def managed_backup_short_term_retention_policies_update(request: web.Request, resource_group_name, managed_instance_name, database_name, policy_name, subscription_id, api_version, parameters) -> web.Response:
    """managed_backup_short_term_retention_policies_update

    Updates a managed database&#39;s short term retention policy.

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param managed_instance_name: The name of the managed instance.
    :type managed_instance_name: str
    :param database_name: The name of the database.
    :type database_name: str
    :param policy_name: The policy name. Should always be \&quot;default\&quot;.
    :type policy_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str
    :param parameters: The short term retention policy info.
    :type parameters: dict | bytes

    """
    parameters = ManagedBackupShortTermRetentionPolicy.from_dict(parameters)
    return web.Response(status=200)
