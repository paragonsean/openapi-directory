# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.connection_role import ConnectionRole


pytestmark = pytest.mark.asyncio

async def test_setup_connection_role_get(client):
    """Test case for setup_connection_role_get

    Returns a list of connection roles
    """
    headers = { 
        'Accept': 'application/json',
        'X-User-Access-Key': 'special-key',
        'X-User-Access-Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/setup/connection_role',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_setup_connection_role_id_delete(client):
    """Test case for setup_connection_role_id_delete

    Delete a connection role.
    """
    headers = { 
        'X-User-Access-Key': 'special-key',
        'X-User-Access-Token': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/setup/connection_role/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_setup_connection_role_id_get(client):
    """Test case for setup_connection_role_id_get

    Return a connection role
    """
    headers = { 
        'Accept': 'application/json',
        'X-User-Access-Key': 'special-key',
        'X-User-Access-Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/setup/connection_role/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_setup_connection_role_post(client):
    """Test case for setup_connection_role_post

    Create or update a connection role
    """
    headers = { 
        'Accept': 'application/json',
        'X-User-Access-Key': 'special-key',
        'X-User-Access-Token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/setup/connection_role',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

