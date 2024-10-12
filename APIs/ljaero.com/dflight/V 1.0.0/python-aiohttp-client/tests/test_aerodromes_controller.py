# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.aerodrome_distance_response import AerodromeDistanceResponse
from openapi_server.models.aerodrome_poly_response import AerodromePolyResponse
from openapi_server.models.aerodrome_route_response import AerodromeRouteResponse
from openapi_server.models.aerodromes_by_distance import AerodromesByDistance
from openapi_server.models.aerodromes_by_polygon import AerodromesByPolygon
from openapi_server.models.aerodromes_by_route import AerodromesByRoute
from openapi_server.models.http_validation_error import HTTPValidationError


pytestmark = pytest.mark.asyncio

async def test_aerodromes_by_distance_us_v1_aerodromes_distance_query_post(client):
    """Test case for aerodromes_by_distance_us_v1_aerodromes_distance_query_post

    Retrieve aerodromes within given distance of location.
    """
    body = {"distance":5000,"latitude":39.94,"longitude":-82.97}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_api_key': 'x_api_key_example',
    }
    response = await client.request(
        method='POST',
        path='/us/v1/aerodromes/distance-query',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aerodromes_by_poly_us_v1_aerodromes_polygon_query_post(client):
    """Test case for aerodromes_by_poly_us_v1_aerodromes_polygon_query_post

    Retrieve aerodromes located within given area.
    """
    body = {"poly":{"coordinates":[[[-122.338707447052,47.62958028571895],[-122.35679626464844,47.61773556745509],[-122.33343388885261,47.61953540719045],[-122.338707447052,47.62958028571895]]],"type":"Polygon"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_api_key': 'x_api_key_example',
    }
    response = await client.request(
        method='POST',
        path='/us/v1/aerodromes/polygon-query',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aerodromes_by_route_us_v1_aerodromes_route_query_post(client):
    """Test case for aerodromes_by_route_us_v1_aerodromes_route_query_post

    Retrieve aerodromes found along a route.
    """
    body = {"route":{"coordinates":[[-89.353316,29.270685],[-89.36921,29.290526],[-89.376006,29.298966]],"type":"LineString"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_api_key': 'x_api_key_example',
    }
    response = await client.request(
        method='POST',
        path='/us/v1/aerodromes/route-query',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

