from typing import List, Dict
from aiohttp import web

from openapi_server.models.network_operation_result import NetworkOperationResult
from openapi_server.models.network_operation_result_list import NetworkOperationResultList
from openapi_server import util


async def network_operation_results_get(request: web.Request, subscription_id, resource_group_name, location, operation, api_version) -> web.Response:
    """network_operation_results_get

    Returns the status of a network operation.

    :param subscription_id: Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: Name of the resource group.
    :type resource_group_name: str
    :param location: Location of the resource.
    :type location: str
    :param operation: Operation identifier.
    :type operation: str
    :param api_version: Client API Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def network_operation_results_list(request: web.Request, subscription_id, resource_group_name, location, api_version, filter=None) -> web.Response:
    """network_operation_results_list

    Returns a list of all network operation results at a location.

    :param subscription_id: Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: Name of the resource group.
    :type resource_group_name: str
    :param location: Location of the resource.
    :type location: str
    :param api_version: Client API Version.
    :type api_version: str
    :param filter: OData filter parameter.
    :type filter: str

    """
    return web.Response(status=200)
