from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_model import ErrorModel
from openapi_server.models.operation_list_result import OperationListResult
from openapi_server import util


async def operations_list(request: web.Request, api_version) -> web.Response:
    """Lists all of the available Service Fabric resource provider API operations.

    Get the list of available Service Fabric resource provider API operations.

    :param api_version: The version of the Service Fabric resource provider API
    :type api_version: str

    """
    return web.Response(status=200)
