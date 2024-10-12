# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.time_get200_response import TimeGet200Response


pytestmark = pytest.mark.asyncio

async def test_ping_get(client):
    """Test case for ping_get

    Ping
    """
    headers = { 
        'Accept': 'application/json',
        'Secured': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/ping',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_time_get(client):
    """Test case for time_get

    Get current server time
    """
    headers = { 
        'Accept': 'application/json',
        'Secured': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/time',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

