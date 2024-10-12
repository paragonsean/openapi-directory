# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.client_initial_access_create_presentation import ClientInitialAccessCreatePresentation
from openapi_server.models.client_initial_access_presentation import ClientInitialAccessPresentation


pytestmark = pytest.mark.asyncio

async def test_realm_clients_initial_access_get(client):
    """Test case for realm_clients_initial_access_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{realm}/clients-initial-access'.format(realm='realm_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_clients_initial_access_id_delete(client):
    """Test case for realm_clients_initial_access_id_delete

    
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/{realm}/clients-initial-access/{id}'.format(realm='realm_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_clients_initial_access_post(client):
    """Test case for realm_clients_initial_access_post

    Create a new initial access token.
    """
    body = {"count":0,"expiration":6}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/{realm}/clients-initial-access'.format(realm='realm_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

