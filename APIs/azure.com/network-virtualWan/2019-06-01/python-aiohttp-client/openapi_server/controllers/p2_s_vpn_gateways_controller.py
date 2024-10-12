from typing import List, Dict
from aiohttp import web

from openapi_server.models.p2_s_vpn_gateway import P2SVpnGateway
from openapi_server.models.p2_s_vpn_profile_parameters import P2SVpnProfileParameters
from openapi_server.models.p2s_vpn_gateways_list_default_response import P2sVpnGatewaysListDefaultResponse
from openapi_server.models.p2s_vpn_gateways_update_tags_request import P2sVpnGatewaysUpdateTagsRequest
from openapi_server.models.vpn_profile_response import VpnProfileResponse
from openapi_server import util


async def p2s_vpn_gateways_generate_vpn_profile(request: web.Request, resource_group_name, gateway_name, api_version, subscription_id, parameters) -> web.Response:
    """p2s_vpn_gateways_generate_vpn_profile

    Generates VPN profile for P2S client of the P2SVpnGateway in the specified resource group.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param gateway_name: The name of the P2SVpnGateway.
    :type gateway_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters supplied to the generate P2SVpnGateway VPN client package operation.
    :type parameters: dict | bytes

    """
    parameters = P2SVpnProfileParameters.from_dict(parameters)
    return web.Response(status=200)


async def p2s_vpn_gateways_get_p2s_vpn_connection_health(request: web.Request, resource_group_name, gateway_name, api_version, subscription_id) -> web.Response:
    """p2s_vpn_gateways_get_p2s_vpn_connection_health

    Gets the connection health of P2S clients of the virtual wan P2SVpnGateway in the specified resource group.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param gateway_name: The name of the P2SVpnGateway.
    :type gateway_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def p2s_vpn_gateways_update_tags(request: web.Request, subscription_id, resource_group_name, gateway_name, api_version, p2_s_vpn_gateway_parameters) -> web.Response:
    """p2s_vpn_gateways_update_tags

    Updates virtual wan p2s vpn gateway tags.

    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The resource group name of the P2SVpnGateway.
    :type resource_group_name: str
    :param gateway_name: The name of the gateway.
    :type gateway_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param p2_s_vpn_gateway_parameters: Parameters supplied to update a virtual wan p2s vpn gateway tags.
    :type p2_s_vpn_gateway_parameters: dict | bytes

    """
    p2_s_vpn_gateway_parameters = P2sVpnGatewaysUpdateTagsRequest.from_dict(p2_s_vpn_gateway_parameters)
    return web.Response(status=200)
