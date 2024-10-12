# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_products_link_search_get(client):
    """Test case for products_link_search_get

    Search for similar products by providing a link to any e-commerce product.
    """
    params = [('url', 'url_example'),
                    ('providers', 'providers_example')]
    headers = { 
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/products/link-search',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_products_link_search_v2_get(client):
    """Test case for products_link_search_v2_get

    Search for similar products by providing a link to any e-commerce product.
    """
    params = [('url', 'url_example'),
                    ('providers', 'providers_example')]
    headers = { 
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/products/link-search-v2',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_products_search_get(client):
    """Test case for products_search_get

    Search for any product using title
    """
    params = [('term', 'term_example'),
                    ('providers', 'providers_example')]
    headers = { 
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/products/search',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_products_search_v2_get(client):
    """Test case for products_search_v2_get

    Search for any product using title
    """
    params = [('term', 'term_example'),
                    ('providers', 'providers_example')]
    headers = { 
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/products/search-v2',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_products_title_search_get(client):
    """Test case for products_title_search_get

    Search for any product using title
    """
    params = [('term', 'term_example')]
    headers = { 
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/products/title-search',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

