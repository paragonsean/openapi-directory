from typing import List, Dict
from aiohttp import web

from openapi_server.models.available_provider_operations import AvailableProviderOperations
from openapi_server.models.error import Error
from openapi_server import util


async def available_provider_operations_list(request: web.Request, api_version) -> web.Response:
    """available_provider_operations_list

    List of AvailableProviderOperations

    :param api_version: The api version
    :type api_version: str

    """
    return web.Response(status=200)
