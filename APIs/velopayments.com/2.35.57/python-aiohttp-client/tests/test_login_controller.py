# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.access_token_response import AccessTokenResponse
from openapi_server.models.access_token_validation_request import AccessTokenValidationRequest
from openapi_server.models.auth_response import AuthResponse
from openapi_server.models.inline_response400 import InlineResponse400
from openapi_server.models.inline_response401 import InlineResponse401
from openapi_server.models.inline_response403 import InlineResponse403
from openapi_server.models.reset_password_request import ResetPasswordRequest


pytestmark = pytest.mark.asyncio

async def test_logout(client):
    """Test case for logout

    Logout
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/logout',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reset_password(client):
    """Test case for reset_password

    Reset password
    """
    body = {"email":"foo@example.com"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/password/reset',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_validate_access_token(client):
    """Test case for validate_access_token

    validate
    """
    body = {"otp":"123456"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'authorization_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/validate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_velo_auth(client):
    """Test case for velo_auth

    Authentication endpoint
    """
    params = [('grant_type', 'client_credentials')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/v1/authenticate',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

