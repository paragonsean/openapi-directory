# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.patch_charge_station200_response import PatchChargeStation200Response
from openapi_server.models.post_charge_stations201_response import PostChargeStations201Response
from openapi_server.models.schema1 import Schema1


pytestmark = pytest.mark.asyncio

async def test_delete_charge_station(client):
    """Test case for delete_charge_station

    
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/chargestations/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_charge_station(client):
    """Test case for get_charge_station

    
    """
    params = [('include_location', True),
                    ('include_evses', True),
                    ('include_organization', True)]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/chargestations/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_charge_station_connectors(client):
    """Test case for get_charge_station_connectors

    
    """
    params = [('include_evse', True),
                    ('include_organization', True)]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/chargestations/{id}/connectors'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_charge_stations(client):
    """Test case for get_charge_stations

    
    """
    params = [('organization', 'organization_example'),
                    ('location', 'location_example'),
                    ('online', True),
                    ('active', True),
                    ('public', True),
                    ('paginate_limit', 20),
                    ('paginate_page', 'paginate_page_example'),
                    ('paginate_enabled', True),
                    ('sort_by', 'createdAt'),
                    ('sort_order', desc),
                    ('createdAt[$gte]', '2013-10-20T19:20:30+01:00'),
                    ('createdAt[$lte]', '2013-10-20T19:20:30+01:00'),
                    ('updatedAt[$gte]', '2013-10-20T19:20:30+01:00'),
                    ('updatedAt[$lte]', '2013-10-20T19:20:30+01:00'),
                    ('include_location', True),
                    ('include_evses', True),
                    ('include_organization', True)]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/chargestations',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patch_charge_station(client):
    """Test case for patch_charge_station

    
    """
    body = openapi_server.Schema1()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v1/chargestations/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_charge_stations(client):
    """Test case for post_charge_stations

    
    """
    body = openapi_server.Schema1()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/chargestations',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

