from typing import List, Dict
from aiohttp import web

from openapi_server.models.admin_overview import AdminOverview
from openapi_server.models.locations_list import LocationsList
from openapi_server.models.operation_list import OperationList
from openapi_server.models.operation_result_list import OperationResultList
from openapi_server import util


async def locations_operation_results_list(request: web.Request, api_version, location) -> web.Response:
    """locations_operation_results_list

    Returns the list of operation results for a location

    :param api_version: Client API Version.
    :type api_version: str
    :param location: Location of the resource.
    :type location: str

    """
    return web.Response(status=200)


async def locations_operations_list(request: web.Request, api_version, location) -> web.Response:
    """locations_operations_list

    Returns the list of support REST operations.

    :param api_version: Client API Version.
    :type api_version: str
    :param location: Location of the resource.
    :type location: str

    """
    return web.Response(status=200)


async def on_prem_locations_list(request: web.Request, api_version) -> web.Response:
    """on_prem_locations_list

    Returns the list of supported locations

    :param api_version: Client API Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def operations_list(request: web.Request, api_version) -> web.Response:
    """operations_list

    Returns the list of support REST operations.

    :param api_version: Client API Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def resource_provider_state_get(request: web.Request, subscription_id, api_version) -> web.Response:
    """resource_provider_state_get

    Get an overview of the state of the network resource provider.

    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client API Version.
    :type api_version: str

    """
    return web.Response(status=200)
