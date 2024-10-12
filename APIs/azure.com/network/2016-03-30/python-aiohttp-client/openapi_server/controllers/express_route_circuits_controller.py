from typing import List, Dict
from aiohttp import web

from openapi_server.models.express_route_circuit import ExpressRouteCircuit
from openapi_server.models.express_route_circuit_list_result import ExpressRouteCircuitListResult
from openapi_server import util


async def express_route_circuits_create_or_update(request: web.Request, resource_group_name, circuit_name, api_version, subscription_id, parameters) -> web.Response:
    """express_route_circuits_create_or_update

    The Put ExpressRouteCircuit operation creates/updates a ExpressRouteCircuit

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param circuit_name: The name of the circuit.
    :type circuit_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters supplied to the create/delete ExpressRouteCircuit operation
    :type parameters: dict | bytes

    """
    parameters = ExpressRouteCircuit.from_dict(parameters)
    return web.Response(status=200)


async def express_route_circuits_delete(request: web.Request, resource_group_name, circuit_name, api_version, subscription_id) -> web.Response:
    """express_route_circuits_delete

    The delete ExpressRouteCircuit operation deletes the specified ExpressRouteCircuit.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param circuit_name: The name of the express route Circuit.
    :type circuit_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def express_route_circuits_get(request: web.Request, resource_group_name, circuit_name, api_version, subscription_id) -> web.Response:
    """express_route_circuits_get

    The Get ExpressRouteCircuit operation retrieves information about the specified ExpressRouteCircuit.

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


async def express_route_circuits_list(request: web.Request, resource_group_name, api_version, subscription_id) -> web.Response:
    """express_route_circuits_list

    The List ExpressRouteCircuit operation retrieves all the ExpressRouteCircuits in a resource group.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def express_route_circuits_list_all(request: web.Request, api_version, subscription_id) -> web.Response:
    """express_route_circuits_list_all

    The List ExpressRouteCircuit operation retrieves all the ExpressRouteCircuits in a subscription.

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)
