# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.count import Count
from openapi_server.models.digital_product import DigitalProduct
from openapi_server.models.digital_product_edit import DigitalProductEdit
from openapi_server.models.not_found import NotFound


pytestmark = pytest.mark.asyncio

async def test_products_id_digital_products_count_json_get(client):
    """Test case for products_id_digital_products_count_json_get

    Count all Product DigitalProducts.
    """
    params = [('login', 'login_example'),
                    ('authtoken', 'authtoken_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/products/{id}/digital_products/count.json'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_products_id_digital_products_digital_product_id_json_delete(client):
    """Test case for products_id_digital_products_digital_product_id_json_delete

    Delete a Product DigitalProduct.
    """
    params = [('login', 'login_example'),
                    ('authtoken', 'authtoken_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/products/{id}/digital_products/{digital_product_id_jso}'.format(id=56, digital_product_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_products_id_digital_products_digital_product_id_json_get(client):
    """Test case for products_id_digital_products_digital_product_id_json_get

    Retrieve a single Product DigitalProduct.
    """
    params = [('login', 'login_example'),
                    ('authtoken', 'authtoken_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/products/{id}/digital_products/{digital_product_id_jso}'.format(id=56, digital_product_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_products_id_digital_products_json_get(client):
    """Test case for products_id_digital_products_json_get

    Retrieve all Product DigitalProducts.
    """
    params = [('login', 'login_example'),
                    ('authtoken', 'authtoken_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/products/{id}/digital_products.json'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_products_id_digital_products_json_post(client):
    """Test case for products_id_digital_products_json_post

    Create a new Product DigitalProduct.
    """
    body = {"digital_product":{"filename":"filename","url":"url"}}
    params = [('login', 'login_example'),
                    ('authtoken', 'authtoken_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/products/{id}/digital_products.json'.format(id=56),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

