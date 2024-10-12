# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.artists_image_search_field_values import ArtistsImageSearchFieldValues
from openapi_server.models.artists_video_search_field_values import ArtistsVideoSearchFieldValues


pytestmark = pytest.mark.asyncio

async def test_v3_artists_images_get(client):
    """Test case for v3_artists_images_get

    Search for images by a photographer
    """
    params = [('artist_name', 'artist_name_example'),
                    ('fields', [openapi_server.ArtistsImageSearchFieldValues()]),
                    ('page', 1),
                    ('page_size', 10)]
    headers = { 
        'accept_language': 'accept_language_example',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Api-Key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/artists/images',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v3_artists_videos_get(client):
    """Test case for v3_artists_videos_get

    Search for videos by a photographer
    """
    params = [('artist_name', 'artist_name_example'),
                    ('fields', [openapi_server.ArtistsVideoSearchFieldValues()]),
                    ('page', 1),
                    ('page_size', 10)]
    headers = { 
        'accept_language': 'accept_language_example',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Api-Key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/artists/videos',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

