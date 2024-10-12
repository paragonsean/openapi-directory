from typing import List, Dict
from aiohttp import web

from openapi_server.models.virtual_network import VirtualNetwork
from openapi_server.models.virtual_network_list_result import VirtualNetworkListResult
from openapi_server import util


async def virtual_networks_create_or_update(request: web.Request, resource_group_name, virtual_network_name, api_version, subscription_id, parameters) -> web.Response:
    """virtual_networks_create_or_update

    The Put VirtualNetwork operation creates/updates a virtual network in the specified resource group.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param virtual_network_name: The name of the virtual network.
    :type virtual_network_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters supplied to the create/update Virtual Network operation
    :type parameters: dict | bytes

    """
    parameters = VirtualNetwork.from_dict(parameters)
    return web.Response(status=200)


async def virtual_networks_delete(request: web.Request, resource_group_name, virtual_network_name, api_version, subscription_id) -> web.Response:
    """virtual_networks_delete

    The Delete VirtualNetwork operation deletes the specified virtual network

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


async def virtual_networks_get(request: web.Request, resource_group_name, virtual_network_name, api_version, subscription_id, expand=None) -> web.Response:
    """virtual_networks_get

    The Get VirtualNetwork operation retrieves information about the specified virtual network.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param virtual_network_name: The name of the virtual network.
    :type virtual_network_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param expand: expand references resources.
    :type expand: str

    """
    return web.Response(status=200)


async def virtual_networks_list(request: web.Request, resource_group_name, api_version, subscription_id) -> web.Response:
    """virtual_networks_list

    The list VirtualNetwork returns all Virtual Networks in a resource group

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def virtual_networks_list_all(request: web.Request, api_version, subscription_id) -> web.Response:
    """virtual_networks_list_all

    The list VirtualNetwork returns all Virtual Networks in a subscription

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)
