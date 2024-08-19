# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_box_office_movie_lists(client):
    """Test case for box_office_movie_lists

    
    """
    params = [('limit', '16'),
                    ('country', 'us')]
    headers = { 
        'key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/public/v1.0/lists/movies/box_office.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_in_theaters_movie_lists(client):
    """Test case for in_theaters_movie_lists

    
    """
    params = [('page_limit', '16'),
                    ('page', '1'),
                    ('country', 'us')]
    headers = { 
        'key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/public/v1.0/lists/movies/in_theaters.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_opening_movies_movie_lists(client):
    """Test case for opening_movies_movie_lists

    
    """
    params = [('limit', '16'),
                    ('country', 'us')]
    headers = { 
        'key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/public/v1.0/lists/movies/opening.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_upcoming_movies_movie_lists(client):
    """Test case for upcoming_movies_movie_lists

    
    """
    params = [('page_limit', '16'),
                    ('page', '1'),
                    ('country', 'us')]
    headers = { 
        'key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/public/v1.0/lists/movies/upcoming.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

