from typing import List, Dict
from aiohttp import web

from openapi_server.models.operation_status import OperationStatus
from openapi_server import util


async def compute_fabric_operations_get(request: web.Request, subscription_id, location, provider, compute_operation_result, api_version) -> web.Response:
    """compute_fabric_operations_get

    Get the status of a compute fabric operation.

    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param location: Location of the resource.
    :type location: str
    :param provider: Name of the provider.
    :type provider: str
    :param compute_operation_result: Id of a compute fabric operation.
    :type compute_operation_result: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)
