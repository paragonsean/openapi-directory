# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_users_usage_get(client):
    """Test case for users_usage_get

    Get API usuage details
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/v1/users/usage',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

