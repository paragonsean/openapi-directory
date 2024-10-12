# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.category_object import CategoryObject
from openapi_server.models.get_categories200_response import GetCategories200Response
from openapi_server.models.get_multiple_albums401_response import GetMultipleAlbums401Response
from openapi_server.models.paging_featured_playlist_object import PagingFeaturedPlaylistObject


pytestmark = pytest.mark.asyncio

async def test_get_a_categories_playlists_0(client):
    """Test case for get_a_categories_playlists_0

    Get Category's Playlists 
    """
    params = [('country', 'SE'),
                    ('limit', 20),
                    ('offset', 0)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/browse/categories/{category_id}/playlists'.format(category_id='dinner'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_a_category(client):
    """Test case for get_a_category

    Get Single Browse Category 
    """
    params = [('country', 'SE'),
                    ('locale', 'sv_SE')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/browse/categories/{category_id}'.format(category_id='dinner'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_categories(client):
    """Test case for get_categories

    Get Several Browse Categories 
    """
    params = [('country', 'SE'),
                    ('locale', 'sv_SE'),
                    ('limit', 20),
                    ('offset', 0)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/browse/categories',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

