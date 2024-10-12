# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_translate_ermahgerd_get(client):
    """Test case for translate_ermahgerd_get

    
    """
    params = [('text', 'text_example')]
    headers = { 
        'Accept': 'application/json',
        'X-Funtranslations-Api-Secret': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/translate/ermahgerd',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

