from typing import List, Dict
from aiohttp import web

from openapi_server.models.available_provider_operation_list import AvailableProviderOperationList
from openapi_server import util


async def operations_list(request: web.Request, api_version) -> web.Response:
    """operations_list

    Lists all of the available REST API operations of the Microsoft.StorSimple provider

    :param api_version: The api version
    :type api_version: str

    """
    return web.Response(status=200)
