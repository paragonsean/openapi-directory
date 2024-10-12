# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_gifs_by_id200_response import GetGifsById200Response
from openapi_server.models.random_gif200_response import RandomGif200Response


pytestmark = pytest.mark.asyncio

async def test_get_gif_by_id(client):
    """Test case for get_gif_by_id

    Get GIF by Id
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/gifs/{gif_id}'.format(gif_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_gifs_by_id(client):
    """Test case for get_gifs_by_id

    Get GIFs by ID
    """
    params = [('ids', 'ids_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/gifs',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_random_gif(client):
    """Test case for random_gif

    Random GIF
    """
    params = [('tag', 'tag_example'),
                    ('rating', 'rating_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/gifs/random',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_gifs(client):
    """Test case for search_gifs

    Search GIFs
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
        path='/v1/gifs/search',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_translate_gif(client):
    """Test case for translate_gif

    Translate phrase to GIF
    """
    params = [('s', 's_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/gifs/translate',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_trending_gifs(client):
    """Test case for trending_gifs

    Trending GIFs
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
        path='/v1/gifs/trending',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

