from typing import List, Dict
from aiohttp import web

from openapi_server.models.express_route_circuit_stats import ExpressRouteCircuitStats
from openapi_server import util


async def express_route_circuits_get_peering_stats(request: web.Request, resource_group_name, circuit_name, peering_name, api_version, subscription_id) -> web.Response:
    """express_route_circuits_get_peering_stats

    The List stats ExpressRouteCircuit operation retrieves all the stats from a ExpressRouteCircuits in a resource group.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param circuit_name: The name of the circuit.
    :type circuit_name: str
    :param peering_name: The name of the peering.
    :type peering_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def express_route_circuits_get_stats(request: web.Request, resource_group_name, circuit_name, api_version, subscription_id) -> web.Response:
    """express_route_circuits_get_stats

    The List stats ExpressRouteCircuit operation retrieves all the stats from a ExpressRouteCircuits in a resource group.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param circuit_name: The name of the circuit.
    :type circuit_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)
