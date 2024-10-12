from typing import List, Dict
from aiohttp import web

from openapi_server.models.express_route_cross_connections_list_arp_table200_response import ExpressRouteCrossConnectionsListArpTable200Response
from openapi_server import util


async def express_route_cross_connections_list_arp_table(request: web.Request, resource_group_name, cross_connection_name, peering_name, device_path, api_version, subscription_id) -> web.Response:
    """express_route_cross_connections_list_arp_table

    Gets the currently advertised ARP table associated with the express route cross connection in a resource group.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param cross_connection_name: The name of the ExpressRouteCrossConnection.
    :type cross_connection_name: str
    :param peering_name: The name of the peering.
    :type peering_name: str
    :param device_path: The path of the device.
    :type device_path: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)
