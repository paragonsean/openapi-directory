# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.add_network_switch_stack_request import AddNetworkSwitchStackRequest
from openapi_server.models.create_device_switch_routing_static_route_request import CreateDeviceSwitchRoutingStaticRouteRequest
from openapi_server.models.create_network_switch_stack_request import CreateNetworkSwitchStackRequest
from openapi_server.models.create_network_switch_stack_routing_interface_request import CreateNetworkSwitchStackRoutingInterfaceRequest
from openapi_server.models.get_network_switch_stack200_response import GetNetworkSwitchStack200Response
from openapi_server.models.remove_network_switch_stack_request import RemoveNetworkSwitchStackRequest
from openapi_server.models.update_device_switch_routing_static_route_request import UpdateDeviceSwitchRoutingStaticRouteRequest
from openapi_server.models.update_network_switch_stack_routing_interface_dhcp_request import UpdateNetworkSwitchStackRoutingInterfaceDhcpRequest
from openapi_server.models.update_network_switch_stack_routing_interface_request import UpdateNetworkSwitchStackRoutingInterfaceRequest


pytestmark = pytest.mark.asyncio

async def test_add_network_switch_stack_1(client):
    """Test case for add_network_switch_stack_1

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

async def test_create_network_switch_stack_1(client):
    """Test case for create_network_switch_stack_1

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

async def test_create_network_switch_stack_routing_interface_1(client):
    """Test case for create_network_switch_stack_routing_interface_1

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

async def test_create_network_switch_stack_routing_static_route_1(client):
    """Test case for create_network_switch_stack_routing_static_route_1

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

async def test_delete_network_switch_stack_1(client):
    """Test case for delete_network_switch_stack_1

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

async def test_delete_network_switch_stack_routing_interface_1(client):
    """Test case for delete_network_switch_stack_routing_interface_1

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

async def test_delete_network_switch_stack_routing_static_route_1(client):
    """Test case for delete_network_switch_stack_routing_static_route_1

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

async def test_get_network_switch_stack_1(client):
    """Test case for get_network_switch_stack_1

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

async def test_get_network_switch_stack_routing_interface_1(client):
    """Test case for get_network_switch_stack_routing_interface_1

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

async def test_get_network_switch_stack_routing_interface_dhcp_1(client):
    """Test case for get_network_switch_stack_routing_interface_dhcp_1

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

async def test_get_network_switch_stack_routing_interfaces_1(client):
    """Test case for get_network_switch_stack_routing_interfaces_1

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

async def test_get_network_switch_stack_routing_static_route_1(client):
    """Test case for get_network_switch_stack_routing_static_route_1

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

async def test_get_network_switch_stack_routing_static_routes_1(client):
    """Test case for get_network_switch_stack_routing_static_routes_1

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

async def test_get_network_switch_stacks_1(client):
    """Test case for get_network_switch_stacks_1

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

async def test_remove_network_switch_stack_1(client):
    """Test case for remove_network_switch_stack_1

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

async def test_update_network_switch_stack_routing_interface_1(client):
    """Test case for update_network_switch_stack_routing_interface_1

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

async def test_update_network_switch_stack_routing_interface_dhcp_1(client):
    """Test case for update_network_switch_stack_routing_interface_dhcp_1

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

async def test_update_network_switch_stack_routing_static_route_1(client):
    """Test case for update_network_switch_stack_routing_static_route_1

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

