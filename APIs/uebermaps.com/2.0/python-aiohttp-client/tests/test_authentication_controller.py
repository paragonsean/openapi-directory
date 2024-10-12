# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.user_authentication import UserAuthentication
from openapi_server.models.user_full_profile import UserFullProfile


pytestmark = pytest.mark.asyncio

async def test_authentication_post(client):
    """Test case for authentication_post

    Sign in user
    """
    user = {"password":"••••••••","email":"a@b.com"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/authentication',
        headers=headers,
        json=user,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

