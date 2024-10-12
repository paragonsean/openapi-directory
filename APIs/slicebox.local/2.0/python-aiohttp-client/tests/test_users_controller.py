# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.new_user import NewUser
from openapi_server.models.user import User
from openapi_server.models.user_info import UserInfo
from openapi_server.models.user_pass import UserPass


pytestmark = pytest.mark.asyncio

async def test_users_current_get(client):
    """Test case for users_current_get

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/users/current',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_get(client):
    """Test case for users_get

    
    """
    params = [('startindex', 0),
                    ('count', 20)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/users',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_id_delete(client):
    """Test case for users_id_delete

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/api/users/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_users_login_post(client):
    """Test case for users_login_post

    
    """
    user_pass = openapi_server.UserPass()
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/users/login',
        headers=headers,
        json=user_pass,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_logout_post(client):
    """Test case for users_logout_post

    
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/api/users/logout',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_users_post(client):
    """Test case for users_post

    
    """
    user = openapi_server.NewUser()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/users',
        headers=headers,
        json=user,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

