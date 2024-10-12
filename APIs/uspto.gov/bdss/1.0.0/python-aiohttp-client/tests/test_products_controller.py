# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_get_latest_product_files_by_product_id_and_time(client):
    """Test case for get_latest_product_files_by_product_id_and_time

    Returns products along with their latest files by short names.
    """
    params = [('year', 56),
                    ('hierarchy', 'false')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/BDSS-API/products/{short_name}/latest'.format(short_name='short_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_populart_products(client):
    """Test case for get_populart_products

    Returns popular products along with latest files.
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/BDSS-API/products/popular',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_product_sub_tree(client):
    """Test case for get_product_sub_tree

    Returns products' hierarchical subtree.
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/BDSS-API/products/tree/{short_name}'.format(short_name='short_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_products_by_name(client):
    """Test case for get_products_by_name

    Returns files associated with products (of level PRODUCT) based on their full or partial names.
    """
    params = [('fromYear', 56),
                    ('toYear', 56),
                    ('fromMonth', 56),
                    ('toMonth', 56),
                    ('fromDay', 56),
                    ('toDay', 56),
                    ('hierarchy', 'false'),
                    ('maxFiles', 20)]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/BDSS-API/products/byname/{product_name}'.format(product_name='product_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_products_by_short_name(client):
    """Test case for get_products_by_short_name

    Returns products along with their associated files by short names.
    """
    params = [('fromYear', 56),
                    ('toYear', 56),
                    ('fromMonth', 56),
                    ('toMonth', 56),
                    ('fromDay', 56),
                    ('toDay', 56),
                    ('fromDate', 'from_date_example'),
                    ('toDate', 'to_date_example'),
                    ('hierarchy', 'false')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/BDSS-API/products/{short_name}'.format(short_name='short_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_products_tree(client):
    """Test case for get_products_tree

    Returns products' hierarchical tree.
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/BDSS-API/products/tree',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_products_with_latest_product_files(client):
    """Test case for get_products_with_latest_product_files

    Returns all products with Latest Files.
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/BDSS-API/products/all/latest',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

