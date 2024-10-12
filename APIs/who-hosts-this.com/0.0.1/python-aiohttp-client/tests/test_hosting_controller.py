# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_detect_get(client):
    """Test case for detect_get

    Discover the hosting provider for a web site
    """
    params = [('url', 'url_example')]
    headers = { 
        'QueryKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/APIEndpoint/Detect',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

