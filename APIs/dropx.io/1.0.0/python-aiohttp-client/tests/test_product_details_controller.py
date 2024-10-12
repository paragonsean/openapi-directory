# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_products_get(client):
    """Test case for products_get

    Get product details by providing the product IDs
    """
    params = [('pids', 'pids_example')]
    headers = { 
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/products/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

