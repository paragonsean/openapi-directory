from typing import List, Dict
from aiohttp import web

from openapi_server.models.virtual_network_gateway import VirtualNetworkGateway
from openapi_server.models.virtual_network_gateway_list_result import VirtualNetworkGatewayListResult
from openapi_server.models.vpn_client_parameters import VpnClientParameters
from openapi_server import util


async def virtual_network_gateways_create_or_update(request: web.Request, resource_group_name, virtual_network_gateway_name, api_version, subscription_id, parameters) -> web.Response:
    """virtual_network_gateways_create_or_update

    The Put VirtualNetworkGateway operation creates/updates a virtual network gateway in the specified resource group through Network resource provider.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param virtual_network_gateway_name: The name of the virtual network gateway.
    :type virtual_network_gateway_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters supplied to the Begin Create or update Virtual Network Gateway operation through Network resource provider.
    :type parameters: dict | bytes

    """
    parameters = VirtualNetworkGateway.from_dict(parameters)
    return web.Response(status=200)


async def virtual_network_gateways_delete(request: web.Request, resource_group_name, virtual_network_gateway_name, api_version, subscription_id) -> web.Response:
    """virtual_network_gateways_delete

    The Delete VirtualNetworkGateway operation deletes the specified virtual network Gateway through Network resource provider.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param virtual_network_gateway_name: The name of the virtual network gateway.
    :type virtual_network_gateway_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def virtual_network_gateways_generatevpnclientpackage(request: web.Request, resource_group_name, virtual_network_gateway_name, api_version, subscription_id, parameters) -> web.Response:
    """virtual_network_gateways_generatevpnclientpackage

    The Generatevpnclientpackage operation generates Vpn client package for P2S client of the virtual network gateway in the specified resource group through Network resource provider.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param virtual_network_gateway_name: The name of the virtual network gateway.
    :type virtual_network_gateway_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters supplied to the Begin Generating  Virtual Network Gateway Vpn client package operation through Network resource provider.
    :type parameters: dict | bytes

    """
    parameters = VpnClientParameters.from_dict(parameters)
    return web.Response(status=200)


async def virtual_network_gateways_get(request: web.Request, resource_group_name, virtual_network_gateway_name, api_version, subscription_id) -> web.Response:
    """virtual_network_gateways_get

    The Get VirtualNetworkGateway operation retrieves information about the specified virtual network gateway through Network resource provider.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param virtual_network_gateway_name: The name of the virtual network gateway.
    :type virtual_network_gateway_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def virtual_network_gateways_list(request: web.Request, resource_group_name, api_version, subscription_id) -> web.Response:
    """virtual_network_gateways_list

    The List VirtualNetworkGateways operation retrieves all the virtual network gateways stored.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def virtual_network_gateways_reset(request: web.Request, resource_group_name, virtual_network_gateway_name, api_version, subscription_id, parameters) -> web.Response:
    """virtual_network_gateways_reset

    The Reset VirtualNetworkGateway operation resets the primary of the virtual network gateway in the specified resource group through Network resource provider.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param virtual_network_gateway_name: The name of the virtual network gateway.
    :type virtual_network_gateway_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters supplied to the Begin Reset Virtual Network Gateway operation through Network resource provider.
    :type parameters: dict | bytes

    """
    parameters = VirtualNetworkGateway.from_dict(parameters)
    return web.Response(status=200)
