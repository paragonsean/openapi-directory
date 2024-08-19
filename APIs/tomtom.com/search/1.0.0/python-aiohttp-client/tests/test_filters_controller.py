# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.search_version_number_geometry_filter_ext_post_request import SearchVersionNumberGeometryFilterExtPostRequest
from openapi_server.models.search_version_number_routed_filter_position_heading_ext_post_request import SearchVersionNumberRoutedFilterPositionHeadingExtPostRequest


pytestmark = pytest.mark.asyncio

async def test_search_version_number_geometry_filter_ext_get(client):
    """Test case for search_version_number_geometry_filter_ext_get

    Geometry Filter
    """
    params = [('geometryList', '[{\"type\":\"CIRCLE\", \"position\":\"40.80558, -73.96548\", \"radius\":100}, {\"type\":\"POLYGON\", \"vertices\":[\"37.7524152343544, -122.43576049804686\", \"37.70660472542312, -122.43301391601562\", \"37.712059855877314, -122.36434936523438\", \"37.75350561243041, -122.37396240234374\"]}]'),
                    ('poiList', '[{\"poi\":{\"name\":\"S Restaurant Toms\"},\"address\":{\"freeformAddress\":\"2880 Broadway, New York, NY 10025\"},\"position\":{\"lat\":40.80558,\"lon\":-73.96548}},{\"poi\":{\"name\":\"Yasha Raman Corporation\"},\"address\":{\"freeformAddress\":\"940 Amsterdam Ave, New York, NY 10025\"},\"position\":{\"lat\":40.80076,\"lon\":-73.96556}}]')]
    headers = { 
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/search/{version_number}/geometryFilter.{ext}'.format(version_number=56, ext='xml'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_version_number_geometry_filter_ext_post(client):
    """Test case for search_version_number_geometry_filter_ext_post

    Geometry Filter
    """
    body = openapi_server.SearchVersionNumberGeometryFilterExtPostRequest()
    headers = { 
        'Content-Type': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/search/{version_number}/geometryFilter.{ext}'.format(version_number=56, ext='xml'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_version_number_routed_filter_position_heading_ext_get(client):
    """Test case for search_version_number_routed_filter_position_heading_ext_get

    Routed Filter
    """
    params = [('poiList', '[{\"poi\":{\"name\":\"Cleaire Advanced Emission Controls\"},\"address\":{\"freeformAddress\":\"7220 Trade St, San Diego, CA 92121\"},\"position\":{\"lat\":\"37.83274\",\"lon\":\"-122.27631\"}}]'),
                    ('routingTimeout', 4000)]
    headers = { 
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/search/{version_number}/routedFilter/{position}/{heading_ext}'.format(version_number=56, position='37.8328,-122.27669', heading=-15.6, ext='xml'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_version_number_routed_filter_position_heading_ext_post(client):
    """Test case for search_version_number_routed_filter_position_heading_ext_post

    Routed Filter
    """
    body = openapi_server.SearchVersionNumberRoutedFilterPositionHeadingExtPostRequest()
    params = [('routingTimeout', 4000)]
    headers = { 
        'Content-Type': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/search/{version_number}/routedFilter/{position}/{heading_ext}'.format(version_number=56, position='37.8328,-122.27669', heading=90, ext='xml'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

