from typing import List, Dict
from aiohttp import web

from openapi_server.models.operation_status import OperationStatus
from openapi_server import util


async def protection_policy_operation_statuses_get(request: web.Request, api_version, vault_name, resource_group_name, subscription_id, policy_name, operation_id) -> web.Response:
    """protection_policy_operation_statuses_get

    Provides the status of the asynchronous operations like backup or restore. The status can be: in progress, completed, or failed. You can refer to the Operation Status enumeration for the possible states of an operation. Some operations create jobs. This method returns the list of jobs associated with the operation.

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
    :param operation_id: The ID associated with this GET operation.
    :type operation_id: str

    """
    return web.Response(status=200)
