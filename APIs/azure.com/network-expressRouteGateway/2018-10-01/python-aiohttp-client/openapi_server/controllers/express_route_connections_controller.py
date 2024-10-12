from typing import List, Dict
from aiohttp import web

from openapi_server.models.express_route_connection import ExpressRouteConnection
from openapi_server.models.express_route_connection_list import ExpressRouteConnectionList
from openapi_server import util


async def express_route_connections_create_or_update(request: web.Request, resource_group_name, express_route_gateway_name, connection_name, api_version, subscription_id, put_express_route_connection_parameters) -> web.Response:
    """express_route_connections_create_or_update

    Creates a connection between an ExpressRoute gateway and an ExpressRoute circuit.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param express_route_gateway_name: The name of the ExpressRoute gateway.
    :type express_route_gateway_name: str
    :param connection_name: The name of the connection subresource.
    :type connection_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param put_express_route_connection_parameters: Parameters required in an ExpressRouteConnection PUT operation.
    :type put_express_route_connection_parameters: dict | bytes

    """
    put_express_route_connection_parameters = ExpressRouteConnection.from_dict(put_express_route_connection_parameters)
    return web.Response(status=200)


async def express_route_connections_delete(request: web.Request, resource_group_name, express_route_gateway_name, connection_name, api_version, subscription_id) -> web.Response:
    """express_route_connections_delete

    Deletes a connection to a ExpressRoute circuit.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param express_route_gateway_name: The name of the ExpressRoute gateway.
    :type express_route_gateway_name: str
    :param connection_name: The name of the connection subresource.
    :type connection_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def express_route_connections_get(request: web.Request, resource_group_name, express_route_gateway_name, connection_name, api_version, subscription_id) -> web.Response:
    """express_route_connections_get

    Gets the specified ExpressRouteConnection.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param express_route_gateway_name: The name of the ExpressRoute gateway.
    :type express_route_gateway_name: str
    :param connection_name: The name of the ExpressRoute connection.
    :type connection_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def express_route_connections_list(request: web.Request, resource_group_name, express_route_gateway_name, api_version, subscription_id) -> web.Response:
    """express_route_connections_list

    Lists ExpressRouteConnections.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param express_route_gateway_name: The name of the ExpressRoute gateway.
    :type express_route_gateway_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)
