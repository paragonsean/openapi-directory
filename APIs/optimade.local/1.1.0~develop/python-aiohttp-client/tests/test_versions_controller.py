# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_get_versions_versions_get(client):
    """Test case for get_versions_versions_get

    Get Versions
    """
    headers = { 
        'Accept': 'text/csv; header=present',
    }
    response = await client.request(
        method='GET',
        path='/versions',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

