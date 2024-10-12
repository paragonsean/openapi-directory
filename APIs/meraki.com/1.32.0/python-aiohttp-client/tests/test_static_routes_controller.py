# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_device_switch_routing_static_route_request import CreateDeviceSwitchRoutingStaticRouteRequest
from openapi_server.models.create_network_appliance_static_route_request import CreateNetworkApplianceStaticRouteRequest
from openapi_server.models.get_device_switch_routing_static_route200_response import GetDeviceSwitchRoutingStaticRoute200Response
from openapi_server.models.update_device_switch_routing_static_route_request import UpdateDeviceSwitchRoutingStaticRouteRequest
from openapi_server.models.update_network_appliance_static_route_request import UpdateNetworkApplianceStaticRouteRequest


pytestmark = pytest.mark.asyncio

async def test_create_device_switch_routing_static_route_2(client):
    """Test case for create_device_switch_routing_static_route_2

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

async def test_create_network_appliance_static_route_1(client):
    """Test case for create_network_appliance_static_route_1

    Add a static route for an MX or teleworker network
    """
    body = openapi_server.CreateNetworkApplianceStaticRouteRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/networks/{network_id}/appliance/staticRoutes'.format(network_id='network_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_network_switch_stack_routing_static_route_3(client):
    """Test case for create_network_switch_stack_routing_static_route_3

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

async def test_delete_device_switch_routing_static_route_2(client):
    """Test case for delete_device_switch_routing_static_route_2

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

async def test_delete_network_appliance_static_route_1(client):
    """Test case for delete_network_appliance_static_route_1

    Delete a static route from an MX or teleworker network
    """
    headers = { 
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/networks/{network_id}/appliance/staticRoutes/{static_route_id}'.format(network_id='network_id_example', static_route_id='static_route_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_network_switch_stack_routing_static_route_3(client):
    """Test case for delete_network_switch_stack_routing_static_route_3

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

async def test_get_device_switch_routing_static_route_2(client):
    """Test case for get_device_switch_routing_static_route_2

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

async def test_get_device_switch_routing_static_routes_2(client):
    """Test case for get_device_switch_routing_static_routes_2

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

async def test_get_network_appliance_static_route_1(client):
    """Test case for get_network_appliance_static_route_1

    Return a static route for an MX or teleworker network
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/appliance/staticRoutes/{static_route_id}'.format(network_id='network_id_example', static_route_id='static_route_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_appliance_static_routes_1(client):
    """Test case for get_network_appliance_static_routes_1

    List the static routes for an MX or teleworker network
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/appliance/staticRoutes'.format(network_id='network_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_switch_stack_routing_static_route_3(client):
    """Test case for get_network_switch_stack_routing_static_route_3

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

async def test_get_network_switch_stack_routing_static_routes_3(client):
    """Test case for get_network_switch_stack_routing_static_routes_3

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

async def test_update_device_switch_routing_static_route_2(client):
    """Test case for update_device_switch_routing_static_route_2

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

async def test_update_network_appliance_static_route_1(client):
    """Test case for update_network_appliance_static_route_1

    Update a static route for an MX or teleworker network
    """
    body = openapi_server.UpdateNetworkApplianceStaticRouteRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/networks/{network_id}/appliance/staticRoutes/{static_route_id}'.format(network_id='network_id_example', static_route_id='static_route_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_network_switch_stack_routing_static_route_3(client):
    """Test case for update_network_switch_stack_routing_static_route_3

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

