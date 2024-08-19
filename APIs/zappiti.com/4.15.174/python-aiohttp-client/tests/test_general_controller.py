# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.connection_details_request import ConnectionDetailsRequest
from openapi_server.models.connection_details_result import ConnectionDetailsResult
from openapi_server.models.is_alive_request import IsAliveRequest
from openapi_server.models.is_alive_result import IsAliveResult


pytestmark = pytest.mark.asyncio

async def test_connection_details_post(client):
    """Test case for connection_details_post

    Get user's login details
    """
    body = {"ApiKey":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/ConnectionDetails',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_is_alive_post(client):
    """Test case for is_alive_post

    Get server status
    """
    body = {"ApiKey":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/IsAlive',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

