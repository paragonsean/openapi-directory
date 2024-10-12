from typing import List, Dict
from aiohttp import web

from openapi_server.models.express_route_cross_connection_peering import ExpressRouteCrossConnectionPeering
from openapi_server.models.express_route_cross_connection_peering_list import ExpressRouteCrossConnectionPeeringList
from openapi_server import util


async def express_route_cross_connection_peerings_create_or_update(request: web.Request, resource_group_name, cross_connection_name, peering_name, api_version, subscription_id, peering_parameters) -> web.Response:
    """express_route_cross_connection_peerings_create_or_update

    Creates or updates a peering in the specified ExpressRouteCrossConnection.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param cross_connection_name: The name of the ExpressRouteCrossConnection.
    :type cross_connection_name: str
    :param peering_name: The name of the peering.
    :type peering_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param peering_parameters: Parameters supplied to the create or update ExpressRouteCrossConnection peering operation.
    :type peering_parameters: dict | bytes

    """
    peering_parameters = ExpressRouteCrossConnectionPeering.from_dict(peering_parameters)
    return web.Response(status=200)


async def express_route_cross_connection_peerings_delete(request: web.Request, resource_group_name, cross_connection_name, peering_name, api_version, subscription_id) -> web.Response:
    """express_route_cross_connection_peerings_delete

    Deletes the specified peering from the ExpressRouteCrossConnection.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param cross_connection_name: The name of the ExpressRouteCrossConnection.
    :type cross_connection_name: str
    :param peering_name: The name of the peering.
    :type peering_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def express_route_cross_connection_peerings_get(request: web.Request, resource_group_name, cross_connection_name, peering_name, api_version, subscription_id) -> web.Response:
    """express_route_cross_connection_peerings_get

    Gets the specified peering for the ExpressRouteCrossConnection.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param cross_connection_name: The name of the ExpressRouteCrossConnection.
    :type cross_connection_name: str
    :param peering_name: The name of the peering.
    :type peering_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def express_route_cross_connection_peerings_list(request: web.Request, resource_group_name, cross_connection_name, api_version, subscription_id) -> web.Response:
    """express_route_cross_connection_peerings_list

    Gets all peerings in a specified ExpressRouteCrossConnection.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param cross_connection_name: The name of the ExpressRouteCrossConnection.
    :type cross_connection_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)
