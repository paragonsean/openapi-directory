# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.step import Step
from openapi_server.models.trip import Trip


pytestmark = pytest.mark.asyncio

async def test_trip_get(client):
    """Test case for trip_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/pub/api/trip',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_trip_trip_id_stop_get(client):
    """Test case for trip_trip_id_stop_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/pub/api/trip/{trip_id}/stop'.format(trip_id='trip_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

