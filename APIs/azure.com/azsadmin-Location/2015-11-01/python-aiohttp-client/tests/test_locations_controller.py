# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.location import Location
from openapi_server.models.location_list import LocationList
from openapi_server.models.operations_status import OperationsStatus


pytestmark = pytest.mark.asyncio

async def test_locations_create_or_update(client):
    """Test case for locations_create_or_update

    
    """
    new_location = {"displayName":"displayName","latitude":"latitude","name":"name","id":"id","longitude":"longitude"}
    params = [('api-version', '2015-11-01')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Subscriptions.Admin/locations/{location}'.format(subscription_id='subscription_id_example', location='location_example'),
        headers=headers,
        json=new_location,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_locations_get(client):
    """Test case for locations_get

    
    """
    params = [('api-version', '2015-11-01')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Subscriptions.Admin/locations/{location}'.format(subscription_id='subscription_id_example', location='location_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_locations_get_operations_status(client):
    """Test case for locations_get_operations_status

    
    """
    params = [('api-version', '2015-11-01')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Subscriptions.Admin/locations/{location}/operationsStatus/{operations_status_name}'.format(subscription_id='subscription_id_example', location='location_example', operations_status_name='operations_status_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_locations_list(client):
    """Test case for locations_list

    
    """
    params = [('api-version', '2015-11-01')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Subscriptions.Admin/locations'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

