# coding: utf-8

import pytest
import json
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


pytestmark = pytest.mark.asyncio

async def test_add_network_switch_stack(client):
    """Test case for add_network_switch_stack

    Add a switch to a stack
    """
    body = openapi_server.AddNetworkSwitchStackRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/networks/{network_id}/switch/stacks/{switch_stack_id}/add'.format(network_id='network_id_example', switch_stack_id='switch_stack_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_clone_organization_switch_devices(client):
    """Test case for clone_organization_switch_devices

    Clone port-level and some switch-level configuration settings from a source switch to one or more target switches
    """
    body = openapi_server.CloneOrganizationSwitchDevicesRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/organizations/{organization_id}/switch/devices/clone'.format(organization_id='organization_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_device_switch_routing_interface(client):
    """Test case for create_device_switch_routing_interface

    Create a layer 3 interface for a switch
    """
    body = openapi_server.CreateDeviceSwitchRoutingInterfaceRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/devices/{serial}/switch/routing/interfaces'.format(serial='serial_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_device_switch_routing_static_route(client):
    """Test case for create_device_switch_routing_static_route

    Create a layer 3 static route for a switch
    """
    body = openapi_server.CreateDeviceSwitchRoutingStaticRouteRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/devices/{serial}/switch/routing/staticRoutes'.format(serial='serial_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_network_switch_access_policy(client):
    """Test case for create_network_switch_access_policy

    Create an access policy for a switch network
    """
    body = openapi_server.CreateNetworkSwitchAccessPolicyRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/networks/{network_id}/switch/accessPolicies'.format(network_id='network_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_network_switch_dhcp_server_policy_arp_inspection_trusted_server(client):
    """Test case for create_network_switch_dhcp_server_policy_arp_inspection_trusted_server

    Add a server to be trusted by Dynamic ARP Inspection on this network
    """
    body = openapi_server.CreateNetworkSwitchDhcpServerPolicyArpInspectionTrustedServerRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/networks/{network_id}/switch/dhcpServerPolicy/arpInspection/trustedServers'.format(network_id='network_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_network_switch_link_aggregation(client):
    """Test case for create_network_switch_link_aggregation

    Create a link aggregation group
    """
    body = openapi_server.CreateNetworkSwitchLinkAggregationRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/networks/{network_id}/switch/linkAggregations'.format(network_id='network_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_network_switch_port_schedule(client):
    """Test case for create_network_switch_port_schedule

    Add a switch port schedule
    """
    body = openapi_server.CreateNetworkSwitchPortScheduleRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/networks/{network_id}/switch/portSchedules'.format(network_id='network_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_network_switch_qos_rule(client):
    """Test case for create_network_switch_qos_rule

    Add a quality of service rule
    """
    body = openapi_server.CreateNetworkSwitchQosRuleRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/networks/{network_id}/switch/qosRules'.format(network_id='network_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_network_switch_routing_multicast_rendezvous_point(client):
    """Test case for create_network_switch_routing_multicast_rendezvous_point

    Create a multicast rendezvous point
    """
    body = openapi_server.CreateNetworkSwitchRoutingMulticastRendezvousPointRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/networks/{network_id}/switch/routing/multicast/rendezvousPoints'.format(network_id='network_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_network_switch_stack(client):
    """Test case for create_network_switch_stack

    Create a stack
    """
    body = openapi_server.CreateNetworkSwitchStackRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/networks/{network_id}/switch/stacks'.format(network_id='network_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_network_switch_stack_routing_interface(client):
    """Test case for create_network_switch_stack_routing_interface

    Create a layer 3 interface for a switch stack
    """
    body = openapi_server.CreateNetworkSwitchStackRoutingInterfaceRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/networks/{network_id}/switch/stacks/{switch_stack_id}/routing/interfaces'.format(network_id='network_id_example', switch_stack_id='switch_stack_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_network_switch_stack_routing_static_route(client):
    """Test case for create_network_switch_stack_routing_static_route

    Create a layer 3 static route for a switch stack
    """
    body = openapi_server.CreateDeviceSwitchRoutingStaticRouteRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/networks/{network_id}/switch/stacks/{switch_stack_id}/routing/staticRoutes'.format(network_id='network_id_example', switch_stack_id='switch_stack_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cycle_device_switch_ports(client):
    """Test case for cycle_device_switch_ports

    Cycle a set of switch ports
    """
    body = openapi_server.CycleDeviceSwitchPortsRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/devices/{serial}/switch/ports/cycle'.format(serial='serial_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_device_switch_routing_interface(client):
    """Test case for delete_device_switch_routing_interface

    Delete a layer 3 interface from the switch
    """
    headers = { 
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/devices/{serial}/switch/routing/interfaces/{interface_id}'.format(serial='serial_example', interface_id='interface_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_device_switch_routing_static_route(client):
    """Test case for delete_device_switch_routing_static_route

    Delete a layer 3 static route for a switch
    """
    headers = { 
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/devices/{serial}/switch/routing/staticRoutes/{static_route_id}'.format(serial='serial_example', static_route_id='static_route_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_network_switch_access_policy(client):
    """Test case for delete_network_switch_access_policy

    Delete an access policy for a switch network
    """
    headers = { 
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/networks/{network_id}/switch/accessPolicies/{access_policy_number}'.format(network_id='network_id_example', access_policy_number='access_policy_number_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_network_switch_dhcp_server_policy_arp_inspection_trusted_server(client):
    """Test case for delete_network_switch_dhcp_server_policy_arp_inspection_trusted_server

    Remove a server from being trusted by Dynamic ARP Inspection on this network
    """
    headers = { 
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/networks/{network_id}/switch/dhcpServerPolicy/arpInspection/trustedServers/{trusted_server_id}'.format(network_id='network_id_example', trusted_server_id='trusted_server_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_network_switch_link_aggregation(client):
    """Test case for delete_network_switch_link_aggregation

    Split a link aggregation group into separate ports
    """
    headers = { 
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/networks/{network_id}/switch/linkAggregations/{link_aggregation_id}'.format(network_id='network_id_example', link_aggregation_id='link_aggregation_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_network_switch_port_schedule(client):
    """Test case for delete_network_switch_port_schedule

    Delete a switch port schedule
    """
    headers = { 
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/networks/{network_id}/switch/portSchedules/{port_schedule_id}'.format(network_id='network_id_example', port_schedule_id='port_schedule_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_network_switch_qos_rule(client):
    """Test case for delete_network_switch_qos_rule

    Delete a quality of service rule
    """
    headers = { 
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/networks/{network_id}/switch/qosRules/{qos_rule_id}'.format(network_id='network_id_example', qos_rule_id='qos_rule_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_network_switch_routing_multicast_rendezvous_point(client):
    """Test case for delete_network_switch_routing_multicast_rendezvous_point

    Delete a multicast rendezvous point
    """
    headers = { 
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/networks/{network_id}/switch/routing/multicast/rendezvousPoints/{rendezvous_point_id}'.format(network_id='network_id_example', rendezvous_point_id='rendezvous_point_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_network_switch_stack(client):
    """Test case for delete_network_switch_stack

    Delete a stack
    """
    headers = { 
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/networks/{network_id}/switch/stacks/{switch_stack_id}'.format(network_id='network_id_example', switch_stack_id='switch_stack_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_network_switch_stack_routing_interface(client):
    """Test case for delete_network_switch_stack_routing_interface

    Delete a layer 3 interface from a switch stack
    """
    headers = { 
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/networks/{network_id}/switch/stacks/{switch_stack_id}/routing/interfaces/{interface_id}'.format(network_id='network_id_example', switch_stack_id='switch_stack_id_example', interface_id='interface_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_network_switch_stack_routing_static_route(client):
    """Test case for delete_network_switch_stack_routing_static_route

    Delete a layer 3 static route for a switch stack
    """
    headers = { 
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/networks/{network_id}/switch/stacks/{switch_stack_id}/routing/staticRoutes/{static_route_id}'.format(network_id='network_id_example', switch_stack_id='switch_stack_id_example', static_route_id='static_route_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_device_switch_port(client):
    """Test case for get_device_switch_port

    Return a switch port
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/devices/{serial}/switch/ports/{port_id}'.format(serial='serial_example', port_id='port_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_device_switch_ports(client):
    """Test case for get_device_switch_ports

    List the switch ports for a switch
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/devices/{serial}/switch/ports'.format(serial='serial_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_device_switch_ports_statuses(client):
    """Test case for get_device_switch_ports_statuses

    Return the status for all the ports of a switch
    """
    params = [('t0', 't0_example'),
                    ('timespan', 3.4)]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/devices/{serial}/switch/ports/statuses'.format(serial='serial_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_device_switch_ports_statuses_packets(client):
    """Test case for get_device_switch_ports_statuses_packets

    Return the packet counters for all the ports of a switch
    """
    params = [('t0', 't0_example'),
                    ('timespan', 3.4)]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/devices/{serial}/switch/ports/statuses/packets'.format(serial='serial_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_device_switch_routing_interface(client):
    """Test case for get_device_switch_routing_interface

    Return a layer 3 interface for a switch
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/devices/{serial}/switch/routing/interfaces/{interface_id}'.format(serial='serial_example', interface_id='interface_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_device_switch_routing_interface_dhcp(client):
    """Test case for get_device_switch_routing_interface_dhcp

    Return a layer 3 interface DHCP configuration for a switch
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/devices/{serial}/switch/routing/interfaces/{interface_id}/dhcp'.format(serial='serial_example', interface_id='interface_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_device_switch_routing_interfaces(client):
    """Test case for get_device_switch_routing_interfaces

    List layer 3 interfaces for a switch
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/devices/{serial}/switch/routing/interfaces'.format(serial='serial_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_device_switch_routing_static_route(client):
    """Test case for get_device_switch_routing_static_route

    Return a layer 3 static route for a switch
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/devices/{serial}/switch/routing/staticRoutes/{static_route_id}'.format(serial='serial_example', static_route_id='static_route_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_device_switch_routing_static_routes(client):
    """Test case for get_device_switch_routing_static_routes

    List layer 3 static routes for a switch
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/devices/{serial}/switch/routing/staticRoutes'.format(serial='serial_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_device_switch_warm_spare(client):
    """Test case for get_device_switch_warm_spare

    Return warm spare configuration for a switch
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/devices/{serial}/switch/warmSpare'.format(serial='serial_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_switch_access_control_lists(client):
    """Test case for get_network_switch_access_control_lists

    Return the access control lists for a MS network
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/switch/accessControlLists'.format(network_id='network_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_switch_access_policies(client):
    """Test case for get_network_switch_access_policies

    List the access policies for a switch network
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/switch/accessPolicies'.format(network_id='network_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_switch_access_policy(client):
    """Test case for get_network_switch_access_policy

    Return a specific access policy for a switch network
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/switch/accessPolicies/{access_policy_number}'.format(network_id='network_id_example', access_policy_number='access_policy_number_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_switch_alternate_management_interface(client):
    """Test case for get_network_switch_alternate_management_interface

    Return the switch alternate management interface for the network
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/switch/alternateManagementInterface'.format(network_id='network_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_switch_dhcp_server_policy(client):
    """Test case for get_network_switch_dhcp_server_policy

    Return the DHCP server settings
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/switch/dhcpServerPolicy'.format(network_id='network_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_switch_dhcp_server_policy_arp_inspection_trusted_servers(client):
    """Test case for get_network_switch_dhcp_server_policy_arp_inspection_trusted_servers

    Return the list of servers trusted by Dynamic ARP Inspection on this network
    """
    params = [('perPage', 56),
                    ('startingAfter', 'starting_after_example'),
                    ('endingBefore', 'ending_before_example')]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/switch/dhcpServerPolicy/arpInspection/trustedServers'.format(network_id='network_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_switch_dhcp_server_policy_arp_inspection_warnings_by_device(client):
    """Test case for get_network_switch_dhcp_server_policy_arp_inspection_warnings_by_device

    Return the devices that have a Dynamic ARP Inspection warning and their warnings
    """
    params = [('perPage', 56),
                    ('startingAfter', 'starting_after_example'),
                    ('endingBefore', 'ending_before_example')]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/switch/dhcpServerPolicy/arpInspection/warnings/byDevice'.format(network_id='network_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_switch_dhcp_v4_servers_seen(client):
    """Test case for get_network_switch_dhcp_v4_servers_seen

    Return the network's DHCPv4 servers seen within the selected timeframe (default 1 day)
    """
    params = [('t0', 't0_example'),
                    ('timespan', 3.4),
                    ('perPage', 56),
                    ('startingAfter', 'starting_after_example'),
                    ('endingBefore', 'ending_before_example')]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/switch/dhcp/v4/servers/seen'.format(network_id='network_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_switch_dscp_to_cos_mappings(client):
    """Test case for get_network_switch_dscp_to_cos_mappings

    Return the DSCP to CoS mappings
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/switch/dscpToCosMappings'.format(network_id='network_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_switch_link_aggregations(client):
    """Test case for get_network_switch_link_aggregations

    List link aggregation groups
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/switch/linkAggregations'.format(network_id='network_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_switch_mtu(client):
    """Test case for get_network_switch_mtu

    Return the MTU configuration
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/switch/mtu'.format(network_id='network_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_switch_port_schedules(client):
    """Test case for get_network_switch_port_schedules

    List switch port schedules
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/switch/portSchedules'.format(network_id='network_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_switch_qos_rule(client):
    """Test case for get_network_switch_qos_rule

    Return a quality of service rule
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/switch/qosRules/{qos_rule_id}'.format(network_id='network_id_example', qos_rule_id='qos_rule_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_switch_qos_rules(client):
    """Test case for get_network_switch_qos_rules

    List quality of service rules
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/switch/qosRules'.format(network_id='network_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_switch_qos_rules_order(client):
    """Test case for get_network_switch_qos_rules_order

    Return the quality of service rule IDs by order in which they will be processed by the switch
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/switch/qosRules/order'.format(network_id='network_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_switch_routing_multicast(client):
    """Test case for get_network_switch_routing_multicast

    Return multicast settings for a network
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/switch/routing/multicast'.format(network_id='network_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_switch_routing_multicast_rendezvous_point(client):
    """Test case for get_network_switch_routing_multicast_rendezvous_point

    Return a multicast rendezvous point
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/switch/routing/multicast/rendezvousPoints/{rendezvous_point_id}'.format(network_id='network_id_example', rendezvous_point_id='rendezvous_point_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_switch_routing_multicast_rendezvous_points(client):
    """Test case for get_network_switch_routing_multicast_rendezvous_points

    List multicast rendezvous points
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/switch/routing/multicast/rendezvousPoints'.format(network_id='network_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_switch_routing_ospf(client):
    """Test case for get_network_switch_routing_ospf

    Return layer 3 OSPF routing configuration
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/switch/routing/ospf'.format(network_id='network_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_switch_settings(client):
    """Test case for get_network_switch_settings

    Returns the switch network settings
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/switch/settings'.format(network_id='network_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_switch_stack(client):
    """Test case for get_network_switch_stack

    Show a switch stack
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/switch/stacks/{switch_stack_id}'.format(network_id='network_id_example', switch_stack_id='switch_stack_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_switch_stack_routing_interface(client):
    """Test case for get_network_switch_stack_routing_interface

    Return a layer 3 interface from a switch stack
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/switch/stacks/{switch_stack_id}/routing/interfaces/{interface_id}'.format(network_id='network_id_example', switch_stack_id='switch_stack_id_example', interface_id='interface_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_switch_stack_routing_interface_dhcp(client):
    """Test case for get_network_switch_stack_routing_interface_dhcp

    Return a layer 3 interface DHCP configuration for a switch stack
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/switch/stacks/{switch_stack_id}/routing/interfaces/{interface_id}/dhcp'.format(network_id='network_id_example', switch_stack_id='switch_stack_id_example', interface_id='interface_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_switch_stack_routing_interfaces(client):
    """Test case for get_network_switch_stack_routing_interfaces

    List layer 3 interfaces for a switch stack
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/switch/stacks/{switch_stack_id}/routing/interfaces'.format(network_id='network_id_example', switch_stack_id='switch_stack_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_switch_stack_routing_static_route(client):
    """Test case for get_network_switch_stack_routing_static_route

    Return a layer 3 static route for a switch stack
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/switch/stacks/{switch_stack_id}/routing/staticRoutes/{static_route_id}'.format(network_id='network_id_example', switch_stack_id='switch_stack_id_example', static_route_id='static_route_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_switch_stack_routing_static_routes(client):
    """Test case for get_network_switch_stack_routing_static_routes

    List layer 3 static routes for a switch stack
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/switch/stacks/{switch_stack_id}/routing/staticRoutes'.format(network_id='network_id_example', switch_stack_id='switch_stack_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_switch_stacks(client):
    """Test case for get_network_switch_stacks

    List the switch stacks in a network
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/switch/stacks'.format(network_id='network_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_switch_storm_control(client):
    """Test case for get_network_switch_storm_control

    Return the storm control configuration for a switch network
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/switch/stormControl'.format(network_id='network_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_switch_stp(client):
    """Test case for get_network_switch_stp

    Returns STP settings
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/switch/stp'.format(network_id='network_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_config_template_switch_profile_port(client):
    """Test case for get_organization_config_template_switch_profile_port

    Return a switch profile port
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/configTemplates/{config_template_id}/switch/profiles/{profile_id}/ports/{port_id}'.format(organization_id='organization_id_example', config_template_id='config_template_id_example', profile_id='profile_id_example', port_id='port_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_config_template_switch_profile_ports(client):
    """Test case for get_organization_config_template_switch_profile_ports

    Return all the ports of a switch profile
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/configTemplates/{config_template_id}/switch/profiles/{profile_id}/ports'.format(organization_id='organization_id_example', config_template_id='config_template_id_example', profile_id='profile_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_config_template_switch_profiles(client):
    """Test case for get_organization_config_template_switch_profiles

    List the switch profiles for your switch template configuration
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/configTemplates/{config_template_id}/switch/profiles'.format(organization_id='organization_id_example', config_template_id='config_template_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_switch_ports_by_switch(client):
    """Test case for get_organization_switch_ports_by_switch

    List the switchports in an organization by switch
    """
    params = [('perPage', 56),
                    ('startingAfter', 'starting_after_example'),
                    ('endingBefore', 'ending_before_example'),
                    ('networkIds', ['network_ids_example']),
                    ('portProfileIds', ['port_profile_ids_example']),
                    ('name', 'name_example'),
                    ('mac', 'mac_example'),
                    ('macs', ['macs_example']),
                    ('serial', 'serial_example'),
                    ('serials', ['serials_example']),
                    ('configurationUpdatedAfter', 'configuration_updated_after_example')]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/switch/ports/bySwitch'.format(organization_id='organization_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_network_switch_stack(client):
    """Test case for remove_network_switch_stack

    Remove a switch from a stack
    """
    body = openapi_server.RemoveNetworkSwitchStackRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/networks/{network_id}/switch/stacks/{switch_stack_id}/remove'.format(network_id='network_id_example', switch_stack_id='switch_stack_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_device_switch_port(client):
    """Test case for update_device_switch_port

    Update a switch port
    """
    body = openapi_server.UpdateDeviceSwitchPortRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/devices/{serial}/switch/ports/{port_id}'.format(serial='serial_example', port_id='port_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_device_switch_routing_interface(client):
    """Test case for update_device_switch_routing_interface

    Update a layer 3 interface for a switch
    """
    body = openapi_server.CreateDeviceSwitchRoutingInterfaceRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/devices/{serial}/switch/routing/interfaces/{interface_id}'.format(serial='serial_example', interface_id='interface_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_device_switch_routing_interface_dhcp(client):
    """Test case for update_device_switch_routing_interface_dhcp

    Update a layer 3 interface DHCP configuration for a switch
    """
    body = openapi_server.UpdateDeviceSwitchRoutingInterfaceDhcpRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/devices/{serial}/switch/routing/interfaces/{interface_id}/dhcp'.format(serial='serial_example', interface_id='interface_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_device_switch_routing_static_route(client):
    """Test case for update_device_switch_routing_static_route

    Update a layer 3 static route for a switch
    """
    body = openapi_server.UpdateDeviceSwitchRoutingStaticRouteRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/devices/{serial}/switch/routing/staticRoutes/{static_route_id}'.format(serial='serial_example', static_route_id='static_route_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_device_switch_warm_spare(client):
    """Test case for update_device_switch_warm_spare

    Update warm spare configuration for a switch
    """
    body = openapi_server.UpdateDeviceSwitchWarmSpareRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/devices/{serial}/switch/warmSpare'.format(serial='serial_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_network_switch_access_control_lists(client):
    """Test case for update_network_switch_access_control_lists

    Update the access control lists for a MS network
    """
    body = openapi_server.UpdateNetworkSwitchAccessControlListsRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/networks/{network_id}/switch/accessControlLists'.format(network_id='network_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_network_switch_access_policy(client):
    """Test case for update_network_switch_access_policy

    Update an access policy for a switch network
    """
    body = openapi_server.UpdateNetworkSwitchAccessPolicyRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/networks/{network_id}/switch/accessPolicies/{access_policy_number}'.format(network_id='network_id_example', access_policy_number='access_policy_number_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_network_switch_alternate_management_interface(client):
    """Test case for update_network_switch_alternate_management_interface

    Update the switch alternate management interface for the network
    """
    body = openapi_server.UpdateNetworkSwitchAlternateManagementInterfaceRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/networks/{network_id}/switch/alternateManagementInterface'.format(network_id='network_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_network_switch_dhcp_server_policy(client):
    """Test case for update_network_switch_dhcp_server_policy

    Update the DHCP server settings
    """
    body = openapi_server.UpdateNetworkSwitchDhcpServerPolicyRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/networks/{network_id}/switch/dhcpServerPolicy'.format(network_id='network_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_network_switch_dhcp_server_policy_arp_inspection_trusted_server(client):
    """Test case for update_network_switch_dhcp_server_policy_arp_inspection_trusted_server

    Update a server that is trusted by Dynamic ARP Inspection on this network
    """
    body = openapi_server.UpdateNetworkSwitchDhcpServerPolicyArpInspectionTrustedServerRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/networks/{network_id}/switch/dhcpServerPolicy/arpInspection/trustedServers/{trusted_server_id}'.format(network_id='network_id_example', trusted_server_id='trusted_server_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_network_switch_dscp_to_cos_mappings(client):
    """Test case for update_network_switch_dscp_to_cos_mappings

    Update the DSCP to CoS mappings
    """
    body = openapi_server.UpdateNetworkSwitchDscpToCosMappingsRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/networks/{network_id}/switch/dscpToCosMappings'.format(network_id='network_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_network_switch_link_aggregation(client):
    """Test case for update_network_switch_link_aggregation

    Update a link aggregation group
    """
    body = openapi_server.UpdateNetworkSwitchLinkAggregationRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/networks/{network_id}/switch/linkAggregations/{link_aggregation_id}'.format(network_id='network_id_example', link_aggregation_id='link_aggregation_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_network_switch_mtu(client):
    """Test case for update_network_switch_mtu

    Update the MTU configuration
    """
    body = openapi_server.UpdateNetworkSwitchMtuRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/networks/{network_id}/switch/mtu'.format(network_id='network_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_network_switch_port_schedule(client):
    """Test case for update_network_switch_port_schedule

    Update a switch port schedule
    """
    body = openapi_server.UpdateNetworkSwitchPortScheduleRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/networks/{network_id}/switch/portSchedules/{port_schedule_id}'.format(network_id='network_id_example', port_schedule_id='port_schedule_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_network_switch_qos_rule(client):
    """Test case for update_network_switch_qos_rule

    Update a quality of service rule
    """
    body = openapi_server.UpdateNetworkSwitchQosRuleRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/networks/{network_id}/switch/qosRules/{qos_rule_id}'.format(network_id='network_id_example', qos_rule_id='qos_rule_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_network_switch_qos_rules_order(client):
    """Test case for update_network_switch_qos_rules_order

    Update the order in which the rules should be processed by the switch
    """
    body = openapi_server.UpdateNetworkSwitchQosRulesOrderRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/networks/{network_id}/switch/qosRules/order'.format(network_id='network_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_network_switch_routing_multicast(client):
    """Test case for update_network_switch_routing_multicast

    Update multicast settings for a network
    """
    body = openapi_server.UpdateNetworkSwitchRoutingMulticastRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/networks/{network_id}/switch/routing/multicast'.format(network_id='network_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_network_switch_routing_multicast_rendezvous_point(client):
    """Test case for update_network_switch_routing_multicast_rendezvous_point

    Update a multicast rendezvous point
    """
    body = openapi_server.UpdateNetworkSwitchRoutingMulticastRendezvousPointRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/networks/{network_id}/switch/routing/multicast/rendezvousPoints/{rendezvous_point_id}'.format(network_id='network_id_example', rendezvous_point_id='rendezvous_point_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_network_switch_routing_ospf(client):
    """Test case for update_network_switch_routing_ospf

    Update layer 3 OSPF routing configuration
    """
    body = openapi_server.UpdateNetworkSwitchRoutingOspfRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/networks/{network_id}/switch/routing/ospf'.format(network_id='network_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_network_switch_settings(client):
    """Test case for update_network_switch_settings

    Update switch network settings
    """
    body = openapi_server.UpdateNetworkSwitchSettingsRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/networks/{network_id}/switch/settings'.format(network_id='network_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_network_switch_stack_routing_interface(client):
    """Test case for update_network_switch_stack_routing_interface

    Update a layer 3 interface for a switch stack
    """
    body = openapi_server.UpdateNetworkSwitchStackRoutingInterfaceRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/networks/{network_id}/switch/stacks/{switch_stack_id}/routing/interfaces/{interface_id}'.format(network_id='network_id_example', switch_stack_id='switch_stack_id_example', interface_id='interface_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_network_switch_stack_routing_interface_dhcp(client):
    """Test case for update_network_switch_stack_routing_interface_dhcp

    Update a layer 3 interface DHCP configuration for a switch stack
    """
    body = openapi_server.UpdateNetworkSwitchStackRoutingInterfaceDhcpRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/networks/{network_id}/switch/stacks/{switch_stack_id}/routing/interfaces/{interface_id}/dhcp'.format(network_id='network_id_example', switch_stack_id='switch_stack_id_example', interface_id='interface_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_network_switch_stack_routing_static_route(client):
    """Test case for update_network_switch_stack_routing_static_route

    Update a layer 3 static route for a switch stack
    """
    body = openapi_server.UpdateDeviceSwitchRoutingStaticRouteRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/networks/{network_id}/switch/stacks/{switch_stack_id}/routing/staticRoutes/{static_route_id}'.format(network_id='network_id_example', switch_stack_id='switch_stack_id_example', static_route_id='static_route_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_network_switch_storm_control(client):
    """Test case for update_network_switch_storm_control

    Update the storm control configuration for a switch network
    """
    body = openapi_server.UpdateNetworkSwitchStormControlRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/networks/{network_id}/switch/stormControl'.format(network_id='network_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_network_switch_stp(client):
    """Test case for update_network_switch_stp

    Updates STP settings
    """
    body = openapi_server.UpdateNetworkSwitchStpRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/networks/{network_id}/switch/stp'.format(network_id='network_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_organization_config_template_switch_profile_port(client):
    """Test case for update_organization_config_template_switch_profile_port

    Update a switch profile port
    """
    body = openapi_server.UpdateOrganizationConfigTemplateSwitchProfilePortRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/organizations/{organization_id}/configTemplates/{config_template_id}/switch/profiles/{profile_id}/ports/{port_id}'.format(organization_id='organization_id_example', config_template_id='config_template_id_example', profile_id='profile_id_example', port_id='port_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

