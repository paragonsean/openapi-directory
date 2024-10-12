from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.operation_list_result import OperationListResult
from openapi_server import util


async def operations_list(request: web.Request, api_version) -> web.Response:
    """operations_list

    Lists all the available REST API operations.

    :param api_version: The API version to be used with the HTTP request.
    :type api_version: str

    """
    return web.Response(status=200)
