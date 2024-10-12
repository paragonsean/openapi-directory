# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_taunt_categories_get(client):
    """Test case for taunt_categories_get

    
    """
    params = [('start', 56),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'X-Fungenerators-Api-Secret': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/taunt/categories',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_taunt_generate_get(client):
    """Test case for taunt_generate_get

    
    """
    params = [('category', 'category_example'),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'X-Fungenerators-Api-Secret': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/taunt/generate',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

