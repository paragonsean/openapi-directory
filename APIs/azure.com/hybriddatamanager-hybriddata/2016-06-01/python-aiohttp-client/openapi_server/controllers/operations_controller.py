from typing import List, Dict
from aiohttp import web

from openapi_server.models.available_provider_operations import AvailableProviderOperations
from openapi_server import util


async def operations_list(request: web.Request, api_version) -> web.Response:
    """This method gets all the operations.

    

    :param api_version: The API Version
    :type api_version: str

    """
    return web.Response(status=200)
