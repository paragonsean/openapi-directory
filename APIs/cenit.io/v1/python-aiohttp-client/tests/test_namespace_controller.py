# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.namespace import Namespace


pytestmark = pytest.mark.asyncio

async def test_setup_namespace_get(client):
    """Test case for setup_namespace_get

    Returns a list of namespaces
    """
    headers = { 
        'Accept': 'application/json',
        'X-User-Access-Key': 'special-key',
        'X-User-Access-Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/setup/namespace/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_setup_namespace_id_delete(client):
    """Test case for setup_namespace_id_delete

    Delete a namespace
    """
    headers = { 
        'X-User-Access-Key': 'special-key',
        'X-User-Access-Token': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/setup/namespace/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_setup_namespace_id_get(client):
    """Test case for setup_namespace_id_get

    Retrieve an existing namespace
    """
    headers = { 
        'Accept': 'application/json',
        'X-User-Access-Key': 'special-key',
        'X-User-Access-Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/setup/namespace/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_setup_namespace_post(client):
    """Test case for setup_namespace_post

    Create or update a namespace
    """
    headers = { 
        'Accept': 'application/json',
        'X-User-Access-Key': 'special-key',
        'X-User-Access-Token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/setup/namespace/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

