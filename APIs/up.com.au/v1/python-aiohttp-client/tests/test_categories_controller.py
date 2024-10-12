# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_category_response import GetCategoryResponse
from openapi_server.models.list_categories_response import ListCategoriesResponse
from openapi_server.models.update_transaction_category_request import UpdateTransactionCategoryRequest


pytestmark = pytest.mark.asyncio

async def test_categories_get(client):
    """Test case for categories_get

    List categories
    """
    params = [('filter[parent]', 'good-life')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/categories',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_categories_id_get(client):
    """Test case for categories_id_get

    Retrieve category
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/categories/{id}'.format(id='restaurants-and-cafes'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_transactions_transaction_id_relationships_category_patch(client):
    """Test case for transactions_transaction_id_relationships_category_patch

    Categorize transaction
    """
    body = {"data":""}
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v1/transactions/{transaction_id}/relationships/category'.format(transaction_id='a572c7c3-b637-433c-a4ce-c0be5dcb0a5a'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

