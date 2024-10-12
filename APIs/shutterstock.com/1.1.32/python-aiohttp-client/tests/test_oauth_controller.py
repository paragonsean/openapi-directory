# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_access_token_request import CreateAccessTokenRequest
from openapi_server.models.create_access_token_request1 import CreateAccessTokenRequest1
from openapi_server.models.oauth_access_token_response import OauthAccessTokenResponse


pytestmark = pytest.mark.asyncio

async def test_authorize(client):
    """Test case for authorize

    Authorize applications
    """
    params = [('client_id', '6d097450b209c6dcd859'),
                    ('realm', customer),
                    ('redirect_uri', 'localhost'),
                    ('response_type', 'code'),
                    ('scope', 'user.view'),
                    ('state', '1540290465000')]
    headers = { 
        'Accept': 'text/html',
    }
    response = await client.request(
        method='GET',
        path='/v2/oauth/authorize',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_create_access_token(client):
    """Test case for create_access_token

    Get access tokens
    """
    body = {"client_id":"141024g14g28104gff1h"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/oauth/access_token',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

