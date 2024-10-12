# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_g_etv1_ping_format(client):
    """Test case for g_etv1_ping_format

    Returns whether the system is up.
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v1/ping.json',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

