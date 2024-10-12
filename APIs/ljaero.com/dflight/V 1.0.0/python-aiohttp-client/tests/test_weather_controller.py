# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.http_validation_error import HTTPValidationError
from openapi_server.models.wx_by_distance import WxByDistance
from openapi_server.models.wx_by_polygon import WxByPolygon
from openapi_server.models.wx_by_route import WxByRoute
from openapi_server.models.wx_distance_response import WxDistanceResponse
from openapi_server.models.wx_poly_response import WxPolyResponse
from openapi_server.models.wx_route_response import WxRouteResponse


pytestmark = pytest.mark.asyncio

async def test_wx_by_distance_us_v1_wx_forecast_distance_query_post(client):
    """Test case for wx_by_distance_us_v1_wx_forecast_distance_query_post

    Retrieve forecast values within given distance of location for all requested weather elements and time periods.
    """
    body = {"distance":5000,"hours":2,"latitude":37.871,"longitude":-122.283,"wxtypes":["VIS","SKY"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_api_key': 'x_api_key_example',
    }
    response = await client.request(
        method='POST',
        path='/us/v1/wx-forecast/distance-query',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_wx_by_poly_us_v1_wx_forecast_polygon_query_post(client):
    """Test case for wx_by_poly_us_v1_wx_forecast_polygon_query_post

    Retrieve forecast values within given GeoJSON polygon for all requested weather elements and time periods.
    """
    body = {"hours":5,"poly":{"coordinates":[[[-90.621,41.505],[-90.599,41.498],[-90.514,41.508],[-90.501,41.523],[-90.543,41.538],[-90.621,41.505]]],"type":"Polygon"},"wxtypes":["TEMP","DEWPT"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_api_key': 'x_api_key_example',
    }
    response = await client.request(
        method='POST',
        path='/us/v1/wx-forecast/polygon-query',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_wx_by_route_us_v1_wx_forecast_route_query_post(client):
    """Test case for wx_by_route_us_v1_wx_forecast_route_query_post

    Retrieve forecast values along a route for all requested weather elements and time periods.
    """
    body = {"hours":4,"route":{"coordinates":[[-86.247,43.058],[-86.214,43.076],[-86.203,43.089],[-86.192,43.083],[-86.185,43.11]],"type":"LineString"},"wxtypes":["WINDDIR","WINDSPEED"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_api_key': 'x_api_key_example',
    }
    response = await client.request(
        method='POST',
        path='/us/v1/wx-forecast/route-query',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

