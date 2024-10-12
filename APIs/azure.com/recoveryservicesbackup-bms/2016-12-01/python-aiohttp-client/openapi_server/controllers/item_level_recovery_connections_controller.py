from typing import List, Dict
from aiohttp import web

from openapi_server.models.ilr_request_resource import ILRRequestResource
from openapi_server import util


async def item_level_recovery_connections_provision(request: web.Request, api_version, vault_name, resource_group_name, subscription_id, fabric_name, container_name, protected_item_name, recovery_point_id, parameters) -> web.Response:
    """item_level_recovery_connections_provision

    Provisions a script which invokes an iSCSI connection to the backup data. Executing this script opens a file  explorer displaying all the recoverable files and folders. This is an asynchronous operation. To know the status of  provisioning, call GetProtectedItemOperationResult API.

    :param api_version: Client Api Version.
    :type api_version: str
    :param vault_name: The name of the recovery services vault.
    :type vault_name: str
    :param resource_group_name: The name of the resource group where the recovery services vault is present.
    :type resource_group_name: str
    :param subscription_id: The subscription Id.
    :type subscription_id: str
    :param fabric_name: Fabric name associated with the backed up items.
    :type fabric_name: str
    :param container_name: Container name associated with the backed up items.
    :type container_name: str
    :param protected_item_name: Backed up item name whose files/folders are to be restored.
    :type protected_item_name: str
    :param recovery_point_id: Recovery point ID which represents backed up data. iSCSI connection will be provisioned  for this backed up data.
    :type recovery_point_id: str
    :param parameters: resource ILR request
    :type parameters: dict | bytes

    """
    parameters = ILRRequestResource.from_dict(parameters)
    return web.Response(status=200)


async def item_level_recovery_connections_revoke(request: web.Request, api_version, vault_name, resource_group_name, subscription_id, fabric_name, container_name, protected_item_name, recovery_point_id) -> web.Response:
    """item_level_recovery_connections_revoke

    Revokes an iSCSI connection which can be used to download a script. Executing this script opens a file explorer  displaying all recoverable files and folders. This is an asynchronous operation.

    :param api_version: Client Api Version.
    :type api_version: str
    :param vault_name: The name of the recovery services vault.
    :type vault_name: str
    :param resource_group_name: The name of the resource group where the recovery services vault is present.
    :type resource_group_name: str
    :param subscription_id: The subscription Id.
    :type subscription_id: str
    :param fabric_name: Fabric name associated with the backed up items.
    :type fabric_name: str
    :param container_name: Container name associated with the backed up items.
    :type container_name: str
    :param protected_item_name: Backed up item name whose files/folders are to be restored.
    :type protected_item_name: str
    :param recovery_point_id: Recovery point ID which represents backed up data. iSCSI connection will be revoked for  this backed up data.
    :type recovery_point_id: str

    """
    return web.Response(status=200)
