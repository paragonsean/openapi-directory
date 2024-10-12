# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_name_categories_get(client):
    """Test case for name_categories_get

    
    """
    params = [('start', 56),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'X-Fungenerators-Api-Secret': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/name/categories',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_name_generate_get(client):
    """Test case for name_generate_get

    
    """
    params = [('category', 'category_example'),
                    ('suggest', 'suggest_example'),
                    ('start', 56),
                    ('limit', 56),
                    ('variation', 'variation_example')]
    headers = { 
        'Accept': 'application/json',
        'X-Fungenerators-Api-Secret': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/name/generate',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

