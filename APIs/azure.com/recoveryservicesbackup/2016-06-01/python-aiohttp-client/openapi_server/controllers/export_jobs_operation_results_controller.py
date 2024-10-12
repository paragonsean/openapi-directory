from typing import List, Dict
from aiohttp import web

from openapi_server.models.operation_result_info_base_resource import OperationResultInfoBaseResource
from openapi_server import util


async def export_jobs_operation_results_get(request: web.Request, api_version, vault_name, resource_group_name, subscription_id, operation_id) -> web.Response:
    """export_jobs_operation_results_get

    Gets the result of the operation triggered by the ExportJob API.

    :param api_version: Client API version.
    :type api_version: str
    :param vault_name: The name of the Recovery Services vault.
    :type vault_name: str
    :param resource_group_name: The name of the resource group associated with the Recovery Services vault.
    :type resource_group_name: str
    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param operation_id: The ID associated with the export job.
    :type operation_id: str

    """
    return web.Response(status=200)
