# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.http_validation_error import HTTPValidationError
from openapi_server.models.obstacle_distance_response import ObstacleDistanceResponse
from openapi_server.models.obstacle_poly_response import ObstaclePolyResponse
from openapi_server.models.obstacle_route_response import ObstacleRouteResponse
from openapi_server.models.obstacles_by_distance import ObstaclesByDistance
from openapi_server.models.obstacles_by_polygon import ObstaclesByPolygon
from openapi_server.models.obstacles_by_route import ObstaclesByRoute


pytestmark = pytest.mark.asyncio

async def test_obstacles_by_distance_us_v1_obstacles_distance_query_post(client):
    """Test case for obstacles_by_distance_us_v1_obstacles_distance_query_post

    Retrieve obstacles within given distance of location.
    """
    body = {"distance":1500,"latitude":40.23,"longitude":-79.96}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_api_key': 'x_api_key_example',
    }
    response = await client.request(
        method='POST',
        path='/us/v1/obstacles/distance-query',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_obstacles_by_poly_us_v1_obstacles_polygon_query_post(client):
    """Test case for obstacles_by_poly_us_v1_obstacles_polygon_query_post

    Retrieve obstacles located within given area.
    """
    body = {"poly":{"coordinates":[[[-90.166,35.078],[-90.104,35.066],[-90.132,35.085],[-90.166,35.078]]],"type":"Polygon"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_api_key': 'x_api_key_example',
    }
    response = await client.request(
        method='POST',
        path='/us/v1/obstacles/polygon-query',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_obstacles_by_route_us_v1_obstacles_route_query_post(client):
    """Test case for obstacles_by_route_us_v1_obstacles_route_query_post

    Retrieve obstacles found along a route.
    """
    body = {"route":{"coordinates":[[-86.91,41.728],[-86.91,41.718],[-86.91,41.715]],"type":"LineString"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_api_key': 'x_api_key_example',
    }
    response = await client.request(
        method='POST',
        path='/us/v1/obstacles/route-query',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

