from typing import List, Dict
from aiohttp import web

from openapi_server.models.p2s_vpn_gateways_list_default_response import P2sVpnGatewaysListDefaultResponse
from openapi_server.models.p2s_vpn_gateways_update_tags_request import P2sVpnGatewaysUpdateTagsRequest
from openapi_server.models.vpn_site import VpnSite
from openapi_server import util


async def vpn_sites_update_tags(request: web.Request, subscription_id, resource_group_name, vpn_site_name, api_version, vpn_site_parameters) -> web.Response:
    """vpn_sites_update_tags

    Updates VpnSite tags.

    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The resource group name of the VpnSite.
    :type resource_group_name: str
    :param vpn_site_name: The name of the VpnSite being updated.
    :type vpn_site_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param vpn_site_parameters: Parameters supplied to update VpnSite tags.
    :type vpn_site_parameters: dict | bytes

    """
    vpn_site_parameters = P2sVpnGatewaysUpdateTagsRequest.from_dict(vpn_site_parameters)
    return web.Response(status=200)
