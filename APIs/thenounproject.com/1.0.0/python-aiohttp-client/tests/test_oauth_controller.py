# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_get_api_quota_status(client):
    """Test case for get_api_quota_status

    Get api quota status
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/oauth/usage',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

