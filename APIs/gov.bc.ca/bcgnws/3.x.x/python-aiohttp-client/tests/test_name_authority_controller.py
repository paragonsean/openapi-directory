# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_name_authorities_get(client):
    """Test case for name_authorities_get

    Get all name authorities
    """
    params = [('outputFormat', json)]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/pub/bcgnws/nameAuthorities',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

