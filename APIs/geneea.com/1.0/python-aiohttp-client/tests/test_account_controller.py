# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_get_info(client):
    """Test case for get_info

    Information about current user account
    """
    headers = { 
        'Accept': 'application/json',
        'user_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/account',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

