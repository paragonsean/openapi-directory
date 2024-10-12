# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.fetchrequest import Fetchrequest


pytestmark = pytest.mark.asyncio

async def test_fetch(client):
    """Test case for fetch

    Download web page content
    """
    body = openapi_server.Fetchrequest()
    headers = { 
        'Accept': 'text/plain; charset=utf-8',
        'Content-Type': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/fetch',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

