from typing import List, Dict
from aiohttp import web

from openapi_server.models.express_route_circuits_stats_list_result import ExpressRouteCircuitsStatsListResult
from openapi_server import util


async def express_route_circuits_list_stats(request: web.Request, resource_group_name, circuit_name, api_version, subscription_id) -> web.Response:
    """express_route_circuits_list_stats

    The ListStats ExpressRouteCircuit operation retrieves all the stats from a ExpressRouteCircuits in a resource group.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param circuit_name: The name of the loadBalancer.
    :type circuit_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)
