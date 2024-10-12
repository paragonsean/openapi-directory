from typing import List, Dict
from aiohttp import web

from openapi_server.models.data_share_error import DataShareError
from openapi_server.models.operation_list import OperationList
from openapi_server import util


async def operations_list(request: web.Request, api_version) -> web.Response:
    """Lists the available operations

    List of available operations

    :param api_version: The api version to use.
    :type api_version: str

    """
    return web.Response(status=200)
