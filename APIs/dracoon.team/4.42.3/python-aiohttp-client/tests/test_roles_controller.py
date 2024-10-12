# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.group_ids import GroupIds
from openapi_server.models.role_group_list import RoleGroupList
from openapi_server.models.role_list import RoleList
from openapi_server.models.role_user_list import RoleUserList
from openapi_server.models.user_ids import UserIds


pytestmark = pytest.mark.asyncio

async def test_add_role_groups(client):
    """Test case for add_role_groups

    Assign group(s) to the role
    """
    body = {"ids":[0,0]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v4/roles/{role_id}/groups'.format(role_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_add_role_users(client):
    """Test case for add_role_users

    Assign user(s) to the role
    """
    body = {"ids":[0,0]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v4/roles/{role_id}/users'.format(role_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_request_role_groups(client):
    """Test case for request_role_groups

    Request groups with specific role
    """
    params = [('offset', 56),
                    ('limit', 56),
                    ('filter', 'filter_example')]
    headers = { 
        'Accept': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/roles/{role_id}/groups'.format(role_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_request_role_users(client):
    """Test case for request_role_users

    Request users with specific role
    """
    params = [('offset', 56),
                    ('limit', 56),
                    ('filter', 'filter_example')]
    headers = { 
        'Accept': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/roles/{role_id}/users'.format(role_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_request_roles(client):
    """Test case for request_roles

    Request all roles with assigned rights
    """
    headers = { 
        'Accept': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/roles',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_revoke_role_groups(client):
    """Test case for revoke_role_groups

    Revoke granted role from group(s)
    """
    body = {"ids":[0,0]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v4/roles/{role_id}/groups'.format(role_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_revoke_role_users(client):
    """Test case for revoke_role_users

    Revoke granted role from user(s)
    """
    body = {"ids":[0,0]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v4/roles/{role_id}/users'.format(role_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

