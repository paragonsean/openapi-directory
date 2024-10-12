# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.http_validation_error import HTTPValidationError
from openapi_server.models.uoas_by_distance import UOAsByDistance
from openapi_server.models.uoas_by_polygon import UOAsByPolygon
from openapi_server.models.uoas_by_route import UOAsByRoute
from openapi_server.models.uoas_distance_response import UOAsDistanceResponse
from openapi_server.models.uoas_poly_response import UOAsPolyResponse
from openapi_server.models.uoas_route_response import UOAsRouteResponse


pytestmark = pytest.mark.asyncio

async def test_uoa_by_distance_us_v1_uoa_distance_query_post(client):
    """Test case for uoa_by_distance_us_v1_uoa_distance_query_post

    Retrieve UAS Operating Areas (UOAs) found within given distance of location.
    """
    body = {"distance":25000,"latitude":36.36,"longitude":-94.07}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_api_key': 'x_api_key_example',
    }
    response = await client.request(
        method='POST',
        path='/us/v1/uoa/distance-query',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_uoa_by_poly_us_v1_uoa_polygon_query_post(client):
    """Test case for uoa_by_poly_us_v1_uoa_polygon_query_post

    Retrieve UAS Operating Areas (UOAs) found within given area.
    """
    body = {"poly":{"coordinates":[[[-84.31182861328125,39.47171528483254],[-83.9959716796875,39.47224533091448],[-84.07218933105469,39.627374847167204],[-84.31182861328125,39.47171528483254]]],"type":"Polygon"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_api_key': 'x_api_key_example',
    }
    response = await client.request(
        method='POST',
        path='/us/v1/uoa/polygon-query',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_uoa_by_route_us_v1_uoa_route_query_post(client):
    """Test case for uoa_by_route_us_v1_uoa_route_query_post

    Retrieve UAS Operating Areas (UOAs) found along route.
    """
    body = {"route":{"coordinates":[[-89.428019,38.693705],[-89.256689,38.604771],[-89.331396,38.388092]],"type":"LineString"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_api_key': 'x_api_key_example',
    }
    response = await client.request(
        method='POST',
        path='/us/v1/uoa/route-query',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

