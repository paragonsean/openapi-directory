# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_network_floor_plan_request import CreateNetworkFloorPlanRequest
from openapi_server.models.update_network_floor_plan_request import UpdateNetworkFloorPlanRequest


pytestmark = pytest.mark.asyncio

async def test_create_network_floor_plan(client):
    """Test case for create_network_floor_plan

    Upload a floor plan
    """
    body = openapi_server.CreateNetworkFloorPlanRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v0/networks/{network_id}/floorPlans'.format(network_id='network_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_network_floor_plan(client):
    """Test case for delete_network_floor_plan

    Destroy a floor plan
    """
    headers = { 
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v0/networks/{network_id}/floorPlans/{floor_plan_id}'.format(network_id='network_id_example', floor_plan_id='floor_plan_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_floor_plan(client):
    """Test case for get_network_floor_plan

    Find a floor plan by ID
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v0/networks/{network_id}/floorPlans/{floor_plan_id}'.format(network_id='network_id_example', floor_plan_id='floor_plan_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_floor_plans(client):
    """Test case for get_network_floor_plans

    List the floor plans that belong to your network
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v0/networks/{network_id}/floorPlans'.format(network_id='network_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_network_floor_plan(client):
    """Test case for update_network_floor_plan

    Update a floor plan's geolocation and other meta data
    """
    body = openapi_server.UpdateNetworkFloorPlanRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v0/networks/{network_id}/floorPlans/{floor_plan_id}'.format(network_id='network_id_example', floor_plan_id='floor_plan_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

