from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def job_operation_results_get(request: web.Request, api_version, vault_name, resource_group_name, subscription_id, job_name, operation_id) -> web.Response:
    """job_operation_results_get

    Fetches the result of any operation.

    :param api_version: Client Api Version.
    :type api_version: str
    :param vault_name: The name of the recovery services vault.
    :type vault_name: str
    :param resource_group_name: The name of the resource group where the recovery services vault is present.
    :type resource_group_name: str
    :param subscription_id: The subscription Id.
    :type subscription_id: str
    :param job_name: Job name whose operation result has to be fetched.
    :type job_name: str
    :param operation_id: OperationID which represents the operation whose result has to be fetched.
    :type operation_id: str

    """
    return web.Response(status=200)
