from typing import List, Dict
from aiohttp import web

from openapi_server.models.provider_operation_result import ProviderOperationResult
from openapi_server import util


async def provider_operations_list(request: web.Request, api_version) -> web.Response:
    """provider_operations_list

    Result of the request to list REST API operations

    :param api_version: Client API version.
    :type api_version: str

    """
    return web.Response(status=200)
