# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.list_tags_response import ListTagsResponse
from openapi_server.models.update_transaction_tags_request import UpdateTransactionTagsRequest


pytestmark = pytest.mark.asyncio

async def test_tags_get(client):
    """Test case for tags_get

    List tags
    """
    params = [('page[size]', 50)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/tags',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_transactions_transaction_id_relationships_tags_delete(client):
    """Test case for transactions_transaction_id_relationships_tags_delete

    Remove tags from transaction
    """
    body = {"data":[{"id":"id","type":"type"},{"id":"id","type":"type"}]}
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/transactions/{transaction_id}/relationships/tags'.format(transaction_id='c3feb4ba-829c-4482-b882-1b9bd23da82d'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_transactions_transaction_id_relationships_tags_post(client):
    """Test case for transactions_transaction_id_relationships_tags_post

    Add tags to transaction
    """
    body = {"data":[{"id":"id","type":"type"},{"id":"id","type":"type"}]}
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/transactions/{transaction_id}/relationships/tags'.format(transaction_id='acde4631-db56-49a6-aea3-4e2311ef1d6a'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

