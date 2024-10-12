# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.request_body import RequestBody


pytestmark = pytest.mark.asyncio

async def test_sessions_post(client):
    """Test case for sessions_post

    Update Order Configuration
    """
    body = openapi_server.RequestBody()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/sessions/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

