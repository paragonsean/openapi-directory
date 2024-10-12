from typing import List, Dict
from aiohttp import web

from openapi_server.models.update_network_appliance_firewall_cellular_firewall_rules_request import UpdateNetworkApplianceFirewallCellularFirewallRulesRequest
from openapi_server.models.update_network_appliance_firewall_firewalled_service_request import UpdateNetworkApplianceFirewallFirewalledServiceRequest
from openapi_server.models.update_network_appliance_firewall_inbound_firewall_rules_request import UpdateNetworkApplianceFirewallInboundFirewallRulesRequest
from openapi_server.models.update_network_appliance_firewall_l7_firewall_rules_request import UpdateNetworkApplianceFirewallL7FirewallRulesRequest
from openapi_server.models.update_network_appliance_firewall_one_to_many_nat_rules_request import UpdateNetworkApplianceFirewallOneToManyNatRulesRequest
from openapi_server.models.update_network_appliance_firewall_one_to_one_nat_rules_request import UpdateNetworkApplianceFirewallOneToOneNatRulesRequest
from openapi_server.models.update_network_appliance_firewall_port_forwarding_rules_request import UpdateNetworkApplianceFirewallPortForwardingRulesRequest
from openapi_server.models.update_network_appliance_firewall_settings_request import UpdateNetworkApplianceFirewallSettingsRequest
from openapi_server.models.update_network_wireless_ssid_firewall_l3_firewall_rules_request import UpdateNetworkWirelessSsidFirewallL3FirewallRulesRequest
from openapi_server.models.update_network_wireless_ssid_firewall_l7_firewall_rules_request import UpdateNetworkWirelessSsidFirewallL7FirewallRulesRequest
from openapi_server import util


async def get_network_appliance_firewall_cellular_firewall_rules_1(request: web.Request, network_id) -> web.Response:
    """Return the cellular firewall rules for an MX network

    Return the cellular firewall rules for an MX network

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_appliance_firewall_firewalled_service_1(request: web.Request, network_id, service) -> web.Response:
    """Return the accessibility settings of the given service (&#39;ICMP&#39;, &#39;web&#39;, or &#39;SNMP&#39;)

    Return the accessibility settings of the given service (&#39;ICMP&#39;, &#39;web&#39;, or &#39;SNMP&#39;)

    :param network_id: 
    :type network_id: str
    :param service: 
    :type service: str

    """
    return web.Response(status=200)


async def get_network_appliance_firewall_firewalled_services_1(request: web.Request, network_id) -> web.Response:
    """List the appliance services and their accessibility rules

    List the appliance services and their accessibility rules

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_appliance_firewall_inbound_cellular_firewall_rules_1(request: web.Request, network_id) -> web.Response:
    """Return the inbound cellular firewall rules for an MX network

    Return the inbound cellular firewall rules for an MX network

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_appliance_firewall_inbound_firewall_rules_1(request: web.Request, network_id) -> web.Response:
    """Return the inbound firewall rules for an MX network

    Return the inbound firewall rules for an MX network

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_appliance_firewall_l3_firewall_rules_1(request: web.Request, network_id) -> web.Response:
    """Return the L3 firewall rules for an MX network

    Return the L3 firewall rules for an MX network

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_appliance_firewall_l7_firewall_rules_1(request: web.Request, network_id) -> web.Response:
    """List the MX L7 firewall rules for an MX network

    List the MX L7 firewall rules for an MX network

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_appliance_firewall_l7_firewall_rules_application_categories_1(request: web.Request, network_id) -> web.Response:
    """Return the L7 firewall application categories and their associated applications for an MX network

    Return the L7 firewall application categories and their associated applications for an MX network

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_appliance_firewall_one_to_many_nat_rules_1(request: web.Request, network_id) -> web.Response:
    """Return the 1:Many NAT mapping rules for an MX network

    Return the 1:Many NAT mapping rules for an MX network

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_appliance_firewall_one_to_one_nat_rules_1(request: web.Request, network_id) -> web.Response:
    """Return the 1:1 NAT mapping rules for an MX network

    Return the 1:1 NAT mapping rules for an MX network

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_appliance_firewall_port_forwarding_rules_1(request: web.Request, network_id) -> web.Response:
    """Return the port forwarding rules for an MX network

    Return the port forwarding rules for an MX network

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_appliance_firewall_settings_1(request: web.Request, network_id) -> web.Response:
    """Return the firewall settings for this network

    Return the firewall settings for this network

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_wireless_ssid_firewall_l3_firewall_rules_2(request: web.Request, network_id, number) -> web.Response:
    """Return the L3 firewall rules for an SSID on an MR network

    Return the L3 firewall rules for an SSID on an MR network

    :param network_id: 
    :type network_id: str
    :param number: 
    :type number: str

    """
    return web.Response(status=200)


async def get_network_wireless_ssid_firewall_l7_firewall_rules_2(request: web.Request, network_id, number) -> web.Response:
    """Return the L7 firewall rules for an SSID on an MR network

    Return the L7 firewall rules for an SSID on an MR network

    :param network_id: 
    :type network_id: str
    :param number: 
    :type number: str

    """
    return web.Response(status=200)


async def update_network_appliance_firewall_cellular_firewall_rules_1(request: web.Request, network_id, body=None) -> web.Response:
    """Update the cellular firewall rules of an MX network

    Update the cellular firewall rules of an MX network

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkApplianceFirewallCellularFirewallRulesRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_appliance_firewall_firewalled_service_1(request: web.Request, network_id, service, body) -> web.Response:
    """Updates the accessibility settings for the given service (&#39;ICMP&#39;, &#39;web&#39;, or &#39;SNMP&#39;)

    Updates the accessibility settings for the given service (&#39;ICMP&#39;, &#39;web&#39;, or &#39;SNMP&#39;)

    :param network_id: 
    :type network_id: str
    :param service: 
    :type service: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkApplianceFirewallFirewalledServiceRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_appliance_firewall_inbound_cellular_firewall_rules_1(request: web.Request, network_id, body=None) -> web.Response:
    """Update the inbound cellular firewall rules of an MX network

    Update the inbound cellular firewall rules of an MX network

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkApplianceFirewallCellularFirewallRulesRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_appliance_firewall_inbound_firewall_rules_1(request: web.Request, network_id, body=None) -> web.Response:
    """Update the inbound firewall rules of an MX network

    Update the inbound firewall rules of an MX network

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkApplianceFirewallInboundFirewallRulesRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_appliance_firewall_l3_firewall_rules_1(request: web.Request, network_id, body=None) -> web.Response:
    """Update the L3 firewall rules of an MX network

    Update the L3 firewall rules of an MX network

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkApplianceFirewallInboundFirewallRulesRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_appliance_firewall_l7_firewall_rules_1(request: web.Request, network_id, body=None) -> web.Response:
    """Update the MX L7 firewall rules for an MX network

    Update the MX L7 firewall rules for an MX network

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkApplianceFirewallL7FirewallRulesRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_appliance_firewall_one_to_many_nat_rules_1(request: web.Request, network_id, body) -> web.Response:
    """Set the 1:Many NAT mapping rules for an MX network

    Set the 1:Many NAT mapping rules for an MX network

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkApplianceFirewallOneToManyNatRulesRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_appliance_firewall_one_to_one_nat_rules_1(request: web.Request, network_id, body) -> web.Response:
    """Set the 1:1 NAT mapping rules for an MX network

    Set the 1:1 NAT mapping rules for an MX network

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkApplianceFirewallOneToOneNatRulesRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_appliance_firewall_port_forwarding_rules_1(request: web.Request, network_id, body) -> web.Response:
    """Update the port forwarding rules for an MX network

    Update the port forwarding rules for an MX network

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkApplianceFirewallPortForwardingRulesRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_appliance_firewall_settings_1(request: web.Request, network_id, body=None) -> web.Response:
    """Update the firewall settings for this network

    Update the firewall settings for this network

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkApplianceFirewallSettingsRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_wireless_ssid_firewall_l3_firewall_rules_2(request: web.Request, network_id, number, body=None) -> web.Response:
    """Update the L3 firewall rules of an SSID on an MR network

    Update the L3 firewall rules of an SSID on an MR network

    :param network_id: 
    :type network_id: str
    :param number: 
    :type number: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkWirelessSsidFirewallL3FirewallRulesRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_wireless_ssid_firewall_l7_firewall_rules_2(request: web.Request, network_id, number, body=None) -> web.Response:
    """Update the L7 firewall rules of an SSID on an MR network

    Update the L7 firewall rules of an SSID on an MR network

    :param network_id: 
    :type network_id: str
    :param number: 
    :type number: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkWirelessSsidFirewallL7FirewallRulesRequest.from_dict(body)
    return web.Response(status=200)
