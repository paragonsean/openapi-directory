from typing import List, Dict
from aiohttp import web

from openapi_server.models.operation_status import OperationStatus
from openapi_server import util


async def backup_operation_statuses_get(request: web.Request, api_version, vault_name, resource_group_name, subscription_id, operation_id) -> web.Response:
    """backup_operation_statuses_get

    Gets the status of an operation such as triggering a backup or restore. The status can be In progress, Completed or Failed. You can refer to the OperationStatus enum for all the possible states of an operation. Some operations create jobs. This method returns the list of jobs when the operation is complete.

    :param api_version: Client API version.
    :type api_version: str
    :param vault_name: The name of the Recovery Services vault.
    :type vault_name: str
    :param resource_group_name: The name of the resource group associated with the Recovery Services vault.
    :type resource_group_name: str
    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param operation_id: The ID of the operation.
    :type operation_id: str

    """
    return web.Response(status=200)
