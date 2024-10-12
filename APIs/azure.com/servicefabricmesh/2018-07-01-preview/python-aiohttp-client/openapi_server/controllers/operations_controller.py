from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_model import ErrorModel
from openapi_server.models.operation_list_result import OperationListResult
from openapi_server import util


async def operations_list(request: web.Request, api_version) -> web.Response:
    """Lists all of the available operations.

    Lists all the available operations provided by Service Fabric SeaBreeze resource provider.

    :param api_version: The version of the API. This parameter is required and its value must be &#x60;2018-07-01-preview&#x60;.
    :type api_version: str

    """
    return web.Response(status=200)
