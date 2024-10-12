# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.group_representation import GroupRepresentation
from openapi_server.models.management_permission_reference import ManagementPermissionReference
from openapi_server.models.user_representation import UserRepresentation


pytestmark = pytest.mark.asyncio

async def test_realm_groups_count_get(client):
    """Test case for realm_groups_count_get

    Returns the groups counts.
    """
    params = [('search', 'search_example'),
                    ('top', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{realm}/groups/count'.format(realm='realm_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_groups_get(client):
    """Test case for realm_groups_get

    Get group hierarchy.
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
        path='/{realm}/groups'.format(realm='realm_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_groups_id_children_post(client):
    """Test case for realm_groups_id_children_post

    Set or create child.
    """
    body = {"path":"path","realmRoles":["realmRoles","realmRoles"],"access":{"key":""},"name":"name","subGroups":[null,null],"attributes":{"key":""},"id":"id","clientRoles":{"key":""}}
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/{realm}/groups/{id}/children'.format(realm='realm_example', id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_groups_id_delete(client):
    """Test case for realm_groups_id_delete

    
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/{realm}/groups/{id}'.format(realm='realm_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_groups_id_get(client):
    """Test case for realm_groups_id_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{realm}/groups/{id}'.format(realm='realm_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_groups_id_management_permissions_get(client):
    """Test case for realm_groups_id_management_permissions_get

    Return object stating whether client Authorization permissions have been initialized or not and a reference
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{realm}/groups/{id}/management/permissions'.format(realm='realm_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_groups_id_management_permissions_put(client):
    """Test case for realm_groups_id_management_permissions_put

    Return object stating whether client Authorization permissions have been initialized or not and a reference
    """
    body = {"scopePermissions":{"key":""},"resource":"resource","enabled":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/{realm}/groups/{id}/management/permissions'.format(realm='realm_example', id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_groups_id_members_get(client):
    """Test case for realm_groups_id_members_get

    Get users   Returns a list of users, filtered according to query parameters
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
        path='/{realm}/groups/{id}/members'.format(realm='realm_example', id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_groups_id_put(client):
    """Test case for realm_groups_id_put

    Update group, ignores subgroups.
    """
    body = {"path":"path","realmRoles":["realmRoles","realmRoles"],"access":{"key":""},"name":"name","subGroups":[null,null],"attributes":{"key":""},"id":"id","clientRoles":{"key":""}}
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/{realm}/groups/{id}'.format(realm='realm_example', id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_groups_post(client):
    """Test case for realm_groups_post

    create or add a top level realm groupSet or create child.
    """
    body = {"path":"path","realmRoles":["realmRoles","realmRoles"],"access":{"key":""},"name":"name","subGroups":[null,null],"attributes":{"key":""},"id":"id","clientRoles":{"key":""}}
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/{realm}/groups'.format(realm='realm_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

