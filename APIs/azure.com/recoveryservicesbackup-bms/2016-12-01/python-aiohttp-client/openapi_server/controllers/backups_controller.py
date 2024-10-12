from typing import List, Dict
from aiohttp import web

from openapi_server.models.backup_request_resource import BackupRequestResource
from openapi_server import util


async def backups_trigger(request: web.Request, api_version, vault_name, resource_group_name, subscription_id, fabric_name, container_name, protected_item_name, parameters) -> web.Response:
    """backups_trigger

    Triggers backup for specified backed up item. This is an asynchronous operation. To know the status of the  operation, call GetProtectedItemOperationResult API.

    :param api_version: Client Api Version.
    :type api_version: str
    :param vault_name: The name of the recovery services vault.
    :type vault_name: str
    :param resource_group_name: The name of the resource group where the recovery services vault is present.
    :type resource_group_name: str
    :param subscription_id: The subscription Id.
    :type subscription_id: str
    :param fabric_name: Fabric name associated with the backup item.
    :type fabric_name: str
    :param container_name: Container name associated with the backup item.
    :type container_name: str
    :param protected_item_name: Backup item for which backup needs to be triggered.
    :type protected_item_name: str
    :param parameters: resource backup request
    :type parameters: dict | bytes

    """
    parameters = BackupRequestResource.from_dict(parameters)
    return web.Response(status=200)
