from typing import List, Dict
from aiohttp import web

from openapi_server.models.express_route_circuit_connection import ExpressRouteCircuitConnection
from openapi_server.models.express_route_circuit_connection_list_result import ExpressRouteCircuitConnectionListResult
from openapi_server import util


async def express_route_circuit_connections_create_or_update(request: web.Request, resource_group_name, circuit_name, peering_name, connection_name, api_version, subscription_id, express_route_circuit_connection_parameters) -> web.Response:
    """express_route_circuit_connections_create_or_update

    Creates or updates a Express Route Circuit Connection in the specified express route circuits.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param circuit_name: The name of the express route circuit.
    :type circuit_name: str
    :param peering_name: The name of the peering.
    :type peering_name: str
    :param connection_name: The name of the express route circuit connection.
    :type connection_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param express_route_circuit_connection_parameters: Parameters supplied to the create or update express route circuit connection operation.
    :type express_route_circuit_connection_parameters: dict | bytes

    """
    express_route_circuit_connection_parameters = ExpressRouteCircuitConnection.from_dict(express_route_circuit_connection_parameters)
    return web.Response(status=200)


async def express_route_circuit_connections_delete(request: web.Request, resource_group_name, circuit_name, peering_name, connection_name, api_version, subscription_id) -> web.Response:
    """express_route_circuit_connections_delete

    Deletes the specified Express Route Circuit Connection from the specified express route circuit.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param circuit_name: The name of the express route circuit.
    :type circuit_name: str
    :param peering_name: The name of the peering.
    :type peering_name: str
    :param connection_name: The name of the express route circuit connection.
    :type connection_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def express_route_circuit_connections_get(request: web.Request, resource_group_name, circuit_name, peering_name, connection_name, api_version, subscription_id) -> web.Response:
    """express_route_circuit_connections_get

    Gets the specified Express Route Circuit Connection from the specified express route circuit.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param circuit_name: The name of the express route circuit.
    :type circuit_name: str
    :param peering_name: The name of the peering.
    :type peering_name: str
    :param connection_name: The name of the express route circuit connection.
    :type connection_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def express_route_circuit_connections_list(request: web.Request, resource_group_name, circuit_name, peering_name, api_version, subscription_id) -> web.Response:
    """express_route_circuit_connections_list

    Gets all global reach connections associated with a private peering in an express route circuit.

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
