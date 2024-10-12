# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.map import Map
from openapi_server.models.spot import Spot
from openapi_server.models.user import User


pytestmark = pytest.mark.asyncio

async def test_maps_search_get(client):
    """Test case for maps_search_get

    Search maps
    """
    params = [('q', 'q_example'),
                    ('d', 56),
                    ('lat', 3.4),
                    ('lon', 3.4)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/maps/search',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_spots_search_get(client):
    """Test case for spots_search_get

    Search spots
    """
    params = [('q', 'q_example'),
                    ('d', 56),
                    ('lat', 3.4),
                    ('lon', 3.4)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/spots/search',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_search_get(client):
    """Test case for users_search_get

    Search users
    """
    params = [('q', 'q_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/users/search',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

