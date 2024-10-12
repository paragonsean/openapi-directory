from typing import List, Dict
from aiohttp import web

from openapi_server.models.operation_list import OperationList
from openapi_server import util


async def fabric_list_operations(request: web.Request, api_version) -> web.Response:
    """fabric_list_operations

    Returns the list of support REST operations.

    :param api_version: Client API Version.
    :type api_version: str

    """
    return web.Response(status=200)
