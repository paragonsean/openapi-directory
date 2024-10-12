from typing import List, Dict
from aiohttp import web

from openapi_server.models.backup_request_resource import BackupRequestResource
from openapi_server import util


async def backups_trigger(request: web.Request, api_version, vault_name, resource_group_name, subscription_id, fabric_name, container_name, protected_item_name, resource_backup_request) -> web.Response:
    """backups_trigger

    Triggers the backup job for the specified backup item. This is an asynchronous operation. To know the status of the operation, call GetProtectedItemOperationResult API.

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
    :param protected_item_name: The name of backup item used in this POST operation.
    :type protected_item_name: str
    :param resource_backup_request: The resource backup request.
    :type resource_backup_request: dict | bytes

    """
    resource_backup_request = BackupRequestResource.from_dict(resource_backup_request)
    return web.Response(status=200)
