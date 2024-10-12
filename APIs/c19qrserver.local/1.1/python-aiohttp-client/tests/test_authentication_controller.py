# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.invalid_token import InvalidToken
from openapi_server.models.login_response import LoginResponse
from openapi_server.models.sample1 import Sample1


pytestmark = pytest.mark.asyncio

async def test_login_post(client):
    """Test case for login_post

    Log in to get an API token
    """
    body = openapi_server.Sample1()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/login',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_logout_post(client):
    """Test case for logout_post

    Log out
    """
    headers = { 
        'TokenHeader': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/logout',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

