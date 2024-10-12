from typing import List, Dict
from aiohttp import web

from openapi_server.models.operation_list_result import OperationListResult
from openapi_server import util


async def authorization_operations_list(request: web.Request, api_version) -> web.Response:
    """authorization_operations_list

    Lists all of the available Microsoft.Authorization REST API operations.

    :param api_version: The API version to use for the operation.
    :type api_version: str

    """
    return web.Response(status=200)
