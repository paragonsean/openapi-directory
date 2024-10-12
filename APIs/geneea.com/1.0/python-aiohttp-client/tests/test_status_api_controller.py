# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_status(client):
    """Test case for status

    Gets status of the Interpretor service
    """
    headers = { 
        'Accept': 'application/json',
        'user_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/status',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

