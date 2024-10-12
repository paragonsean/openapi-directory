# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.place_response import PlaceResponse
from openapi_server.models.routes_response import RoutesResponse


pytestmark = pytest.mark.asyncio

async def test_g_et_places(client):
    """Test case for g_et_places

    Returns possible modes of transportation between two cities.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2.0/places',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_routes(client):
    """Test case for g_et_routes

    
    """
    params = [('origin_lat', 3.4),
                    ('origin_lng', 3.4),
                    ('destination_lat', 3.4),
                    ('destination_lng', 3.4)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2.0/routes',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

