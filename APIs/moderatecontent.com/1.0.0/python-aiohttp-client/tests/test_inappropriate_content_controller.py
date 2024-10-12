# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_root_get(client):
    """Test case for root_get

    Blocks images with nudity
    """
    params = [('url', 'url_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/moderate/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

