# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.travel_center import TravelCenter


pytestmark = pytest.mark.asyncio

async def test_reisezentren_get(client):
    """Test case for reisezentren_get

    Get all station infos
    """
    params = [('name', 'name_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/reisezentren/v1/reisezentren',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reisezentren_id_get(client):
    """Test case for reisezentren_id_get

    Get information about a specific station
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/reisezentren/v1/reisezentren/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reisezentren_loc_lat_lon_dist_get(client):
    """Test case for reisezentren_loc_lat_lon_dist_get

    Get stations in a given radius
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/reisezentren/v1/reisezentren/loc/{lat}/{lon}/{dist}'.format(lat=3.4, lon=3.4, dist=3.4),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reisezentren_loc_lat_lon_get(client):
    """Test case for reisezentren_loc_lat_lon_get

    Get information about a station near a location
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/reisezentren/v1/reisezentren/loc/{lat}/{lon}'.format(lat=3.4, lon=3.4),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

