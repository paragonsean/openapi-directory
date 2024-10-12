# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.count import Count
from openapi_server.models.not_found import NotFound
from openapi_server.models.variant import Variant
from openapi_server.models.variant_edit import VariantEdit


pytestmark = pytest.mark.asyncio

async def test_products_id_variants_count_json_get(client):
    """Test case for products_id_variants_count_json_get

    Count all Product Variants.
    """
    params = [('login', 'login_example'),
                    ('authtoken', 'authtoken_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/products/{id}/variants/count.json'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_products_id_variants_json_get(client):
    """Test case for products_id_variants_json_get

    Retrieve all Product Variants.
    """
    params = [('login', 'login_example'),
                    ('authtoken', 'authtoken_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/products/{id}/variants.json'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_products_id_variants_json_post(client):
    """Test case for products_id_variants_json_post

    Create a new Product Variant.
    """
    body = {"variant":{"price":6.0274563,"options":[{"product_value_position":1,"product_option_id":4,"product_option_position":7,"product_option_value_id":1,"name":"name","value":"value"},{"product_value_position":1,"product_option_id":4,"product_option_position":7,"product_option_value_id":1,"name":"name","value":"value"}],"stock_unlimited":True,"image_id":0,"sku":"sku","stock":1}}
    params = [('login', 'login_example'),
                    ('authtoken', 'authtoken_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/products/{id}/variants.json'.format(id=56),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_products_id_variants_variant_id_json_get(client):
    """Test case for products_id_variants_variant_id_json_get

    Retrieve a single Product Variant.
    """
    params = [('login', 'login_example'),
                    ('authtoken', 'authtoken_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/products/{id}/variants/{variant_id_jso}'.format(id=56, variant_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_products_id_variants_variant_id_json_put(client):
    """Test case for products_id_variants_variant_id_json_put

    Modify an existing Product Variant.
    """
    body = {"variant":{"price":6.0274563,"options":[{"product_value_position":1,"product_option_id":4,"product_option_position":7,"product_option_value_id":1,"name":"name","value":"value"},{"product_value_position":1,"product_option_id":4,"product_option_position":7,"product_option_value_id":1,"name":"name","value":"value"}],"stock_unlimited":True,"image_id":0,"sku":"sku","stock":1}}
    params = [('login', 'login_example'),
                    ('authtoken', 'authtoken_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/v1/products/{id}/variants/{variant_id_jso}'.format(id=56, variant_id=56),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

