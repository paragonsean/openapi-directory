# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.netlicensing import Netlicensing


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_product(client):
    """Test case for create_product

    Create Product
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'active': True,
        'description': 'description_example',
        'licensee_auto_create': True,
        'licensing_info': 'licensing_info_example',
        'name': 'name_example',
        'number': 'number_example',
        'vat_mode': 'vat_mode_example',
        'version': 'version_example'
        }
    response = await client.request(
        method='POST',
        path='/core/v2/rest/product',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_product(client):
    """Test case for delete_product

    Delete Product
    """
    params = [('forceCascade', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/core/v2/rest/product/{product_number}'.format(product_number='product_number_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_products(client):
    """Test case for list_products

    List Products
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/core/v2/rest/product',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_product_number(client):
    """Test case for product_number

    Get Product
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/core/v2/rest/product/{product_number}'.format(product_number='product_number_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_update_product(client):
    """Test case for update_product

    Update Product
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'active': True,
        'description': 'description_example',
        'licensee_auto_create': True,
        'licensing_info': 'licensing_info_example',
        'name': 'name_example',
        'number': 'number_example',
        'vat_mode': 'vat_mode_example',
        'version': 'version_example'
        }
    response = await client.request(
        method='POST',
        path='/core/v2/rest/product/{product_number}'.format(product_number='product_number_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

