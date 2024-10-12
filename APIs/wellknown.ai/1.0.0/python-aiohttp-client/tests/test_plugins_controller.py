# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_get_provider(client):
    """Test case for get_provider

    List all the Wellknown AI Plugins.
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/plugins',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

