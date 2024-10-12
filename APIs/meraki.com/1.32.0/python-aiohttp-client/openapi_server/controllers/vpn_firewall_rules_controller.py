from typing import List, Dict
from aiohttp import web

from openapi_server.models.update_organization_appliance_vpn_vpn_firewall_rules_request import UpdateOrganizationApplianceVpnVpnFirewallRulesRequest
from openapi_server import util


async def get_organization_appliance_vpn_vpn_firewall_rules_2(request: web.Request, organization_id) -> web.Response:
    """Return the firewall rules for an organization&#39;s site-to-site VPN

    Return the firewall rules for an organization&#39;s site-to-site VPN

    :param organization_id: 
    :type organization_id: str

    """
    return web.Response(status=200)


async def update_organization_appliance_vpn_vpn_firewall_rules_2(request: web.Request, organization_id, body=None) -> web.Response:
    """Update the firewall rules of an organization&#39;s site-to-site VPN

    Update the firewall rules of an organization&#39;s site-to-site VPN

    :param organization_id: 
    :type organization_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateOrganizationApplianceVpnVpnFirewallRulesRequest.from_dict(body)
    return web.Response(status=200)
