# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.body4 import Body4
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_my_plays_post(client):
    """Test case for my_plays_post

    Write Play Event
    """
    body = openapi_server.Body4()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'Bearer OAUTH_TOKEN',
        'x_api_key': 'x_api_key_example',
    }
    response = await client.request(
        method='POST',
        path='/my/plays',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

