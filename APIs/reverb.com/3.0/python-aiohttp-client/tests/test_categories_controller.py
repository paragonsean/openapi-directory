# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_categories_flat_get(client):
    """Test case for categories_flat_get

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/categories/flat',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_categories_get(client):
    """Test case for categories_get

    List of supported product categories
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/categories',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_categories_product_type_category_get(client):
    """Test case for categories_product_type_category_get

    Get subcategory details
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/categories/{product_type}/{category}'.format(product_type='product_type_example', category='category_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_categories_taxonomy_get(client):
    """Test case for categories_taxonomy_get

    Full taxonomy tree of categories including middle categories
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/categories/taxonomy',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_categories_uuid_get(client):
    """Test case for categories_uuid_get

    Get category details
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/categories/{uuid}'.format(uuid='uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

