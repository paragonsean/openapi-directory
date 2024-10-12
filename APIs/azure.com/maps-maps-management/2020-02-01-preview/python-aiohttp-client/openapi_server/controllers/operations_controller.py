from typing import List, Dict
from aiohttp import web

from openapi_server.models.maps_list_operations_default_response import MapsListOperationsDefaultResponse
from openapi_server.models.maps_operations import MapsOperations
from openapi_server import util


async def maps_list_operations(request: web.Request, api_version) -> web.Response:
    """maps_list_operations

    List operations available for the Maps Resource Provider

    :param api_version: The API version to use for this operation.
    :type api_version: str

    """
    return web.Response(status=200)
