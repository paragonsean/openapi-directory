# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.count import Count
from openapi_server.models.not_found import NotFound
from openapi_server.models.product_option_value import ProductOptionValue
from openapi_server.models.product_option_value_edit import ProductOptionValueEdit


pytestmark = pytest.mark.asyncio

async def test_products_id_options_option_id_values_count_json_get(client):
    """Test case for products_id_options_option_id_values_count_json_get

    Count all Product Option Values.
    """
    params = [('login', 'login_example'),
                    ('authtoken', 'authtoken_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/products/{id}/options/{option_id}/values/count.json'.format(id=56, option_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_products_id_options_option_id_values_json_get(client):
    """Test case for products_id_options_option_id_values_json_get

    Retrieve all Product Option Values.
    """
    params = [('login', 'login_example'),
                    ('authtoken', 'authtoken_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/products/{id}/options/{option_id}/values.json'.format(id=56, option_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_products_id_options_option_id_values_json_post(client):
    """Test case for products_id_options_option_id_values_json_post

    Create a new Product Option Value.
    """
    body = {"value":{"name":"name","position":0}}
    params = [('login', 'login_example'),
                    ('authtoken', 'authtoken_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/products/{id}/options/{option_id}/values.json'.format(id=56, option_id=56),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_products_id_options_option_id_values_value_id_json_delete(client):
    """Test case for products_id_options_option_id_values_value_id_json_delete

    Delete a Product Option Value.
    """
    params = [('login', 'login_example'),
                    ('authtoken', 'authtoken_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/products/{id}/options/{option_id}/values/{value_id_jso}'.format(id=56, option_id=56, value_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_products_id_options_option_id_values_value_id_json_get(client):
    """Test case for products_id_options_option_id_values_value_id_json_get

    Retrieve a single Product Option Value.
    """
    params = [('login', 'login_example'),
                    ('authtoken', 'authtoken_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/products/{id}/options/{option_id}/values/{value_id_jso}'.format(id=56, option_id=56, value_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_products_id_options_option_id_values_value_id_json_put(client):
    """Test case for products_id_options_option_id_values_value_id_json_put

    Modify an existing Product Option Value.
    """
    body = {"value":{"name":"name","position":0}}
    params = [('login', 'login_example'),
                    ('authtoken', 'authtoken_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/v1/products/{id}/options/{option_id}/values/{value_id_jso}'.format(id=56, option_id=56, value_id=56),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

