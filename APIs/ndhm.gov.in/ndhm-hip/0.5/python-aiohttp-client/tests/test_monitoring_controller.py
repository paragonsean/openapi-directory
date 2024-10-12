# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.heartbeat_response import HeartbeatResponse


pytestmark = pytest.mark.asyncio

async def test_v05_heartbeat_get(client):
    """Test case for v05_heartbeat_get

    Get consent request status
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/gateway/v0.5/heartbeat',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

