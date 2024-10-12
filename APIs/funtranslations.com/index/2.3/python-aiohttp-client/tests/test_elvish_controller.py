# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_translate_quneya_get(client):
    """Test case for translate_quneya_get

    
    """
    params = [('text', 'text_example')]
    headers = { 
        'Accept': 'application/json',
        'X-Funtranslations-Api-Secret': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/translate/quneya',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_translate_sindarin_get(client):
    """Test case for translate_sindarin_get

    
    """
    params = [('text', 'text_example')]
    headers = { 
        'Accept': 'application/json',
        'X-Funtranslations-Api-Secret': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/translate/sindarin',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

