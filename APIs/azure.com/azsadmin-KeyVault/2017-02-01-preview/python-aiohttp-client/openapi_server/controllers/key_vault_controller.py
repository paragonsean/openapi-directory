from typing import List, Dict
from aiohttp import web

from openapi_server.models.operation_list import OperationList
from openapi_server import util


async def operations_list(request: web.Request, api_version) -> web.Response:
    """operations_list

    Get the list of support rest operations.

    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)
