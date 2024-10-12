from typing import List, Dict
from aiohttp import web

from openapi_server.models.operation_result_info_base_resource import OperationResultInfoBaseResource
from openapi_server import util


async def export_jobs_operation_results_get(request: web.Request, api_version, vault_name, resource_group_name, subscription_id, operation_id) -> web.Response:
    """export_jobs_operation_results_get

    Gets the operation result of operation triggered by Export Jobs API. If the operation is successful, then it also  contains URL of a Blob and a SAS key to access the same. The blob contains exported jobs in JSON serialized format.

    :param api_version: Client Api Version.
    :type api_version: str
    :param vault_name: The name of the recovery services vault.
    :type vault_name: str
    :param resource_group_name: The name of the resource group where the recovery services vault is present.
    :type resource_group_name: str
    :param subscription_id: The subscription Id.
    :type subscription_id: str
    :param operation_id: OperationID which represents the export job.
    :type operation_id: str

    """
    return web.Response(status=200)
