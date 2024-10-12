from typing import List, Dict
from aiohttp import web

from openapi_server.models.resource_provider_operation_collection import ResourceProviderOperationCollection
from openapi_server import util


async def operations_list(request: web.Request, api_version) -> web.Response:
    """operations_list

    Lists the available operations of Microsoft.Blockchain resource provider.

    :param api_version: Client API Version.
    :type api_version: str

    """
    return web.Response(status=200)
