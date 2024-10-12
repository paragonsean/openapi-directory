# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_health_check_ping_get(client):
    """Test case for health_check_ping_get

    Health check for API
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/health-check/ping',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

