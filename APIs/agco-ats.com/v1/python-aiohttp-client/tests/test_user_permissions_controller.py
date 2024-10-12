# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_models_api_error import APIModelsApiError
from openapi_server.models.api_models_role_user_change import APIModelsRoleUserChange
from openapi_server.models.api_models_user_role_change import APIModelsUserRoleChange
from openapi_server.models.api_paged_response_api_models_role import APIPagedResponseAPIModelsRole
from openapi_server.models.api_paged_response_api_models_user import APIPagedResponseAPIModelsUser
from openapi_server.models.api_paged_response_api_models_user_effective_permission import APIPagedResponseAPIModelsUserEffectivePermission


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_v2_roles_id_users_put(client):
    """Test case for api_v2_roles_id_users_put

    Update a Role's users
    """
    body = [openapi_server.APIModelsRoleUserChange()]
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v2/Roles/{id}/Users'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v2_users_current_permissions_get(client):
    """Test case for api_v2_users_current_permissions_get

    Get a user's permissions
    """
    params = [('Permission', 'permission_example'),
                    ('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/Users/Current/Permissions',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_user_permissions_get_current_user_roles(client):
    """Test case for user_permissions_get_current_user_roles

    Gets the current user's roles
    """
    params = [('Role', 'role_example'),
                    ('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/Users/Current/Roles',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_user_permissions_get_permissions(client):
    """Test case for user_permissions_get_permissions

    Get a user's permissions
    """
    params = [('Permission', 'permission_example'),
                    ('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/Users/{id}/Permissions'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_user_permissions_get_roles(client):
    """Test case for user_permissions_get_roles

    Get a user's roles
    """
    params = [('Role', 'role_example'),
                    ('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/Users/{id}/Roles'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_user_permissions_get_users(client):
    """Test case for user_permissions_get_users

    Get all user's in a role
    """
    params = [('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/Roles/{id}/Users'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_user_permissions_put(client):
    """Test case for user_permissions_put

    Update a user's roles
    """
    body = [openapi_server.APIModelsUserRoleChange()]
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v2/Users/{id}/Roles'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

