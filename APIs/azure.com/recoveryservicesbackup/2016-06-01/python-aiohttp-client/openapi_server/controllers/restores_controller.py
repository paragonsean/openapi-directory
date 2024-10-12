from typing import List, Dict
from aiohttp import web

from openapi_server.models.restore_request_resource import RestoreRequestResource
from openapi_server import util


async def restores_trigger(request: web.Request, api_version, vault_name, resource_group_name, subscription_id, fabric_name, container_name, protected_item_name, recovery_point_id, resource_restore_request) -> web.Response:
    """restores_trigger

    Restores the specified backup data. This is an asynchronous operation. To know the status of this API call, use GetProtectedItemOperationResult API.

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
    :param protected_item_name: The backup item to be restored.
    :type protected_item_name: str
    :param recovery_point_id: The recovery point ID for the backup data to be restored.
    :type recovery_point_id: str
    :param resource_restore_request: The resource restore request.
    :type resource_restore_request: dict | bytes

    """
    resource_restore_request = RestoreRequestResource.from_dict(resource_restore_request)
    return web.Response(status=200)
