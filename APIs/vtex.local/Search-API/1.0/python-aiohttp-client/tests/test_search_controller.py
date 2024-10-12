# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.product_search_who_bought_also_bought200_response_inner import ProductSearchWhoBoughtAlsoBought200ResponseInner


pytestmark = pytest.mark.asyncio

async def test_product_search(client):
    """Test case for product_search

    Search for Products
    """
    headers = { 
        'Accept': 'application/json',
        'accept': 'application/json',
        'content_type': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/catalog_system/pub/products/search/{search}'.format(search='jacket'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_product_search_filteredand_ordered(client):
    """Test case for product_search_filteredand_ordered

    Search for Products with Filter, Order and Pagination
    """
    params = [('_from', '1'),
                    ('_to', '50'),
                    ('ft', 'television'),
                    ('fq', 'C:/1000041/1000049/'),
                    ('O', 'OrderByNameASC')]
    headers = { 
        'Accept': 'application/json',
        'accept': 'application/json',
        'content_type': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/catalog_system/pub/products/search',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_searchbyproducturl(client):
    """Test case for searchbyproducturl

    Search Product by Product URL
    """
    headers = { 
        'Accept': 'application/json',
        'accept': 'application/json',
        'content_type': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/catalog_system/pub/products/search/{product_text_link}/p'.format(product_text_link='blue-shirt'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

