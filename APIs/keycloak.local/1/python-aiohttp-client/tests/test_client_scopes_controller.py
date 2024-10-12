# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.client_scope_representation import ClientScopeRepresentation


pytestmark = pytest.mark.asyncio

async def test_realm_client_scopes_get(client):
    """Test case for realm_client_scopes_get

    Get client scopes belonging to the realm   Returns a list of client scopes belonging to the realm
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{realm}/client-scopes'.format(realm='realm_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_client_scopes_id_delete(client):
    """Test case for realm_client_scopes_id_delete

    Delete the client scope
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/{realm}/client-scopes/{id}'.format(realm='realm_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_client_scopes_id_get(client):
    """Test case for realm_client_scopes_id_get

    Get representation of the client scope
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{realm}/client-scopes/{id}'.format(realm='realm_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_client_scopes_id_put(client):
    """Test case for realm_client_scopes_id_put

    Update the client scope
    """
    body = {"protocol":"protocol","name":"name","description":"description","attributes":{"key":""},"protocolMappers":[{"protocol":"protocol","protocolMapper":"protocolMapper","name":"name","id":"id","config":{"key":""}},{"protocol":"protocol","protocolMapper":"protocolMapper","name":"name","id":"id","config":{"key":""}}],"id":"id"}
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/{realm}/client-scopes/{id}'.format(realm='realm_example', id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_client_scopes_post(client):
    """Test case for realm_client_scopes_post

    Create a new client scope   Client Scope’s name must be unique!
    """
    body = {"protocol":"protocol","name":"name","description":"description","attributes":{"key":""},"protocolMappers":[{"protocol":"protocol","protocolMapper":"protocolMapper","name":"name","id":"id","config":{"key":""}},{"protocol":"protocol","protocolMapper":"protocolMapper","name":"name","id":"id","config":{"key":""}}],"id":"id"}
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/{realm}/client-scopes'.format(realm='realm_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

