# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_status import CreateStatus
from openapi_server.models.delete_status import DeleteStatus
from openapi_server.models.error import Error
from openapi_server.models.update_status import UpdateStatus


pytestmark = pytest.mark.asyncio

async def test_bin_id_delete(client):
    """Test case for bin_id_delete

    Delete a json bin
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/api/json-storage/bin/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_bin_id_get(client):
    """Test case for bin_id_get

    Return a json bin
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/json-storage/bin/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_bin_id_patch(client):
    """Test case for bin_id_patch

    Partially update a json bin with JSON Merge Patch
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/api/json-storage/bin/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_bin_id_put(client):
    """Test case for bin_id_put

    Update a json bin
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/json-storage/bin/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_bin_post(client):
    """Test case for bin_post

    Create a json bin
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/json-storage/bin',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

