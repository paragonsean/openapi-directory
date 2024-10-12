# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.ping_get200_response import PingGet200Response


pytestmark = pytest.mark.asyncio

async def test_ping_get(client):
    """Test case for ping_get

    Check if API is up and API key works
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/ping',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

