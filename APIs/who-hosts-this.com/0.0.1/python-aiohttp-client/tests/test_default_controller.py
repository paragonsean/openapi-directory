# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_status_get(client):
    """Test case for status_get

    View usage details for the current billing period
    """
    headers = { 
        'QueryKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/APIEndpoint/Status',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

