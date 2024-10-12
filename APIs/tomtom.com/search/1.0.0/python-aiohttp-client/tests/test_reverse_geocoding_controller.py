# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_search_version_number_reverse_geocode_cross_street_position_ext_get(client):
    """Test case for search_version_number_reverse_geocode_cross_street_position_ext_get

    Cross Street lookup
    """
    params = [('limit', 1),
                    ('spatialKeys', False),
                    ('heading', 3.4),
                    ('radius', 10000),
                    ('language', 'language_example')]
    headers = { 
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/search/{version_number}/reverseGeocode/crossStreet/{position_ext}'.format(version_number=56, position='37.8328,-122.27669', ext='xml'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_version_number_reverse_geocode_position_ext_get(client):
    """Test case for search_version_number_reverse_geocode_position_ext_get

    Reverse Geocode
    """
    params = [('spatialKeys', False),
                    ('returnSpeedLimit', False),
                    ('heading', 3.4),
                    ('radius', 10000),
                    ('number', 'number_example'),
                    ('returnRoadUse', False),
                    ('roadUse', 'road_use_example'),
                    ('callback', 'cb')]
    headers = { 
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/search/{version_number}/reverseGeocode/{position_ext}'.format(version_number=56, position='37.8328,-122.27669', ext='xml'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

