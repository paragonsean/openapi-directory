# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.generate_access_token_response import GenerateAccessTokenResponse


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_generate_token_v2(client):
    """Test case for generate_token_v2

    Generate an OAuth Token
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'assertion': 'assertion_example',
        'grant_type': 'grant_type_example',
        'refresh_token': 'refresh_token_example',
        'scope': 'scope_example',
        'valid_for': 60
        }
    response = await client.request(
        method='POST',
        path='/v2/oauth2/token',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_revoke_refresh_token_v2(client):
    """Test case for revoke_refresh_token_v2

    Delete a Refresh Token
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v2/oauth2/tokens/{token}'.format(token='SOME_REFRESH_TOKEN'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

