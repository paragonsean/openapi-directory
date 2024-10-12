# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.auth_login import AuthLogin
from openapi_server.models.auth_refresh import AuthRefresh
from openapi_server.models.auth_reset_password import AuthResetPassword
from openapi_server.models.auth_tokens import AuthTokens
from openapi_server.models.default_error import DefaultError


pytestmark = pytest.mark.asyncio

async def test_auth_account_login(client):
    """Test case for auth_account_login

    Get a token using login+password
    """
    login_info = {"password":"password","appId":"appId","login":"login","ttl":1800}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/auth/login',
        headers=headers,
        json=login_info,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_auth_refresh_token(client):
    """Test case for auth_refresh_token

    Refresh a token
    """
    refresh_info = {"appId":"appId","refreshToken":"refreshToken"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/auth/refresh',
        headers=headers,
        json=refresh_info,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_auth_reset_password(client):
    """Test case for auth_reset_password

    Ask for a new password
    """
    reset_password_info = {"appId":"appId","login":"login","email":"email"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/auth/reset-password',
        headers=headers,
        json=reset_password_info,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_auth_revoke_token(client):
    """Test case for auth_revoke_token

    Revoke a token
    """
    headers = { 
        'Accept': 'application/json',
        'Token in query': 'special-key',
        'Token in Access-Token header': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/auth/revoke',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

