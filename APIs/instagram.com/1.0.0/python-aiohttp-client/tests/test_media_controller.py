# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.media_entry_response import MediaEntryResponse
from openapi_server.models.media_search_response import MediaSearchResponse


pytestmark = pytest.mark.asyncio

async def test_media_media_id_get(client):
    """Test case for media_media_id_get

    Get information about a media object.
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/media/{media_id}'.format(media_id='media_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_media_popular_get(client):
    """Test case for media_popular_get

    Get a list of currently popular media.
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/media/popular',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_media_search_get(client):
    """Test case for media_search_get

    Search for media in a given area.
    """
    params = [('lat', 3.4),
                    ('lng', 3.4),
                    ('min_timestamp', 56),
                    ('max_timestamp', 56),
                    ('distance', 56)]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/media/search',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_media_shortcode_shortcode_get(client):
    """Test case for media_shortcode_shortcode_get

    Get information about a media object.
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/media/shortcode/{shortcode}'.format(shortcode='shortcode_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

