from typing import List, Dict
from aiohttp import web

from openapi_server.models.management_policies_rules_set_parameter import ManagementPoliciesRulesSetParameter
from openapi_server.models.storage_account_management_policies import StorageAccountManagementPolicies
from openapi_server import util


async def management_policies_create_or_update(request: web.Request, resource_group_name, account_name, api_version, subscription_id, management_policy_name, properties) -> web.Response:
    """management_policies_create_or_update

    Sets the data policy rules associated with the specified storage account.

    :param resource_group_name: The name of the resource group within the user&#39;s subscription. The name is case insensitive.
    :type resource_group_name: str
    :param account_name: The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.
    :type account_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param management_policy_name: The name of the Storage Account Management Policy. It should always be &#39;default&#39;
    :type management_policy_name: str
    :param properties: The data policy rules to set to a storage account.
    :type properties: dict | bytes

    """
    properties = ManagementPoliciesRulesSetParameter.from_dict(properties)
    return web.Response(status=200)


async def management_policies_delete(request: web.Request, resource_group_name, account_name, api_version, subscription_id, management_policy_name) -> web.Response:
    """management_policies_delete

    Deletes the data policy rules associated with the specified storage account.

    :param resource_group_name: The name of the resource group within the user&#39;s subscription. The name is case insensitive.
    :type resource_group_name: str
    :param account_name: The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.
    :type account_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param management_policy_name: The name of the Storage Account Management Policy. It should always be &#39;default&#39;
    :type management_policy_name: str

    """
    return web.Response(status=200)


async def management_policies_get(request: web.Request, resource_group_name, account_name, api_version, subscription_id, management_policy_name) -> web.Response:
    """management_policies_get

    Gets the data policy rules associated with the specified storage account.

    :param resource_group_name: The name of the resource group within the user&#39;s subscription. The name is case insensitive.
    :type resource_group_name: str
    :param account_name: The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.
    :type account_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param management_policy_name: The name of the Storage Account Management Policy. It should always be &#39;default&#39;
    :type management_policy_name: str

    """
    return web.Response(status=200)
