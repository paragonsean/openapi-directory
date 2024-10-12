# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_v1_charitypremium_post(client):
    """Test case for v1_charitypremium_post

    Get details!
    """
    params = [('ein', 'ein_example')]
    headers = { 
        'user_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/charitypremium',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

