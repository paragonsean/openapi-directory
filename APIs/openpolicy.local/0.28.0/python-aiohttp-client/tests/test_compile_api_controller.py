# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.model400 import Model400
from openapi_server.models.post_compile200_response import PostCompile200Response


pytestmark = pytest.mark.asyncio

async def test_post_compile(client):
    """Test case for post_compile

    Compile
    """
    body = None
    params = [('pretty', true),
                    ('explain', 'full'),
                    ('metrics', false),
                    ('instrument', false)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/compile',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

