# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_cast_info_detailed_info(client):
    """Test case for cast_info_detailed_info

    
    """
    headers = { 
        'key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/public/v1.0/movies/{id}/cast.json'.format(id='770672122'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_movie_clips_detailed_info(client):
    """Test case for movie_clips_detailed_info

    
    """
    headers = { 
        'key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/public/v1.0/movies/{id}/clips.json'.format(id='770672122'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_movies_alias_detailed_info(client):
    """Test case for movies_alias_detailed_info

    
    """
    params = [('id', '0031381'),
                    ('type', 'imdb')]
    headers = { 
        'key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/public/v1.0/movie_alias.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_movies_info_detailed_info(client):
    """Test case for movies_info_detailed_info

    
    """
    headers = { 
        'key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/public/v1.0/movies/{id_jso}'.format(id='770672122'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_movies_reviews_detailed_info(client):
    """Test case for movies_reviews_detailed_info

    
    """
    params = [('review_type', 'top_critic'),
                    ('page_limit', '20'),
                    ('page', '1'),
                    ('country', 'us')]
    headers = { 
        'key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/public/v1.0/movies/{id}/reviews.json'.format(id='770672122'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_movies_similar_detailed_info(client):
    """Test case for movies_similar_detailed_info

    
    """
    params = [('limit', '5')]
    headers = { 
        'key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/public/v1.0/movies/{id}/similar.json'.format(id='770672122'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

