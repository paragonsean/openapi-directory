# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.location_info_response import LocationInfoResponse
from openapi_server.models.location_search_response import LocationSearchResponse
from openapi_server.models.media_list_response import MediaListResponse


pytestmark = pytest.mark.asyncio

async def test_locations_location_id_get(client):
    """Test case for locations_location_id_get

    Get information about a location.
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/locations/{location_id}'.format(location_id='location_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_locations_location_id_media_recent_get(client):
    """Test case for locations_location_id_media_recent_get

    Get a list of recent media objects from a given location.
    """
    params = [('min_timestamp', 56),
                    ('max_timestamp', 56),
                    ('min_id', 'min_id_example'),
                    ('max_id', 'max_id_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/locations/{location_id}/media/recent'.format(location_id='location_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_locations_search_get(client):
    """Test case for locations_search_get

    Search for a location by geographic coordinate.
    """
    params = [('distance', 56),
                    ('facebook_places_id', 'facebook_places_id_example'),
                    ('foursquare_id', 'foursquare_id_example'),
                    ('lat', 3.4),
                    ('lng', 3.4),
                    ('foursquare_v2_id', 'foursquare_v2_id_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/locations/search',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

