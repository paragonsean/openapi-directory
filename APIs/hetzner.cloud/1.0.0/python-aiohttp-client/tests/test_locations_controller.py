# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.locations_get200_response import LocationsGet200Response
from openapi_server.models.locations_id_get200_response import LocationsIdGet200Response


pytestmark = pytest.mark.asyncio

async def test_locations_get(client):
    """Test case for locations_get

    Get all Locations
    """
    params = [('name', 'name_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/locations',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_locations_id_get(client):
    """Test case for locations_id_get

    Get a Location
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/locations/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

