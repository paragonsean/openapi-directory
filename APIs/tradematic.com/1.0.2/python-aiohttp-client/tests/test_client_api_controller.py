# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_key import APIKey
from openapi_server.models.client_apikeys_keyid_delete200_response import ClientApikeysKeyidDelete200Response
from openapi_server.models.client_apikeys_post200_response import ClientApikeysPost200Response
from openapi_server.models.client_users_login_post200_response import ClientUsersLoginPost200Response
from openapi_server.models.client_users_register_post200_response import ClientUsersRegisterPost200Response
from openapi_server.models.client_users_register_post_request import ClientUsersRegisterPostRequest
from openapi_server.models.error import Error
from openapi_server.models.user import User


pytestmark = pytest.mark.asyncio

async def test_client_apikeys_get(client):
    """Test case for client_apikeys_get

    Get API keys
    """
    headers = { 
        'Accept': 'application/json',
        'Secured': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/client/apikeys',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_client_apikeys_keyid_delete(client):
    """Test case for client_apikeys_keyid_delete

    Delete API key
    """
    headers = { 
        'Accept': 'application/json',
        'Secured': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/client/apikeys/{keyid}'.format(keyid=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_client_apikeys_post(client):
    """Test case for client_apikeys_post

    Create new API key
    """
    headers = { 
        'Accept': 'application/json',
        'Secured': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/client/apikeys',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_client_users_get(client):
    """Test case for client_users_get

    Get users list
    """
    headers = { 
        'Accept': 'application/json',
        'Secured': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/client/users',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_client_users_login_post(client):
    """Test case for client_users_login_post

    Logs user into the system
    """
    headers = { 
        'Accept': 'application/json',
        'Secured': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/client/users/login',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_client_users_register_post(client):
    """Test case for client_users_register_post

    Register a new user
    """
    body = openapi_server.ClientUsersRegisterPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Secured': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/client/users/register',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_client_users_userid_get(client):
    """Test case for client_users_userid_get

    Get user by ID
    """
    headers = { 
        'Accept': 'application/json',
        'Secured': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/client/users/{userid}'.format(userid=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

