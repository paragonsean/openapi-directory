# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_get_health(client):
    """Test case for get_health

    Get health of Tune-in service (which includes its uptime).
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/health',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

