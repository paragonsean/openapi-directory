# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.parserequest import Parserequest


pytestmark = pytest.mark.asyncio

async def test_parse(client):
    """Test case for parse

    Extract structured data from web pages
    """
    body = openapi_server.Parserequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/parse',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

