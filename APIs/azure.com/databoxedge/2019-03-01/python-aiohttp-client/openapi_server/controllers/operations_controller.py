from typing import List, Dict
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.operations_list import OperationsList
from openapi_server import util


async def operations_list(request: web.Request, api_version) -> web.Response:
    """List all the supported operations.

    

    :param api_version: The API version.
    :type api_version: str

    """
    return web.Response(status=200)
