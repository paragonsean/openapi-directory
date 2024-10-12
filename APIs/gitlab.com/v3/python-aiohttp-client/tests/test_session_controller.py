# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.post_v3_session_request import PostV3SessionRequest
from openapi_server.models.user_with_private_token import UserWithPrivateToken


pytestmark = pytest.mark.asyncio

async def test_post_v3_session(client):
    """Test case for post_v3_session

    Login to get token
    """
    body = openapi_server.PostV3SessionRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/session',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

