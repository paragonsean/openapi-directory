from typing import List, Dict
from aiohttp import web

from openapi_server.models.operation_status import OperationStatus
from openapi_server import util


async def protected_item_operation_statuses_get(request: web.Request, api_version, vault_name, resource_group_name, subscription_id, fabric_name, container_name, protected_item_name, operation_id) -> web.Response:
    """protected_item_operation_statuses_get

    Gets the status of an operation such as triggering a backup or restore. The status can be: In progress, Completed, or Failed. You can refer to the OperationStatus enum for all the possible states of the operation. Some operations create jobs. This method returns the list of jobs associated with the operation.

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
