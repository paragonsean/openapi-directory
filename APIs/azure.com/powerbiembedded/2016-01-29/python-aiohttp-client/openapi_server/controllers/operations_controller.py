from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.operation_list import OperationList
from openapi_server import util


async def get_available_operations(request: web.Request, api_version) -> web.Response:
    """get_available_operations

    Indicates which operations can be performed by the Power BI Resource Provider.

    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)
