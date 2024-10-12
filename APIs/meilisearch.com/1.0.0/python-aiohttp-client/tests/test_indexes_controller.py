# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_index_with_primary_key_request import CreateIndexWithPrimaryKeyRequest
from openapi_server.models.swap_indexes_request_inner import SwapIndexesRequestInner
from openapi_server.models.update_index_request import UpdateIndexRequest


pytestmark = pytest.mark.asyncio

async def test_create_index_with_primary_key(client):
    """Test case for create_index_with_primary_key

    Create index with primary key
    """
    body = {"primaryKey":"number","uid":"books"}
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/indexes',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_an_index(client):
    """Test case for delete_an_index

    Delete an index
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/indexes/books',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_indexes(client):
    """Test case for get_indexes

    Get indexes
    """
    params = [('offset', '0'),
                    ('limit', '2')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/indexes',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_show_index(client):
    """Test case for show_index

    Show index
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/indexes/books',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_swap_indexes(client):
    """Test case for swap_indexes

    Swap indexes
    """
    body = [{"indexes":["books","books_temp"]}]
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/indexes/swap-indexes',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_index(client):
    """Test case for update_index

    Update index
    """
    body = {"primaryKey":"title"}
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/indexes/books',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

