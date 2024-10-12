from typing import List, Dict
from aiohttp import web

from openapi_server.models.add_network_switch_stack_request import AddNetworkSwitchStackRequest
from openapi_server.models.clone_organization_switch_devices_request import CloneOrganizationSwitchDevicesRequest
from openapi_server.models.create_device_switch_routing_interface_request import CreateDeviceSwitchRoutingInterfaceRequest
from openapi_server.models.create_device_switch_routing_static_route_request import CreateDeviceSwitchRoutingStaticRouteRequest
from openapi_server.models.create_network_switch_access_policy_request import CreateNetworkSwitchAccessPolicyRequest
from openapi_server.models.create_network_switch_dhcp_server_policy_arp_inspection_trusted_server_request import CreateNetworkSwitchDhcpServerPolicyArpInspectionTrustedServerRequest
from openapi_server.models.create_network_switch_link_aggregation_request import CreateNetworkSwitchLinkAggregationRequest
from openapi_server.models.create_network_switch_port_schedule_request import CreateNetworkSwitchPortScheduleRequest
from openapi_server.models.create_network_switch_qos_rule_request import CreateNetworkSwitchQosRuleRequest
from openapi_server.models.create_network_switch_routing_multicast_rendezvous_point_request import CreateNetworkSwitchRoutingMulticastRendezvousPointRequest
from openapi_server.models.create_network_switch_stack_request import CreateNetworkSwitchStackRequest
from openapi_server.models.create_network_switch_stack_routing_interface_request import CreateNetworkSwitchStackRoutingInterfaceRequest
from openapi_server.models.cycle_device_switch_ports_request import CycleDeviceSwitchPortsRequest
from openapi_server.models.get_device_switch_ports200_response_inner import GetDeviceSwitchPorts200ResponseInner
from openapi_server.models.get_device_switch_ports_statuses200_response_inner import GetDeviceSwitchPortsStatuses200ResponseInner
from openapi_server.models.get_device_switch_routing_interfaces200_response_inner import GetDeviceSwitchRoutingInterfaces200ResponseInner
from openapi_server.models.get_device_switch_routing_static_route200_response import GetDeviceSwitchRoutingStaticRoute200Response
from openapi_server.models.get_network_switch_access_control_lists200_response import GetNetworkSwitchAccessControlLists200Response
from openapi_server.models.get_network_switch_access_policies200_response_inner import GetNetworkSwitchAccessPolicies200ResponseInner
from openapi_server.models.get_network_switch_dhcp_server_policy_arp_inspection_trusted_servers200_response_inner import GetNetworkSwitchDhcpServerPolicyArpInspectionTrustedServers200ResponseInner
from openapi_server.models.get_network_switch_dhcp_server_policy_arp_inspection_warnings_by_device200_response_inner import GetNetworkSwitchDhcpServerPolicyArpInspectionWarningsByDevice200ResponseInner
from openapi_server.models.get_network_switch_dhcp_v4_servers_seen200_response_inner import GetNetworkSwitchDhcpV4ServersSeen200ResponseInner
from openapi_server.models.get_network_switch_mtu200_response import GetNetworkSwitchMtu200Response
from openapi_server.models.get_network_switch_settings200_response import GetNetworkSwitchSettings200Response
from openapi_server.models.get_network_switch_stack200_response import GetNetworkSwitchStack200Response
from openapi_server.models.get_network_switch_storm_control200_response import GetNetworkSwitchStormControl200Response
from openapi_server.models.get_organization_config_template_switch_profile_ports200_response_inner import GetOrganizationConfigTemplateSwitchProfilePorts200ResponseInner
from openapi_server.models.get_organization_config_template_switch_profiles200_response import GetOrganizationConfigTemplateSwitchProfiles200Response
from openapi_server.models.get_organization_switch_ports_by_switch200_response_inner import GetOrganizationSwitchPortsBySwitch200ResponseInner
from openapi_server.models.remove_network_switch_stack_request import RemoveNetworkSwitchStackRequest
from openapi_server.models.update_device_switch_port_request import UpdateDeviceSwitchPortRequest
from openapi_server.models.update_device_switch_routing_interface_dhcp_request import UpdateDeviceSwitchRoutingInterfaceDhcpRequest
from openapi_server.models.update_device_switch_routing_static_route_request import UpdateDeviceSwitchRoutingStaticRouteRequest
from openapi_server.models.update_device_switch_warm_spare_request import UpdateDeviceSwitchWarmSpareRequest
from openapi_server.models.update_network_switch_access_control_lists_request import UpdateNetworkSwitchAccessControlListsRequest
from openapi_server.models.update_network_switch_access_policy_request import UpdateNetworkSwitchAccessPolicyRequest
from openapi_server.models.update_network_switch_alternate_management_interface_request import UpdateNetworkSwitchAlternateManagementInterfaceRequest
from openapi_server.models.update_network_switch_dhcp_server_policy_arp_inspection_trusted_server_request import UpdateNetworkSwitchDhcpServerPolicyArpInspectionTrustedServerRequest
from openapi_server.models.update_network_switch_dhcp_server_policy_request import UpdateNetworkSwitchDhcpServerPolicyRequest
from openapi_server.models.update_network_switch_dscp_to_cos_mappings_request import UpdateNetworkSwitchDscpToCosMappingsRequest
from openapi_server.models.update_network_switch_link_aggregation_request import UpdateNetworkSwitchLinkAggregationRequest
from openapi_server.models.update_network_switch_mtu_request import UpdateNetworkSwitchMtuRequest
from openapi_server.models.update_network_switch_port_schedule_request import UpdateNetworkSwitchPortScheduleRequest
from openapi_server.models.update_network_switch_qos_rule_request import UpdateNetworkSwitchQosRuleRequest
from openapi_server.models.update_network_switch_qos_rules_order_request import UpdateNetworkSwitchQosRulesOrderRequest
from openapi_server.models.update_network_switch_routing_multicast_rendezvous_point_request import UpdateNetworkSwitchRoutingMulticastRendezvousPointRequest
from openapi_server.models.update_network_switch_routing_multicast_request import UpdateNetworkSwitchRoutingMulticastRequest
from openapi_server.models.update_network_switch_routing_ospf_request import UpdateNetworkSwitchRoutingOspfRequest
from openapi_server.models.update_network_switch_settings_request import UpdateNetworkSwitchSettingsRequest
from openapi_server.models.update_network_switch_stack_routing_interface_dhcp_request import UpdateNetworkSwitchStackRoutingInterfaceDhcpRequest
from openapi_server.models.update_network_switch_stack_routing_interface_request import UpdateNetworkSwitchStackRoutingInterfaceRequest
from openapi_server.models.update_network_switch_storm_control_request import UpdateNetworkSwitchStormControlRequest
from openapi_server.models.update_network_switch_stp_request import UpdateNetworkSwitchStpRequest
from openapi_server.models.update_organization_config_template_switch_profile_port_request import UpdateOrganizationConfigTemplateSwitchProfilePortRequest
from openapi_server import util


async def add_network_switch_stack(request: web.Request, network_id, switch_stack_id, body) -> web.Response:
    """Add a switch to a stack

    Add a switch to a stack

    :param network_id: 
    :type network_id: str
    :param switch_stack_id: 
    :type switch_stack_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = AddNetworkSwitchStackRequest.from_dict(body)
    return web.Response(status=200)


async def clone_organization_switch_devices(request: web.Request, organization_id, body) -> web.Response:
    """Clone port-level and some switch-level configuration settings from a source switch to one or more target switches

    Clone port-level and some switch-level configuration settings from a source switch to one or more target switches. Cloned settings include: Aggregation Groups, Power Settings, Multicast Settings, MTU Configuration, STP Bridge priority, Port Mirroring

    :param organization_id: 
    :type organization_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CloneOrganizationSwitchDevicesRequest.from_dict(body)
    return web.Response(status=200)


async def create_device_switch_routing_interface(request: web.Request, serial, body=None) -> web.Response:
    """Create a layer 3 interface for a switch

    Create a layer 3 interface for a switch

    :param serial: 
    :type serial: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateDeviceSwitchRoutingInterfaceRequest.from_dict(body)
    return web.Response(status=200)


async def create_device_switch_routing_static_route(request: web.Request, serial, body) -> web.Response:
    """Create a layer 3 static route for a switch

    Create a layer 3 static route for a switch

    :param serial: 
    :type serial: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateDeviceSwitchRoutingStaticRouteRequest.from_dict(body)
    return web.Response(status=200)


async def create_network_switch_access_policy(request: web.Request, network_id, body) -> web.Response:
    """Create an access policy for a switch network

    Create an access policy for a switch network. If you would like to enable Meraki Authentication, set radiusServers to empty array.

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateNetworkSwitchAccessPolicyRequest.from_dict(body)
    return web.Response(status=200)


async def create_network_switch_dhcp_server_policy_arp_inspection_trusted_server(request: web.Request, network_id, body) -> web.Response:
    """Add a server to be trusted by Dynamic ARP Inspection on this network

    Add a server to be trusted by Dynamic ARP Inspection on this network

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateNetworkSwitchDhcpServerPolicyArpInspectionTrustedServerRequest.from_dict(body)
    return web.Response(status=200)


async def create_network_switch_link_aggregation(request: web.Request, network_id, body=None) -> web.Response:
    """Create a link aggregation group

    Create a link aggregation group

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateNetworkSwitchLinkAggregationRequest.from_dict(body)
    return web.Response(status=200)


async def create_network_switch_port_schedule(request: web.Request, network_id, body) -> web.Response:
    """Add a switch port schedule

    Add a switch port schedule

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateNetworkSwitchPortScheduleRequest.from_dict(body)
    return web.Response(status=200)


async def create_network_switch_qos_rule(request: web.Request, network_id, body) -> web.Response:
    """Add a quality of service rule

    Add a quality of service rule

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateNetworkSwitchQosRuleRequest.from_dict(body)
    return web.Response(status=200)


async def create_network_switch_routing_multicast_rendezvous_point(request: web.Request, network_id, body) -> web.Response:
    """Create a multicast rendezvous point

    Create a multicast rendezvous point

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateNetworkSwitchRoutingMulticastRendezvousPointRequest.from_dict(body)
    return web.Response(status=200)


async def create_network_switch_stack(request: web.Request, network_id, body) -> web.Response:
    """Create a stack

    Create a stack

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateNetworkSwitchStackRequest.from_dict(body)
    return web.Response(status=200)


async def create_network_switch_stack_routing_interface(request: web.Request, network_id, switch_stack_id, body) -> web.Response:
    """Create a layer 3 interface for a switch stack

    Create a layer 3 interface for a switch stack

    :param network_id: 
    :type network_id: str
    :param switch_stack_id: 
    :type switch_stack_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateNetworkSwitchStackRoutingInterfaceRequest.from_dict(body)
    return web.Response(status=200)


async def create_network_switch_stack_routing_static_route(request: web.Request, network_id, switch_stack_id, body) -> web.Response:
    """Create a layer 3 static route for a switch stack

    Create a layer 3 static route for a switch stack

    :param network_id: 
    :type network_id: str
    :param switch_stack_id: 
    :type switch_stack_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateDeviceSwitchRoutingStaticRouteRequest.from_dict(body)
    return web.Response(status=200)


async def cycle_device_switch_ports(request: web.Request, serial, body) -> web.Response:
    """Cycle a set of switch ports

    Cycle a set of switch ports

    :param serial: 
    :type serial: str
    :param body: 
    :type body: dict | bytes

    """
    body = CycleDeviceSwitchPortsRequest.from_dict(body)
    return web.Response(status=200)


async def delete_device_switch_routing_interface(request: web.Request, serial, interface_id) -> web.Response:
    """Delete a layer 3 interface from the switch

    Delete a layer 3 interface from the switch

    :param serial: 
    :type serial: str
    :param interface_id: 
    :type interface_id: str

    """
    return web.Response(status=200)


async def delete_device_switch_routing_static_route(request: web.Request, serial, static_route_id) -> web.Response:
    """Delete a layer 3 static route for a switch

    Delete a layer 3 static route for a switch

    :param serial: 
    :type serial: str
    :param static_route_id: 
    :type static_route_id: str

    """
    return web.Response(status=200)


async def delete_network_switch_access_policy(request: web.Request, network_id, access_policy_number) -> web.Response:
    """Delete an access policy for a switch network

    Delete an access policy for a switch network

    :param network_id: 
    :type network_id: str
    :param access_policy_number: 
    :type access_policy_number: str

    """
    return web.Response(status=200)


async def delete_network_switch_dhcp_server_policy_arp_inspection_trusted_server(request: web.Request, network_id, trusted_server_id) -> web.Response:
    """Remove a server from being trusted by Dynamic ARP Inspection on this network

    Remove a server from being trusted by Dynamic ARP Inspection on this network

    :param network_id: 
    :type network_id: str
    :param trusted_server_id: 
    :type trusted_server_id: str

    """
    return web.Response(status=200)


async def delete_network_switch_link_aggregation(request: web.Request, network_id, link_aggregation_id) -> web.Response:
    """Split a link aggregation group into separate ports

    Split a link aggregation group into separate ports

    :param network_id: 
    :type network_id: str
    :param link_aggregation_id: 
    :type link_aggregation_id: str

    """
    return web.Response(status=200)


async def delete_network_switch_port_schedule(request: web.Request, network_id, port_schedule_id) -> web.Response:
    """Delete a switch port schedule

    Delete a switch port schedule

    :param network_id: 
    :type network_id: str
    :param port_schedule_id: 
    :type port_schedule_id: str

    """
    return web.Response(status=200)


async def delete_network_switch_qos_rule(request: web.Request, network_id, qos_rule_id) -> web.Response:
    """Delete a quality of service rule

    Delete a quality of service rule

    :param network_id: 
    :type network_id: str
    :param qos_rule_id: 
    :type qos_rule_id: str

    """
    return web.Response(status=200)


async def delete_network_switch_routing_multicast_rendezvous_point(request: web.Request, network_id, rendezvous_point_id) -> web.Response:
    """Delete a multicast rendezvous point

    Delete a multicast rendezvous point

    :param network_id: 
    :type network_id: str
    :param rendezvous_point_id: 
    :type rendezvous_point_id: str

    """
    return web.Response(status=200)


async def delete_network_switch_stack(request: web.Request, network_id, switch_stack_id) -> web.Response:
    """Delete a stack

    Delete a stack

    :param network_id: 
    :type network_id: str
    :param switch_stack_id: 
    :type switch_stack_id: str

    """
    return web.Response(status=200)


async def delete_network_switch_stack_routing_interface(request: web.Request, network_id, switch_stack_id, interface_id) -> web.Response:
    """Delete a layer 3 interface from a switch stack

    Delete a layer 3 interface from a switch stack

    :param network_id: 
    :type network_id: str
    :param switch_stack_id: 
    :type switch_stack_id: str
    :param interface_id: 
    :type interface_id: str

    """
    return web.Response(status=200)


async def delete_network_switch_stack_routing_static_route(request: web.Request, network_id, switch_stack_id, static_route_id) -> web.Response:
    """Delete a layer 3 static route for a switch stack

    Delete a layer 3 static route for a switch stack

    :param network_id: 
    :type network_id: str
    :param switch_stack_id: 
    :type switch_stack_id: str
    :param static_route_id: 
    :type static_route_id: str

    """
    return web.Response(status=200)


async def get_device_switch_port(request: web.Request, serial, port_id) -> web.Response:
    """Return a switch port

    Return a switch port

    :param serial: 
    :type serial: str
    :param port_id: 
    :type port_id: str

    """
    return web.Response(status=200)


async def get_device_switch_ports(request: web.Request, serial) -> web.Response:
    """List the switch ports for a switch

    List the switch ports for a switch

    :param serial: 
    :type serial: str

    """
    return web.Response(status=200)


async def get_device_switch_ports_statuses(request: web.Request, serial, t0=None, timespan=None) -> web.Response:
    """Return the status for all the ports of a switch

    Return the status for all the ports of a switch

    :param serial: 
    :type serial: str
    :param t0: The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
    :type t0: str
    :param timespan: The timespan for which the information will be fetched. If specifying timespan, do not specify parameter t0. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.
    :type timespan: float

    """
    return web.Response(status=200)


async def get_device_switch_ports_statuses_packets(request: web.Request, serial, t0=None, timespan=None) -> web.Response:
    """Return the packet counters for all the ports of a switch

    Return the packet counters for all the ports of a switch

    :param serial: 
    :type serial: str
    :param t0: The beginning of the timespan for the data. The maximum lookback period is 1 day from today.
    :type t0: str
    :param timespan: The timespan for which the information will be fetched. If specifying timespan, do not specify parameter t0. The value must be in seconds and be less than or equal to 1 day. The default is 1 day.
    :type timespan: float

    """
    return web.Response(status=200)


async def get_device_switch_routing_interface(request: web.Request, serial, interface_id) -> web.Response:
    """Return a layer 3 interface for a switch

    Return a layer 3 interface for a switch

    :param serial: 
    :type serial: str
    :param interface_id: 
    :type interface_id: str

    """
    return web.Response(status=200)


async def get_device_switch_routing_interface_dhcp(request: web.Request, serial, interface_id) -> web.Response:
    """Return a layer 3 interface DHCP configuration for a switch

    Return a layer 3 interface DHCP configuration for a switch

    :param serial: 
    :type serial: str
    :param interface_id: 
    :type interface_id: str

    """
    return web.Response(status=200)


async def get_device_switch_routing_interfaces(request: web.Request, serial) -> web.Response:
    """List layer 3 interfaces for a switch

    List layer 3 interfaces for a switch. Those for a stack may be found under switch stack routing.

    :param serial: 
    :type serial: str

    """
    return web.Response(status=200)


async def get_device_switch_routing_static_route(request: web.Request, serial, static_route_id) -> web.Response:
    """Return a layer 3 static route for a switch

    Return a layer 3 static route for a switch

    :param serial: 
    :type serial: str
    :param static_route_id: 
    :type static_route_id: str

    """
    return web.Response(status=200)


async def get_device_switch_routing_static_routes(request: web.Request, serial) -> web.Response:
    """List layer 3 static routes for a switch

    List layer 3 static routes for a switch

    :param serial: 
    :type serial: str

    """
    return web.Response(status=200)


async def get_device_switch_warm_spare(request: web.Request, serial) -> web.Response:
    """Return warm spare configuration for a switch

    Return warm spare configuration for a switch

    :param serial: 
    :type serial: str

    """
    return web.Response(status=200)


async def get_network_switch_access_control_lists(request: web.Request, network_id) -> web.Response:
    """Return the access control lists for a MS network

    Return the access control lists for a MS network

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_switch_access_policies(request: web.Request, network_id) -> web.Response:
    """List the access policies for a switch network

    List the access policies for a switch network. Only returns access policies with &#39;my RADIUS server&#39; as authentication method

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_switch_access_policy(request: web.Request, network_id, access_policy_number) -> web.Response:
    """Return a specific access policy for a switch network

    Return a specific access policy for a switch network

    :param network_id: 
    :type network_id: str
    :param access_policy_number: 
    :type access_policy_number: str

    """
    return web.Response(status=200)


async def get_network_switch_alternate_management_interface(request: web.Request, network_id) -> web.Response:
    """Return the switch alternate management interface for the network

    Return the switch alternate management interface for the network

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_switch_dhcp_server_policy(request: web.Request, network_id) -> web.Response:
    """Return the DHCP server settings

    Return the DHCP server settings. Blocked/allowed servers are only applied when default policy is allow/block, respectively

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_switch_dhcp_server_policy_arp_inspection_trusted_servers(request: web.Request, network_id, per_page=None, starting_after=None, ending_before=None) -> web.Response:
    """Return the list of servers trusted by Dynamic ARP Inspection on this network

    Return the list of servers trusted by Dynamic ARP Inspection on this network. These are also known as whitelisted snoop entries

    :param network_id: 
    :type network_id: str
    :param per_page: The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
    :type per_page: int
    :param starting_after: A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type starting_after: str
    :param ending_before: A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type ending_before: str

    """
    return web.Response(status=200)


async def get_network_switch_dhcp_server_policy_arp_inspection_warnings_by_device(request: web.Request, network_id, per_page=None, starting_after=None, ending_before=None) -> web.Response:
    """Return the devices that have a Dynamic ARP Inspection warning and their warnings

    Return the devices that have a Dynamic ARP Inspection warning and their warnings

    :param network_id: 
    :type network_id: str
    :param per_page: The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
    :type per_page: int
    :param starting_after: A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type starting_after: str
    :param ending_before: A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type ending_before: str

    """
    return web.Response(status=200)


async def get_network_switch_dhcp_v4_servers_seen(request: web.Request, network_id, t0=None, timespan=None, per_page=None, starting_after=None, ending_before=None) -> web.Response:
    """Return the network&#39;s DHCPv4 servers seen within the selected timeframe (default 1 day)

    Return the network&#39;s DHCPv4 servers seen within the selected timeframe (default 1 day)

    :param network_id: 
    :type network_id: str
    :param t0: The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
    :type t0: str
    :param timespan: The timespan for which the information will be fetched. If specifying timespan, do not specify parameter t0. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.
    :type timespan: float
    :param per_page: The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
    :type per_page: int
    :param starting_after: A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type starting_after: str
    :param ending_before: A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type ending_before: str

    """
    return web.Response(status=200)


async def get_network_switch_dscp_to_cos_mappings(request: web.Request, network_id) -> web.Response:
    """Return the DSCP to CoS mappings

    Return the DSCP to CoS mappings

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_switch_link_aggregations(request: web.Request, network_id) -> web.Response:
    """List link aggregation groups

    List link aggregation groups

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_switch_mtu(request: web.Request, network_id) -> web.Response:
    """Return the MTU configuration

    Return the MTU configuration

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_switch_port_schedules(request: web.Request, network_id) -> web.Response:
    """List switch port schedules

    List switch port schedules

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_switch_qos_rule(request: web.Request, network_id, qos_rule_id) -> web.Response:
    """Return a quality of service rule

    Return a quality of service rule

    :param network_id: 
    :type network_id: str
    :param qos_rule_id: 
    :type qos_rule_id: str

    """
    return web.Response(status=200)


async def get_network_switch_qos_rules(request: web.Request, network_id) -> web.Response:
    """List quality of service rules

    List quality of service rules

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_switch_qos_rules_order(request: web.Request, network_id) -> web.Response:
    """Return the quality of service rule IDs by order in which they will be processed by the switch

    Return the quality of service rule IDs by order in which they will be processed by the switch

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_switch_routing_multicast(request: web.Request, network_id) -> web.Response:
    """Return multicast settings for a network

    Return multicast settings for a network

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_switch_routing_multicast_rendezvous_point(request: web.Request, network_id, rendezvous_point_id) -> web.Response:
    """Return a multicast rendezvous point

    Return a multicast rendezvous point

    :param network_id: 
    :type network_id: str
    :param rendezvous_point_id: 
    :type rendezvous_point_id: str

    """
    return web.Response(status=200)


async def get_network_switch_routing_multicast_rendezvous_points(request: web.Request, network_id) -> web.Response:
    """List multicast rendezvous points

    List multicast rendezvous points

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_switch_routing_ospf(request: web.Request, network_id) -> web.Response:
    """Return layer 3 OSPF routing configuration

    Return layer 3 OSPF routing configuration

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_switch_settings(request: web.Request, network_id) -> web.Response:
    """Returns the switch network settings

    Returns the switch network settings

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_switch_stack(request: web.Request, network_id, switch_stack_id) -> web.Response:
    """Show a switch stack

    Show a switch stack

    :param network_id: 
    :type network_id: str
    :param switch_stack_id: 
    :type switch_stack_id: str

    """
    return web.Response(status=200)


async def get_network_switch_stack_routing_interface(request: web.Request, network_id, switch_stack_id, interface_id) -> web.Response:
    """Return a layer 3 interface from a switch stack

    Return a layer 3 interface from a switch stack

    :param network_id: 
    :type network_id: str
    :param switch_stack_id: 
    :type switch_stack_id: str
    :param interface_id: 
    :type interface_id: str

    """
    return web.Response(status=200)


async def get_network_switch_stack_routing_interface_dhcp(request: web.Request, network_id, switch_stack_id, interface_id) -> web.Response:
    """Return a layer 3 interface DHCP configuration for a switch stack

    Return a layer 3 interface DHCP configuration for a switch stack

    :param network_id: 
    :type network_id: str
    :param switch_stack_id: 
    :type switch_stack_id: str
    :param interface_id: 
    :type interface_id: str

    """
    return web.Response(status=200)


async def get_network_switch_stack_routing_interfaces(request: web.Request, network_id, switch_stack_id) -> web.Response:
    """List layer 3 interfaces for a switch stack

    List layer 3 interfaces for a switch stack

    :param network_id: 
    :type network_id: str
    :param switch_stack_id: 
    :type switch_stack_id: str

    """
    return web.Response(status=200)


async def get_network_switch_stack_routing_static_route(request: web.Request, network_id, switch_stack_id, static_route_id) -> web.Response:
    """Return a layer 3 static route for a switch stack

    Return a layer 3 static route for a switch stack

    :param network_id: 
    :type network_id: str
    :param switch_stack_id: 
    :type switch_stack_id: str
    :param static_route_id: 
    :type static_route_id: str

    """
    return web.Response(status=200)


async def get_network_switch_stack_routing_static_routes(request: web.Request, network_id, switch_stack_id) -> web.Response:
    """List layer 3 static routes for a switch stack

    List layer 3 static routes for a switch stack

    :param network_id: 
    :type network_id: str
    :param switch_stack_id: 
    :type switch_stack_id: str

    """
    return web.Response(status=200)


async def get_network_switch_stacks(request: web.Request, network_id) -> web.Response:
    """List the switch stacks in a network

    List the switch stacks in a network

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_switch_storm_control(request: web.Request, network_id) -> web.Response:
    """Return the storm control configuration for a switch network

    Return the storm control configuration for a switch network

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_switch_stp(request: web.Request, network_id) -> web.Response:
    """Returns STP settings

    Returns STP settings

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_organization_config_template_switch_profile_port(request: web.Request, organization_id, config_template_id, profile_id, port_id) -> web.Response:
    """Return a switch profile port

    Return a switch profile port

    :param organization_id: 
    :type organization_id: str
    :param config_template_id: 
    :type config_template_id: str
    :param profile_id: 
    :type profile_id: str
    :param port_id: 
    :type port_id: str

    """
    return web.Response(status=200)


async def get_organization_config_template_switch_profile_ports(request: web.Request, organization_id, config_template_id, profile_id) -> web.Response:
    """Return all the ports of a switch profile

    Return all the ports of a switch profile

    :param organization_id: 
    :type organization_id: str
    :param config_template_id: 
    :type config_template_id: str
    :param profile_id: 
    :type profile_id: str

    """
    return web.Response(status=200)


async def get_organization_config_template_switch_profiles(request: web.Request, organization_id, config_template_id) -> web.Response:
    """List the switch profiles for your switch template configuration

    List the switch profiles for your switch template configuration

    :param organization_id: 
    :type organization_id: str
    :param config_template_id: 
    :type config_template_id: str

    """
    return web.Response(status=200)


async def get_organization_switch_ports_by_switch(request: web.Request, organization_id, per_page=None, starting_after=None, ending_before=None, network_ids=None, port_profile_ids=None, name=None, mac=None, macs=None, serial=None, serials=None, configuration_updated_after=None) -> web.Response:
    """List the switchports in an organization by switch

    List the switchports in an organization by switch

    :param organization_id: 
    :type organization_id: str
    :param per_page: The number of entries per page returned. Acceptable range is 3 - 50. Default is 50.
    :type per_page: int
    :param starting_after: A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type starting_after: str
    :param ending_before: A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type ending_before: str
    :param network_ids: Optional parameter to filter switchports by network.
    :type network_ids: List[str]
    :param port_profile_ids: Optional parameter to filter switchports belonging to the specified switchport profiles.
    :type port_profile_ids: List[str]
    :param name: Optional parameter to filter switchports belonging to switches by name. All returned switches will have a name that contains the search term or is an exact match.
    :type name: str
    :param mac: Optional parameter to filter switchports belonging to switches by MAC address. All returned switches will have a MAC address that contains the search term or is an exact match.
    :type mac: str
    :param macs: Optional parameter to filter switchports by one or more MAC addresses belonging to devices. All switchports returned belong to MAC addresses of switches that are an exact match.
    :type macs: List[str]
    :param serial: Optional parameter to filter switchports belonging to switches by serial number. All returned switches will have a serial number that contains the search term or is an exact match.
    :type serial: str
    :param serials: Optional parameter to filter switchports belonging to switches with one or more serial numbers. All switchports returned belong to serial numbers of switches that are an exact match.
    :type serials: List[str]
    :param configuration_updated_after: Optional parameter to filter results by switches where the configuration has been updated after the given timestamp.
    :type configuration_updated_after: str

    """
    return web.Response(status=200)


async def remove_network_switch_stack(request: web.Request, network_id, switch_stack_id, body) -> web.Response:
    """Remove a switch from a stack

    Remove a switch from a stack

    :param network_id: 
    :type network_id: str
    :param switch_stack_id: 
    :type switch_stack_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = RemoveNetworkSwitchStackRequest.from_dict(body)
    return web.Response(status=200)


async def update_device_switch_port(request: web.Request, serial, port_id, body=None) -> web.Response:
    """Update a switch port

    Update a switch port

    :param serial: 
    :type serial: str
    :param port_id: 
    :type port_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateDeviceSwitchPortRequest.from_dict(body)
    return web.Response(status=200)


async def update_device_switch_routing_interface(request: web.Request, serial, interface_id, body=None) -> web.Response:
    """Update a layer 3 interface for a switch

    Update a layer 3 interface for a switch

    :param serial: 
    :type serial: str
    :param interface_id: 
    :type interface_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateDeviceSwitchRoutingInterfaceRequest.from_dict(body)
    return web.Response(status=200)


async def update_device_switch_routing_interface_dhcp(request: web.Request, serial, interface_id, body=None) -> web.Response:
    """Update a layer 3 interface DHCP configuration for a switch

    Update a layer 3 interface DHCP configuration for a switch

    :param serial: 
    :type serial: str
    :param interface_id: 
    :type interface_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateDeviceSwitchRoutingInterfaceDhcpRequest.from_dict(body)
    return web.Response(status=200)


async def update_device_switch_routing_static_route(request: web.Request, serial, static_route_id, body=None) -> web.Response:
    """Update a layer 3 static route for a switch

    Update a layer 3 static route for a switch

    :param serial: 
    :type serial: str
    :param static_route_id: 
    :type static_route_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateDeviceSwitchRoutingStaticRouteRequest.from_dict(body)
    return web.Response(status=200)


async def update_device_switch_warm_spare(request: web.Request, serial, body) -> web.Response:
    """Update warm spare configuration for a switch

    Update warm spare configuration for a switch. The spare will use the same L3 configuration as the primary. Note that this will irreversibly destroy any existing L3 configuration on the spare.

    :param serial: 
    :type serial: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateDeviceSwitchWarmSpareRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_switch_access_control_lists(request: web.Request, network_id, body) -> web.Response:
    """Update the access control lists for a MS network

    Update the access control lists for a MS network

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkSwitchAccessControlListsRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_switch_access_policy(request: web.Request, network_id, access_policy_number, body=None) -> web.Response:
    """Update an access policy for a switch network

    Update an access policy for a switch network. If you would like to enable Meraki Authentication, set radiusServers to empty array.

    :param network_id: 
    :type network_id: str
    :param access_policy_number: 
    :type access_policy_number: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkSwitchAccessPolicyRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_switch_alternate_management_interface(request: web.Request, network_id, body=None) -> web.Response:
    """Update the switch alternate management interface for the network

    Update the switch alternate management interface for the network

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkSwitchAlternateManagementInterfaceRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_switch_dhcp_server_policy(request: web.Request, network_id, body=None) -> web.Response:
    """Update the DHCP server settings

    Update the DHCP server settings. Blocked/allowed servers are only applied when default policy is allow/block, respectively

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkSwitchDhcpServerPolicyRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_switch_dhcp_server_policy_arp_inspection_trusted_server(request: web.Request, network_id, trusted_server_id, body=None) -> web.Response:
    """Update a server that is trusted by Dynamic ARP Inspection on this network

    Update a server that is trusted by Dynamic ARP Inspection on this network

    :param network_id: 
    :type network_id: str
    :param trusted_server_id: 
    :type trusted_server_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkSwitchDhcpServerPolicyArpInspectionTrustedServerRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_switch_dscp_to_cos_mappings(request: web.Request, network_id, body) -> web.Response:
    """Update the DSCP to CoS mappings

    Update the DSCP to CoS mappings

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkSwitchDscpToCosMappingsRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_switch_link_aggregation(request: web.Request, network_id, link_aggregation_id, body=None) -> web.Response:
    """Update a link aggregation group

    Update a link aggregation group

    :param network_id: 
    :type network_id: str
    :param link_aggregation_id: 
    :type link_aggregation_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkSwitchLinkAggregationRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_switch_mtu(request: web.Request, network_id, body=None) -> web.Response:
    """Update the MTU configuration

    Update the MTU configuration

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkSwitchMtuRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_switch_port_schedule(request: web.Request, network_id, port_schedule_id, body=None) -> web.Response:
    """Update a switch port schedule

    Update a switch port schedule

    :param network_id: 
    :type network_id: str
    :param port_schedule_id: 
    :type port_schedule_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkSwitchPortScheduleRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_switch_qos_rule(request: web.Request, network_id, qos_rule_id, body=None) -> web.Response:
    """Update a quality of service rule

    Update a quality of service rule

    :param network_id: 
    :type network_id: str
    :param qos_rule_id: 
    :type qos_rule_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkSwitchQosRuleRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_switch_qos_rules_order(request: web.Request, network_id, body) -> web.Response:
    """Update the order in which the rules should be processed by the switch

    Update the order in which the rules should be processed by the switch

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkSwitchQosRulesOrderRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_switch_routing_multicast(request: web.Request, network_id, body=None) -> web.Response:
    """Update multicast settings for a network

    Update multicast settings for a network

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkSwitchRoutingMulticastRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_switch_routing_multicast_rendezvous_point(request: web.Request, network_id, rendezvous_point_id, body) -> web.Response:
    """Update a multicast rendezvous point

    Update a multicast rendezvous point

    :param network_id: 
    :type network_id: str
    :param rendezvous_point_id: 
    :type rendezvous_point_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkSwitchRoutingMulticastRendezvousPointRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_switch_routing_ospf(request: web.Request, network_id, body=None) -> web.Response:
    """Update layer 3 OSPF routing configuration

    Update layer 3 OSPF routing configuration

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkSwitchRoutingOspfRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_switch_settings(request: web.Request, network_id, body=None) -> web.Response:
    """Update switch network settings

    Update switch network settings

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkSwitchSettingsRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_switch_stack_routing_interface(request: web.Request, network_id, switch_stack_id, interface_id, body=None) -> web.Response:
    """Update a layer 3 interface for a switch stack

    Update a layer 3 interface for a switch stack

    :param network_id: 
    :type network_id: str
    :param switch_stack_id: 
    :type switch_stack_id: str
    :param interface_id: 
    :type interface_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkSwitchStackRoutingInterfaceRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_switch_stack_routing_interface_dhcp(request: web.Request, network_id, switch_stack_id, interface_id, body=None) -> web.Response:
    """Update a layer 3 interface DHCP configuration for a switch stack

    Update a layer 3 interface DHCP configuration for a switch stack

    :param network_id: 
    :type network_id: str
    :param switch_stack_id: 
    :type switch_stack_id: str
    :param interface_id: 
    :type interface_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkSwitchStackRoutingInterfaceDhcpRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_switch_stack_routing_static_route(request: web.Request, network_id, switch_stack_id, static_route_id, body=None) -> web.Response:
    """Update a layer 3 static route for a switch stack

    Update a layer 3 static route for a switch stack

    :param network_id: 
    :type network_id: str
    :param switch_stack_id: 
    :type switch_stack_id: str
    :param static_route_id: 
    :type static_route_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateDeviceSwitchRoutingStaticRouteRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_switch_storm_control(request: web.Request, network_id, body=None) -> web.Response:
    """Update the storm control configuration for a switch network

    Update the storm control configuration for a switch network

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkSwitchStormControlRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_switch_stp(request: web.Request, network_id, body=None) -> web.Response:
    """Updates STP settings

    Updates STP settings

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkSwitchStpRequest.from_dict(body)
    return web.Response(status=200)


async def update_organization_config_template_switch_profile_port(request: web.Request, organization_id, config_template_id, profile_id, port_id, body=None) -> web.Response:
    """Update a switch profile port

    Update a switch profile port

    :param organization_id: 
    :type organization_id: str
    :param config_template_id: 
    :type config_template_id: str
    :param profile_id: 
    :type profile_id: str
    :param port_id: 
    :type port_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateOrganizationConfigTemplateSwitchProfilePortRequest.from_dict(body)
    return web.Response(status=200)
