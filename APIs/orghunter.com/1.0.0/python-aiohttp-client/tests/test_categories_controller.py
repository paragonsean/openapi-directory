# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_get_categories(client):
    """Test case for get_categories

    Get categories!
    """
    headers = { 
        'user_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/categories',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

