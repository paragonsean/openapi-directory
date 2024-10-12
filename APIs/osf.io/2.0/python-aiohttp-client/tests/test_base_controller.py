# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_base_read(client):
    """Test case for base_read

    Root
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v2/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

