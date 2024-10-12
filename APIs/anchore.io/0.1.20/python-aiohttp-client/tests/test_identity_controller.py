# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.access_credential import AccessCredential
from openapi_server.models.account import Account
from openapi_server.models.api_error_response import ApiErrorResponse
from openapi_server.models.user import User


pytestmark = pytest.mark.asyncio

async def test_add_credential(client):
    """Test case for add_credential

    add/replace credential
    """
    body = {"created_at":"created_at","type":"password","value":"value"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/user/credentials',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_credentials(client):
    """Test case for get_credentials

    Get current credential summary
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/user/credentials',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_user(client):
    """Test case for get_user

    List authenticated user info
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/user',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_users_account(client):
    """Test case for get_users_account

    List the account for the authenticated user
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/account',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

