# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_token_request import CreateTokenRequest
from openapi_server.models.token import Token


pytestmark = pytest.mark.asyncio

async def test_all_tokens(client):
    """Test case for all_tokens

    All tokens for current user
    """
    headers = { 
        'Accept': 'application/json',
        'HeaderSignature': 'special-key',
        'QueryKey': 'special-key',
        'HeaderKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/{username}/tokens'.format(username='username_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_create_token(client):
    """Test case for create_token

    Create a new Token
    """
    token = openapi_server.CreateTokenRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'HeaderSignature': 'special-key',
        'QueryKey': 'special-key',
        'HeaderKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/{username}/tokens'.format(username='username_example'),
        headers=headers,
        json=token,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_destroy_token(client):
    """Test case for destroy_token

    Delete an existing Token
    """
    headers = { 
        'Accept': 'application/json',
        'HeaderSignature': 'special-key',
        'QueryKey': 'special-key',
        'HeaderKey': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v2/{username}/tokens/{id}'.format(username='username_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_token(client):
    """Test case for get_token

    Returns Token based on ID
    """
    headers = { 
        'Accept': 'application/json',
        'HeaderSignature': 'special-key',
        'QueryKey': 'special-key',
        'HeaderKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/{username}/tokens/{id}'.format(username='username_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_replace_token(client):
    """Test case for replace_token

    Replace an existing Token
    """
    token = openapi_server.CreateTokenRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'HeaderSignature': 'special-key',
        'QueryKey': 'special-key',
        'HeaderKey': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v2/{username}/tokens/{id}'.format(username='username_example', id='id_example'),
        headers=headers,
        json=token,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_update_token(client):
    """Test case for update_token

    Update properties of an existing Token
    """
    token = openapi_server.CreateTokenRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'HeaderSignature': 'special-key',
        'QueryKey': 'special-key',
        'HeaderKey': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v2/{username}/tokens/{id}'.format(username='username_example', id='id_example'),
        headers=headers,
        json=token,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

