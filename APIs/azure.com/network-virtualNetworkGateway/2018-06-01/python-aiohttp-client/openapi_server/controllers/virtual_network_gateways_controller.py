from typing import List, Dict
from aiohttp import web

from openapi_server.models.bgp_peer_status_list_result import BgpPeerStatusListResult
from openapi_server.models.gateway_route_list_result import GatewayRouteListResult
from openapi_server.models.virtual_network_gateway import VirtualNetworkGateway
from openapi_server.models.virtual_network_gateway_connections_update_tags_request import VirtualNetworkGatewayConnectionsUpdateTagsRequest
from openapi_server.models.virtual_network_gateway_list_connections_result import VirtualNetworkGatewayListConnectionsResult
from openapi_server.models.virtual_network_gateway_list_result import VirtualNetworkGatewayListResult
from openapi_server.models.vpn_client_i_psec_parameters import VpnClientIPsecParameters
from openapi_server.models.vpn_client_parameters import VpnClientParameters
from openapi_server.models.vpn_device_script_parameters import VpnDeviceScriptParameters
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


async def virtual_network_gateways_generate_vpn_profile(request: web.Request, resource_group_name, virtual_network_gateway_name, api_version, subscription_id, parameters) -> web.Response:
    """virtual_network_gateways_generate_vpn_profile

    Generates VPN profile for P2S client of the virtual network gateway in the specified resource group. Used for IKEV2 and radius based authentication.

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


async def virtual_network_gateways_get_advertised_routes(request: web.Request, resource_group_name, virtual_network_gateway_name, peer, api_version, subscription_id) -> web.Response:
    """virtual_network_gateways_get_advertised_routes

    This operation retrieves a list of routes the virtual network gateway is advertising to the specified peer.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param virtual_network_gateway_name: The name of the virtual network gateway.
    :type virtual_network_gateway_name: str
    :param peer: The IP address of the peer
    :type peer: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def virtual_network_gateways_get_bgp_peer_status(request: web.Request, resource_group_name, virtual_network_gateway_name, api_version, subscription_id, peer=None) -> web.Response:
    """virtual_network_gateways_get_bgp_peer_status

    The GetBgpPeerStatus operation retrieves the status of all BGP peers.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param virtual_network_gateway_name: The name of the virtual network gateway.
    :type virtual_network_gateway_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param peer: The IP address of the peer to retrieve the status of.
    :type peer: str

    """
    return web.Response(status=200)


async def virtual_network_gateways_get_learned_routes(request: web.Request, resource_group_name, virtual_network_gateway_name, api_version, subscription_id) -> web.Response:
    """virtual_network_gateways_get_learned_routes

    This operation retrieves a list of routes the virtual network gateway has learned, including routes learned from BGP peers.

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


async def virtual_network_gateways_get_vpn_profile_package_url(request: web.Request, resource_group_name, virtual_network_gateway_name, api_version, subscription_id) -> web.Response:
    """virtual_network_gateways_get_vpn_profile_package_url

    Gets pre-generated VPN profile for P2S client of the virtual network gateway in the specified resource group. The profile needs to be generated first using generateVpnProfile.

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


async def virtual_network_gateways_get_vpnclient_ipsec_parameters(request: web.Request, resource_group_name, virtual_network_gateway_name, api_version, subscription_id) -> web.Response:
    """virtual_network_gateways_get_vpnclient_ipsec_parameters

    The Get VpnclientIpsecParameters operation retrieves information about the vpnclient ipsec policy for P2S client of virtual network gateway in the specified resource group through Network resource provider.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param virtual_network_gateway_name: The virtual network gateway name.
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


async def virtual_network_gateways_list_connections(request: web.Request, resource_group_name, virtual_network_gateway_name, api_version, subscription_id) -> web.Response:
    """virtual_network_gateways_list_connections

    Gets all the connections in a virtual network gateway.

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


async def virtual_network_gateways_reset(request: web.Request, resource_group_name, virtual_network_gateway_name, api_version, subscription_id, gateway_vip=None) -> web.Response:
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
    :param gateway_vip: Virtual network gateway vip address supplied to the begin reset of the active-active feature enabled gateway.
    :type gateway_vip: str

    """
    return web.Response(status=200)


async def virtual_network_gateways_reset_vpn_client_shared_key(request: web.Request, resource_group_name, virtual_network_gateway_name, api_version, subscription_id) -> web.Response:
    """virtual_network_gateways_reset_vpn_client_shared_key

    Resets the VPN client shared key of the virtual network gateway in the specified resource group.

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


async def virtual_network_gateways_set_vpnclient_ipsec_parameters(request: web.Request, resource_group_name, virtual_network_gateway_name, api_version, subscription_id, vpnclient_ipsec_params) -> web.Response:
    """virtual_network_gateways_set_vpnclient_ipsec_parameters

    The Set VpnclientIpsecParameters operation sets the vpnclient ipsec policy for P2S client of virtual network gateway in the specified resource group through Network resource provider.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param virtual_network_gateway_name: The name of the virtual network gateway.
    :type virtual_network_gateway_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param vpnclient_ipsec_params: Parameters supplied to the Begin Set vpnclient ipsec parameters of Virtual Network Gateway P2S client operation through Network resource provider.
    :type vpnclient_ipsec_params: dict | bytes

    """
    vpnclient_ipsec_params = VpnClientIPsecParameters.from_dict(vpnclient_ipsec_params)
    return web.Response(status=200)


async def virtual_network_gateways_supported_vpn_devices(request: web.Request, resource_group_name, virtual_network_gateway_name, api_version, subscription_id) -> web.Response:
    """virtual_network_gateways_supported_vpn_devices

    Gets a xml format representation for supported vpn devices.

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


async def virtual_network_gateways_update_tags(request: web.Request, resource_group_name, virtual_network_gateway_name, api_version, subscription_id, parameters) -> web.Response:
    """virtual_network_gateways_update_tags

    Updates a virtual network gateway tags.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param virtual_network_gateway_name: The name of the virtual network gateway.
    :type virtual_network_gateway_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters supplied to update virtual network gateway tags.
    :type parameters: dict | bytes

    """
    parameters = VirtualNetworkGatewayConnectionsUpdateTagsRequest.from_dict(parameters)
    return web.Response(status=200)


async def virtual_network_gateways_vpn_device_configuration_script(request: web.Request, resource_group_name, virtual_network_gateway_connection_name, api_version, subscription_id, parameters) -> web.Response:
    """virtual_network_gateways_vpn_device_configuration_script

    Gets a xml format representation for vpn device configuration script.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param virtual_network_gateway_connection_name: The name of the virtual network gateway connection for which the configuration script is generated.
    :type virtual_network_gateway_connection_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters supplied to the generate vpn device script operation.
    :type parameters: dict | bytes

    """
    parameters = VpnDeviceScriptParameters.from_dict(parameters)
    return web.Response(status=200)
