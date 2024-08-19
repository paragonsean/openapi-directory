# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_drivers200_response import GetDrivers200Response
from openapi_server.models.patch_charge_station200_response import PatchChargeStation200Response
from openapi_server.models.post_charge_request import PostChargeRequest


pytestmark = pytest.mark.asyncio

async def test_get_vehicle(client):
    """Test case for get_vehicle

    
    """
    params = [('include_driver', True),
                    ('include_token', True),
                    ('include_organization', True)]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/vehicles/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_vehicle_battery(client):
    """Test case for get_vehicle_battery

    
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/vehicles/{id}/battery'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_vehicle_charge(client):
    """Test case for get_vehicle_charge

    
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/vehicles/{id}/charge'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_vehicle_location(client):
    """Test case for get_vehicle_location

    
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/vehicles/{id}/location'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_vehicle_odometer(client):
    """Test case for get_vehicle_odometer

    
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/vehicles/{id}/odometer'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_vehicles(client):
    """Test case for get_vehicles

    
    """
    params = [('active', True),
                    ('paginate_limit', 20),
                    ('paginate_page', 'paginate_page_example'),
                    ('paginate_enabled', True),
                    ('sort_by', 'createdAt'),
                    ('sort_order', desc),
                    ('createdAt[$gte]', '2013-10-20T19:20:30+01:00'),
                    ('createdAt[$lte]', '2013-10-20T19:20:30+01:00'),
                    ('updatedAt[$gte]', '2013-10-20T19:20:30+01:00'),
                    ('updatedAt[$lte]', '2013-10-20T19:20:30+01:00'),
                    ('include_driver', True),
                    ('include_token', True),
                    ('include_organization', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/vehicles',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_charge(client):
    """Test case for post_charge

    
    """
    body = openapi_server.PostChargeRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/vehicles/{id}/charge'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

