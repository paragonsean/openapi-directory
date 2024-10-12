# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_get_health(client):
    """Test case for get_health

    Health
    """
    params = [('bundles', true),
                    ('plugins', false)]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/health',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

