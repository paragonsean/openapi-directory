# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_auth_oauth_token_post(client):
    """Test case for auth_oauth_token_post

    Send client credentials and get an access token.
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'client_id': 'client_id_example',
        'client_secret': 'client_secret_example',
        'grant_type': 'client_credentials',
        'scope': 'verse chapter'
        }
    response = await client.request(
        method='POST',
        path='/auth/oauth/token',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

