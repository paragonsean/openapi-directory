# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.access_token import AccessToken
from openapi_server.models.authenticate_payload import AuthenticatePayload
from openapi_server.models.bad_request import BadRequest
from openapi_server.models.refresh_token_payload import RefreshTokenPayload


pytestmark = pytest.mark.asyncio

async def test_p_ost_auth_api_key(client):
    """Test case for p_ost_auth_api_key

    Authenticate
    """
    body = openapi_server.AuthenticatePayload()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/auth/api-key',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_p_ost_auth_refresh(client):
    """Test case for p_ost_auth_refresh

    Refresh token
    """
    body = openapi_server.RefreshTokenPayload()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/auth/refresh',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

