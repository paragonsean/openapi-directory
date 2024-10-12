# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.protocol_mapper_representation import ProtocolMapperRepresentation


pytestmark = pytest.mark.asyncio

async def test_realm_client_scopes_id1_protocol_mappers_models_id2_delete(client):
    """Test case for realm_client_scopes_id1_protocol_mappers_models_id2_delete

    Delete the mapper
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/{realm}/client-scopes/{id1}/protocol-mappers/models/{id2}'.format(realm='realm_example', id1='id1_example', id2='id2_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_client_scopes_id1_protocol_mappers_models_id2_get(client):
    """Test case for realm_client_scopes_id1_protocol_mappers_models_id2_get

    Get mapper by id
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{realm}/client-scopes/{id1}/protocol-mappers/models/{id2}'.format(realm='realm_example', id1='id1_example', id2='id2_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_client_scopes_id1_protocol_mappers_models_id2_put(client):
    """Test case for realm_client_scopes_id1_protocol_mappers_models_id2_put

    Update the mapper
    """
    body = {"protocol":"protocol","protocolMapper":"protocolMapper","name":"name","id":"id","config":{"key":""}}
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/{realm}/client-scopes/{id1}/protocol-mappers/models/{id2}'.format(realm='realm_example', id1='id1_example', id2='id2_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_client_scopes_id_protocol_mappers_add_models_post(client):
    """Test case for realm_client_scopes_id_protocol_mappers_add_models_post

    Create multiple mappers
    """
    body = {"protocol":"protocol","protocolMapper":"protocolMapper","name":"name","id":"id","config":{"key":""}}
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/{realm}/client-scopes/{id}/protocol-mappers/add-models'.format(realm='realm_example', id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_client_scopes_id_protocol_mappers_models_get(client):
    """Test case for realm_client_scopes_id_protocol_mappers_models_get

    Get mappers
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{realm}/client-scopes/{id}/protocol-mappers/models'.format(realm='realm_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_client_scopes_id_protocol_mappers_models_post(client):
    """Test case for realm_client_scopes_id_protocol_mappers_models_post

    Create a mapper
    """
    body = {"protocol":"protocol","protocolMapper":"protocolMapper","name":"name","id":"id","config":{"key":""}}
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/{realm}/client-scopes/{id}/protocol-mappers/models'.format(realm='realm_example', id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_client_scopes_id_protocol_mappers_protocol_protocol_get(client):
    """Test case for realm_client_scopes_id_protocol_mappers_protocol_protocol_get

    Get mappers by name for a specific protocol
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{realm}/client-scopes/{id}/protocol-mappers/protocol/{protocol}'.format(realm='realm_example', id='id_example', protocol='protocol_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_clients_id1_protocol_mappers_models_id2_delete(client):
    """Test case for realm_clients_id1_protocol_mappers_models_id2_delete

    Delete the mapper
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/{realm}/clients/{id1}/protocol-mappers/models/{id2}'.format(realm='realm_example', id1='id1_example', id2='id2_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_clients_id1_protocol_mappers_models_id2_get(client):
    """Test case for realm_clients_id1_protocol_mappers_models_id2_get

    Get mapper by id
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{realm}/clients/{id1}/protocol-mappers/models/{id2}'.format(realm='realm_example', id1='id1_example', id2='id2_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_clients_id1_protocol_mappers_models_id2_put(client):
    """Test case for realm_clients_id1_protocol_mappers_models_id2_put

    Update the mapper
    """
    body = {"protocol":"protocol","protocolMapper":"protocolMapper","name":"name","id":"id","config":{"key":""}}
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/{realm}/clients/{id1}/protocol-mappers/models/{id2}'.format(realm='realm_example', id1='id1_example', id2='id2_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_clients_id_protocol_mappers_add_models_post(client):
    """Test case for realm_clients_id_protocol_mappers_add_models_post

    Create multiple mappers
    """
    body = {"protocol":"protocol","protocolMapper":"protocolMapper","name":"name","id":"id","config":{"key":""}}
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/{realm}/clients/{id}/protocol-mappers/add-models'.format(realm='realm_example', id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_clients_id_protocol_mappers_models_get(client):
    """Test case for realm_clients_id_protocol_mappers_models_get

    Get mappers
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{realm}/clients/{id}/protocol-mappers/models'.format(realm='realm_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_clients_id_protocol_mappers_models_post(client):
    """Test case for realm_clients_id_protocol_mappers_models_post

    Create a mapper
    """
    body = {"protocol":"protocol","protocolMapper":"protocolMapper","name":"name","id":"id","config":{"key":""}}
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/{realm}/clients/{id}/protocol-mappers/models'.format(realm='realm_example', id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_clients_id_protocol_mappers_protocol_protocol_get(client):
    """Test case for realm_clients_id_protocol_mappers_protocol_protocol_get

    Get mappers by name for a specific protocol
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{realm}/clients/{id}/protocol-mappers/protocol/{protocol}'.format(realm='realm_example', id='id_example', protocol='protocol_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

