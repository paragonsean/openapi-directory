from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.operations_discovery_collection import OperationsDiscoveryCollection
from openapi_server import util


async def operations_list(request: web.Request, api_version) -> web.Response:
    """operations_list

    Operation to return the list of available operations.

    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)
