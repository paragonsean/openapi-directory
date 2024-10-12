# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_uuid_post(client):
    """Test case for uuid_post

    
    """
    params = [('uuidstr', 'uuidstr_example')]
    headers = { 
        'Accept': 'application/json',
        'X-Fungenerators-Api-Secret': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/uuid',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

