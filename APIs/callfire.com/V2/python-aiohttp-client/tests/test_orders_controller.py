# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.keyword_purchase_request import KeywordPurchaseRequest
from openapi_server.models.number_order import NumberOrder
from openapi_server.models.number_purchase_request import NumberPurchaseRequest
from openapi_server.models.page_number_order import PageNumberOrder
from openapi_server.models.resource_id import ResourceId


pytestmark = pytest.mark.asyncio

async def test_find_orders(client):
    """Test case for find_orders

    Find orders
    """
    params = [('limit', 20),
                    ('offset', 0),
                    ('fields', 'fields_example'),
                    ('status', ['status_example']),
                    ('intervalBegin', 56),
                    ('intervalEnd', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/orders',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_order(client):
    """Test case for get_order

    Find a specific order
    """
    params = [('fields', 'fields_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/orders/{id}'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_order_keywords(client):
    """Test case for order_keywords

    Purchase keywords
    """
    body = {"keywords":["keywords","keywords"]}
    params = [('fields', 'fields_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/v2/orders/keywords',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_order_numbers(client):
    """Test case for order_numbers

    Purchase numbers
    """
    body = {"promo":"promo","zipcode":"zipcode","tollFreeCount":6,"city":"city","prefix":"prefix","numbers":["numbers","numbers"],"state":"state","localCount":0}
    params = [('fields', 'fields_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/v2/orders/numbers',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

