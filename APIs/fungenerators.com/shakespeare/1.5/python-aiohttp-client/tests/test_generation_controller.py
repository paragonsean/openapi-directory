# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_shakespeare_generate_insult_get(client):
    """Test case for shakespeare_generate_insult_get

    
    """
    params = [('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'X-Fungenerators-Api-Secret': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/shakespeare/generate/insult',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_shakespeare_generate_lorem_ipsum_get(client):
    """Test case for shakespeare_generate_lorem_ipsum_get

    
    """
    params = [('type', 'type_example'),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'X-Fungenerators-Api-Secret': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/shakespeare/generate/lorem-ipsum',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_shakespeare_generate_name_get(client):
    """Test case for shakespeare_generate_name_get

    
    """
    params = [('variation', 'variation_example'),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'X-Fungenerators-Api-Secret': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/shakespeare/generate/name',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

