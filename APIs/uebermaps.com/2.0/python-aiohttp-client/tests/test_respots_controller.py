# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.map import Map
from openapi_server.models.respot import Respot


pytestmark = pytest.mark.asyncio

async def test_maps_id_respots_get(client):
    """Test case for maps_id_respots_get

    List respots of a map
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/maps/{id}/respots'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_maps_map_id_spots_spot_id_respot_delete(client):
    """Test case for maps_map_id_spots_spot_id_respot_delete

    Delete respot from map by spot id
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v2/maps/{map_id}/spots/{spot_id}/respot'.format(map_id=56, spot_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_respot_maps_get(client):
    """Test case for respot_maps_get

    List maps that user can respot to
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/respot_maps',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_respots_id_delete(client):
    """Test case for respots_id_delete

    Delete respot
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v2/respots/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_respots_id_get(client):
    """Test case for respots_id_get

    Get respot
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/respots/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_spots_id_respots_post(client):
    """Test case for spots_id_respots_post

    Respot a spot onto a map
    """
    map_id = 3.4
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/spots/{id}/respots'.format(id=56),
        headers=headers,
        json=map_id,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

