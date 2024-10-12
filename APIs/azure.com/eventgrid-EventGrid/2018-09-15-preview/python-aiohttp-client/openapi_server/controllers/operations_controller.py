from typing import List, Dict
from aiohttp import web

from openapi_server.models.operations_list_result import OperationsListResult
from openapi_server import util


async def operations_list(request: web.Request, api_version) -> web.Response:
    """List available operations

    List the available operations supported by the Microsoft.EventGrid resource provider

    :param api_version: Version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)
