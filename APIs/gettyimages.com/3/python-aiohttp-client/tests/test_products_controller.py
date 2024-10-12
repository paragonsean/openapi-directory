# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.product_field_values import ProductFieldValues
from openapi_server.models.products_result import ProductsResult


pytestmark = pytest.mark.asyncio

async def test_v3_products_get(client):
    """Test case for v3_products_get

    Get Products
    """
    params = [('fields', [openapi_server.ProductFieldValues()])]
    headers = { 
        'Accept': 'application/json',
        'accept_language': 'accept_language_example',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Api-Key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/products',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

