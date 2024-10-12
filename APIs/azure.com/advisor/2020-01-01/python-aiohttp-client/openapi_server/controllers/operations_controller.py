from typing import List, Dict
from aiohttp import web

from openapi_server.models.operation_entity_list_result import OperationEntityListResult
from openapi_server import util


async def operations_list(request: web.Request, api_version) -> web.Response:
    """operations_list

    Lists all the available Advisor REST API operations.

    :param api_version: The version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)
