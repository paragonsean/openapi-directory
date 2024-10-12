# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_api_plugins_get(client):
    """Test case for api_plugins_get

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/api/plugins',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

