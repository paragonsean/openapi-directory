from typing import List, Dict
from aiohttp import web

from openapi_server.models.managed_database_security_alert_policy import ManagedDatabaseSecurityAlertPolicy
from openapi_server.models.managed_database_security_alert_policy_list_result import ManagedDatabaseSecurityAlertPolicyListResult
from openapi_server import util


async def managed_database_security_alert_policies_create_or_update(request: web.Request, resource_group_name, managed_instance_name, database_name, security_alert_policy_name, subscription_id, api_version, parameters) -> web.Response:
    """managed_database_security_alert_policies_create_or_update

    Creates or updates a database&#39;s security alert policy.

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param managed_instance_name: The name of the managed instance.
    :type managed_instance_name: str
    :param database_name: The name of the managed database for which the security alert policy is defined.
    :type database_name: str
    :param security_alert_policy_name: The name of the security alert policy.
    :type security_alert_policy_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str
    :param parameters: The database security alert policy.
    :type parameters: dict | bytes

    """
    parameters = ManagedDatabaseSecurityAlertPolicy.from_dict(parameters)
    return web.Response(status=200)


async def managed_database_security_alert_policies_get(request: web.Request, resource_group_name, managed_instance_name, database_name, security_alert_policy_name, subscription_id, api_version) -> web.Response:
    """managed_database_security_alert_policies_get

    Gets a managed database&#39;s security alert policy.

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param managed_instance_name: The name of the managed instance.
    :type managed_instance_name: str
    :param database_name: The name of the managed database for which the security alert policy is defined.
    :type database_name: str
    :param security_alert_policy_name: The name of the security alert policy.
    :type security_alert_policy_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str

    """
    return web.Response(status=200)


async def managed_database_security_alert_policies_list_by_database(request: web.Request, resource_group_name, managed_instance_name, database_name, subscription_id, api_version) -> web.Response:
    """managed_database_security_alert_policies_list_by_database

    Gets a list of managed database&#39;s security alert policies.

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param managed_instance_name: The name of the managed instance.
    :type managed_instance_name: str
    :param database_name: The name of the managed database for which the security alert policies are defined.
    :type database_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str

    """
    return web.Response(status=200)
