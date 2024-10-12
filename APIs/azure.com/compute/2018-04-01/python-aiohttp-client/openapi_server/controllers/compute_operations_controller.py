from typing import List, Dict
from aiohttp import web

from openapi_server.models.compute_operation_list_result import ComputeOperationListResult
from openapi_server import util


async def operations_list(request: web.Request, api_version) -> web.Response:
    """operations_list

    Gets a list of compute operations.

    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)
