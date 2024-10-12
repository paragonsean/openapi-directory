from typing import List, Dict
from aiohttp import web

from openapi_server.models.operation_list_result import OperationListResult
from openapi_server import util


async def api_management_operations_list(request: web.Request, api_version) -> web.Response:
    """api_management_operations_list

    Lists all of the available REST API operations of the Microsoft.ApiManagement provider.

    :param api_version: Version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)
