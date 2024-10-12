# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_device_switch_routing_interface_request import CreateDeviceSwitchRoutingInterfaceRequest
from openapi_server.models.create_network_switch_stack_routing_interface_request import CreateNetworkSwitchStackRoutingInterfaceRequest
from openapi_server.models.get_device_switch_routing_interfaces200_response_inner import GetDeviceSwitchRoutingInterfaces200ResponseInner
from openapi_server.models.update_device_switch_routing_interface_dhcp_request import UpdateDeviceSwitchRoutingInterfaceDhcpRequest
from openapi_server.models.update_network_switch_stack_routing_interface_dhcp_request import UpdateNetworkSwitchStackRoutingInterfaceDhcpRequest
from openapi_server.models.update_network_switch_stack_routing_interface_request import UpdateNetworkSwitchStackRoutingInterfaceRequest


pytestmark = pytest.mark.asyncio

async def test_create_device_switch_routing_interface_2(client):
    """Test case for create_device_switch_routing_interface_2

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

async def test_create_network_switch_stack_routing_interface_3(client):
    """Test case for create_network_switch_stack_routing_interface_3

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

async def test_delete_device_switch_routing_interface_2(client):
    """Test case for delete_device_switch_routing_interface_2

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

async def test_delete_network_switch_stack_routing_interface_3(client):
    """Test case for delete_network_switch_stack_routing_interface_3

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

async def test_get_device_switch_routing_interface_2(client):
    """Test case for get_device_switch_routing_interface_2

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

async def test_get_device_switch_routing_interface_dhcp_2(client):
    """Test case for get_device_switch_routing_interface_dhcp_2

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

async def test_get_device_switch_routing_interfaces_2(client):
    """Test case for get_device_switch_routing_interfaces_2

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

async def test_get_network_switch_stack_routing_interface_3(client):
    """Test case for get_network_switch_stack_routing_interface_3

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

async def test_get_network_switch_stack_routing_interface_dhcp_3(client):
    """Test case for get_network_switch_stack_routing_interface_dhcp_3

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

async def test_get_network_switch_stack_routing_interfaces_3(client):
    """Test case for get_network_switch_stack_routing_interfaces_3

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

async def test_update_device_switch_routing_interface_2(client):
    """Test case for update_device_switch_routing_interface_2

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

async def test_update_device_switch_routing_interface_dhcp_2(client):
    """Test case for update_device_switch_routing_interface_dhcp_2

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

async def test_update_network_switch_stack_routing_interface_3(client):
    """Test case for update_network_switch_stack_routing_interface_3

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

async def test_update_network_switch_stack_routing_interface_dhcp_3(client):
    """Test case for update_network_switch_stack_routing_interface_dhcp_3

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

