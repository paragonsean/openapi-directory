# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.count import Count
from openapi_server.models.not_found import NotFound
from openapi_server.models.product import Product
from openapi_server.models.product_edit import ProductEdit
from openapi_server.models.status_invalid import StatusInvalid


pytestmark = pytest.mark.asyncio

async def test_products_after_id_json_get(client):
    """Test case for products_after_id_json_get

    Retrieves Products after the given id.
    """
    params = [('login', 'login_example'),
                    ('authtoken', 'authtoken_example'),
                    ('locale', 'locale_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/products/after/{id_jso}'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_products_category_category_id_count_json_get(client):
    """Test case for products_category_category_id_count_json_get

    Count Products filtered by category.
    """
    params = [('login', 'login_example'),
                    ('authtoken', 'authtoken_example'),
                    ('locale', 'locale_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/products/category/{category_id}/count.json'.format(category_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_products_category_category_id_json_get(client):
    """Test case for products_category_category_id_json_get

    Retrieve Products filtered by category.
    """
    params = [('login', 'login_example'),
                    ('authtoken', 'authtoken_example'),
                    ('locale', 'locale_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/products/category/{category_id_jso}'.format(category_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_products_count_json_get(client):
    """Test case for products_count_json_get

    Count all Products.
    """
    params = [('login', 'login_example'),
                    ('authtoken', 'authtoken_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/products/count.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_products_id_json_delete(client):
    """Test case for products_id_json_delete

    Delete an existing Product.
    """
    params = [('login', 'login_example'),
                    ('authtoken', 'authtoken_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/products/{id_jso}'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_products_id_json_get(client):
    """Test case for products_id_json_get

    Retrieve a single Product.
    """
    params = [('login', 'login_example'),
                    ('authtoken', 'authtoken_example'),
                    ('locale', 'locale_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/products/{id_jso}'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_products_id_json_put(client):
    """Test case for products_id_json_put

    Modify an existing Product.
    """
    body = {"product":{"featured":False,"page_title":"page_title","length":1.4658129,"description":"description","stock_unlimited":True,"weight":2.302136,"package_format":"box","meta_description":"meta_description","diameter":0.8008282,"price":5.962134,"name":"name","width":7.0614014,"categories":[{"parent_id":6,"name":"name","id":0,"permalink":"permalink"},{"parent_id":6,"name":"name","id":0,"permalink":"permalink"}],"permalink":"permalink","sku":"sku","stock":5,"barcode":"barcode","google_product_category":"google_product_category","height":6.0274563,"shipping_required":True,"status":"available"}}
    params = [('login', 'login_example'),
                    ('authtoken', 'authtoken_example'),
                    ('locale', 'locale_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/v1/products/{id_jso}'.format(id=56),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_products_json_get(client):
    """Test case for products_json_get

    Retrieve all Products.
    """
    params = [('login', 'login_example'),
                    ('authtoken', 'authtoken_example'),
                    ('limit', 50),
                    ('page', 1),
                    ('locale', 'locale_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/products.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_products_json_post(client):
    """Test case for products_json_post

    Create a new Product.
    """
    body = {"product":{"featured":False,"page_title":"page_title","length":1.4658129,"description":"description","stock_unlimited":True,"weight":2.302136,"package_format":"box","meta_description":"meta_description","diameter":0.8008282,"price":5.962134,"name":"name","width":7.0614014,"categories":[{"parent_id":6,"name":"name","id":0,"permalink":"permalink"},{"parent_id":6,"name":"name","id":0,"permalink":"permalink"}],"permalink":"permalink","sku":"sku","stock":5,"barcode":"barcode","google_product_category":"google_product_category","height":6.0274563,"shipping_required":True,"status":"available"}}
    params = [('login', 'login_example'),
                    ('authtoken', 'authtoken_example'),
                    ('locale', 'locale_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/products.json',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_products_search_json_get(client):
    """Test case for products_search_json_get

    Retrieve a Product List from a query.
    """
    params = [('login', 'login_example'),
                    ('authtoken', 'authtoken_example'),
                    ('locale', 'locale_example'),
                    ('query', 'query_example'),
                    ('fields', 'fields_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/products/search.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_products_status_status_count_json_get(client):
    """Test case for products_status_status_count_json_get

    Count Products filtered by status.
    """
    params = [('login', 'login_example'),
                    ('authtoken', 'authtoken_example'),
                    ('locale', 'locale_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/products/status/{status}/count.json'.format(status='status_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_products_status_status_json_get(client):
    """Test case for products_status_status_json_get

    Retrieve Products filtered by status.
    """
    params = [('login', 'login_example'),
                    ('authtoken', 'authtoken_example'),
                    ('locale', 'locale_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/products/status/{status_jso}'.format(status='status_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

