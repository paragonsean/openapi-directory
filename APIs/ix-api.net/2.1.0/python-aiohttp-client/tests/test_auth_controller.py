# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.accounts_list400_response import AccountsList400Response
from openapi_server.models.auth_token import AuthToken
from openapi_server.models.auth_token_refresh401_response import AuthTokenRefresh401Response
from openapi_server.models.auth_token_request import AuthTokenRequest
from openapi_server.models.refresh_token_request import RefreshTokenRequest


pytestmark = pytest.mark.asyncio

async def test_auth_token_create(client):
    """Test case for auth_token_create

    
    """
    body = {"api_key":"api_key","api_secret":"api_secret"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/auth/token',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_auth_token_refresh(client):
    """Test case for auth_token_refresh

    
    """
    body = {"refresh_token":"refresh_token"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/auth/refresh',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

