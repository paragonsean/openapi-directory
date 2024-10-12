# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_gifs_by_id200_response import GetGifsById200Response
from openapi_server.models.random_gif200_response import RandomGif200Response


pytestmark = pytest.mark.asyncio

async def test_random_sticker(client):
    """Test case for random_sticker

    Random Sticker
    """
    params = [('tag', 'tag_example'),
                    ('rating', 'rating_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/stickers/random',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_stickers(client):
    """Test case for search_stickers

    Search Stickers
    """
    params = [('q', 'q_example'),
                    ('limit', 25),
                    ('offset', 0),
                    ('rating', 'rating_example'),
                    ('lang', 'lang_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/stickers/search',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_translate_sticker(client):
    """Test case for translate_sticker

    Translate phrase to Sticker
    """
    params = [('s', 's_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/stickers/translate',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_trending_stickers(client):
    """Test case for trending_stickers

    Trending Stickers
    """
    params = [('limit', 25),
                    ('offset', 0),
                    ('rating', 'rating_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/stickers/trending',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

