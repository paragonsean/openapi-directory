# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.geo_convert_request import GeoConvertRequest
from openapi_server.models.geo_convert_response import GeoConvertResponse
from openapi_server.models.geo_distance_request import GeoDistanceRequest
from openapi_server.models.geo_distance_response import GeoDistanceResponse
from openapi_server.models.geo_fence_request import GeoFenceRequest
from openapi_server.models.geo_fence_response import GeoFenceResponse
from openapi_server.models.geo_sky_request import GeoSkyRequest
from openapi_server.models.geo_sky_response import GeoSkyResponse
from openapi_server.models.wyjyt_error_response import WyjytErrorResponse


pytestmark = pytest.mark.asyncio

async def test_convert(client):
    """Test case for convert

    Convert the list of geo coordinates to a standard format - (latlon | utm | mgrs | ecef | epsg3857 | georef | cartesian)
    """
    body = openapi_server.GeoConvertRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/Convert',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_distance(client):
    """Test case for distance

    Calculate the distance between two geo coordinates.
    """
    body = openapi_server.GeoDistanceRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/Distance',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fence(client):
    """Test case for fence

    Check if a list of coordinates are inside of a fence of coordinates.
    """
    body = openapi_server.GeoFenceRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/Fence',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sky(client):
    """Test case for sky

    Calculate sun, moon, eclipse and sky information for the date and location.
    """
    body = openapi_server.GeoSkyRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/Sky',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

