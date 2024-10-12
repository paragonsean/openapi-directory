from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.operation_list import OperationList
from openapi_server import util


async def operation_list(request: web.Request, api_version) -> web.Response:
    """Get operations.

    List all the operations.

    :param api_version: Supported version for this document is 2019-04-01
    :type api_version: str

    """
    return web.Response(status=200)
