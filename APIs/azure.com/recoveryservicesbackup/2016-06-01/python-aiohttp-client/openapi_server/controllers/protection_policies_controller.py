from typing import List, Dict
from aiohttp import web

from openapi_server.models.protection_policy_resource import ProtectionPolicyResource
from openapi_server.models.protection_policy_resource_list import ProtectionPolicyResourceList
from openapi_server import util


async def protection_policies_create_or_update(request: web.Request, api_version, vault_name, resource_group_name, subscription_id, policy_name, resource_protection_policy) -> web.Response:
    """protection_policies_create_or_update

    Creates or modifies a backup policy. This is an asynchronous operation. Use the GetPolicyOperationResult API to Get the operation status.

    :param api_version: Client API version.
    :type api_version: str
    :param vault_name: The name of the Recovery Services vault.
    :type vault_name: str
    :param resource_group_name: The name of the resource group associated with the Recovery Services vault.
    :type resource_group_name: str
    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param policy_name: The backup policy to be created.
    :type policy_name: str
    :param resource_protection_policy: The resource backup policy.
    :type resource_protection_policy: dict | bytes

    """
    resource_protection_policy = ProtectionPolicyResource.from_dict(resource_protection_policy)
    return web.Response(status=200)


async def protection_policies_delete(request: web.Request, api_version, vault_name, resource_group_name, subscription_id, policy_name) -> web.Response:
    """protection_policies_delete

    Deletes the specified backup policy from your Recovery Services vault. This is an asynchronous operation. Use the GetPolicyOperationResult API to Get the operation status.

    :param api_version: Client API version.
    :type api_version: str
    :param vault_name: The name of the Recovery Services vault.
    :type vault_name: str
    :param resource_group_name: The name of the resource group associated with the Recovery Services vault.
    :type resource_group_name: str
    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param policy_name: The name of the backup policy to be deleted.
    :type policy_name: str

    """
    return web.Response(status=200)


async def protection_policies_get(request: web.Request, api_version, vault_name, resource_group_name, subscription_id, policy_name) -> web.Response:
    """protection_policies_get

    Gets the details of the backup policy associated with the Recovery Services vault. This is an asynchronous operation. Use the GetPolicyOperationResult API to Get the operation status.

    :param api_version: Client API version.
    :type api_version: str
    :param vault_name: The name of the Recovery Services vault.
    :type vault_name: str
    :param resource_group_name: The name of the resource group associated with the Recovery Services vault.
    :type resource_group_name: str
    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param policy_name: The backup policy name used in this GET operation.
    :type policy_name: str

    """
    return web.Response(status=200)


async def protection_policies_list(request: web.Request, api_version, vault_name, resource_group_name, subscription_id, filter=None) -> web.Response:
    """protection_policies_list

    Lists the backup policies associated with the Recovery Services vault. The API provides parameters to Get scoped results.

    :param api_version: Client API version.
    :type api_version: str
    :param vault_name: The name of the Recovery Services vault.
    :type vault_name: str
    :param resource_group_name: The name of the resource group associated with the Recovery Services vault.
    :type resource_group_name: str
    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param filter: The following equation can be used to filter the list of backup policies. backupManagementType eq {AzureIaasVM, MAB, DPM, AzureBackupServer, AzureSql}.
    :type filter: str

    """
    return web.Response(status=200)
