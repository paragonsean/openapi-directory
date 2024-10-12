# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_server_health200_response import GetServerHealth200Response


pytestmark = pytest.mark.asyncio

async def test_get_heartbeat(client):
    """Test case for get_heartbeat

    Ping the server for liveness
    """
    headers = { 
        'Accept': 'text/plain',
    }
    response = await client.request(
        method='GET',
        path='/heartbeat',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_server_health(client):
    """Test case for get_server_health

    Get state of the server and its dependencies.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/health',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

