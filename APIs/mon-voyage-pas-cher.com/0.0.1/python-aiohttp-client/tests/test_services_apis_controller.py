# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.distance_response import DistanceResponse
from openapi_server.models.elevation_response import ElevationResponse
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.sun_position_response import SunPositionResponse
from openapi_server.models.timezone_response import TimezoneResponse


pytestmark = pytest.mark.asyncio

async def test_get_distance(client):
    """Test case for get_distance

    Calculate distance between lats/longs
    """
    params = [('locationA', 'location_a_example'),
                    ('locationB', 'location_b_example'),
                    ('unit', kms)]
    headers = { 
        'Accept': 'application/json',
        'x-api-key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/distance',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_elevation(client):
    """Test case for get_elevation

    Search elevation informations from lat/long
    """
    params = [('locations', '67.85572,20.22513'),
                    ('unit', meters)]
    headers = { 
        'Accept': 'application/json',
        'x-api-key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/elevation',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_sun(client):
    """Test case for get_sun

    Search position of sun from lat/long and date
    """
    params = [('location', 'location_example'),
                    ('date', '2013-10-20')]
    headers = { 
        'Accept': 'application/json',
        'x-api-key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/sun_positions',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_timezone(client):
    """Test case for get_timezone

    Search timezone and time informations from lat/long
    """
    params = [('location', '45.8326307,6.8650517')]
    headers = { 
        'Accept': 'application/json',
        'x-api-key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/timezone',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

