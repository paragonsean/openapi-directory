# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.access_token import AccessToken
from openapi_server.models.access_token_description import AccessTokenDescription
from openapi_server.models.error import Error
from openapi_server.models.multi_access_tokens import MultiAccessTokens
from openapi_server.models.user import User


pytestmark = pytest.mark.asyncio

async def test_admin_user_self_access_token_access_token_key_delete(client):
    """Test case for admin_user_self_access_token_access_token_key_delete

    Delete the specified access token.
    """
    params = [('checksum', '9cd24183-f848-48f8-6f55-0f07240700b9')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1.0/admin/user/self/access_token/{access_token_key}'.format(access_token_key='9cd24183-f848-48f8-6f55-0f0724070000'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_admin_user_self_access_tokens_get(client):
    """Test case for admin_user_self_access_tokens_get

    Lists Access Tokens that are configured for the authenticated user.
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1.0/admin/user/self/access_tokens',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_admin_user_self_access_tokens_post(client):
    """Test case for admin_user_self_access_tokens_post

    Creates a new Access Token and associates it with the authenticated user.
    """
    description = {"description":"description"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1.0/admin/user/self/access_tokens',
        headers=headers,
        json=description,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_admin_user_self_get(client):
    """Test case for admin_user_self_get

    Returns the user object for the account authorized and making this request.
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1.0/admin/user/self',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

