# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.user import User
from openapi_server.models.user_collection import UserCollection
from openapi_server.models.user_definition import UserDefinition


pytestmark = pytest.mark.asyncio

async def test_create_users(client):
    """Test case for create_users

    Create User
    """
    body = {"password":"password","displayName":"displayName","timezone":"timezone","name":{"familyName":"familyName","givenName":"givenName"},"locale":"locale","userName":"userName"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='POST',
        path='/identity/v1/Users',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_user(client):
    """Test case for delete_user

    Delete User
    """
    headers = { 
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='DELETE',
        path='/identity/v1/Users/{user_key}'.format(user_key=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_me(client):
    """Test case for get_me

    Get Current User
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='GET',
        path='/identity/v1/Users/me',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_user(client):
    """Test case for get_user

    Get User
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='GET',
        path='/identity/v1/Users/{user_key}'.format(user_key=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_users(client):
    """Test case for get_users

    Get Users
    """
    params = [('filter', 'filter_example')]
    headers = { 
        'Accept': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='GET',
        path='/identity/v1/Users',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_replace_me(client):
    """Test case for replace_me

    Replace Current User
    """
    body = {"password":"password","displayName":"displayName","timezone":"timezone","name":{"familyName":"familyName","givenName":"givenName"},"locale":"locale","userName":"userName"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='PUT',
        path='/identity/v1/Users/me',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_replace_user(client):
    """Test case for replace_user

    Replace User
    """
    body = {"password":"password","displayName":"displayName","timezone":"timezone","name":{"familyName":"familyName","givenName":"givenName"},"locale":"locale","userName":"userName"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='PUT',
        path='/identity/v1/Users/{user_key}'.format(user_key=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_me(client):
    """Test case for update_me

    Update Current User
    """
    body = {"password":"password","displayName":"displayName","timezone":"timezone","name":{"familyName":"familyName","givenName":"givenName"},"locale":"locale","userName":"userName"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='PATCH',
        path='/identity/v1/Users/me',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_user(client):
    """Test case for update_user

    Update User
    """
    body = {"password":"password","displayName":"displayName","timezone":"timezone","name":{"familyName":"familyName","givenName":"givenName"},"locale":"locale","userName":"userName"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='PATCH',
        path='/identity/v1/Users/{user_key}'.format(user_key=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

