# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.joke_of_the_day_response import JokeOfTheDayResponse


pytestmark = pytest.mark.asyncio

async def test_jod_categories_get(client):
    """Test case for jod_categories_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'X-JokesOne-Api-Secret': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/jod/categories',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_jod_get(client):
    """Test case for jod_get

    
    """
    params = [('category', 'category_example')]
    headers = { 
        'Accept': 'application/json',
        'X-JokesOne-Api-Secret': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/jod',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

