# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.exchange_refresh_token_for_access_token_request import ExchangeRefreshTokenForAccessTokenRequest
from openapi_server.models.revoke_an_access_token_request import RevokeAnAccessTokenRequest


pytestmark = pytest.mark.asyncio

async def test_authorize_application(client):
    """Test case for authorize_application

    Authorize Application
    """
    body = 'body_example'
    params = [('response_type', 'code'),
                    ('client_id', ' '),
                    ('redirect_uri', ' '),
                    ('state', ' ')]
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/oauth/authorize',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_exchange_refresh_token_for_access_token(client):
    """Test case for exchange_refresh_token_for_access_token

    Exchange refresh_token for access_token
    """
    body = openapi_server.ExchangeRefreshTokenForAccessTokenRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/oauth/token',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_revoke_an_access_token(client):
    """Test case for revoke_an_access_token

    Revoke an access_token
    """
    body = openapi_server.RevokeAnAccessTokenRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/oauth/revoke',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

