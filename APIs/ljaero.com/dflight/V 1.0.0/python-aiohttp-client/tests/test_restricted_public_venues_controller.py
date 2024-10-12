# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.http_validation_error import HTTPValidationError
from openapi_server.models.venue_distance_response import VenueDistanceResponse
from openapi_server.models.venue_poly_response import VenuePolyResponse
from openapi_server.models.venue_route_response import VenueRouteResponse
from openapi_server.models.venues_by_distance import VenuesByDistance
from openapi_server.models.venues_by_polygon import VenuesByPolygon
from openapi_server.models.venues_by_route import VenuesByRoute


pytestmark = pytest.mark.asyncio

async def test_ven_by_distance_us_v1_venues_distance_query_post(client):
    """Test case for ven_by_distance_us_v1_venues_distance_query_post

    Retrieve all restricted public venues located within given distance of location.
    """
    body = {"distance":2000,"latitude":32.75,"longitude":-97.09}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_api_key': 'x_api_key_example',
    }
    response = await client.request(
        method='POST',
        path='/us/v1/venues/distance-query',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ven_by_poly_us_v1_venues_polygon_query_post(client):
    """Test case for ven_by_poly_us_v1_venues_polygon_query_post

    Retrieve all restricted public venues located within given GeoJSON Polygon.
    """
    body = {"poly":{"coordinates":[[[-68.26861381530762,44.36801121434667],[-68.26221942901611,44.36006491796501],[-68.25882911682127,44.36561823465291],[-68.26861381530762,44.36801121434667]]],"type":"Polygon"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_api_key': 'x_api_key_example',
    }
    response = await client.request(
        method='POST',
        path='/us/v1/venues/polygon-query',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ven_by_route_us_v1_venues_route_query_post(client):
    """Test case for ven_by_route_us_v1_venues_route_query_post

    Retrieve all restricted public venues traversed by route.
    """
    body = {"route":{"coordinates":[[-80.3798,25.4551],[-80.3479,25.489],[-80.3129,25.4696]],"type":"LineString"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_api_key': 'x_api_key_example',
    }
    response = await client.request(
        method='POST',
        path='/us/v1/venues/route-query',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

