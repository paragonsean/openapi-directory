from typing import List, Dict
from aiohttp import web

from openapi_server.models.resource_provider_operation_list import ResourceProviderOperationList
from openapi_server import util


async def operations_list(request: web.Request, api_version) -> web.Response:
    """operations_list

    List all of the available operations the Blueprint resource provider supports.

    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)
