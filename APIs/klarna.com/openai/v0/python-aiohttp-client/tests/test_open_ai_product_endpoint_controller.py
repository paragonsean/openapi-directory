# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.product_response import ProductResponse


pytestmark = pytest.mark.asyncio

async def test_products_using_get(client):
    """Test case for products_using_get

    API for fetching Klarna product information
    """
    params = [('q', 'q_example'),
                    ('size', 56),
                    ('budget', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/us/shopping/public/openai/v0/products',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

