# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.ping_response import PingResponse


pytestmark = pytest.mark.asyncio

async def test_util_ping_get(client):
    """Test case for util_ping_get

    Ping
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/util/ping',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

