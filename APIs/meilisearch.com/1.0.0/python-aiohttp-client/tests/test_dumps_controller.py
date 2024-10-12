# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_create_a_dump(client):
    """Test case for create_a_dump

    Create a dump
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/dumps',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

