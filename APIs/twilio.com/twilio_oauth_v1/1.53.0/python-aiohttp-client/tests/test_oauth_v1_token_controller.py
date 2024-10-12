# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.oauth_v1_token import OauthV1Token


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_token(client):
    """Test case for create_token

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'client_secret': 'client_secret_example',
        'client_sid': 'client_sid_example',
        'code': 'code_example',
        'code_verifier': 'code_verifier_example',
        'device_code': 'device_code_example',
        'device_id': 'device_id_example',
        'grant_type': 'grant_type_example',
        'refresh_token': 'refresh_token_example'
        }
    response = await client.request(
        method='POST',
        path='/v1/token',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

