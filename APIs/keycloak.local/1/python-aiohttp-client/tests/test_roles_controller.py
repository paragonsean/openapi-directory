# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.group_representation import GroupRepresentation
from openapi_server.models.management_permission_reference import ManagementPermissionReference
from openapi_server.models.role_representation import RoleRepresentation
from openapi_server.models.user_representation import UserRepresentation


pytestmark = pytest.mark.asyncio

async def test_realm_clients_id_roles_get(client):
    """Test case for realm_clients_id_roles_get

    Get all roles for the realm or client
    """
    params = [('briefRepresentation', True),
                    ('first', 56),
                    ('max', 56),
                    ('search', 'search_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{realm}/clients/{id}/roles'.format(realm='realm_example', id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_clients_id_roles_post(client):
    """Test case for realm_clients_id_roles_post

    Create a new role for the realm or client
    """
    body = {"composites":{"client":{"key":""},"realm":["realm","realm"]},"clientRole":True,"composite":True,"name":"name","description":"description","attributes":{"key":""},"id":"id","containerId":"containerId"}
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/{realm}/clients/{id}/roles'.format(realm='realm_example', id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_clients_id_roles_role_name_composites_clients_client_get(client):
    """Test case for realm_clients_id_roles_role_name_composites_clients_client_get

    An app-level roles for the specified app for the role’s composite
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{realm}/clients/{id}/roles/{role_name}/composites/clients/{client}'.format(realm='realm_example', id='id_example', role_name='role_name_example', client='client_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_clients_id_roles_role_name_composites_delete(client):
    """Test case for realm_clients_id_roles_role_name_composites_delete

    Remove roles from the role’s composite
    """
    body = {"composites":{"client":{"key":""},"realm":["realm","realm"]},"clientRole":True,"composite":True,"name":"name","description":"description","attributes":{"key":""},"id":"id","containerId":"containerId"}
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/{realm}/clients/{id}/roles/{role_name}/composites'.format(realm='realm_example', id='id_example', role_name='role_name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_clients_id_roles_role_name_composites_get(client):
    """Test case for realm_clients_id_roles_role_name_composites_get

    Get composites of the role
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{realm}/clients/{id}/roles/{role_name}/composites'.format(realm='realm_example', id='id_example', role_name='role_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_clients_id_roles_role_name_composites_post(client):
    """Test case for realm_clients_id_roles_role_name_composites_post

    Add a composite to the role
    """
    body = {"composites":{"client":{"key":""},"realm":["realm","realm"]},"clientRole":True,"composite":True,"name":"name","description":"description","attributes":{"key":""},"id":"id","containerId":"containerId"}
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/{realm}/clients/{id}/roles/{role_name}/composites'.format(realm='realm_example', id='id_example', role_name='role_name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_clients_id_roles_role_name_composites_realm_get(client):
    """Test case for realm_clients_id_roles_role_name_composites_realm_get

    Get realm-level roles of the role’s composite
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{realm}/clients/{id}/roles/{role_name}/composites/realm'.format(realm='realm_example', id='id_example', role_name='role_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_clients_id_roles_role_name_delete(client):
    """Test case for realm_clients_id_roles_role_name_delete

    Delete a role by name
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/{realm}/clients/{id}/roles/{role_name}'.format(realm='realm_example', id='id_example', role_name='role_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_clients_id_roles_role_name_get(client):
    """Test case for realm_clients_id_roles_role_name_get

    Get a role by name
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{realm}/clients/{id}/roles/{role_name}'.format(realm='realm_example', id='id_example', role_name='role_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_clients_id_roles_role_name_groups_get(client):
    """Test case for realm_clients_id_roles_role_name_groups_get

    Return List of Groups that have the specified role name
    """
    params = [('briefRepresentation', True),
                    ('first', 56),
                    ('max', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{realm}/clients/{id}/roles/{role_name}/groups'.format(realm='realm_example', id='id_example', role_name='role_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_clients_id_roles_role_name_management_permissions_get(client):
    """Test case for realm_clients_id_roles_role_name_management_permissions_get

    Return object stating whether role Authoirzation permissions have been initialized or not and a reference
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{realm}/clients/{id}/roles/{role_name}/management/permissions'.format(realm='realm_example', id='id_example', role_name='role_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_clients_id_roles_role_name_management_permissions_put(client):
    """Test case for realm_clients_id_roles_role_name_management_permissions_put

    Return object stating whether role Authoirzation permissions have been initialized or not and a reference
    """
    body = {"scopePermissions":{"key":""},"resource":"resource","enabled":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/{realm}/clients/{id}/roles/{role_name}/management/permissions'.format(realm='realm_example', id='id_example', role_name='role_name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_clients_id_roles_role_name_put(client):
    """Test case for realm_clients_id_roles_role_name_put

    Update a role by name
    """
    body = {"composites":{"client":{"key":""},"realm":["realm","realm"]},"clientRole":True,"composite":True,"name":"name","description":"description","attributes":{"key":""},"id":"id","containerId":"containerId"}
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/{realm}/clients/{id}/roles/{role_name}'.format(realm='realm_example', id='id_example', role_name='role_name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_clients_id_roles_role_name_users_get(client):
    """Test case for realm_clients_id_roles_role_name_users_get

    Return List of Users that have the specified role name
    """
    params = [('first', 56),
                    ('max', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{realm}/clients/{id}/roles/{role_name}/users'.format(realm='realm_example', id='id_example', role_name='role_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_roles_get(client):
    """Test case for realm_roles_get

    Get all roles for the realm or client
    """
    params = [('briefRepresentation', True),
                    ('first', 56),
                    ('max', 56),
                    ('search', 'search_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{realm}/roles'.format(realm='realm_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_roles_post(client):
    """Test case for realm_roles_post

    Create a new role for the realm or client
    """
    body = {"composites":{"client":{"key":""},"realm":["realm","realm"]},"clientRole":True,"composite":True,"name":"name","description":"description","attributes":{"key":""},"id":"id","containerId":"containerId"}
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/{realm}/roles'.format(realm='realm_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_roles_role_name_composites_clients_client_get(client):
    """Test case for realm_roles_role_name_composites_clients_client_get

    An app-level roles for the specified app for the role’s composite
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{realm}/roles/{role_name}/composites/clients/{client}'.format(realm='realm_example', role_name='role_name_example', client='client_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_roles_role_name_composites_delete(client):
    """Test case for realm_roles_role_name_composites_delete

    Remove roles from the role’s composite
    """
    body = {"composites":{"client":{"key":""},"realm":["realm","realm"]},"clientRole":True,"composite":True,"name":"name","description":"description","attributes":{"key":""},"id":"id","containerId":"containerId"}
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/{realm}/roles/{role_name}/composites'.format(realm='realm_example', role_name='role_name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_roles_role_name_composites_get(client):
    """Test case for realm_roles_role_name_composites_get

    Get composites of the role
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{realm}/roles/{role_name}/composites'.format(realm='realm_example', role_name='role_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_roles_role_name_composites_post(client):
    """Test case for realm_roles_role_name_composites_post

    Add a composite to the role
    """
    body = {"composites":{"client":{"key":""},"realm":["realm","realm"]},"clientRole":True,"composite":True,"name":"name","description":"description","attributes":{"key":""},"id":"id","containerId":"containerId"}
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/{realm}/roles/{role_name}/composites'.format(realm='realm_example', role_name='role_name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_roles_role_name_composites_realm_get(client):
    """Test case for realm_roles_role_name_composites_realm_get

    Get realm-level roles of the role’s composite
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{realm}/roles/{role_name}/composites/realm'.format(realm='realm_example', role_name='role_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_roles_role_name_delete(client):
    """Test case for realm_roles_role_name_delete

    Delete a role by name
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/{realm}/roles/{role_name}'.format(realm='realm_example', role_name='role_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_roles_role_name_get(client):
    """Test case for realm_roles_role_name_get

    Get a role by name
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{realm}/roles/{role_name}'.format(realm='realm_example', role_name='role_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_roles_role_name_groups_get(client):
    """Test case for realm_roles_role_name_groups_get

    Return List of Groups that have the specified role name
    """
    params = [('briefRepresentation', True),
                    ('first', 56),
                    ('max', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{realm}/roles/{role_name}/groups'.format(realm='realm_example', role_name='role_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_roles_role_name_management_permissions_get(client):
    """Test case for realm_roles_role_name_management_permissions_get

    Return object stating whether role Authoirzation permissions have been initialized or not and a reference
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{realm}/roles/{role_name}/management/permissions'.format(realm='realm_example', role_name='role_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_roles_role_name_management_permissions_put(client):
    """Test case for realm_roles_role_name_management_permissions_put

    Return object stating whether role Authoirzation permissions have been initialized or not and a reference
    """
    body = {"scopePermissions":{"key":""},"resource":"resource","enabled":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/{realm}/roles/{role_name}/management/permissions'.format(realm='realm_example', role_name='role_name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_roles_role_name_put(client):
    """Test case for realm_roles_role_name_put

    Update a role by name
    """
    body = {"composites":{"client":{"key":""},"realm":["realm","realm"]},"clientRole":True,"composite":True,"name":"name","description":"description","attributes":{"key":""},"id":"id","containerId":"containerId"}
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/{realm}/roles/{role_name}'.format(realm='realm_example', role_name='role_name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_roles_role_name_users_get(client):
    """Test case for realm_roles_role_name_users_get

    Return List of Users that have the specified role name
    """
    params = [('first', 56),
                    ('max', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{realm}/roles/{role_name}/users'.format(realm='realm_example', role_name='role_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

