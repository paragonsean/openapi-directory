from typing import List, Dict
from aiohttp import web

from openapi_server.models.p2s_vpn_gateways_list_default_response import P2sVpnGatewaysListDefaultResponse
from openapi_server.models.p2s_vpn_gateways_update_tags_request import P2sVpnGatewaysUpdateTagsRequest
from openapi_server.models.virtual_hub import VirtualHub
from openapi_server.models.virtual_wan import VirtualWAN
from openapi_server import util


async def virtual_hubs_update_tags(request: web.Request, subscription_id, resource_group_name, virtual_hub_name, api_version, virtual_hub_parameters) -> web.Response:
    """virtual_hubs_update_tags

    Updates VirtualHub tags.

    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The resource group name of the VirtualHub.
    :type resource_group_name: str
    :param virtual_hub_name: The name of the VirtualHub.
    :type virtual_hub_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param virtual_hub_parameters: Parameters supplied to update VirtualHub tags.
    :type virtual_hub_parameters: dict | bytes

    """
    virtual_hub_parameters = P2sVpnGatewaysUpdateTagsRequest.from_dict(virtual_hub_parameters)
    return web.Response(status=200)


async def virtual_wans_update_tags(request: web.Request, subscription_id, resource_group_name, virtual_wan_name, api_version, wan_parameters) -> web.Response:
    """virtual_wans_update_tags

    Updates a VirtualWAN tags.

    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The resource group name of the VirtualWan.
    :type resource_group_name: str
    :param virtual_wan_name: The name of the VirtualWAN being updated.
    :type virtual_wan_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param wan_parameters: Parameters supplied to Update VirtualWAN tags.
    :type wan_parameters: dict | bytes

    """
    wan_parameters = P2sVpnGatewaysUpdateTagsRequest.from_dict(wan_parameters)
    return web.Response(status=200)
