# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.http_validation_error import HTTPValidationError
from openapi_server.models.notams_by_distance import NOTAMsByDistance
from openapi_server.models.notams_by_polygon import NOTAMsByPolygon
from openapi_server.models.notams_by_route import NOTAMsByRoute
from openapi_server.models.notams_distance_response import NOTAMsDistanceResponse
from openapi_server.models.notams_poly_response import NOTAMsPolyResponse
from openapi_server.models.notams_route_response import NOTAMsRouteResponse


pytestmark = pytest.mark.asyncio

async def test_tfr_by_distance_us_v1_restrictions_distance_query_post(client):
    """Test case for tfr_by_distance_us_v1_restrictions_distance_query_post

    Retrieve flight restrictions applicable within given distance of location.
    """
    body = {"distance":5000,"latitude":35.753,"longitude":-105.416}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_api_key': 'x_api_key_example',
    }
    response = await client.request(
        method='POST',
        path='/us/v1/restrictions/distance-query',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tfr_by_poly_us_v1_restrictions_polygon_query_post(client):
    """Test case for tfr_by_poly_us_v1_restrictions_polygon_query_post

    Retrieve flight restrictions applicable within given area.
    """
    body = {"poly":{"coordinates":[[[-155.426425,19.545118],[-155.59946,19.440516],[-155.348422,19.335847],[-155.426425,19.545118]]],"type":"Polygon"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_api_key': 'x_api_key_example',
    }
    response = await client.request(
        method='POST',
        path='/us/v1/restrictions/polygon-query',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tfr_by_route_us_v1_restrictions_route_query_post(client):
    """Test case for tfr_by_route_us_v1_restrictions_route_query_post

    Retrieve flight restrictions applicable along route.
    """
    body = {"route":{"coordinates":[[-80.135,25.783],[-80.127,25.797],[-80.128,25.812],[-80.132,25.824]],"type":"LineString"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_api_key': 'x_api_key_example',
    }
    response = await client.request(
        method='POST',
        path='/us/v1/restrictions/route-query',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

