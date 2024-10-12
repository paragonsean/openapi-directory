# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_user_request_body import CreateUserRequestBody
from openapi_server.models.detailed_user_response import DetailedUserResponse
from openapi_server.models.login_admin_request_body import LoginAdminRequestBody
from openapi_server.models.update_user_request_body import UpdateUserRequestBody
from openapi_server.models.user_login_response import UserLoginResponse
from openapi_server.models.user_response import UserResponse


pytestmark = pytest.mark.asyncio

async def test_create_user(client):
    """Test case for create_user

    Create-User
    """
    body = {"password":"{{UserPassword}}","username":"{{UserUsername}}"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/users',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_user(client):
    """Test case for delete_user

    Delete-User
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/users/{user_username}'.format(user_username='user_username_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_user(client):
    """Test case for get_user

    Get-User
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/users/{user_username}'.format(user_username='user_username_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_login_user(client):
    """Test case for login_user

    Login-User
    """
    body = openapi_server.LoginAdminRequestBody()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/users/login',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_logout_user(client):
    """Test case for logout_user

    Logout-User
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/users/logout',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_user(client):
    """Test case for update_user

    Update-User
    """
    body = {"password":"<New Password>"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/users/{user_username}'.format(user_username='user_username_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

