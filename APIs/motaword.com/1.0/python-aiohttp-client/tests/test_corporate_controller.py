# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.corporate_account import CorporateAccount
from openapi_server.models.permission_list import PermissionList
from openapi_server.models.user import User
from openapi_server.models.user_group import UserGroup
from openapi_server.models.user_group_list import UserGroupList
from openapi_server.models.user_list import UserList
from openapi_server.models.user_update_content import UserUpdateContent


pytestmark = pytest.mark.asyncio

async def test_get_available_corporate_permissions(client):
    """Test case for get_available_corporate_permissions

    View available permissions
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/corporate/permissions',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_available_corporate_permissions_by_id(client):
    """Test case for get_available_corporate_permissions_by_id

    Get a list of available permissions for this corporate account. They are used when assigning permissions to corporate users.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/corporates/{corporate_id}/permissions'.format(corporate_id=2),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_corporate(client):
    """Test case for get_corporate

    View your corporate account
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/corporate',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_corporate_by_id(client):
    """Test case for get_corporate_by_id

    Get details of this corporate account
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/corporates/{corporate_id}'.format(corporate_id=2),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_corporate_user_groups(client):
    """Test case for get_corporate_user_groups

    View user groups
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/corporate/user-groups',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_corporate_user_groups_by_id(client):
    """Test case for get_corporate_user_groups_by_id

    Get a list of user groups for this corporate account
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/corporates/{corporate_id}/user-groups'.format(corporate_id=2),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_corporate_users(client):
    """Test case for get_corporate_users

    View users
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/corporate/users',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_corporate_users_by_id(client):
    """Test case for get_corporate_users_by_id

    Get a list of users for this corporate account
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/corporates/{corporate_id}/users'.format(corporate_id=2),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_corporates_list(client):
    """Test case for get_corporates_list

    Get a list of corporate accounts
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/corporates/all',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_save_corporate_user(client):
    """Test case for save_corporate_user

    Create or update a user
    """
    body = {"zip":"zip","birthday":"2000-01-23","country":"country","city":"city","paypal_email":"paypal_email","last_name":"last_name","require_1099":True,"notify":True,"phone":"phone","street":"street","state":"state","id":0,"first_name":"first_name","email":"email","notifications":{"sms_enabled":True,"phone_number":"phone_number"},"user_groups":[6,6]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/corporate/users',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_save_corporate_user_group(client):
    """Test case for save_corporate_user_group

    Create or update a corporate user group
    """
    body = {"permissions":["permissions","permissions"],"corporate_id":2,"name":"name","id":4}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/corporate/user-groups',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_save_corporate_user_group_by_id(client):
    """Test case for save_corporate_user_group_by_id

    Create or update a corporate user group for this corporate account
    """
    body = {"permissions":["permissions","permissions"],"corporate_id":2,"name":"name","id":4}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/corporates/{corporate_id}/user-groups'.format(corporate_id=2),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

