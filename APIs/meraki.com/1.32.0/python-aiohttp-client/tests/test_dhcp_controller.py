# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_network_cellular_gateway_dhcp200_response import GetNetworkCellularGatewayDhcp200Response
from openapi_server.models.get_network_switch_dhcp_v4_servers_seen200_response_inner import GetNetworkSwitchDhcpV4ServersSeen200ResponseInner
from openapi_server.models.update_device_switch_routing_interface_dhcp_request import UpdateDeviceSwitchRoutingInterfaceDhcpRequest
from openapi_server.models.update_network_cellular_gateway_dhcp_request import UpdateNetworkCellularGatewayDhcpRequest
from openapi_server.models.update_network_switch_stack_routing_interface_dhcp_request import UpdateNetworkSwitchStackRoutingInterfaceDhcpRequest


pytestmark = pytest.mark.asyncio

async def test_get_device_appliance_dhcp_subnets_1(client):
    """Test case for get_device_appliance_dhcp_subnets_1

    Return the DHCP subnet information for an appliance
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/devices/{serial}/appliance/dhcp/subnets'.format(serial='serial_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_device_switch_routing_interface_dhcp_3(client):
    """Test case for get_device_switch_routing_interface_dhcp_3

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

async def test_get_network_cellular_gateway_dhcp_1(client):
    """Test case for get_network_cellular_gateway_dhcp_1

    List common DHCP settings of MGs
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/cellularGateway/dhcp'.format(network_id='network_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_switch_dhcp_v4_servers_seen_1(client):
    """Test case for get_network_switch_dhcp_v4_servers_seen_1

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

async def test_get_network_switch_stack_routing_interface_dhcp_4(client):
    """Test case for get_network_switch_stack_routing_interface_dhcp_4

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

async def test_update_device_switch_routing_interface_dhcp_3(client):
    """Test case for update_device_switch_routing_interface_dhcp_3

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

async def test_update_network_cellular_gateway_dhcp_1(client):
    """Test case for update_network_cellular_gateway_dhcp_1

    Update common DHCP settings of MGs
    """
    body = openapi_server.UpdateNetworkCellularGatewayDhcpRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/networks/{network_id}/cellularGateway/dhcp'.format(network_id='network_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_network_switch_stack_routing_interface_dhcp_4(client):
    """Test case for update_network_switch_stack_routing_interface_dhcp_4

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

