# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.add_product_custom_field import AddProductCustomField
from openapi_server.models.count import Count
from openapi_server.models.message_object import MessageObject
from openapi_server.models.not_found import NotFound
from openapi_server.models.product import Product
from openapi_server.models.product_custom_field import ProductCustomField


pytestmark = pytest.mark.asyncio

async def test_products_id_fields_count_json_get(client):
    """Test case for products_id_fields_count_json_get

    Count all Product Custom Fields.
    """
    params = [('login', 'login_example'),
                    ('authtoken', 'authtoken_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/products/{id}/fields/count.json'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_products_id_fields_json_get(client):
    """Test case for products_id_fields_json_get

    Retrieve all Product Custom Fields
    """
    params = [('login', 'login_example'),
                    ('authtoken', 'authtoken_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/products/{id}/fields.json'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_products_id_fields_json_post(client):
    """Test case for products_id_fields_json_post

    Add an existing Custom Field to a Product.
    """
    body = {"field":{"id":0,"value":"value"}}
    params = [('login', 'login_example'),
                    ('authtoken', 'authtoken_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/products/{id}/fields.json'.format(id=56),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_products_product_id_fields_field_id_json_delete(client):
    """Test case for products_product_id_fields_field_id_json_delete

    Delete value of Product Custom Field
    """
    params = [('login', 'login_example'),
                    ('authtoken', 'authtoken_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/products/{product_id}/fields/{field_id_jso}'.format(product_id=56, field_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_products_product_id_fields_field_id_json_put(client):
    """Test case for products_product_id_fields_field_id_json_put

    Update value of Product Custom Field
    """
    params = [('login', 'login_example'),
                    ('authtoken', 'authtoken_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/v1/products/{product_id}/fields/{field_id_jso}'.format(product_id=56, field_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

