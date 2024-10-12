from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_network_appliance_vpn_site_to_site_vpn200_response import GetNetworkApplianceVpnSiteToSiteVpn200Response
from openapi_server.models.update_network_appliance_vpn_site_to_site_vpn_request import UpdateNetworkApplianceVpnSiteToSiteVpnRequest
from openapi_server import util


async def get_network_appliance_vpn_site_to_site_vpn_2(request: web.Request, network_id) -> web.Response:
    """Return the site-to-site VPN settings of a network

    Return the site-to-site VPN settings of a network. Only valid for MX networks.

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def update_network_appliance_vpn_site_to_site_vpn_2(request: web.Request, network_id, body) -> web.Response:
    """Update the site-to-site VPN settings of a network

    Update the site-to-site VPN settings of a network. Only valid for MX networks in NAT mode.

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkApplianceVpnSiteToSiteVpnRequest.from_dict(body)
    return web.Response(status=200)
