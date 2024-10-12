# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.location_list_view_model import LocationListViewModel
from openapi_server.models.location_view_model import LocationViewModel


pytestmark = pytest.mark.asyncio

async def test_consumer_v1_locations_get(client):
    """Test case for consumer_v1_locations_get

    List Locations
    """
    params = [('name', 'name_example'),
                    ('nearestTo', 'nearest_to_example'),
                    ('proximity', 56),
                    ('units', 'units_example'),
                    ('serviceId', 'service_id_example'),
                    ('friendlyId', 'friendly_id_example'),
                    ('regionId', 'region_id_example'),
                    ('ignorePrimary', True),
                    ('offset', 56),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/consumer/v1/locations',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_consumer_v1_locations_id_get(client):
    """Test case for consumer_v1_locations_id_get

    Get Location
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/consumer/v1/locations/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

