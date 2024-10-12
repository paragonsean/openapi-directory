# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.access_token_data import AccessTokenData
from openapi_server.models.device_code_data import DeviceCodeData
from openapi_server.models.simple_error import SimpleError


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_token(client):
    """Test case for create_token

    Create a new OAuth2 access token
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'grant_type': 'grant_type_example',
        'client_id': 'client_id_example',
        'client_secret': 'client_secret_example',
        'code': 'code_example',
        'redirect_uri': 'redirect_uri_example',
        'username': 'username_example',
        'password': 'password_example',
        'service': 'service_example',
        'refresh_token': 'refresh_token_example',
        'scope': 'scope_example',
        'token_type_hint': 'token_type_hint_example'
        }
    response = await client.request(
        method='POST',
        path='/v2/token',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_generate_device_code(client):
    """Test case for generate_device_code

    Initiate an OAuth2 login flow for limited input devices
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'client_id': 'client_id_example',
        'client_secret': 'client_secret_example',
        'scope': 'scope_example'
        }
    response = await client.request(
        method='POST',
        path='/v2/device',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_revoke_token(client):
    """Test case for revoke_token

    Revoke an existing OAuth2 access token
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'authorization': 'authorization_example',
    }
    data = {
        'token': 'token_example',
        'token_type_hint': 'token_type_hint_example'
        }
    response = await client.request(
        method='POST',
        path='/v2/token/revoke',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

