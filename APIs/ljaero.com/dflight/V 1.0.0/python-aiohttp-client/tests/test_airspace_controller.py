# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.airspace_by_distance import AirspaceByDistance
from openapi_server.models.airspace_by_polygon import AirspaceByPolygon
from openapi_server.models.airspace_by_route import AirspaceByRoute
from openapi_server.models.airspace_distance_response import AirspaceDistanceResponse
from openapi_server.models.airspace_poly_response import AirspacePolyResponse
from openapi_server.models.airspace_route_response import AirspaceRouteResponse
from openapi_server.models.http_validation_error import HTTPValidationError


pytestmark = pytest.mark.asyncio

async def test_asp_by_distance_us_v1_airspace_distance_query_post(client):
    """Test case for asp_by_distance_us_v1_airspace_distance_query_post

    Retrieve all requested types of airspace located within given distance of location.
    """
    body = {"asptypes":["MAA","MTR"],"distance":5000,"latitude":44.6031,"longitude":-88.2188}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_api_key': 'x_api_key_example',
    }
    response = await client.request(
        method='POST',
        path='/us/v1/airspace/distance-query',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_asp_by_poly_us_v1_airspace_polygon_query_post(client):
    """Test case for asp_by_poly_us_v1_airspace_polygon_query_post

    Retrieve all requested types of airspace located within given GeoJSON Polygon.
    """
    body = {"asptypes":["CAS"],"poly":{"coordinates":[[[-86.337,41.716],[-86.323,41.718],[-86.327,41.727],[-86.337,41.722],[-86.337,41.716]]],"type":"Polygon"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_api_key': 'x_api_key_example',
    }
    response = await client.request(
        method='POST',
        path='/us/v1/airspace/polygon-query',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_asp_by_route_us_v1_airspace_route_query_post(client):
    """Test case for asp_by_route_us_v1_airspace_route_query_post

    Retrieve all requested types of airspace traversed by route.
    """
    body = {"asptypes":["SUA","MAA"],"route":{"coordinates":[[-80.53,32.44],[-80.52,32.43],[-80.51,32.4]],"type":"LineString"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_api_key': 'x_api_key_example',
    }
    response = await client.request(
        method='POST',
        path='/us/v1/airspace/route-query',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

