# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_product_request import CreateProductRequest
from openapi_server.models.product_model import ProductModel
from openapi_server.models.product_model_haljson import ProductModelHaljson
from openapi_server.models.update_product_request import UpdateProductRequest


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_create_product(client):
    """Test case for create_product

    Create Product
    """
    body = {"name":"name","description":"description"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/v1/organizations/{organization_id}/products'.format(organization_id='organization_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_product(client):
    """Test case for delete_product

    Delete Product
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/products/{product_id}'.format(product_id='product_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_product(client):
    """Test case for get_product

    Get Product
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/products/{product_id}'.format(product_id='product_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_products(client):
    """Test case for get_products

    List Products
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/products',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_update_product(client):
    """Test case for update_product

    Update Product
    """
    body = {"name":"name","description":"description"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/v1/products/{product_id}'.format(product_id='product_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

