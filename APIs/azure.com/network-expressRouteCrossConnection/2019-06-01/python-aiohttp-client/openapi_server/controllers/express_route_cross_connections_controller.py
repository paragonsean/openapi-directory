from typing import List, Dict
from aiohttp import web

from openapi_server.models.express_route_cross_connection import ExpressRouteCrossConnection
from openapi_server.models.express_route_cross_connection_list_result import ExpressRouteCrossConnectionListResult
from openapi_server.models.express_route_cross_connections_update_tags_request import ExpressRouteCrossConnectionsUpdateTagsRequest
from openapi_server import util


async def express_route_cross_connections_create_or_update(request: web.Request, resource_group_name, cross_connection_name, api_version, subscription_id, parameters) -> web.Response:
    """express_route_cross_connections_create_or_update

    Update the specified ExpressRouteCrossConnection.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param cross_connection_name: The name of the ExpressRouteCrossConnection.
    :type cross_connection_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters supplied to the update express route crossConnection operation.
    :type parameters: dict | bytes

    """
    parameters = ExpressRouteCrossConnection.from_dict(parameters)
    return web.Response(status=200)


async def express_route_cross_connections_get(request: web.Request, resource_group_name, cross_connection_name, api_version, subscription_id) -> web.Response:
    """express_route_cross_connections_get

    Gets details about the specified ExpressRouteCrossConnection.

    :param resource_group_name: The name of the resource group (peering location of the circuit).
    :type resource_group_name: str
    :param cross_connection_name: The name of the ExpressRouteCrossConnection (service key of the circuit).
    :type cross_connection_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def express_route_cross_connections_list(request: web.Request, api_version, subscription_id) -> web.Response:
    """express_route_cross_connections_list

    Retrieves all the ExpressRouteCrossConnections in a subscription.

    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def express_route_cross_connections_list_by_resource_group(request: web.Request, resource_group_name, api_version, subscription_id) -> web.Response:
    """express_route_cross_connections_list_by_resource_group

    Retrieves all the ExpressRouteCrossConnections in a resource group.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def express_route_cross_connections_update_tags(request: web.Request, resource_group_name, cross_connection_name, api_version, subscription_id, cross_connection_parameters) -> web.Response:
    """express_route_cross_connections_update_tags

    Updates an express route cross connection tags.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param cross_connection_name: The name of the cross connection.
    :type cross_connection_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param cross_connection_parameters: Parameters supplied to update express route cross connection tags.
    :type cross_connection_parameters: dict | bytes

    """
    cross_connection_parameters = ExpressRouteCrossConnectionsUpdateTagsRequest.from_dict(cross_connection_parameters)
    return web.Response(status=200)
