from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def job_operation_results_get(request: web.Request, api_version, vault_name, resource_group_name, subscription_id, job_name, operation_id) -> web.Response:
    """job_operation_results_get

    Gets the result of the operation.

    :param api_version: Client API version.
    :type api_version: str
    :param vault_name: The name of the Recovery Services vault.
    :type vault_name: str
    :param resource_group_name: The name of the resource group associated with the Recovery Services vault.
    :type resource_group_name: str
    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param job_name: Job name associated with this GET operation.
    :type job_name: str
    :param operation_id: OperationID associated with this GET operation.
    :type operation_id: str

    """
    return web.Response(status=200)
