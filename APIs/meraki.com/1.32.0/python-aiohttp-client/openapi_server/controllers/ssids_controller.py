from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_network_wireless_ssid_identity_psk_request import CreateNetworkWirelessSsidIdentityPskRequest
from openapi_server.models.get_network_appliance_ssids200_response_inner import GetNetworkApplianceSsids200ResponseInner
from openapi_server.models.get_network_wireless_ssid_eap_override200_response import GetNetworkWirelessSsidEapOverride200Response
from openapi_server.models.get_network_wireless_ssid_identity_psks200_response_inner import GetNetworkWirelessSsidIdentityPsks200ResponseInner
from openapi_server.models.get_network_wireless_ssid_splash_settings200_response import GetNetworkWirelessSsidSplashSettings200Response
from openapi_server.models.get_organization_summary_top_ssids_by_usage200_response_inner import GetOrganizationSummaryTopSsidsByUsage200ResponseInner
from openapi_server.models.update_network_appliance_ssid_request import UpdateNetworkApplianceSsidRequest
from openapi_server.models.update_network_wireless_ssid_bonjour_forwarding_request import UpdateNetworkWirelessSsidBonjourForwardingRequest
from openapi_server.models.update_network_wireless_ssid_device_type_group_policies_request import UpdateNetworkWirelessSsidDeviceTypeGroupPoliciesRequest
from openapi_server.models.update_network_wireless_ssid_eap_override_request import UpdateNetworkWirelessSsidEapOverrideRequest
from openapi_server.models.update_network_wireless_ssid_firewall_l3_firewall_rules_request import UpdateNetworkWirelessSsidFirewallL3FirewallRulesRequest
from openapi_server.models.update_network_wireless_ssid_firewall_l7_firewall_rules_request import UpdateNetworkWirelessSsidFirewallL7FirewallRulesRequest
from openapi_server.models.update_network_wireless_ssid_hotspot20_request import UpdateNetworkWirelessSsidHotspot20Request
from openapi_server.models.update_network_wireless_ssid_identity_psk_request import UpdateNetworkWirelessSsidIdentityPskRequest
from openapi_server.models.update_network_wireless_ssid_request import UpdateNetworkWirelessSsidRequest
from openapi_server.models.update_network_wireless_ssid_schedules_request import UpdateNetworkWirelessSsidSchedulesRequest
from openapi_server.models.update_network_wireless_ssid_splash_settings_request import UpdateNetworkWirelessSsidSplashSettingsRequest
from openapi_server.models.update_network_wireless_ssid_traffic_shaping_rules_request import UpdateNetworkWirelessSsidTrafficShapingRulesRequest
from openapi_server.models.update_network_wireless_ssid_vpn_request import UpdateNetworkWirelessSsidVpnRequest
from openapi_server import util


async def create_network_wireless_ssid_identity_psk_1(request: web.Request, network_id, number, body) -> web.Response:
    """Create an Identity PSK

    Create an Identity PSK

    :param network_id: 
    :type network_id: str
    :param number: 
    :type number: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateNetworkWirelessSsidIdentityPskRequest.from_dict(body)
    return web.Response(status=200)


async def delete_network_wireless_ssid_identity_psk_1(request: web.Request, network_id, number, identity_psk_id) -> web.Response:
    """Delete an Identity PSK

    Delete an Identity PSK

    :param network_id: 
    :type network_id: str
    :param number: 
    :type number: str
    :param identity_psk_id: 
    :type identity_psk_id: str

    """
    return web.Response(status=200)


async def get_network_appliance_ssid_1(request: web.Request, network_id, number) -> web.Response:
    """Return a single MX SSID

    Return a single MX SSID

    :param network_id: 
    :type network_id: str
    :param number: 
    :type number: str

    """
    return web.Response(status=200)


async def get_network_appliance_ssids_1(request: web.Request, network_id) -> web.Response:
    """List the MX SSIDs in a network

    List the MX SSIDs in a network

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_wireless_ssid_1(request: web.Request, network_id, number) -> web.Response:
    """Return a single MR SSID

    Return a single MR SSID

    :param network_id: 
    :type network_id: str
    :param number: 
    :type number: str

    """
    return web.Response(status=200)


async def get_network_wireless_ssid_bonjour_forwarding_1(request: web.Request, network_id, number) -> web.Response:
    """List the Bonjour forwarding setting and rules for the SSID

    List the Bonjour forwarding setting and rules for the SSID

    :param network_id: 
    :type network_id: str
    :param number: 
    :type number: str

    """
    return web.Response(status=200)


async def get_network_wireless_ssid_device_type_group_policies_1(request: web.Request, network_id, number) -> web.Response:
    """List the device type group policies for the SSID

    List the device type group policies for the SSID

    :param network_id: 
    :type network_id: str
    :param number: 
    :type number: str

    """
    return web.Response(status=200)


async def get_network_wireless_ssid_eap_override_1(request: web.Request, network_id, number) -> web.Response:
    """Return the EAP overridden parameters for an SSID

    Return the EAP overridden parameters for an SSID

    :param network_id: 
    :type network_id: str
    :param number: 
    :type number: str

    """
    return web.Response(status=200)


async def get_network_wireless_ssid_firewall_l3_firewall_rules_1(request: web.Request, network_id, number) -> web.Response:
    """Return the L3 firewall rules for an SSID on an MR network

    Return the L3 firewall rules for an SSID on an MR network

    :param network_id: 
    :type network_id: str
    :param number: 
    :type number: str

    """
    return web.Response(status=200)


async def get_network_wireless_ssid_firewall_l7_firewall_rules_1(request: web.Request, network_id, number) -> web.Response:
    """Return the L7 firewall rules for an SSID on an MR network

    Return the L7 firewall rules for an SSID on an MR network

    :param network_id: 
    :type network_id: str
    :param number: 
    :type number: str

    """
    return web.Response(status=200)


async def get_network_wireless_ssid_hotspot20_1(request: web.Request, network_id, number) -> web.Response:
    """Return the Hotspot 2.0 settings for an SSID

    Return the Hotspot 2.0 settings for an SSID

    :param network_id: 
    :type network_id: str
    :param number: 
    :type number: str

    """
    return web.Response(status=200)


async def get_network_wireless_ssid_identity_psk_1(request: web.Request, network_id, number, identity_psk_id) -> web.Response:
    """Return an Identity PSK

    Return an Identity PSK

    :param network_id: 
    :type network_id: str
    :param number: 
    :type number: str
    :param identity_psk_id: 
    :type identity_psk_id: str

    """
    return web.Response(status=200)


async def get_network_wireless_ssid_identity_psks_1(request: web.Request, network_id, number) -> web.Response:
    """List all Identity PSKs in a wireless network

    List all Identity PSKs in a wireless network

    :param network_id: 
    :type network_id: str
    :param number: 
    :type number: str

    """
    return web.Response(status=200)


async def get_network_wireless_ssid_schedules_1(request: web.Request, network_id, number) -> web.Response:
    """List the outage schedule for the SSID

    List the outage schedule for the SSID

    :param network_id: 
    :type network_id: str
    :param number: 
    :type number: str

    """
    return web.Response(status=200)


async def get_network_wireless_ssid_splash_settings_1(request: web.Request, network_id, number) -> web.Response:
    """Display the splash page settings for the given SSID

    Display the splash page settings for the given SSID

    :param network_id: 
    :type network_id: str
    :param number: 
    :type number: str

    """
    return web.Response(status=200)


async def get_network_wireless_ssid_traffic_shaping_rules_1(request: web.Request, network_id, number) -> web.Response:
    """Display the traffic shaping settings for a SSID on an MR network

    Display the traffic shaping settings for a SSID on an MR network

    :param network_id: 
    :type network_id: str
    :param number: 
    :type number: str

    """
    return web.Response(status=200)


async def get_network_wireless_ssid_vpn_1(request: web.Request, network_id, number) -> web.Response:
    """List the VPN settings for the SSID.

    List the VPN settings for the SSID.

    :param network_id: 
    :type network_id: str
    :param number: 
    :type number: str

    """
    return web.Response(status=200)


async def get_network_wireless_ssids_1(request: web.Request, network_id) -> web.Response:
    """List the MR SSIDs in a network

    List the MR SSIDs in a network

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_organization_summary_top_ssids_by_usage_3(request: web.Request, organization_id, t0=None, t1=None, timespan=None) -> web.Response:
    """Return metrics for organization&#39;s top 10 ssids by data usage over given time range

    Return metrics for organization&#39;s top 10 ssids by data usage over given time range. Default unit is megabytes.

    :param organization_id: 
    :type organization_id: str
    :param t0: The beginning of the timespan for the data.
    :type t0: str
    :param t1: The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
    :type t1: str
    :param timespan: The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.
    :type timespan: float

    """
    return web.Response(status=200)


async def update_network_appliance_ssid_1(request: web.Request, network_id, number, body=None) -> web.Response:
    """Update the attributes of an MX SSID

    Update the attributes of an MX SSID

    :param network_id: 
    :type network_id: str
    :param number: 
    :type number: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkApplianceSsidRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_wireless_ssid_1(request: web.Request, network_id, number, body=None) -> web.Response:
    """Update the attributes of an MR SSID

    Update the attributes of an MR SSID

    :param network_id: 
    :type network_id: str
    :param number: 
    :type number: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkWirelessSsidRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_wireless_ssid_bonjour_forwarding_1(request: web.Request, network_id, number, body=None) -> web.Response:
    """Update the bonjour forwarding setting and rules for the SSID

    Update the bonjour forwarding setting and rules for the SSID

    :param network_id: 
    :type network_id: str
    :param number: 
    :type number: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkWirelessSsidBonjourForwardingRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_wireless_ssid_device_type_group_policies_1(request: web.Request, network_id, number, body=None) -> web.Response:
    """Update the device type group policies for the SSID

    Update the device type group policies for the SSID

    :param network_id: 
    :type network_id: str
    :param number: 
    :type number: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkWirelessSsidDeviceTypeGroupPoliciesRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_wireless_ssid_eap_override_1(request: web.Request, network_id, number, body=None) -> web.Response:
    """Update the EAP overridden parameters for an SSID.

    Update the EAP overridden parameters for an SSID.

    :param network_id: 
    :type network_id: str
    :param number: 
    :type number: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkWirelessSsidEapOverrideRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_wireless_ssid_firewall_l3_firewall_rules_1(request: web.Request, network_id, number, body=None) -> web.Response:
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


async def update_network_wireless_ssid_firewall_l7_firewall_rules_1(request: web.Request, network_id, number, body=None) -> web.Response:
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


async def update_network_wireless_ssid_hotspot20_1(request: web.Request, network_id, number, body=None) -> web.Response:
    """Update the Hotspot 2.0 settings of an SSID

    Update the Hotspot 2.0 settings of an SSID

    :param network_id: 
    :type network_id: str
    :param number: 
    :type number: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkWirelessSsidHotspot20Request.from_dict(body)
    return web.Response(status=200)


async def update_network_wireless_ssid_identity_psk_1(request: web.Request, network_id, number, identity_psk_id, body=None) -> web.Response:
    """Update an Identity PSK

    Update an Identity PSK

    :param network_id: 
    :type network_id: str
    :param number: 
    :type number: str
    :param identity_psk_id: 
    :type identity_psk_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkWirelessSsidIdentityPskRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_wireless_ssid_schedules_1(request: web.Request, network_id, number, body=None) -> web.Response:
    """Update the outage schedule for the SSID

    Update the outage schedule for the SSID

    :param network_id: 
    :type network_id: str
    :param number: 
    :type number: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkWirelessSsidSchedulesRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_wireless_ssid_splash_settings_1(request: web.Request, network_id, number, body=None) -> web.Response:
    """Modify the splash page settings for the given SSID

    Modify the splash page settings for the given SSID

    :param network_id: 
    :type network_id: str
    :param number: 
    :type number: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkWirelessSsidSplashSettingsRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_wireless_ssid_traffic_shaping_rules_1(request: web.Request, network_id, number, body=None) -> web.Response:
    """Update the traffic shaping settings for an SSID on an MR network

    Update the traffic shaping settings for an SSID on an MR network

    :param network_id: 
    :type network_id: str
    :param number: 
    :type number: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkWirelessSsidTrafficShapingRulesRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_wireless_ssid_vpn_1(request: web.Request, network_id, number, body=None) -> web.Response:
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
