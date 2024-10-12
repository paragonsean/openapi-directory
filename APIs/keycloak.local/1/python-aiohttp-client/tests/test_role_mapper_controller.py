# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.mappings_representation import MappingsRepresentation
from openapi_server.models.role_representation import RoleRepresentation


pytestmark = pytest.mark.asyncio

async def test_realm_groups_id_role_mappings_get(client):
    """Test case for realm_groups_id_role_mappings_get

    Get role mappings
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{realm}/groups/{id}/role-mappings'.format(realm='realm_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_groups_id_role_mappings_realm_available_get(client):
    """Test case for realm_groups_id_role_mappings_realm_available_get

    Get realm-level roles that can be mapped
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{realm}/groups/{id}/role-mappings/realm/available'.format(realm='realm_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_groups_id_role_mappings_realm_composite_get(client):
    """Test case for realm_groups_id_role_mappings_realm_composite_get

    Get effective realm-level role mappings   This will recurse all composite roles to get the result.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{realm}/groups/{id}/role-mappings/realm/composite'.format(realm='realm_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_groups_id_role_mappings_realm_delete(client):
    """Test case for realm_groups_id_role_mappings_realm_delete

    Delete realm-level role mappings
    """
    body = {"composites":{"client":{"key":""},"realm":["realm","realm"]},"clientRole":True,"composite":True,"name":"name","description":"description","attributes":{"key":""},"id":"id","containerId":"containerId"}
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/{realm}/groups/{id}/role-mappings/realm'.format(realm='realm_example', id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_groups_id_role_mappings_realm_get(client):
    """Test case for realm_groups_id_role_mappings_realm_get

    Get realm-level role mappings
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{realm}/groups/{id}/role-mappings/realm'.format(realm='realm_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_groups_id_role_mappings_realm_post(client):
    """Test case for realm_groups_id_role_mappings_realm_post

    Add realm-level role mappings to the user
    """
    body = {"composites":{"client":{"key":""},"realm":["realm","realm"]},"clientRole":True,"composite":True,"name":"name","description":"description","attributes":{"key":""},"id":"id","containerId":"containerId"}
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/{realm}/groups/{id}/role-mappings/realm'.format(realm='realm_example', id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_users_id_role_mappings_get(client):
    """Test case for realm_users_id_role_mappings_get

    Get role mappings
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{realm}/users/{id}/role-mappings'.format(realm='realm_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_users_id_role_mappings_realm_available_get(client):
    """Test case for realm_users_id_role_mappings_realm_available_get

    Get realm-level roles that can be mapped
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{realm}/users/{id}/role-mappings/realm/available'.format(realm='realm_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_users_id_role_mappings_realm_composite_get(client):
    """Test case for realm_users_id_role_mappings_realm_composite_get

    Get effective realm-level role mappings   This will recurse all composite roles to get the result.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{realm}/users/{id}/role-mappings/realm/composite'.format(realm='realm_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_users_id_role_mappings_realm_delete(client):
    """Test case for realm_users_id_role_mappings_realm_delete

    Delete realm-level role mappings
    """
    body = {"composites":{"client":{"key":""},"realm":["realm","realm"]},"clientRole":True,"composite":True,"name":"name","description":"description","attributes":{"key":""},"id":"id","containerId":"containerId"}
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/{realm}/users/{id}/role-mappings/realm'.format(realm='realm_example', id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_users_id_role_mappings_realm_get(client):
    """Test case for realm_users_id_role_mappings_realm_get

    Get realm-level role mappings
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{realm}/users/{id}/role-mappings/realm'.format(realm='realm_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_users_id_role_mappings_realm_post(client):
    """Test case for realm_users_id_role_mappings_realm_post

    Add realm-level role mappings to the user
    """
    body = {"composites":{"client":{"key":""},"realm":["realm","realm"]},"clientRole":True,"composite":True,"name":"name","description":"description","attributes":{"key":""},"id":"id","containerId":"containerId"}
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/{realm}/users/{id}/role-mappings/realm'.format(realm='realm_example', id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

