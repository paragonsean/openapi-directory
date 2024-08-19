# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_d_vd_lists_directory_top_level_lists(client):
    """Test case for d_vd_lists_directory_top_level_lists

    
    """
    headers = { 
        'key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/public/v1.0/lists/dvds.json',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_lists_directory_top_level_lists(client):
    """Test case for lists_directory_top_level_lists

    
    """
    headers = { 
        'key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/public/v1.0/lists.json',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_movie_lists_directory_top_level_lists(client):
    """Test case for movie_lists_directory_top_level_lists

    
    """
    headers = { 
        'key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/public/v1.0/lists/movies.json',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

