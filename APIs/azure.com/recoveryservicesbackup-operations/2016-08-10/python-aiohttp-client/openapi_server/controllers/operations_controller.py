from typing import List, Dict
from aiohttp import web

from openapi_server.models.client_discovery_response import ClientDiscoveryResponse
from openapi_server import util


async def operations_list(request: web.Request, api_version) -> web.Response:
    """operations_list

    Returns the list of available operations.

    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)
