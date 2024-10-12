# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.management_permission_reference import ManagementPermissionReference
from openapi_server.models.role_representation import RoleRepresentation


pytestmark = pytest.mark.asyncio

async def test_realm_roles_by_id_role_id_composites_clients_client_get(client):
    """Test case for realm_roles_by_id_role_id_composites_clients_client_get

    Get client-level roles for the client that are in the role’s composite
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{realm}/roles-by-id/{role_id}/composites/clients/{client}'.format(realm='realm_example', role_id='role_id_example', client='client_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_roles_by_id_role_id_composites_delete(client):
    """Test case for realm_roles_by_id_role_id_composites_delete

    Remove a set of roles from the role’s composite
    """
    body = {"composites":{"client":{"key":""},"realm":["realm","realm"]},"clientRole":True,"composite":True,"name":"name","description":"description","attributes":{"key":""},"id":"id","containerId":"containerId"}
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/{realm}/roles-by-id/{role_id}/composites'.format(realm='realm_example', role_id='role_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_roles_by_id_role_id_composites_get(client):
    """Test case for realm_roles_by_id_role_id_composites_get

    Get role’s children   Returns a set of role’s children provided the role is a composite.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{realm}/roles-by-id/{role_id}/composites'.format(realm='realm_example', role_id='role_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_roles_by_id_role_id_composites_post(client):
    """Test case for realm_roles_by_id_role_id_composites_post

    Make the role a composite role by associating some child roles
    """
    body = {"composites":{"client":{"key":""},"realm":["realm","realm"]},"clientRole":True,"composite":True,"name":"name","description":"description","attributes":{"key":""},"id":"id","containerId":"containerId"}
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/{realm}/roles-by-id/{role_id}/composites'.format(realm='realm_example', role_id='role_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_roles_by_id_role_id_composites_realm_get(client):
    """Test case for realm_roles_by_id_role_id_composites_realm_get

    Get realm-level roles that are in the role’s composite
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{realm}/roles-by-id/{role_id}/composites/realm'.format(realm='realm_example', role_id='role_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_roles_by_id_role_id_delete(client):
    """Test case for realm_roles_by_id_role_id_delete

    Delete the role
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/{realm}/roles-by-id/{role_id}'.format(realm='realm_example', role_id='role_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_roles_by_id_role_id_get(client):
    """Test case for realm_roles_by_id_role_id_get

    Get a specific role’s representation
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{realm}/roles-by-id/{role_id}'.format(realm='realm_example', role_id='role_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_roles_by_id_role_id_management_permissions_get(client):
    """Test case for realm_roles_by_id_role_id_management_permissions_get

    Return object stating whether role Authoirzation permissions have been initialized or not and a reference
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{realm}/roles-by-id/{role_id}/management/permissions'.format(realm='realm_example', role_id='role_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_roles_by_id_role_id_management_permissions_put(client):
    """Test case for realm_roles_by_id_role_id_management_permissions_put

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
        path='/{realm}/roles-by-id/{role_id}/management/permissions'.format(realm='realm_example', role_id='role_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_roles_by_id_role_id_put(client):
    """Test case for realm_roles_by_id_role_id_put

    Update the role
    """
    body = {"composites":{"client":{"key":""},"realm":["realm","realm"]},"clientRole":True,"composite":True,"name":"name","description":"description","attributes":{"key":""},"id":"id","containerId":"containerId"}
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/{realm}/roles-by-id/{role_id}'.format(realm='realm_example', role_id='role_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

