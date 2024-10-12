# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.mappings_representation import MappingsRepresentation
from openapi_server.models.role_representation import RoleRepresentation


pytestmark = pytest.mark.asyncio

async def test_realm_client_scopes_id_scope_mappings_clients_client_available_get(client):
    """Test case for realm_client_scopes_id_scope_mappings_clients_client_available_get

    The available client-level roles   Returns the roles for the client that can be associated with the client’s scope
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{realm}/client-scopes/{id}/scope-mappings/clients/{client}/available'.format(realm='realm_example', id='id_example', client='client_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_client_scopes_id_scope_mappings_clients_client_composite_get(client):
    """Test case for realm_client_scopes_id_scope_mappings_clients_client_composite_get

    Get effective client roles   Returns the roles for the client that are associated with the client’s scope.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{realm}/client-scopes/{id}/scope-mappings/clients/{client}/composite'.format(realm='realm_example', id='id_example', client='client_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_client_scopes_id_scope_mappings_clients_client_delete(client):
    """Test case for realm_client_scopes_id_scope_mappings_clients_client_delete

    Remove client-level roles from the client’s scope.
    """
    body = {"composites":{"client":{"key":""},"realm":["realm","realm"]},"clientRole":True,"composite":True,"name":"name","description":"description","attributes":{"key":""},"id":"id","containerId":"containerId"}
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/{realm}/client-scopes/{id}/scope-mappings/clients/{client}'.format(realm='realm_example', id='id_example', client='client_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_client_scopes_id_scope_mappings_clients_client_get(client):
    """Test case for realm_client_scopes_id_scope_mappings_clients_client_get

    Get the roles associated with a client’s scope   Returns roles for the client.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{realm}/client-scopes/{id}/scope-mappings/clients/{client}'.format(realm='realm_example', id='id_example', client='client_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_client_scopes_id_scope_mappings_clients_client_post(client):
    """Test case for realm_client_scopes_id_scope_mappings_clients_client_post

    Add client-level roles to the client’s scope
    """
    body = {"composites":{"client":{"key":""},"realm":["realm","realm"]},"clientRole":True,"composite":True,"name":"name","description":"description","attributes":{"key":""},"id":"id","containerId":"containerId"}
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/{realm}/client-scopes/{id}/scope-mappings/clients/{client}'.format(realm='realm_example', id='id_example', client='client_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_client_scopes_id_scope_mappings_get(client):
    """Test case for realm_client_scopes_id_scope_mappings_get

    Get all scope mappings for the client
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{realm}/client-scopes/{id}/scope-mappings'.format(realm='realm_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_client_scopes_id_scope_mappings_realm_available_get(client):
    """Test case for realm_client_scopes_id_scope_mappings_realm_available_get

    Get realm-level roles that are available to attach to this client’s scope
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{realm}/client-scopes/{id}/scope-mappings/realm/available'.format(realm='realm_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_client_scopes_id_scope_mappings_realm_composite_get(client):
    """Test case for realm_client_scopes_id_scope_mappings_realm_composite_get

    Get effective realm-level roles associated with the client’s scope   What this does is recurse  any composite roles associated with the client’s scope and adds the roles to this lists.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{realm}/client-scopes/{id}/scope-mappings/realm/composite'.format(realm='realm_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_client_scopes_id_scope_mappings_realm_delete(client):
    """Test case for realm_client_scopes_id_scope_mappings_realm_delete

    Remove a set of realm-level roles from the client’s scope
    """
    body = {"composites":{"client":{"key":""},"realm":["realm","realm"]},"clientRole":True,"composite":True,"name":"name","description":"description","attributes":{"key":""},"id":"id","containerId":"containerId"}
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/{realm}/client-scopes/{id}/scope-mappings/realm'.format(realm='realm_example', id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_client_scopes_id_scope_mappings_realm_get(client):
    """Test case for realm_client_scopes_id_scope_mappings_realm_get

    Get realm-level roles associated with the client’s scope
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{realm}/client-scopes/{id}/scope-mappings/realm'.format(realm='realm_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_client_scopes_id_scope_mappings_realm_post(client):
    """Test case for realm_client_scopes_id_scope_mappings_realm_post

    Add a set of realm-level roles to the client’s scope
    """
    body = {"composites":{"client":{"key":""},"realm":["realm","realm"]},"clientRole":True,"composite":True,"name":"name","description":"description","attributes":{"key":""},"id":"id","containerId":"containerId"}
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/{realm}/client-scopes/{id}/scope-mappings/realm'.format(realm='realm_example', id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_clients_id_scope_mappings_clients_client_available_get(client):
    """Test case for realm_clients_id_scope_mappings_clients_client_available_get

    The available client-level roles   Returns the roles for the client that can be associated with the client’s scope
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{realm}/clients/{id}/scope-mappings/clients/{client}/available'.format(realm='realm_example', id='id_example', client='client_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_clients_id_scope_mappings_clients_client_composite_get(client):
    """Test case for realm_clients_id_scope_mappings_clients_client_composite_get

    Get effective client roles   Returns the roles for the client that are associated with the client’s scope.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{realm}/clients/{id}/scope-mappings/clients/{client}/composite'.format(realm='realm_example', id='id_example', client='client_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_clients_id_scope_mappings_clients_client_delete(client):
    """Test case for realm_clients_id_scope_mappings_clients_client_delete

    Remove client-level roles from the client’s scope.
    """
    body = {"composites":{"client":{"key":""},"realm":["realm","realm"]},"clientRole":True,"composite":True,"name":"name","description":"description","attributes":{"key":""},"id":"id","containerId":"containerId"}
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/{realm}/clients/{id}/scope-mappings/clients/{client}'.format(realm='realm_example', id='id_example', client='client_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_clients_id_scope_mappings_clients_client_get(client):
    """Test case for realm_clients_id_scope_mappings_clients_client_get

    Get the roles associated with a client’s scope   Returns roles for the client.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{realm}/clients/{id}/scope-mappings/clients/{client}'.format(realm='realm_example', id='id_example', client='client_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_clients_id_scope_mappings_clients_client_post(client):
    """Test case for realm_clients_id_scope_mappings_clients_client_post

    Add client-level roles to the client’s scope
    """
    body = {"composites":{"client":{"key":""},"realm":["realm","realm"]},"clientRole":True,"composite":True,"name":"name","description":"description","attributes":{"key":""},"id":"id","containerId":"containerId"}
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/{realm}/clients/{id}/scope-mappings/clients/{client}'.format(realm='realm_example', id='id_example', client='client_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_clients_id_scope_mappings_get(client):
    """Test case for realm_clients_id_scope_mappings_get

    Get all scope mappings for the client
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{realm}/clients/{id}/scope-mappings'.format(realm='realm_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_clients_id_scope_mappings_realm_available_get(client):
    """Test case for realm_clients_id_scope_mappings_realm_available_get

    Get realm-level roles that are available to attach to this client’s scope
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{realm}/clients/{id}/scope-mappings/realm/available'.format(realm='realm_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_clients_id_scope_mappings_realm_composite_get(client):
    """Test case for realm_clients_id_scope_mappings_realm_composite_get

    Get effective realm-level roles associated with the client’s scope   What this does is recurse  any composite roles associated with the client’s scope and adds the roles to this lists.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{realm}/clients/{id}/scope-mappings/realm/composite'.format(realm='realm_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_clients_id_scope_mappings_realm_delete(client):
    """Test case for realm_clients_id_scope_mappings_realm_delete

    Remove a set of realm-level roles from the client’s scope
    """
    body = {"composites":{"client":{"key":""},"realm":["realm","realm"]},"clientRole":True,"composite":True,"name":"name","description":"description","attributes":{"key":""},"id":"id","containerId":"containerId"}
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/{realm}/clients/{id}/scope-mappings/realm'.format(realm='realm_example', id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_clients_id_scope_mappings_realm_get(client):
    """Test case for realm_clients_id_scope_mappings_realm_get

    Get realm-level roles associated with the client’s scope
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{realm}/clients/{id}/scope-mappings/realm'.format(realm='realm_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_clients_id_scope_mappings_realm_post(client):
    """Test case for realm_clients_id_scope_mappings_realm_post

    Add a set of realm-level roles to the client’s scope
    """
    body = {"composites":{"client":{"key":""},"realm":["realm","realm"]},"clientRole":True,"composite":True,"name":"name","description":"description","attributes":{"key":""},"id":"id","containerId":"containerId"}
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/{realm}/clients/{id}/scope-mappings/realm'.format(realm='realm_example', id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

