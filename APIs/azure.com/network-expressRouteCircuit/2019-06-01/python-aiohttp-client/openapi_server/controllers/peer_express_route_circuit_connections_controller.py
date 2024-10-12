from typing import List, Dict
from aiohttp import web

from openapi_server.models.peer_express_route_circuit_connection import PeerExpressRouteCircuitConnection
from openapi_server.models.peer_express_route_circuit_connection_list_result import PeerExpressRouteCircuitConnectionListResult
from openapi_server import util


async def peer_express_route_circuit_connections_get(request: web.Request, resource_group_name, circuit_name, peering_name, connection_name, api_version, subscription_id) -> web.Response:
    """peer_express_route_circuit_connections_get

    Gets the specified Peer Express Route Circuit Connection from the specified express route circuit.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param circuit_name: The name of the express route circuit.
    :type circuit_name: str
    :param peering_name: The name of the peering.
    :type peering_name: str
    :param connection_name: The name of the peer express route circuit connection.
    :type connection_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def peer_express_route_circuit_connections_list(request: web.Request, resource_group_name, circuit_name, peering_name, api_version, subscription_id) -> web.Response:
    """peer_express_route_circuit_connections_list

    Gets all global reach peer connections associated with a private peering in an express route circuit.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param circuit_name: The name of the circuit.
    :type circuit_name: str
    :param peering_name: The name of the peering.
    :type peering_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)
