from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_error import ApiError
from openapi_server.models.operation_list_result import OperationListResult
from openapi_server import util


async def operations_list(request: web.Request, api_version) -> web.Response:
    """operations_list

    Lists available operations for the Microsoft.VirtualMachineImages provider

    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)
