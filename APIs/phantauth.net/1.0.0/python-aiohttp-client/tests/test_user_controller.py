# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.user_post_request import UserPostRequest
from openapi_server.models.user_username_get200_response import UserUsernameGet200Response


pytestmark = pytest.mark.asyncio

async def test_user_post(client):
    """Test case for user_post

    Create a User Selfie
    """
    body = openapi_server.UserPostRequest()
    headers = { 
        'Accept': 'text/plain',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/user',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_user_username_get(client):
    """Test case for user_username_get

    Get a User
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/user/{username}'.format(username='username_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_user_username_token_kind_get(client):
    """Test case for user_username_token_kind_get

    Get a User Token
    """
    params = [('scope', 'scope_example')]
    headers = { 
        'Accept': 'text/plain',
    }
    response = await client.request(
        method='GET',
        path='/user/{username}/token/{kind}'.format(username='username_example', kind='kind_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

