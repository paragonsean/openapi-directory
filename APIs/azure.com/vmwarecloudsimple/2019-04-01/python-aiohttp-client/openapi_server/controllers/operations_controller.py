from typing import List, Dict
from aiohttp import web

from openapi_server.models.available_operations_list_response import AvailableOperationsListResponse
from openapi_server.models.csrp_error import CSRPError
from openapi_server.models.operation_resource import OperationResource
from openapi_server import util


async def operations_get(request: web.Request, subscription_id, api_version, region_id, referer, operation_id) -> web.Response:
    """Implements get of async operation

    Return an async operation

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param api_version: Client API version.
    :type api_version: str
    :param region_id: The region Id (westus, eastus)
    :type region_id: str
    :param referer: referer url
    :type referer: str
    :param operation_id: operation id
    :type operation_id: str

    """
    return web.Response(status=200)


async def operations_list(request: web.Request, api_version) -> web.Response:
    """Implements list of available operations

    Return list of operations

    :param api_version: Client API version.
    :type api_version: str

    """
    return web.Response(status=200)
