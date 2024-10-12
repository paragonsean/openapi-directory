# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_stats_get(client):
    """Test case for stats_get

    Gets status on the ISBNDB Database
    """
    headers = { 
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/stats',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

