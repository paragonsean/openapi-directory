from typing import List, Dict
from aiohttp import web

from openapi_server.models.protected_item_resource import ProtectedItemResource
from openapi_server import util


async def protected_item_operation_results_get(request: web.Request, api_version, vault_name, resource_group_name, subscription_id, fabric_name, container_name, protected_item_name, operation_id) -> web.Response:
    """protected_item_operation_results_get

    Gets the result of any operation on the backup item.

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
    :param protected_item_name: The name of backup item used in this GET operation.
    :type protected_item_name: str
    :param operation_id: The OperationID used in this GET operation.
    :type operation_id: str

    """
    return web.Response(status=200)
