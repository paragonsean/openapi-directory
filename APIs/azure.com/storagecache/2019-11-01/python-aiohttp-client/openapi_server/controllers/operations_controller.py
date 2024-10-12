from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_operation_list_result import ApiOperationListResult
from openapi_server.models.cloud_error import CloudError
from openapi_server import util


async def operations_list(request: web.Request, api_version) -> web.Response:
    """operations_list

    Lists all of the available Resource Provider operations.

    :param api_version: Client API version.
    :type api_version: str

    """
    return web.Response(status=200)
