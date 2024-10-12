from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_device_appliance_vmx_authentication_token201_response import CreateDeviceApplianceVmxAuthenticationToken201Response
from openapi_server.models.create_network_appliance_prefixes_delegated_static_request import CreateNetworkAppliancePrefixesDelegatedStaticRequest
from openapi_server.models.create_network_appliance_static_route_request import CreateNetworkApplianceStaticRouteRequest
from openapi_server.models.create_network_appliance_traffic_shaping_custom_performance_class_request import CreateNetworkApplianceTrafficShapingCustomPerformanceClassRequest
from openapi_server.models.create_network_appliance_vlan201_response import CreateNetworkApplianceVlan201Response
from openapi_server.models.create_network_appliance_vlan_request import CreateNetworkApplianceVlanRequest
from openapi_server.models.get_device_appliance_uplinks_settings200_response import GetDeviceApplianceUplinksSettings200Response
from openapi_server.models.get_network_appliance_ports200_response_inner import GetNetworkAppliancePorts200ResponseInner
from openapi_server.models.get_network_appliance_prefixes_delegated_statics200_response_inner import GetNetworkAppliancePrefixesDelegatedStatics200ResponseInner
from openapi_server.models.get_network_appliance_settings200_response import GetNetworkApplianceSettings200Response
from openapi_server.models.get_network_appliance_single_lan200_response import GetNetworkApplianceSingleLan200Response
from openapi_server.models.get_network_appliance_ssids200_response_inner import GetNetworkApplianceSsids200ResponseInner
from openapi_server.models.get_network_appliance_traffic_shaping_uplink_bandwidth200_response import GetNetworkApplianceTrafficShapingUplinkBandwidth200Response
from openapi_server.models.get_network_appliance_traffic_shaping_uplink_selection200_response import GetNetworkApplianceTrafficShapingUplinkSelection200Response
from openapi_server.models.get_network_appliance_vlans200_response_inner import GetNetworkApplianceVlans200ResponseInner
from openapi_server.models.get_network_appliance_vpn_site_to_site_vpn200_response import GetNetworkApplianceVpnSiteToSiteVpn200Response
from openapi_server.models.get_organization_appliance_vpn_third_party_vpn_peers200_response import GetOrganizationApplianceVpnThirdPartyVPNPeers200Response
from openapi_server.models.update_device_appliance_uplinks_settings_request import UpdateDeviceApplianceUplinksSettingsRequest
from openapi_server.models.update_network_appliance_connectivity_monitoring_destinations_request import UpdateNetworkApplianceConnectivityMonitoringDestinationsRequest
from openapi_server.models.update_network_appliance_content_filtering_request import UpdateNetworkApplianceContentFilteringRequest
from openapi_server.models.update_network_appliance_firewall_cellular_firewall_rules_request import UpdateNetworkApplianceFirewallCellularFirewallRulesRequest
from openapi_server.models.update_network_appliance_firewall_firewalled_service_request import UpdateNetworkApplianceFirewallFirewalledServiceRequest
from openapi_server.models.update_network_appliance_firewall_inbound_firewall_rules_request import UpdateNetworkApplianceFirewallInboundFirewallRulesRequest
from openapi_server.models.update_network_appliance_firewall_l7_firewall_rules_request import UpdateNetworkApplianceFirewallL7FirewallRulesRequest
from openapi_server.models.update_network_appliance_firewall_one_to_many_nat_rules_request import UpdateNetworkApplianceFirewallOneToManyNatRulesRequest
from openapi_server.models.update_network_appliance_firewall_one_to_one_nat_rules_request import UpdateNetworkApplianceFirewallOneToOneNatRulesRequest
from openapi_server.models.update_network_appliance_firewall_port_forwarding_rules_request import UpdateNetworkApplianceFirewallPortForwardingRulesRequest
from openapi_server.models.update_network_appliance_firewall_settings_request import UpdateNetworkApplianceFirewallSettingsRequest
from openapi_server.models.update_network_appliance_port_request import UpdateNetworkAppliancePortRequest
from openapi_server.models.update_network_appliance_prefixes_delegated_static_request import UpdateNetworkAppliancePrefixesDelegatedStaticRequest
from openapi_server.models.update_network_appliance_security_intrusion_request import UpdateNetworkApplianceSecurityIntrusionRequest
from openapi_server.models.update_network_appliance_security_malware_request import UpdateNetworkApplianceSecurityMalwareRequest
from openapi_server.models.update_network_appliance_settings_request import UpdateNetworkApplianceSettingsRequest
from openapi_server.models.update_network_appliance_single_lan_request import UpdateNetworkApplianceSingleLanRequest
from openapi_server.models.update_network_appliance_ssid_request import UpdateNetworkApplianceSsidRequest
from openapi_server.models.update_network_appliance_static_route_request import UpdateNetworkApplianceStaticRouteRequest
from openapi_server.models.update_network_appliance_traffic_shaping_custom_performance_class_request import UpdateNetworkApplianceTrafficShapingCustomPerformanceClassRequest
from openapi_server.models.update_network_appliance_traffic_shaping_request import UpdateNetworkApplianceTrafficShapingRequest
from openapi_server.models.update_network_appliance_traffic_shaping_rules_request import UpdateNetworkApplianceTrafficShapingRulesRequest
from openapi_server.models.update_network_appliance_traffic_shaping_uplink_bandwidth_request import UpdateNetworkApplianceTrafficShapingUplinkBandwidthRequest
from openapi_server.models.update_network_appliance_traffic_shaping_uplink_selection_request import UpdateNetworkApplianceTrafficShapingUplinkSelectionRequest
from openapi_server.models.update_network_appliance_vlan_request import UpdateNetworkApplianceVlanRequest
from openapi_server.models.update_network_appliance_vlans_settings_request import UpdateNetworkApplianceVlansSettingsRequest
from openapi_server.models.update_network_appliance_vpn_bgp_request import UpdateNetworkApplianceVpnBgpRequest
from openapi_server.models.update_network_appliance_vpn_site_to_site_vpn_request import UpdateNetworkApplianceVpnSiteToSiteVpnRequest
from openapi_server.models.update_network_appliance_warm_spare_request import UpdateNetworkApplianceWarmSpareRequest
from openapi_server.models.update_organization_appliance_security_intrusion_request import UpdateOrganizationApplianceSecurityIntrusionRequest
from openapi_server.models.update_organization_appliance_vpn_third_party_vpn_peers_request import UpdateOrganizationApplianceVpnThirdPartyVPNPeersRequest
from openapi_server.models.update_organization_appliance_vpn_vpn_firewall_rules_request import UpdateOrganizationApplianceVpnVpnFirewallRulesRequest
from openapi_server import util


async def create_device_appliance_vmx_authentication_token(request: web.Request, serial) -> web.Response:
    """Generate a new vMX authentication token

    Generate a new vMX authentication token

    :param serial: 
    :type serial: str

    """
    return web.Response(status=200)


async def create_network_appliance_prefixes_delegated_static(request: web.Request, network_id, body) -> web.Response:
    """Add a static delegated prefix from a network

    Add a static delegated prefix from a network

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateNetworkAppliancePrefixesDelegatedStaticRequest.from_dict(body)
    return web.Response(status=200)


async def create_network_appliance_static_route(request: web.Request, network_id, body) -> web.Response:
    """Add a static route for an MX or teleworker network

    Add a static route for an MX or teleworker network

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateNetworkApplianceStaticRouteRequest.from_dict(body)
    return web.Response(status=200)


async def create_network_appliance_traffic_shaping_custom_performance_class(request: web.Request, network_id, body) -> web.Response:
    """Add a custom performance class for an MX network

    Add a custom performance class for an MX network

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateNetworkApplianceTrafficShapingCustomPerformanceClassRequest.from_dict(body)
    return web.Response(status=200)


async def create_network_appliance_vlan(request: web.Request, network_id, body) -> web.Response:
    """Add a VLAN

    Add a VLAN

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateNetworkApplianceVlanRequest.from_dict(body)
    return web.Response(status=200)


async def delete_network_appliance_prefixes_delegated_static(request: web.Request, network_id, static_delegated_prefix_id) -> web.Response:
    """Delete a static delegated prefix from a network

    Delete a static delegated prefix from a network

    :param network_id: 
    :type network_id: str
    :param static_delegated_prefix_id: 
    :type static_delegated_prefix_id: str

    """
    return web.Response(status=200)


async def delete_network_appliance_static_route(request: web.Request, network_id, static_route_id) -> web.Response:
    """Delete a static route from an MX or teleworker network

    Delete a static route from an MX or teleworker network

    :param network_id: 
    :type network_id: str
    :param static_route_id: 
    :type static_route_id: str

    """
    return web.Response(status=200)


async def delete_network_appliance_traffic_shaping_custom_performance_class(request: web.Request, network_id, custom_performance_class_id) -> web.Response:
    """Delete a custom performance class from an MX network

    Delete a custom performance class from an MX network

    :param network_id: 
    :type network_id: str
    :param custom_performance_class_id: 
    :type custom_performance_class_id: str

    """
    return web.Response(status=200)


async def delete_network_appliance_vlan(request: web.Request, network_id, vlan_id) -> web.Response:
    """Delete a VLAN from a network

    Delete a VLAN from a network

    :param network_id: 
    :type network_id: str
    :param vlan_id: 
    :type vlan_id: str

    """
    return web.Response(status=200)


async def get_device_appliance_dhcp_subnets(request: web.Request, serial) -> web.Response:
    """Return the DHCP subnet information for an appliance

    Return the DHCP subnet information for an appliance

    :param serial: 
    :type serial: str

    """
    return web.Response(status=200)


async def get_device_appliance_performance(request: web.Request, serial) -> web.Response:
    """Return the performance score for a single MX

    Return the performance score for a single MX. Only primary MX devices supported. If no data is available, a 204 error code is returned.

    :param serial: 
    :type serial: str

    """
    return web.Response(status=200)


async def get_device_appliance_prefixes_delegated(request: web.Request, serial) -> web.Response:
    """Return current delegated IPv6 prefixes on an appliance.

    Return current delegated IPv6 prefixes on an appliance.

    :param serial: 
    :type serial: str

    """
    return web.Response(status=200)


async def get_device_appliance_prefixes_delegated_vlan_assignments(request: web.Request, serial) -> web.Response:
    """Return prefixes assigned to all IPv6 enabled VLANs on an appliance.

    Return prefixes assigned to all IPv6 enabled VLANs on an appliance.

    :param serial: 
    :type serial: str

    """
    return web.Response(status=200)


async def get_device_appliance_uplinks_settings(request: web.Request, serial) -> web.Response:
    """Return the uplink settings for an MX appliance

    Return the uplink settings for an MX appliance

    :param serial: 
    :type serial: str

    """
    return web.Response(status=200)


async def get_network_appliance_client_security_events(request: web.Request, network_id, client_id, t0=None, t1=None, timespan=None, per_page=None, starting_after=None, ending_before=None, sort_order=None) -> web.Response:
    """List the security events for a client

    List the security events for a client. Clients can be identified by a client key or either the MAC or IP depending on whether the network uses Track-by-IP.

    :param network_id: 
    :type network_id: str
    :param client_id: 
    :type client_id: str
    :param t0: The beginning of the timespan for the data. Data is gathered after the specified t0 value. The maximum lookback period is 791 days from today.
    :type t0: str
    :param t1: The end of the timespan for the data. t1 can be a maximum of 791 days after t0.
    :type t1: str
    :param timespan: The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 791 days. The default is 31 days.
    :type timespan: float
    :param per_page: The number of entries per page returned. Acceptable range is 3 - 1000. Default is 100.
    :type per_page: int
    :param starting_after: A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type starting_after: str
    :param ending_before: A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type ending_before: str
    :param sort_order: Sorted order of security events based on event detection time. Order options are &#39;ascending&#39; or &#39;descending&#39;. Default is ascending order.
    :type sort_order: str

    """
    return web.Response(status=200)


async def get_network_appliance_connectivity_monitoring_destinations(request: web.Request, network_id) -> web.Response:
    """Return the connectivity testing destinations for an MX network

    Return the connectivity testing destinations for an MX network

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_appliance_content_filtering(request: web.Request, network_id) -> web.Response:
    """Return the content filtering settings for an MX network

    Return the content filtering settings for an MX network

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_appliance_content_filtering_categories(request: web.Request, network_id) -> web.Response:
    """List all available content filtering categories for an MX network

    List all available content filtering categories for an MX network

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_appliance_firewall_cellular_firewall_rules(request: web.Request, network_id) -> web.Response:
    """Return the cellular firewall rules for an MX network

    Return the cellular firewall rules for an MX network

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_appliance_firewall_firewalled_service(request: web.Request, network_id, service) -> web.Response:
    """Return the accessibility settings of the given service (&#39;ICMP&#39;, &#39;web&#39;, or &#39;SNMP&#39;)

    Return the accessibility settings of the given service (&#39;ICMP&#39;, &#39;web&#39;, or &#39;SNMP&#39;)

    :param network_id: 
    :type network_id: str
    :param service: 
    :type service: str

    """
    return web.Response(status=200)


async def get_network_appliance_firewall_firewalled_services(request: web.Request, network_id) -> web.Response:
    """List the appliance services and their accessibility rules

    List the appliance services and their accessibility rules

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_appliance_firewall_inbound_cellular_firewall_rules(request: web.Request, network_id) -> web.Response:
    """Return the inbound cellular firewall rules for an MX network

    Return the inbound cellular firewall rules for an MX network

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_appliance_firewall_inbound_firewall_rules(request: web.Request, network_id) -> web.Response:
    """Return the inbound firewall rules for an MX network

    Return the inbound firewall rules for an MX network

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_appliance_firewall_l3_firewall_rules(request: web.Request, network_id) -> web.Response:
    """Return the L3 firewall rules for an MX network

    Return the L3 firewall rules for an MX network

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_appliance_firewall_l7_firewall_rules(request: web.Request, network_id) -> web.Response:
    """List the MX L7 firewall rules for an MX network

    List the MX L7 firewall rules for an MX network

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_appliance_firewall_l7_firewall_rules_application_categories(request: web.Request, network_id) -> web.Response:
    """Return the L7 firewall application categories and their associated applications for an MX network

    Return the L7 firewall application categories and their associated applications for an MX network

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_appliance_firewall_one_to_many_nat_rules(request: web.Request, network_id) -> web.Response:
    """Return the 1:Many NAT mapping rules for an MX network

    Return the 1:Many NAT mapping rules for an MX network

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_appliance_firewall_one_to_one_nat_rules(request: web.Request, network_id) -> web.Response:
    """Return the 1:1 NAT mapping rules for an MX network

    Return the 1:1 NAT mapping rules for an MX network

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_appliance_firewall_port_forwarding_rules(request: web.Request, network_id) -> web.Response:
    """Return the port forwarding rules for an MX network

    Return the port forwarding rules for an MX network

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_appliance_firewall_settings(request: web.Request, network_id) -> web.Response:
    """Return the firewall settings for this network

    Return the firewall settings for this network

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_appliance_port(request: web.Request, network_id, port_id) -> web.Response:
    """Return per-port VLAN settings for a single MX port.

    Return per-port VLAN settings for a single MX port.

    :param network_id: 
    :type network_id: str
    :param port_id: 
    :type port_id: str

    """
    return web.Response(status=200)


async def get_network_appliance_ports(request: web.Request, network_id) -> web.Response:
    """List per-port VLAN settings for all ports of a MX.

    List per-port VLAN settings for all ports of a MX.

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_appliance_prefixes_delegated_static(request: web.Request, network_id, static_delegated_prefix_id) -> web.Response:
    """Return a static delegated prefix from a network

    Return a static delegated prefix from a network

    :param network_id: 
    :type network_id: str
    :param static_delegated_prefix_id: 
    :type static_delegated_prefix_id: str

    """
    return web.Response(status=200)


async def get_network_appliance_prefixes_delegated_statics(request: web.Request, network_id) -> web.Response:
    """List static delegated prefixes for a network

    List static delegated prefixes for a network

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_appliance_security_events(request: web.Request, network_id, t0=None, t1=None, timespan=None, per_page=None, starting_after=None, ending_before=None, sort_order=None) -> web.Response:
    """List the security events for a network

    List the security events for a network

    :param network_id: 
    :type network_id: str
    :param t0: The beginning of the timespan for the data. Data is gathered after the specified t0 value. The maximum lookback period is 365 days from today.
    :type t0: str
    :param t1: The end of the timespan for the data. t1 can be a maximum of 365 days after t0.
    :type t1: str
    :param timespan: The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 365 days. The default is 31 days.
    :type timespan: float
    :param per_page: The number of entries per page returned. Acceptable range is 3 - 1000. Default is 100.
    :type per_page: int
    :param starting_after: A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type starting_after: str
    :param ending_before: A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type ending_before: str
    :param sort_order: Sorted order of security events based on event detection time. Order options are &#39;ascending&#39; or &#39;descending&#39;. Default is ascending order.
    :type sort_order: str

    """
    return web.Response(status=200)


async def get_network_appliance_security_intrusion(request: web.Request, network_id) -> web.Response:
    """Returns all supported intrusion settings for an MX network

    Returns all supported intrusion settings for an MX network

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_appliance_security_malware(request: web.Request, network_id) -> web.Response:
    """Returns all supported malware settings for an MX network

    Returns all supported malware settings for an MX network

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_appliance_settings(request: web.Request, network_id) -> web.Response:
    """Return the appliance settings for a network

    Return the appliance settings for a network

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_appliance_single_lan(request: web.Request, network_id) -> web.Response:
    """Return single LAN configuration

    Return single LAN configuration

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_appliance_ssid(request: web.Request, network_id, number) -> web.Response:
    """Return a single MX SSID

    Return a single MX SSID

    :param network_id: 
    :type network_id: str
    :param number: 
    :type number: str

    """
    return web.Response(status=200)


async def get_network_appliance_ssids(request: web.Request, network_id) -> web.Response:
    """List the MX SSIDs in a network

    List the MX SSIDs in a network

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_appliance_static_route(request: web.Request, network_id, static_route_id) -> web.Response:
    """Return a static route for an MX or teleworker network

    Return a static route for an MX or teleworker network

    :param network_id: 
    :type network_id: str
    :param static_route_id: 
    :type static_route_id: str

    """
    return web.Response(status=200)


async def get_network_appliance_static_routes(request: web.Request, network_id) -> web.Response:
    """List the static routes for an MX or teleworker network

    List the static routes for an MX or teleworker network

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_appliance_traffic_shaping(request: web.Request, network_id) -> web.Response:
    """Display the traffic shaping settings for an MX network

    Display the traffic shaping settings for an MX network

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_appliance_traffic_shaping_custom_performance_class(request: web.Request, network_id, custom_performance_class_id) -> web.Response:
    """Return a custom performance class for an MX network

    Return a custom performance class for an MX network

    :param network_id: 
    :type network_id: str
    :param custom_performance_class_id: 
    :type custom_performance_class_id: str

    """
    return web.Response(status=200)


async def get_network_appliance_traffic_shaping_custom_performance_classes(request: web.Request, network_id) -> web.Response:
    """List all custom performance classes for an MX network

    List all custom performance classes for an MX network

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_appliance_traffic_shaping_rules(request: web.Request, network_id) -> web.Response:
    """Display the traffic shaping settings rules for an MX network

    Display the traffic shaping settings rules for an MX network

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_appliance_traffic_shaping_uplink_bandwidth(request: web.Request, network_id) -> web.Response:
    """Returns the uplink bandwidth limits for your MX network

    Returns the uplink bandwidth limits for your MX network. This may not reflect the affected device&#39;s hardware capabilities.  For more information on your device&#39;s hardware capabilities, please consult our MX Family Datasheet - [https://meraki.cisco.com/product-collateral/mx-family-datasheet/?file]

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_appliance_traffic_shaping_uplink_selection(request: web.Request, network_id) -> web.Response:
    """Show uplink selection settings for an MX network

    Show uplink selection settings for an MX network

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_appliance_uplinks_usage_history(request: web.Request, network_id, t0=None, t1=None, timespan=None, resolution=None) -> web.Response:
    """Get the sent and received bytes for each uplink of a network.

    Get the sent and received bytes for each uplink of a network.

    :param network_id: 
    :type network_id: str
    :param t0: The beginning of the timespan for the data. The maximum lookback period is 365 days from today.
    :type t0: str
    :param t1: The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
    :type t1: str
    :param timespan: The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 10 minutes.
    :type timespan: float
    :param resolution: The time resolution in seconds for returned data. The valid resolutions are: 60, 300, 600, 1800, 3600, 86400. The default is 60.
    :type resolution: int

    """
    return web.Response(status=200)


async def get_network_appliance_vlan(request: web.Request, network_id, vlan_id) -> web.Response:
    """Return a VLAN

    Return a VLAN

    :param network_id: 
    :type network_id: str
    :param vlan_id: 
    :type vlan_id: str

    """
    return web.Response(status=200)


async def get_network_appliance_vlans(request: web.Request, network_id) -> web.Response:
    """List the VLANs for an MX network

    List the VLANs for an MX network

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_appliance_vlans_settings(request: web.Request, network_id) -> web.Response:
    """Returns the enabled status of VLANs for the network

    Returns the enabled status of VLANs for the network

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_appliance_vpn_bgp(request: web.Request, network_id) -> web.Response:
    """Return a Hub BGP Configuration

    Return a Hub BGP Configuration

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_appliance_vpn_site_to_site_vpn(request: web.Request, network_id) -> web.Response:
    """Return the site-to-site VPN settings of a network

    Return the site-to-site VPN settings of a network. Only valid for MX networks.

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_appliance_warm_spare(request: web.Request, network_id) -> web.Response:
    """Return MX warm spare settings

    Return MX warm spare settings

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_organization_appliance_security_events(request: web.Request, organization_id, t0=None, t1=None, timespan=None, per_page=None, starting_after=None, ending_before=None, sort_order=None) -> web.Response:
    """List the security events for an organization

    List the security events for an organization

    :param organization_id: 
    :type organization_id: str
    :param t0: The beginning of the timespan for the data. Data is gathered after the specified t0 value. The maximum lookback period is 365 days from today.
    :type t0: str
    :param t1: The end of the timespan for the data. t1 can be a maximum of 365 days after t0.
    :type t1: str
    :param timespan: The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 365 days. The default is 31 days.
    :type timespan: float
    :param per_page: The number of entries per page returned. Acceptable range is 3 - 1000. Default is 100.
    :type per_page: int
    :param starting_after: A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type starting_after: str
    :param ending_before: A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type ending_before: str
    :param sort_order: Sorted order of security events based on event detection time. Order options are &#39;ascending&#39; or &#39;descending&#39;. Default is ascending order.
    :type sort_order: str

    """
    return web.Response(status=200)


async def get_organization_appliance_security_intrusion(request: web.Request, organization_id) -> web.Response:
    """Returns all supported intrusion settings for an organization

    Returns all supported intrusion settings for an organization

    :param organization_id: 
    :type organization_id: str

    """
    return web.Response(status=200)


async def get_organization_appliance_uplink_statuses(request: web.Request, organization_id, per_page=None, starting_after=None, ending_before=None, network_ids=None, serials=None, iccids=None) -> web.Response:
    """List the uplink status of every Meraki MX and Z series appliances in the organization

    List the uplink status of every Meraki MX and Z series appliances in the organization

    :param organization_id: 
    :type organization_id: str
    :param per_page: The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
    :type per_page: int
    :param starting_after: A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type starting_after: str
    :param ending_before: A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type ending_before: str
    :param network_ids: A list of network IDs. The returned devices will be filtered to only include these networks.
    :type network_ids: List[str]
    :param serials: A list of serial numbers. The returned devices will be filtered to only include these serials.
    :type serials: List[str]
    :param iccids: A list of ICCIDs. The returned devices will be filtered to only include these ICCIDs.
    :type iccids: List[str]

    """
    return web.Response(status=200)


async def get_organization_appliance_vpn_stats(request: web.Request, organization_id, per_page=None, starting_after=None, ending_before=None, network_ids=None, t0=None, t1=None, timespan=None) -> web.Response:
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


async def get_organization_appliance_vpn_statuses(request: web.Request, organization_id, per_page=None, starting_after=None, ending_before=None, network_ids=None) -> web.Response:
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


async def get_organization_appliance_vpn_third_party_vpn_peers(request: web.Request, organization_id) -> web.Response:
    """Return the third party VPN peers for an organization

    Return the third party VPN peers for an organization

    :param organization_id: 
    :type organization_id: str

    """
    return web.Response(status=200)


async def get_organization_appliance_vpn_vpn_firewall_rules(request: web.Request, organization_id) -> web.Response:
    """Return the firewall rules for an organization&#39;s site-to-site VPN

    Return the firewall rules for an organization&#39;s site-to-site VPN

    :param organization_id: 
    :type organization_id: str

    """
    return web.Response(status=200)


async def swap_network_appliance_warm_spare(request: web.Request, network_id) -> web.Response:
    """Swap MX primary and warm spare appliances

    Swap MX primary and warm spare appliances

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def update_device_appliance_uplinks_settings(request: web.Request, serial, body) -> web.Response:
    """Update the uplink settings for an MX appliance

    Update the uplink settings for an MX appliance

    :param serial: 
    :type serial: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateDeviceApplianceUplinksSettingsRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_appliance_connectivity_monitoring_destinations(request: web.Request, network_id, body=None) -> web.Response:
    """Update the connectivity testing destinations for an MX network

    Update the connectivity testing destinations for an MX network

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkApplianceConnectivityMonitoringDestinationsRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_appliance_content_filtering(request: web.Request, network_id, body=None) -> web.Response:
    """Update the content filtering settings for an MX network

    Update the content filtering settings for an MX network

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkApplianceContentFilteringRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_appliance_firewall_cellular_firewall_rules(request: web.Request, network_id, body=None) -> web.Response:
    """Update the cellular firewall rules of an MX network

    Update the cellular firewall rules of an MX network

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkApplianceFirewallCellularFirewallRulesRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_appliance_firewall_firewalled_service(request: web.Request, network_id, service, body) -> web.Response:
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


async def update_network_appliance_firewall_inbound_cellular_firewall_rules(request: web.Request, network_id, body=None) -> web.Response:
    """Update the inbound cellular firewall rules of an MX network

    Update the inbound cellular firewall rules of an MX network

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkApplianceFirewallCellularFirewallRulesRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_appliance_firewall_inbound_firewall_rules(request: web.Request, network_id, body=None) -> web.Response:
    """Update the inbound firewall rules of an MX network

    Update the inbound firewall rules of an MX network

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkApplianceFirewallInboundFirewallRulesRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_appliance_firewall_l3_firewall_rules(request: web.Request, network_id, body=None) -> web.Response:
    """Update the L3 firewall rules of an MX network

    Update the L3 firewall rules of an MX network

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkApplianceFirewallInboundFirewallRulesRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_appliance_firewall_l7_firewall_rules(request: web.Request, network_id, body=None) -> web.Response:
    """Update the MX L7 firewall rules for an MX network

    Update the MX L7 firewall rules for an MX network

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkApplianceFirewallL7FirewallRulesRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_appliance_firewall_one_to_many_nat_rules(request: web.Request, network_id, body) -> web.Response:
    """Set the 1:Many NAT mapping rules for an MX network

    Set the 1:Many NAT mapping rules for an MX network

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkApplianceFirewallOneToManyNatRulesRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_appliance_firewall_one_to_one_nat_rules(request: web.Request, network_id, body) -> web.Response:
    """Set the 1:1 NAT mapping rules for an MX network

    Set the 1:1 NAT mapping rules for an MX network

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkApplianceFirewallOneToOneNatRulesRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_appliance_firewall_port_forwarding_rules(request: web.Request, network_id, body) -> web.Response:
    """Update the port forwarding rules for an MX network

    Update the port forwarding rules for an MX network

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkApplianceFirewallPortForwardingRulesRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_appliance_firewall_settings(request: web.Request, network_id, body=None) -> web.Response:
    """Update the firewall settings for this network

    Update the firewall settings for this network

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkApplianceFirewallSettingsRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_appliance_port(request: web.Request, network_id, port_id, body=None) -> web.Response:
    """Update the per-port VLAN settings for a single MX port.

    Update the per-port VLAN settings for a single MX port.

    :param network_id: 
    :type network_id: str
    :param port_id: 
    :type port_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkAppliancePortRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_appliance_prefixes_delegated_static(request: web.Request, network_id, static_delegated_prefix_id, body=None) -> web.Response:
    """Update a static delegated prefix from a network

    Update a static delegated prefix from a network

    :param network_id: 
    :type network_id: str
    :param static_delegated_prefix_id: 
    :type static_delegated_prefix_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkAppliancePrefixesDelegatedStaticRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_appliance_security_intrusion(request: web.Request, network_id, body=None) -> web.Response:
    """Set the supported intrusion settings for an MX network

    Set the supported intrusion settings for an MX network

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkApplianceSecurityIntrusionRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_appliance_security_malware(request: web.Request, network_id, body) -> web.Response:
    """Set the supported malware settings for an MX network

    Set the supported malware settings for an MX network

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkApplianceSecurityMalwareRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_appliance_settings(request: web.Request, network_id, body=None) -> web.Response:
    """Update the appliance settings for a network

    Update the appliance settings for a network

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkApplianceSettingsRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_appliance_single_lan(request: web.Request, network_id, body=None) -> web.Response:
    """Update single LAN configuration

    Update single LAN configuration

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkApplianceSingleLanRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_appliance_ssid(request: web.Request, network_id, number, body=None) -> web.Response:
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


async def update_network_appliance_static_route(request: web.Request, network_id, static_route_id, body=None) -> web.Response:
    """Update a static route for an MX or teleworker network

    Update a static route for an MX or teleworker network

    :param network_id: 
    :type network_id: str
    :param static_route_id: 
    :type static_route_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkApplianceStaticRouteRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_appliance_traffic_shaping(request: web.Request, network_id, body=None) -> web.Response:
    """Update the traffic shaping settings for an MX network

    Update the traffic shaping settings for an MX network

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkApplianceTrafficShapingRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_appliance_traffic_shaping_custom_performance_class(request: web.Request, network_id, custom_performance_class_id, body=None) -> web.Response:
    """Update a custom performance class for an MX network

    Update a custom performance class for an MX network

    :param network_id: 
    :type network_id: str
    :param custom_performance_class_id: 
    :type custom_performance_class_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkApplianceTrafficShapingCustomPerformanceClassRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_appliance_traffic_shaping_rules(request: web.Request, network_id, body=None) -> web.Response:
    """Update the traffic shaping settings rules for an MX network

    Update the traffic shaping settings rules for an MX network

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkApplianceTrafficShapingRulesRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_appliance_traffic_shaping_uplink_bandwidth(request: web.Request, network_id, body=None) -> web.Response:
    """Updates the uplink bandwidth settings for your MX network.

    Updates the uplink bandwidth settings for your MX network.

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkApplianceTrafficShapingUplinkBandwidthRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_appliance_traffic_shaping_uplink_selection(request: web.Request, network_id, body=None) -> web.Response:
    """Update uplink selection settings for an MX network

    Update uplink selection settings for an MX network

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkApplianceTrafficShapingUplinkSelectionRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_appliance_vlan(request: web.Request, network_id, vlan_id, body=None) -> web.Response:
    """Update a VLAN

    Update a VLAN

    :param network_id: 
    :type network_id: str
    :param vlan_id: 
    :type vlan_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkApplianceVlanRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_appliance_vlans_settings(request: web.Request, network_id, body=None) -> web.Response:
    """Enable/Disable VLANs for the given network

    Enable/Disable VLANs for the given network

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkApplianceVlansSettingsRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_appliance_vpn_bgp(request: web.Request, network_id, body) -> web.Response:
    """Update a Hub BGP Configuration

    Update a Hub BGP Configuration

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkApplianceVpnBgpRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_appliance_vpn_site_to_site_vpn(request: web.Request, network_id, body) -> web.Response:
    """Update the site-to-site VPN settings of a network

    Update the site-to-site VPN settings of a network. Only valid for MX networks in NAT mode.

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkApplianceVpnSiteToSiteVpnRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_appliance_warm_spare(request: web.Request, network_id, body) -> web.Response:
    """Update MX warm spare settings

    Update MX warm spare settings

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkApplianceWarmSpareRequest.from_dict(body)
    return web.Response(status=200)


async def update_organization_appliance_security_intrusion(request: web.Request, organization_id, body) -> web.Response:
    """Sets supported intrusion settings for an organization

    Sets supported intrusion settings for an organization

    :param organization_id: 
    :type organization_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateOrganizationApplianceSecurityIntrusionRequest.from_dict(body)
    return web.Response(status=200)


async def update_organization_appliance_vpn_third_party_vpn_peers(request: web.Request, organization_id, body) -> web.Response:
    """Update the third party VPN peers for an organization

    Update the third party VPN peers for an organization

    :param organization_id: 
    :type organization_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateOrganizationApplianceVpnThirdPartyVPNPeersRequest.from_dict(body)
    return web.Response(status=200)


async def update_organization_appliance_vpn_vpn_firewall_rules(request: web.Request, organization_id, body=None) -> web.Response:
    """Update the firewall rules of an organization&#39;s site-to-site VPN

    Update the firewall rules of an organization&#39;s site-to-site VPN

    :param organization_id: 
    :type organization_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateOrganizationApplianceVpnVpnFirewallRulesRequest.from_dict(body)
    return web.Response(status=200)
