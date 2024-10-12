from typing import List, Dict
from aiohttp import web

from openapi_server.models.resource_provider_operation_list import ResourceProviderOperationList
from openapi_server import util


async def operations_list(request: web.Request, api_version) -> web.Response:
    """Lists operations for the resource provider.

    Lists all the supported operations by the Microsoft.DevSpaces resource provider along with their description.

    :param api_version: Client API version.
    :type api_version: str

    """
    return web.Response(status=200)
