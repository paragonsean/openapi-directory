from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_network_appliance_vpn_site_to_site_vpn200_response import GetNetworkApplianceVpnSiteToSiteVpn200Response
from openapi_server.models.get_organization_appliance_vpn_third_party_vpn_peers200_response import GetOrganizationApplianceVpnThirdPartyVPNPeers200Response
from openapi_server.models.update_network_appliance_vpn_bgp_request import UpdateNetworkApplianceVpnBgpRequest
from openapi_server.models.update_network_appliance_vpn_site_to_site_vpn_request import UpdateNetworkApplianceVpnSiteToSiteVpnRequest
from openapi_server.models.update_network_wireless_ssid_vpn_request import UpdateNetworkWirelessSsidVpnRequest
from openapi_server.models.update_organization_appliance_vpn_third_party_vpn_peers_request import UpdateOrganizationApplianceVpnThirdPartyVPNPeersRequest
from openapi_server.models.update_organization_appliance_vpn_vpn_firewall_rules_request import UpdateOrganizationApplianceVpnVpnFirewallRulesRequest
from openapi_server import util


async def get_network_appliance_vpn_bgp_1(request: web.Request, network_id) -> web.Response:
    """Return a Hub BGP Configuration

    Return a Hub BGP Configuration

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_appliance_vpn_site_to_site_vpn_1(request: web.Request, network_id) -> web.Response:
    """Return the site-to-site VPN settings of a network

    Return the site-to-site VPN settings of a network. Only valid for MX networks.

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_wireless_ssid_vpn_2(request: web.Request, network_id, number) -> web.Response:
    """List the VPN settings for the SSID.

    List the VPN settings for the SSID.

    :param network_id: 
    :type network_id: str
    :param number: 
    :type number: str

    """
    return web.Response(status=200)


async def get_organization_appliance_vpn_stats_1(request: web.Request, organization_id, per_page=None, starting_after=None, ending_before=None, network_ids=None, t0=None, t1=None, timespan=None) -> web.Response:
    """Show VPN history stat for networks in an organization

    Show VPN history stat for networks in an organization

    :param organization_id: 
    :type organization_id: str
    :param per_page: The number of entries per page returned. Acceptable range is 3 - 300. Default is 300.
    :type per_page: int
    :param starting_after: A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type starting_after: str
    :param ending_before: A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type ending_before: str
    :param network_ids: A list of Meraki network IDs to filter results to contain only specified networks. E.g.: networkIds[]&#x3D;N_12345678&amp;networkIds[]&#x3D;L_3456
    :type network_ids: List[str]
    :param t0: The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
    :type t0: str
    :param t1: The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
    :type t1: str
    :param timespan: The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.
    :type timespan: float

    """
    return web.Response(status=200)


async def get_organization_appliance_vpn_statuses_1(request: web.Request, organization_id, per_page=None, starting_after=None, ending_before=None, network_ids=None) -> web.Response:
    """Show VPN status for networks in an organization

    Show VPN status for networks in an organization

    :param organization_id: 
    :type organization_id: str
    :param per_page: The number of entries per page returned. Acceptable range is 3 - 300. Default is 300.
    :type per_page: int
    :param starting_after: A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type starting_after: str
    :param ending_before: A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type ending_before: str
    :param network_ids: A list of Meraki network IDs to filter results to contain only specified networks. E.g.: networkIds[]&#x3D;N_12345678&amp;networkIds[]&#x3D;L_3456
    :type network_ids: List[str]

    """
    return web.Response(status=200)


async def get_organization_appliance_vpn_third_party_vpn_peers_1(request: web.Request, organization_id) -> web.Response:
    """Return the third party VPN peers for an organization

    Return the third party VPN peers for an organization

    :param organization_id: 
    :type organization_id: str

    """
    return web.Response(status=200)


async def get_organization_appliance_vpn_vpn_firewall_rules_1(request: web.Request, organization_id) -> web.Response:
    """Return the firewall rules for an organization&#39;s site-to-site VPN

    Return the firewall rules for an organization&#39;s site-to-site VPN

    :param organization_id: 
    :type organization_id: str

    """
    return web.Response(status=200)


async def update_network_appliance_vpn_bgp_1(request: web.Request, network_id, body) -> web.Response:
    """Update a Hub BGP Configuration

    Update a Hub BGP Configuration

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkApplianceVpnBgpRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_appliance_vpn_site_to_site_vpn_1(request: web.Request, network_id, body) -> web.Response:
    """Update the site-to-site VPN settings of a network

    Update the site-to-site VPN settings of a network. Only valid for MX networks in NAT mode.

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkApplianceVpnSiteToSiteVpnRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_wireless_ssid_vpn_2(request: web.Request, network_id, number, body=None) -> web.Response:
    """Update the VPN settings for the SSID

    Update the VPN settings for the SSID

    :param network_id: 
    :type network_id: str
    :param number: 
    :type number: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkWirelessSsidVpnRequest.from_dict(body)
    return web.Response(status=200)


async def update_organization_appliance_vpn_third_party_vpn_peers_1(request: web.Request, organization_id, body) -> web.Response:
    """Update the third party VPN peers for an organization

    Update the third party VPN peers for an organization

    :param organization_id: 
    :type organization_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateOrganizationApplianceVpnThirdPartyVPNPeersRequest.from_dict(body)
    return web.Response(status=200)


async def update_organization_appliance_vpn_vpn_firewall_rules_1(request: web.Request, organization_id, body=None) -> web.Response:
    """Update the firewall rules of an organization&#39;s site-to-site VPN

    Update the firewall rules of an organization&#39;s site-to-site VPN

    :param organization_id: 
    :type organization_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateOrganizationApplianceVpnVpnFirewallRulesRequest.from_dict(body)
    return web.Response(status=200)
