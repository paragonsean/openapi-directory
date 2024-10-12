# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.serprequest import Serprequest


pytestmark = pytest.mark.asyncio

async def test_serp(client):
    """Test case for serp

    Collect search results from search engines
    """
    body = openapi_server.Serprequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/serp',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

