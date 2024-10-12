from typing import List, Dict
from aiohttp import web

from openapi_server.models.operation_result import OperationResult
from openapi_server import util


async def blockchain_member_operation_results_get(request: web.Request, location_name, operation_id, api_version, subscription_id) -> web.Response:
    """blockchain_member_operation_results_get

    Get Async operation result.

    :param location_name: Location name.
    :type location_name: str
    :param operation_id: Operation Id.
    :type operation_id: str
    :param api_version: Client API Version.
    :type api_version: str
    :param subscription_id: Gets the subscription Id which uniquely identifies the Microsoft Azure subscription. The subscription ID is part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)
