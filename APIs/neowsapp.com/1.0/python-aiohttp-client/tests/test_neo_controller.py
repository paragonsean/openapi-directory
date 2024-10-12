# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.near_earth_object import NearEarthObject


pytestmark = pytest.mark.asyncio

async def test_browse_near_earth_objects(client):
    """Test case for browse_near_earth_objects

    Browse the Near Earth Objects service
    """
    params = [('page', 0),
                    ('size', 20)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/rest/v1/neo/browse',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retrieve_near_earth_object_by_id(client):
    """Test case for retrieve_near_earth_object_by_id

    Find Near Earth Objects by id
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/rest/v1/neo/{asteroid_id}'.format(asteroid_id='asteroid_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

