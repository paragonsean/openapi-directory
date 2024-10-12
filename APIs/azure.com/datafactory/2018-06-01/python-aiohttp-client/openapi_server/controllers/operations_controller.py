from typing import List, Dict
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.operation_list_response import OperationListResponse
from openapi_server import util


async def operations_list(request: web.Request, api_version) -> web.Response:
    """operations_list

    Lists the available Azure Data Factory API operations.

    :param api_version: The API version.
    :type api_version: str

    """
    return web.Response(status=200)
