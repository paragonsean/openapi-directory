# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_numbers_nod_get(client):
    """Test case for numbers_nod_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'X-Mathtools-Api-Secret': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/numbers/nod',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

