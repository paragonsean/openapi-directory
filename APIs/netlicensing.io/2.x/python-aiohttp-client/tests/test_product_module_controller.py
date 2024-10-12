# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.netlicensing import Netlicensing


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_product_module(client):
    """Test case for create_product_module

    Create Product Module
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'active': True,
        'license_template': TIMEVOLUME,
        'licensing_model': 'licensing_model_example',
        'max_checkout_validity': 56,
        'name': 'name_example',
        'node_secret_mode': PREDEFINED,
        'number': 'number_example',
        'product_number': 'product_number_example',
        'red_threshold': 56,
        'yellow_threshold': 56
        }
    response = await client.request(
        method='POST',
        path='/core/v2/rest/productmodule',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_product_module(client):
    """Test case for delete_product_module

    Delete Product Module
    """
    params = [('forceCascade', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/core/v2/rest/productmodule/{product_module_number}'.format(product_module_number='product_module_number_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_product_module(client):
    """Test case for get_product_module

    Get Product Module
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/core/v2/rest/productmodule/{product_module_number}'.format(product_module_number='product_module_number_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_product_modules(client):
    """Test case for list_product_modules

    List Product Modules
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/core/v2/rest/productmodule',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_update_product_module(client):
    """Test case for update_product_module

    Update Product Module
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'active': True,
        'license_template': TIMEVOLUME,
        'licensing_model': 'licensing_model_example',
        'max_checkout_validity': 56,
        'name': 'name_example',
        'node_secret_mode': PREDEFINED,
        'number': 'number_example',
        'red_threshold': 56,
        'yellow_threshold': 56
        }
    response = await client.request(
        method='POST',
        path='/core/v2/rest/productmodule/{product_module_number}'.format(product_module_number='product_module_number_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

