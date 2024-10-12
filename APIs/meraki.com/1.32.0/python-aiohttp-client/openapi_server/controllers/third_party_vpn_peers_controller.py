from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_organization_appliance_vpn_third_party_vpn_peers200_response import GetOrganizationApplianceVpnThirdPartyVPNPeers200Response
from openapi_server.models.update_organization_appliance_vpn_third_party_vpn_peers_request import UpdateOrganizationApplianceVpnThirdPartyVPNPeersRequest
from openapi_server import util


async def get_organization_appliance_vpn_third_party_vpn_peers_2(request: web.Request, organization_id) -> web.Response:
    """Return the third party VPN peers for an organization

    Return the third party VPN peers for an organization

    :param organization_id: 
    :type organization_id: str

    """
    return web.Response(status=200)


async def update_organization_appliance_vpn_third_party_vpn_peers_2(request: web.Request, organization_id, body) -> web.Response:
    """Update the third party VPN peers for an organization

    Update the third party VPN peers for an organization

    :param organization_id: 
    :type organization_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateOrganizationApplianceVpnThirdPartyVPNPeersRequest.from_dict(body)
    return web.Response(status=200)
