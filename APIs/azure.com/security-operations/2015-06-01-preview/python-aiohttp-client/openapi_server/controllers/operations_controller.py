from typing import List, Dict
from aiohttp import web

from openapi_server.models.operation_list import OperationList
from openapi_server.models.operations_list_default_response import OperationsListDefaultResponse
from openapi_server import util


async def operations_list(request: web.Request, api_version) -> web.Response:
    """operations_list

    Exposes all available operations for discovery purposes.

    :param api_version: API version for the operation
    :type api_version: str

    """
    return web.Response(status=200)
