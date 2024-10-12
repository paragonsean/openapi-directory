from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.operation_list_result import OperationListResult
from openapi_server import util


async def operations_list(request: web.Request, api_version) -> web.Response:
    """operations_list

    Lists all of the available HDInsight REST API operations.

    :param api_version: The HDInsight client API Version.
    :type api_version: str

    """
    return web.Response(status=200)
