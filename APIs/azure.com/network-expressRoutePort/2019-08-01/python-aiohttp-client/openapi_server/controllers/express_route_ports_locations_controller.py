from typing import List, Dict
from aiohttp import web

from openapi_server.models.express_route_ports_location import ExpressRoutePortsLocation
from openapi_server.models.express_route_ports_location_list_result import ExpressRoutePortsLocationListResult
from openapi_server import util


async def express_route_ports_locations_get(request: web.Request, subscription_id, api_version, location_name) -> web.Response:
    """express_route_ports_locations_get

    Retrieves a single ExpressRoutePort peering location, including the list of available bandwidths available at said peering location.

    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client API version.
    :type api_version: str
    :param location_name: Name of the requested ExpressRoutePort peering location.
    :type location_name: str

    """
    return web.Response(status=200)


async def express_route_ports_locations_list(request: web.Request, subscription_id, api_version) -> web.Response:
    """express_route_ports_locations_list

    Retrieves all ExpressRoutePort peering locations. Does not return available bandwidths for each location. Available bandwidths can only be obtained when retrieving a specific peering location.

    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client API version.
    :type api_version: str

    """
    return web.Response(status=200)
