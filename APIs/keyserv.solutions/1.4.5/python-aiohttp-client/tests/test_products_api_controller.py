# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.product_view import ProductView
from openapi_server.models.products_api_count200_response import ProductsApiCount200Response
from openapi_server.models.products_api_count_request import ProductsApiCountRequest
from openapi_server.models.products_api_find200_response import ProductsApiFind200Response
from openapi_server.models.products_api_find_request import ProductsApiFindRequest
from openapi_server.models.products_api_patch_product2_request import ProductsApiPatchProduct2Request


pytestmark = pytest.mark.asyncio

async def test_products_api_count(client):
    """Test case for products_api_count

    
    """
    body = openapi_server.ProductsApiCountRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/ProductsApi/Count',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_products_api_delete_product(client):
    """Test case for products_api_delete_product

    
    """
    headers = { 
        'x_api_key': 'x_api_key_example',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/ProductsApi/{serial}'.format(serial='serial_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_products_api_delete_product2(client):
    """Test case for products_api_delete_product2

    
    """
    headers = { 
        'x_api_key': 'x_api_key_example',
    }
    response = await client.request(
        method='POST',
        path='/v1/ProductsApi/{serial}'.format(serial='serial_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_products_api_find(client):
    """Test case for products_api_find

    
    """
    body = openapi_server.ProductsApiFindRequest()
    params = [('page', 56)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/ProductsApi/Find',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_products_api_list(client):
    """Test case for products_api_list

    
    """
    body = openapi_server.ProductsApiCountRequest()
    params = [('page', 56)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/ProductsApi/List',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_products_api_patch_product(client):
    """Test case for products_api_patch_product

    
    """
    body = openapi_server.ProductsApiPatchProduct2Request()
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/v1/ProductsApi',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_products_api_patch_product2(client):
    """Test case for products_api_patch_product2

    
    """
    body = openapi_server.ProductsApiPatchProduct2Request()
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/ProductsApi',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_products_api_save(client):
    """Test case for products_api_save

    
    """
    body = openapi_server.ProductsApiPatchProduct2Request()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/ProductsApi/Save',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

