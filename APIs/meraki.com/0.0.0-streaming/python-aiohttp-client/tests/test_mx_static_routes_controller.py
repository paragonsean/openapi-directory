# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_network_static_route_request import CreateNetworkStaticRouteRequest
from openapi_server.models.update_network_static_route_request import UpdateNetworkStaticRouteRequest


pytestmark = pytest.mark.asyncio

async def test_create_network_static_route(client):
    """Test case for create_network_static_route

    Add a static route for an MX or teleworker network
    """
    body = openapi_server.CreateNetworkStaticRouteRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v0/networks/{network_id}/staticRoutes'.format(network_id='network_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_network_static_route(client):
    """Test case for delete_network_static_route

    Delete a static route from an MX or teleworker network
    """
    headers = { 
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v0/networks/{network_id}/staticRoutes/{static_route_id}'.format(network_id='network_id_example', static_route_id='static_route_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_static_route(client):
    """Test case for get_network_static_route

    Return a static route for an MX or teleworker network
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v0/networks/{network_id}/staticRoutes/{static_route_id}'.format(network_id='network_id_example', static_route_id='static_route_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_static_routes(client):
    """Test case for get_network_static_routes

    List the static routes for an MX or teleworker network
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v0/networks/{network_id}/staticRoutes'.format(network_id='network_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_network_static_route(client):
    """Test case for update_network_static_route

    Update a static route for an MX or teleworker network
    """
    body = openapi_server.UpdateNetworkStaticRouteRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v0/networks/{network_id}/staticRoutes/{static_route_id}'.format(network_id='network_id_example', static_route_id='static_route_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

