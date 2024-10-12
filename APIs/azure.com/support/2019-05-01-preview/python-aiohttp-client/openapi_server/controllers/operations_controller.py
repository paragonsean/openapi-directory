from typing import List, Dict
from aiohttp import web

from openapi_server.models.exception_response import ExceptionResponse
from openapi_server.models.operations_list_result import OperationsListResult
from openapi_server import util


async def operations_list(request: web.Request, api_version) -> web.Response:
    """operations_list

    This lists all the available Microsoft Support REST API operations.

    :param api_version: Api version
    :type api_version: str

    """
    return web.Response(status=200)
