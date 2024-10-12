# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.spot import Spot
from openapi_server.models.spot_editable import SpotEditable


pytestmark = pytest.mark.asyncio

async def test_maps_id_spots_get(client):
    """Test case for maps_id_spots_get

    List spots for a given map
    """
    params = [('order', 'order_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/maps/{id}/spots'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_maps_id_spots_post(client):
    """Test case for maps_id_spots_post

    Create spot
    """
    spot = {"description":"Landed here by accident but look how wonderful this place is in the photos attached","lon":10.58349,"time_zone":"Berlin","title":"Beautiful place out in the country","lat":53.112385,"picture":"<BASE_64_ENCODED_STRING>"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/maps/{id}/spots'.format(id=56),
        headers=headers,
        json=spot,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_maps_map_id_spots_id_get(client):
    """Test case for maps_map_id_spots_id_get

    Get spot
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/maps/{map_id}/spots/{id}'.format(id=56, map_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_spots_get(client):
    """Test case for spots_get

    List your own spots
    """
    params = [('order', 'order_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/spots',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_spots_id_delete(client):
    """Test case for spots_id_delete

    Delete spot
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v2/spots/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_spots_id_patch(client):
    """Test case for spots_id_patch

    Update spot
    """
    spot = {"description":"Landed here by accident but look how wonderful this place is in the photos attached","lon":10.58349,"time_zone":"Berlin","title":"Beautiful place out in the country","lat":53.112385,"picture":"<BASE_64_ENCODED_STRING>"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v2/spots/{id}'.format(id=56),
        headers=headers,
        json=spot,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

