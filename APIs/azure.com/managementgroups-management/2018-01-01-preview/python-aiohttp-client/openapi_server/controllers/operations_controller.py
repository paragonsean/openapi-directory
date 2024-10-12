from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.operation_list_result import OperationListResult
from openapi_server import util


async def operations_list(request: web.Request, api_version) -> web.Response:
    """operations_list

    Lists all of the available Management REST API operations.

    :param api_version: Version of the API to be used with the client request. The current version is 2018-01-01-preview.
    :type api_version: str

    """
    return web.Response(status=200)
