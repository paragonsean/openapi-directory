# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_listings_response import GetListingsResponse
from openapi_server.models.get_product_response import GetProductResponse
from openapi_server.models.get_products_response import GetProductsResponse


pytestmark = pytest.mark.asyncio

async def test_product_listings_all(client):
    """Test case for product_listings_all

    List product listings
    """
    params = [('cursor', 'cursor_example'),
                    ('limit', 50)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/ecosystems/{ecosystem_id}/products/{id}/listings'.format(ecosystem_id='ecosystem_id_example', id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_products_all(client):
    """Test case for products_all

    List products
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/ecosystems/{ecosystem_id}/products'.format(ecosystem_id='ecosystem_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_products_one(client):
    """Test case for products_one

    Get product
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/ecosystems/{ecosystem_id}/products/{id}'.format(ecosystem_id='ecosystem_id_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

