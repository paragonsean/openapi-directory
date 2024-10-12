from typing import List, Dict
from aiohttp import web

from openapi_server.models.p2s_vpn_gateways_list_default_response import P2sVpnGatewaysListDefaultResponse
from openapi_server.models.p2s_vpn_gateways_update_tags_request import P2sVpnGatewaysUpdateTagsRequest
from openapi_server.models.vpn_gateway import VpnGateway
from openapi_server import util


async def vpn_gateways_reset(request: web.Request, resource_group_name, gateway_name, api_version, subscription_id) -> web.Response:
    """vpn_gateways_reset

    Resets the primary of the vpn gateway in the specified resource group.

    :param resource_group_name: The resource group name of the VpnGateway.
    :type resource_group_name: str
    :param gateway_name: The name of the gateway.
    :type gateway_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def vpn_gateways_update_tags(request: web.Request, subscription_id, resource_group_name, gateway_name, api_version, vpn_gateway_parameters) -> web.Response:
    """vpn_gateways_update_tags

    Updates virtual wan vpn gateway tags.

    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The resource group name of the VpnGateway.
    :type resource_group_name: str
    :param gateway_name: The name of the gateway.
    :type gateway_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param vpn_gateway_parameters: Parameters supplied to update a virtual wan vpn gateway tags.
    :type vpn_gateway_parameters: dict | bytes

    """
    vpn_gateway_parameters = P2sVpnGatewaysUpdateTagsRequest.from_dict(vpn_gateway_parameters)
    return web.Response(status=200)
