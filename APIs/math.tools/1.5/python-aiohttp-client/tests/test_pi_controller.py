# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_numbers_pi_get(client):
    """Test case for numbers_pi_get

    
    """
    params = [('from', 56),
                    ('to', 56)]
    headers = { 
        'Accept': 'application/json',
        'X-Mathtools-Api-Secret': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/numbers/pi',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

