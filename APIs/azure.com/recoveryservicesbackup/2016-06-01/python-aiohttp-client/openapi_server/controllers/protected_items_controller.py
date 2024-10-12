from typing import List, Dict
from aiohttp import web

from openapi_server.models.protected_item_resource import ProtectedItemResource
from openapi_server.models.protected_item_resource_list import ProtectedItemResourceList
from openapi_server import util


async def protected_items_create_or_update(request: web.Request, api_version, vault_name, resource_group_name, subscription_id, fabric_name, container_name, protected_item_name, resource_protected_item) -> web.Response:
    """protected_items_create_or_update

    This operation enables an item to be backed up, or modifies the existing backup policy information for an item that has been backed up. This is an asynchronous operation. To learn the status of the operation, call the GetItemOperationResult API.

    :param api_version: Client API version.
    :type api_version: str
    :param vault_name: The name of the Recovery Services vault.
    :type vault_name: str
    :param resource_group_name: The name of the resource group associated with the Recovery Services vault.
    :type resource_group_name: str
    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param fabric_name: The fabric name associated with the backup item.
    :type fabric_name: str
    :param container_name: The container name associated with the backup item.
    :type container_name: str
    :param protected_item_name: The name of the backup item.
    :type protected_item_name: str
    :param resource_protected_item: The resource backup item.
    :type resource_protected_item: dict | bytes

    """
    resource_protected_item = ProtectedItemResource.from_dict(resource_protected_item)
    return web.Response(status=200)


async def protected_items_delete(request: web.Request, api_version, vault_name, resource_group_name, subscription_id, fabric_name, container_name, protected_item_name) -> web.Response:
    """protected_items_delete

    Used to disable the backup job for an item within a container. This is an asynchronous operation. To learn the status of the request, call the GetItemOperationResult API.

    :param api_version: Client API version.
    :type api_version: str
    :param vault_name: The name of the Recovery Services vault.
    :type vault_name: str
    :param resource_group_name: The name of the resource group associated with the Recovery Services vault.
    :type resource_group_name: str
    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param fabric_name:  The fabric name associated with the backup item.
    :type fabric_name: str
    :param container_name: The container name associated with the backup item.
    :type container_name: str
    :param protected_item_name: The backup item to be deleted.
    :type protected_item_name: str

    """
    return web.Response(status=200)


async def protected_items_get(request: web.Request, api_version, vault_name, resource_group_name, subscription_id, fabric_name, container_name, protected_item_name, filter=None) -> web.Response:
    """protected_items_get

    Provides the details of the backup item. This is an asynchronous operation. To know the status of the operation, call the GetItemOperationResult API.

    :param api_version: Client API version.
    :type api_version: str
    :param vault_name: The name of the Recovery Services vault.
    :type vault_name: str
    :param resource_group_name: The name of the resource group associated with the Recovery Services vault.
    :type resource_group_name: str
    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param fabric_name: The fabric name associated with the backup item.
    :type fabric_name: str
    :param container_name: The container name associated with the backup item.
    :type container_name: str
    :param protected_item_name: The backup item name used in this GET operation.
    :type protected_item_name: str
    :param filter: expand eq {extendedInfo}. This filter enables you to choose (or filter) specific items in the list of backup items.
    :type filter: str

    """
    return web.Response(status=200)


async def protected_items_list(request: web.Request, api_version, vault_name, resource_group_name, subscription_id, filter=None, skip_token=None) -> web.Response:
    """protected_items_list

    Provides a pageable list of all items in a subscription, that can be protected.

    :param api_version: Client API version.
    :type api_version: str
    :param vault_name: The name of the Recovery Services vault.
    :type vault_name: str
    :param resource_group_name: The name of the resource group associated with the Recovery Services vault.
    :type resource_group_name: str
    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param filter:  itemType eq { VM , FileFolder , AzureSqlDb , SQLDB , Exchange , Sharepoint , DPMUnknown } and providerType eq { AzureIaasVM, MAB, DPM, AzureBackupServer, AzureSql } and policyName eq {policyName} and containerName eq {containername} and backupManagementType eq { AzureIaasVM, MAB, DPM, AzureBackupServer, AzureSql }.
    :type filter: str
    :param skip_token:  The Skip Token filter.
    :type skip_token: str

    """
    return web.Response(status=200)
