from typing import List, Dict
from aiohttp import web

from openapi_server.models.validate_operation_request import ValidateOperationRequest
from openapi_server.models.validate_operations_response import ValidateOperationsResponse
from openapi_server import util


async def operation_validate(request: web.Request, api_version, vault_name, resource_group_name, subscription_id, parameters) -> web.Response:
    """operation_validate

    Validate operation for specified backed up item. This is a synchronous operation.

    :param api_version: Client Api Version.
    :type api_version: str
    :param vault_name: The name of the recovery services vault.
    :type vault_name: str
    :param resource_group_name: The name of the resource group where the recovery services vault is present.
    :type resource_group_name: str
    :param subscription_id: The subscription Id.
    :type subscription_id: str
    :param parameters: resource validate operation request
    :type parameters: dict | bytes

    """
    parameters = ValidateOperationRequest.from_dict(parameters)
    return web.Response(status=200)
