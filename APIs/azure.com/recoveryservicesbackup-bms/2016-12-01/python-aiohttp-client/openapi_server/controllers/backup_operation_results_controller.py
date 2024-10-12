from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def backup_operation_results_get(request: web.Request, api_version, vault_name, resource_group_name, subscription_id, operation_id) -> web.Response:
    """backup_operation_results_get

    Provides the status of the delete operations such as deleting backed up item. Once the operation has started, the  status code in the response would be Accepted. It will continue to be in this state till it reaches completion. On  successful completion, the status code will be OK. This method expects OperationID as an argument. OperationID is  part of the Location header of the operation response.

    :param api_version: Client Api Version.
    :type api_version: str
    :param vault_name: The name of the recovery services vault.
    :type vault_name: str
    :param resource_group_name: The name of the resource group where the recovery services vault is present.
    :type resource_group_name: str
    :param subscription_id: The subscription Id.
    :type subscription_id: str
    :param operation_id: OperationID which represents the operation.
    :type operation_id: str

    """
    return web.Response(status=200)
