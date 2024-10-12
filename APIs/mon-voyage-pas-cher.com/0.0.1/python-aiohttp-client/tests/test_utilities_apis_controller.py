# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.pong_response import PongResponse


pytestmark = pytest.mark.asyncio

async def test_get_ping(client):
    """Test case for get_ping

    
    """
    headers = { 
        'Accept': 'application/json',
        'x-api-key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/pong',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

