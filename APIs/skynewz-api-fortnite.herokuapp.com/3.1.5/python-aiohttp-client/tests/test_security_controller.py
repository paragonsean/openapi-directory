# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.oauth_token_post200_response import OauthTokenPost200Response
from openapi_server.models.oauth_token_post401_response import OauthTokenPost401Response


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_oauth_token_post(client):
    """Test case for oauth_token_post

    Get a Bearer token
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'email': 'email_example',
        'password': 'password_example'
        }
    response = await client.request(
        method='POST',
        path='/api/oauth/token',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

