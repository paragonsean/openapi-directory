# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_models_role import APIModelsRole
from openapi_server.models.api_models_role_permission_change import APIModelsRolePermissionChange
from openapi_server.models.api_paged_response_api_models_permission import APIPagedResponseAPIModelsPermission
from openapi_server.models.api_paged_response_api_models_role import APIPagedResponseAPIModelsRole


pytestmark = pytest.mark.asyncio

async def test_roles_delete_role(client):
    """Test case for roles_delete_role

    Deletes a User Role
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/api/v2/Roles/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_roles_get_role(client):
    """Test case for roles_get_role

    Gets a User Role
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/Roles/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_roles_get_role_permissions(client):
    """Test case for roles_get_role_permissions

    Get the Permissions for a Role
    """
    params = [('name', 'name_example'),
                    ('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/Roles/{id}/Permissions'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_roles_get_roles(client):
    """Test case for roles_get_roles

    List Roles
    """
    params = [('limit', 56),
                    ('offset', 56),
                    ('name', 'name_example'),
                    ('permissionID', 56),
                    ('permissionName', 'permission_name_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/Roles',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_roles_post_role(client):
    """Test case for roles_post_role

    Adds a User Role
    """
    body = openapi_server.APIModelsRole()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/Roles',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_roles_put_role(client):
    """Test case for roles_put_role

    Updates a User Role
    """
    body = openapi_server.APIModelsRole()
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v2/Roles/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_roles_put_role_permissions(client):
    """Test case for roles_put_role_permissions

    Manage the Permissions for a Role
    """
    body = [openapi_server.APIModelsRolePermissionChange()]
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v2/Roles/{id}/Permissions'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

