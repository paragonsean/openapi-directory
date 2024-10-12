from typing import List, Dict
from aiohttp import web

from openapi_server.models.ilr_request_resource import ILRRequestResource
from openapi_server import util


async def item_level_recovery_connections_provision(request: web.Request, api_version, vault_name, resource_group_name, subscription_id, fabric_name, container_name, protected_item_name, recovery_point_id, resource_ilr_request) -> web.Response:
    """item_level_recovery_connections_provision

    Provisions a script which invokes an iSCSI connection to the backup data. Executing this script opens File Explorer which displays the recoverable files and folders. This is an asynchronous operation. To get the provisioning status, call GetProtectedItemOperationResult API.

    :param api_version: Client API version.
    :type api_version: str
    :param vault_name: The name of the Recovery Services vault.
    :type vault_name: str
    :param resource_group_name: The name of the resource group associated with the Recovery Services vault.
    :type resource_group_name: str
    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param fabric_name: The fabric name associated with the backup items.
    :type fabric_name: str
    :param container_name: The container name associated with the backup items.
    :type container_name: str
    :param protected_item_name: The name of the backup item whose files or folders are to be restored.
    :type protected_item_name: str
    :param recovery_point_id: The recovery point ID for backup data. The iSCSI connection will be provisioned for this backup data.
    :type recovery_point_id: str
    :param resource_ilr_request: The resource Item Level Recovery (ILR) request.
    :type resource_ilr_request: dict | bytes

    """
    resource_ilr_request = ILRRequestResource.from_dict(resource_ilr_request)
    return web.Response(status=200)


async def item_level_recovery_connections_revoke(request: web.Request, api_version, vault_name, resource_group_name, subscription_id, fabric_name, container_name, protected_item_name, recovery_point_id) -> web.Response:
    """item_level_recovery_connections_revoke

    Revokes an iSCSI connection which can be used to download a script. Executing this script opens a file explorer displaying all recoverable files and folders. This is an asynchronous operation.

    :param api_version: Client API version.
    :type api_version: str
    :param vault_name: The name of the Recovery Services vault.
    :type vault_name: str
    :param resource_group_name: The name of the resource group associated with the Recovery Services vault.
    :type resource_group_name: str
    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param fabric_name: The fabric name associated with the backup items. The value allowed is Azure.
    :type fabric_name: str
    :param container_name: The container name associated with the backup items.
    :type container_name: str
    :param protected_item_name: The name of the backup items whose files or folders will be restored.
    :type protected_item_name: str
    :param recovery_point_id: The string that identifies the recovery point. The iSCSI connection will be revoked for this protected data.
    :type recovery_point_id: str

    """
    return web.Response(status=200)
