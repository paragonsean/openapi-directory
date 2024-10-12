from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def backup_operation_results_get(request: web.Request, api_version, vault_name, resource_group_name, subscription_id, operation_id) -> web.Response:
    """backup_operation_results_get

    Provides the status of the delete operations, for example, deleting a backup item. Once the operation starts, the response status code is Accepted. The response status code remains in this state until the operation reaches completion. On successful completion, the status code changes to OK. This method expects OperationID as an argument. OperationID is part of the Location header of the operation response.

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
