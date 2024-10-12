# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_models_authenticated_user import APIModelsAuthenticatedUser
from openapi_server.models.api_models_credentials import APIModelsCredentials
from openapi_server.models.api_models_password_reset import APIModelsPasswordReset
from openapi_server.models.api_models_password_reset_request import APIModelsPasswordResetRequest
from openapi_server.models.api_models_token_options import APIModelsTokenOptions


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_authentication_default(client):
    """Test case for authentication_default

    Authenticate a user.
    """
    body = openapi_server.APIModelsCredentials()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/Authentication',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_authentication_is_alive(client):
    """Test case for authentication_is_alive

    Acknowledges the connection to the API
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/v2/Authentication/IsAlive',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_authentication_put_manage_tokens(client):
    """Test case for authentication_put_manage_tokens

    Manage API tokens.
    """
    body = openapi_server.APIModelsTokenOptions()
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v2/AuthenticatedUsers/{user_id}/Tokens'.format(user_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_authentication_request_password_reset(client):
    """Test case for authentication_request_password_reset

    Request a password reset.
    """
    body = openapi_server.APIModelsPasswordResetRequest()
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/Authentication/RequestPasswordReset',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_authentication_reset_pasword(client):
    """Test case for authentication_reset_pasword

    Reset a password
    """
    body = openapi_server.APIModelsPasswordReset()
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/Authentication/ResetPasword',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

