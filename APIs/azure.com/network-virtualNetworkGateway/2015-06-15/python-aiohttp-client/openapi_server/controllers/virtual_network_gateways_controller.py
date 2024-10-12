from typing import List, Dict
from aiohttp import web

from openapi_server.models.virtual_network_gateway import VirtualNetworkGateway
from openapi_server.models.virtual_network_gateway_list_result import VirtualNetworkGatewayListResult
from openapi_server.models.vpn_client_parameters import VpnClientParameters
from openapi_server import util


async def virtual_network_gateways_create_or_update(request: web.Request, resource_group_name, virtual_network_gateway_name, api_version, subscription_id, parameters) -> web.Response:
    """virtual_network_gateways_create_or_update

    Creates or updates a virtual network gateway in the specified resource group.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param virtual_network_gateway_name: The name of the virtual network gateway.
    :type virtual_network_gateway_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters supplied to create or update virtual network gateway operation.
    :type parameters: dict | bytes

    """
    parameters = VirtualNetworkGateway.from_dict(parameters)
    return web.Response(status=200)


async def virtual_network_gateways_delete(request: web.Request, resource_group_name, virtual_network_gateway_name, api_version, subscription_id) -> web.Response:
    """virtual_network_gateways_delete

    Deletes the specified virtual network gateway.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param virtual_network_gateway_name: The name of the virtual network gateway.
    :type virtual_network_gateway_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def virtual_network_gateways_generatevpnclientpackage(request: web.Request, resource_group_name, virtual_network_gateway_name, api_version, subscription_id, parameters) -> web.Response:
    """virtual_network_gateways_generatevpnclientpackage

    Generates VPN client package for P2S client of the virtual network gateway in the specified resource group.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param virtual_network_gateway_name: The name of the virtual network gateway.
    :type virtual_network_gateway_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters supplied to the generate virtual network gateway VPN client package operation.
    :type parameters: dict | bytes

    """
    parameters = VpnClientParameters.from_dict(parameters)
    return web.Response(status=200)


async def virtual_network_gateways_get(request: web.Request, resource_group_name, virtual_network_gateway_name, api_version, subscription_id) -> web.Response:
    """virtual_network_gateways_get

    Gets the specified virtual network gateway by resource group.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param virtual_network_gateway_name: The name of the virtual network gateway.
    :type virtual_network_gateway_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def virtual_network_gateways_list(request: web.Request, resource_group_name, api_version, subscription_id) -> web.Response:
    """virtual_network_gateways_list

    Gets all virtual network gateways by resource group.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def virtual_network_gateways_reset(request: web.Request, resource_group_name, virtual_network_gateway_name, api_version, subscription_id, parameters) -> web.Response:
    """virtual_network_gateways_reset

    Resets the primary of the virtual network gateway in the specified resource group.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param virtual_network_gateway_name: The name of the virtual network gateway.
    :type virtual_network_gateway_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Virtual network gateway vip address supplied to the begin reset of the active-active feature enabled gateway.
    :type parameters: dict | bytes

    """
    parameters = VirtualNetworkGateway.from_dict(parameters)
    return web.Response(status=200)
