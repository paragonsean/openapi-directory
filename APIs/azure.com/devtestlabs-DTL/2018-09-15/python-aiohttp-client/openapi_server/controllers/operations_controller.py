from typing import List, Dict
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.operation_result import OperationResult
from openapi_server import util


async def operations_get(request: web.Request, subscription_id, location_name, name, api_version) -> web.Response:
    """operations_get

    Get operation.

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param location_name: The name of the location.
    :type location_name: str
    :param name: The name of the operation.
    :type name: str
    :param api_version: Client API version.
    :type api_version: str

    """
    return web.Response(status=200)
