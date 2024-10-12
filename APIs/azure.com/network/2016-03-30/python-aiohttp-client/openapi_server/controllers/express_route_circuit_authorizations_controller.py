from typing import List, Dict
from aiohttp import web

from openapi_server.models.authorization_list_result import AuthorizationListResult
from openapi_server.models.express_route_circuit_authorization import ExpressRouteCircuitAuthorization
from openapi_server import util


async def express_route_circuit_authorizations_create_or_update(request: web.Request, resource_group_name, circuit_name, authorization_name, api_version, subscription_id, authorization_parameters) -> web.Response:
    """express_route_circuit_authorizations_create_or_update

    The Put Authorization operation creates/updates an authorization in the specified ExpressRouteCircuits

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param circuit_name: The name of the express route circuit.
    :type circuit_name: str
    :param authorization_name: The name of the authorization.
    :type authorization_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param authorization_parameters: Parameters supplied to the create/update ExpressRouteCircuitAuthorization operation
    :type authorization_parameters: dict | bytes

    """
    authorization_parameters = ExpressRouteCircuitAuthorization.from_dict(authorization_parameters)
    return web.Response(status=200)


async def express_route_circuit_authorizations_delete(request: web.Request, resource_group_name, circuit_name, authorization_name, api_version, subscription_id) -> web.Response:
    """express_route_circuit_authorizations_delete

    The delete authorization operation deletes the specified authorization from the specified ExpressRouteCircuit.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param circuit_name: The name of the express route circuit.
    :type circuit_name: str
    :param authorization_name: The name of the authorization.
    :type authorization_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def express_route_circuit_authorizations_get(request: web.Request, resource_group_name, circuit_name, authorization_name, api_version, subscription_id) -> web.Response:
    """express_route_circuit_authorizations_get

    The GET authorization operation retrieves the specified authorization from the specified ExpressRouteCircuit.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param circuit_name: The name of the express route circuit.
    :type circuit_name: str
    :param authorization_name: The name of the authorization.
    :type authorization_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def express_route_circuit_authorizations_list(request: web.Request, resource_group_name, circuit_name, api_version, subscription_id) -> web.Response:
    """express_route_circuit_authorizations_list

    The List authorization operation retrieves all the authorizations in an ExpressRouteCircuit.

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
