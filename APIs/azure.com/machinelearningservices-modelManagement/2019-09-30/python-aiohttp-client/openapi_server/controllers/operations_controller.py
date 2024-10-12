from typing import List, Dict
from aiohttp import web

from openapi_server.models.async_operation_status import AsyncOperationStatus
from openapi_server.models.model_error_response import ModelErrorResponse
from openapi_server import util


async def operations_get(request: web.Request, subscription_id, resource_group, workspace, id) -> web.Response:
    """Get the status of an async operation.

    Get the status of an async operation by operation id.

    :param subscription_id: The Azure Subscription ID.
    :type subscription_id: str
    :type subscription_id: str
    :param resource_group: The Name of the resource group in which the workspace is located.
    :type resource_group: str
    :param workspace: The name of the workspace.
    :type workspace: str
    :param id: The operation id.
    :type id: str

    """
    return web.Response(status=200)
