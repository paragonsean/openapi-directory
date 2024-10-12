# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.http_validation_error import HTTPValidationError
from openapi_server.models.ssaby_distance import SSAByDistance
from openapi_server.models.ssaby_polygon import SSAByPolygon
from openapi_server.models.ssaby_route import SSAByRoute
from openapi_server.models.ssa_distance_response import SSADistanceResponse
from openapi_server.models.ssa_poly_response import SSAPolyResponse
from openapi_server.models.ssa_route_response import SSARouteResponse


pytestmark = pytest.mark.asyncio

async def test_ssa_by_distance_us_v1_ssa_distance_query_post(client):
    """Test case for ssa_by_distance_us_v1_ssa_distance_query_post

    Retrieve all special security areas located within given distance of location.
    """
    body = {"distance":3000,"latitude":39.44,"longitude":-77.39}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_api_key': 'x_api_key_example',
    }
    response = await client.request(
        method='POST',
        path='/us/v1/ssa/distance-query',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ssa_by_poly_us_v1_ssa_polygon_query_post(client):
    """Test case for ssa_by_poly_us_v1_ssa_polygon_query_post

    Retrieve all special security areas located within given GeoJSON Polygon.
    """
    body = {"poly":{"coordinates":[[[-120.866559,35.228447],[-120.816434,35.233719],[-120.838956,35.212853],[-120.866559,35.228447]]],"type":"Polygon"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_api_key': 'x_api_key_example',
    }
    response = await client.request(
        method='POST',
        path='/us/v1/ssa/polygon-query',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ssa_by_route_us_v1_ssa_route_query_post(client):
    """Test case for ssa_by_route_us_v1_ssa_route_query_post

    Retrieve all special security areas traversed by route.
    """
    body = {"route":{"coordinates":[[-110.868783,32.068473],[-110.833353,32.17129],[-110.794351,32.180124]],"type":"LineString"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_api_key': 'x_api_key_example',
    }
    response = await client.request(
        method='POST',
        path='/us/v1/ssa/route-query',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

