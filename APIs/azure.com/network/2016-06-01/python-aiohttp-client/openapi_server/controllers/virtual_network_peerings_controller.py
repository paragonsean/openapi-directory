from typing import List, Dict
from aiohttp import web

from openapi_server.models.virtual_network_peering import VirtualNetworkPeering
from openapi_server.models.virtual_network_peering_list_result import VirtualNetworkPeeringListResult
from openapi_server import util


async def virtual_network_peerings_create_or_update(request: web.Request, resource_group_name, virtual_network_name, virtual_network_peering_name, api_version, subscription_id, virtual_network_peering_parameters) -> web.Response:
    """virtual_network_peerings_create_or_update

    The Put virtual network peering operation creates/updates a peering in the specified virtual network

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param virtual_network_name: The name of the virtual network.
    :type virtual_network_name: str
    :param virtual_network_peering_name: The name of the peering.
    :type virtual_network_peering_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param virtual_network_peering_parameters: Parameters supplied to the create/update virtual network peering operation
    :type virtual_network_peering_parameters: dict | bytes

    """
    virtual_network_peering_parameters = VirtualNetworkPeering.from_dict(virtual_network_peering_parameters)
    return web.Response(status=200)


async def virtual_network_peerings_delete(request: web.Request, resource_group_name, virtual_network_name, virtual_network_peering_name, api_version, subscription_id) -> web.Response:
    """virtual_network_peerings_delete

    The delete virtual network peering operation deletes the specified peering.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param virtual_network_name: The name of the virtual network.
    :type virtual_network_name: str
    :param virtual_network_peering_name: The name of the virtual network peering.
    :type virtual_network_peering_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def virtual_network_peerings_get(request: web.Request, resource_group_name, virtual_network_name, virtual_network_peering_name, api_version, subscription_id) -> web.Response:
    """virtual_network_peerings_get

    The Get virtual network peering operation retrieves information about the specified virtual network peering.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param virtual_network_name: The name of the virtual network.
    :type virtual_network_name: str
    :param virtual_network_peering_name: The name of the virtual network peering.
    :type virtual_network_peering_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def virtual_network_peerings_list(request: web.Request, resource_group_name, virtual_network_name, api_version, subscription_id) -> web.Response:
    """virtual_network_peerings_list

    The List virtual network peerings operation retrieves all the peerings in a virtual network.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param virtual_network_name: The name of the virtual network.
    :type virtual_network_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)
