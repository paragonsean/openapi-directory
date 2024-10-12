# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.bad_request_response import BadRequestResponse
from openapi_server.models.empty_success_response import EmptySuccessResponse
from openapi_server.models.error_not_found import ErrorNotFound
from openapi_server.models.products_product_id_variants_get200_response import ProductsProductIdVariantsGet200Response


pytestmark = pytest.mark.asyncio

async def test_products_product_id_variants_get(client):
    """Test case for products_product_id_variants_get

    Get a product's variants
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/products/{product_id}/variants'.format(product_id='product_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_products_product_id_variants_post(client):
    """Test case for products_product_id_variants_post

    Add a new variant to a product
    """
    params = [('name', 'name_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    data = {
        'ratio': 3.4,
        'variant_id': 'variant_id_example',
        'variant_type': 'variant_type_example'
        }
    response = await client.request(
        method='POST',
        path='/api/v1/products/{product_id}/variants'.format(product_id='product_id_example'),
        headers=headers,
        data=data,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_products_product_id_variants_variant_type_variant_id_delete(client):
    """Test case for products_product_id_variants_variant_type_variant_id_delete

    Delete a product variant
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/products/{product_id}/variants/{variant_type}/{variant_id}'.format(product_id='product_id_example', variant_type='variant_type_example', variant_id='variant_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

