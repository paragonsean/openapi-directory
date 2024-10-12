# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.role_representation import RoleRepresentation


pytestmark = pytest.mark.asyncio

async def test_realm_groups_id_role_mappings_clients_client_available_get(client):
    """Test case for realm_groups_id_role_mappings_clients_client_available_get

    Get available client-level roles that can be mapped to the user
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{realm}/groups/{id}/role-mappings/clients/{client}/available'.format(realm='realm_example', id='id_example', client='client_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_groups_id_role_mappings_clients_client_composite_get(client):
    """Test case for realm_groups_id_role_mappings_clients_client_composite_get

    Get effective client-level role mappings   This recurses any composite roles
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{realm}/groups/{id}/role-mappings/clients/{client}/composite'.format(realm='realm_example', id='id_example', client='client_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_groups_id_role_mappings_clients_client_delete(client):
    """Test case for realm_groups_id_role_mappings_clients_client_delete

    Delete client-level roles from user role mapping
    """
    body = {"composites":{"client":{"key":""},"realm":["realm","realm"]},"clientRole":True,"composite":True,"name":"name","description":"description","attributes":{"key":""},"id":"id","containerId":"containerId"}
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/{realm}/groups/{id}/role-mappings/clients/{client}'.format(realm='realm_example', id='id_example', client='client_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_groups_id_role_mappings_clients_client_get(client):
    """Test case for realm_groups_id_role_mappings_clients_client_get

    Get client-level role mappings for the user, and the app
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{realm}/groups/{id}/role-mappings/clients/{client}'.format(realm='realm_example', id='id_example', client='client_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_groups_id_role_mappings_clients_client_post(client):
    """Test case for realm_groups_id_role_mappings_clients_client_post

    Add client-level roles to the user role mapping
    """
    body = {"composites":{"client":{"key":""},"realm":["realm","realm"]},"clientRole":True,"composite":True,"name":"name","description":"description","attributes":{"key":""},"id":"id","containerId":"containerId"}
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/{realm}/groups/{id}/role-mappings/clients/{client}'.format(realm='realm_example', id='id_example', client='client_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_users_id_role_mappings_clients_client_available_get(client):
    """Test case for realm_users_id_role_mappings_clients_client_available_get

    Get available client-level roles that can be mapped to the user
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{realm}/users/{id}/role-mappings/clients/{client}/available'.format(realm='realm_example', id='id_example', client='client_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_users_id_role_mappings_clients_client_composite_get(client):
    """Test case for realm_users_id_role_mappings_clients_client_composite_get

    Get effective client-level role mappings   This recurses any composite roles
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{realm}/users/{id}/role-mappings/clients/{client}/composite'.format(realm='realm_example', id='id_example', client='client_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_users_id_role_mappings_clients_client_delete(client):
    """Test case for realm_users_id_role_mappings_clients_client_delete

    Delete client-level roles from user role mapping
    """
    body = {"composites":{"client":{"key":""},"realm":["realm","realm"]},"clientRole":True,"composite":True,"name":"name","description":"description","attributes":{"key":""},"id":"id","containerId":"containerId"}
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/{realm}/users/{id}/role-mappings/clients/{client}'.format(realm='realm_example', id='id_example', client='client_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_users_id_role_mappings_clients_client_get(client):
    """Test case for realm_users_id_role_mappings_clients_client_get

    Get client-level role mappings for the user, and the app
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{realm}/users/{id}/role-mappings/clients/{client}'.format(realm='realm_example', id='id_example', client='client_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_users_id_role_mappings_clients_client_post(client):
    """Test case for realm_users_id_role_mappings_clients_client_post

    Add client-level roles to the user role mapping
    """
    body = {"composites":{"client":{"key":""},"realm":["realm","realm"]},"clientRole":True,"composite":True,"name":"name","description":"description","attributes":{"key":""},"id":"id","containerId":"containerId"}
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/{realm}/users/{id}/role-mappings/clients/{client}'.format(realm='realm_example', id='id_example', client='client_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

