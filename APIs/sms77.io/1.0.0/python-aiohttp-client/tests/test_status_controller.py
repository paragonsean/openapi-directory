# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_status(client):
    """Test case for status

    
    """
    params = [('msg_id', 'msg_id_example')]
    headers = { 
        'Accept': 'text/plain',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/status',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

