# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_a_key_request import CreateAKeyRequest
from openapi_server.models.update_a_key_request import UpdateAKeyRequest


pytestmark = pytest.mark.asyncio

async def test_create_a_key(client):
    """Test case for create_a_key

    Create a key
    """
    body = {"actions":["documents.add","documents.delete"],"description":"Key to add and delete documents, in `books` index.","expiresAt":null,"indexes":["books"],"name":"docs-key"}
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/keys',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_a_key(client):
    """Test case for delete_a_key

    Delete a key
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/keys/kN2aK9EO8a7b627e425717d9196c8081552ca004e513545ed178f8a56981dbd3080d4a5b',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_keys(client):
    """Test case for get_keys

    Get keys
    """
    params = [('offset', '0'),
                    ('limit', '10')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/keys',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_one_key(client):
    """Test case for get_one_key

    Get one key
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/keys/L8l05tFb188aab693735bbaf1f898b9902fb39f865160d39dddba2b47b940115a0430705',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_a_key(client):
    """Test case for update_a_key

    Update a key
    """
    body = {"description":"Key to add and delete documents, but also to create indexes, in `book` index."}
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/keys/wYZjGJyBcdb0621b97999c233246a8ec0a35d0fcd9a6417ef8ccee0c8978b64b123af2dd',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

