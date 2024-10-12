# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_catalog_pvt_product_post200_response import ApiCatalogPvtProductPost200Response
from openapi_server.models.api_catalog_pvt_product_post_request import ApiCatalogPvtProductPostRequest
from openapi_server.models.api_catalog_pvt_product_product_id_put_request import ApiCatalogPvtProductProductIdPutRequest
from openapi_server.models.get_productbyid200_response import GetProductbyid200Response
from openapi_server.models.product_and_sku_ids200_response import ProductAndSkuIds200Response
from openapi_server.models.product_variations200_response import ProductVariations200Response
from openapi_server.models.productand_trade_policy200_response import ProductandTradePolicy200Response
from openapi_server.models.productby_ref_id200_response import ProductbyRefId200Response


pytestmark = pytest.mark.asyncio

async def test_api_catalog_pvt_product_post(client):
    """Test case for api_catalog_pvt_product_post

    Create Product with Category and Brand
    """
    body = openapi_server.ApiCatalogPvtProductPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/catalog/pvt/product',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_catalog_pvt_product_product_id_put(client):
    """Test case for api_catalog_pvt_product_product_id_put

    Update Product
    """
    body = openapi_server.ApiCatalogPvtProductProductIdPutRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/catalog/pvt/product/{product_id}'.format(product_id=1),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_productbyid(client):
    """Test case for get_productbyid

    Get Product by ID
    """
    headers = { 
        'Accept': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/catalog/pvt/product/{product_id}'.format(product_id='product_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_product_and_sku_ids(client):
    """Test case for product_and_sku_ids

    Get Product and SKU IDs
    """
    params = [('categoryId', 1),
                    ('_from', 1),
                    ('_to', 10)]
    headers = { 
        'Accept': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/catalog_system/pvt/products/GetProductAndSkuIds',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_product_variations(client):
    """Test case for product_variations

    Get Product's SKUs by Product ID
    """
    headers = { 
        'Accept': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/catalog_system/pub/products/variations/{product_id}'.format(product_id=1),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_productand_trade_policy(client):
    """Test case for productand_trade_policy

    Get Product and its general context
    """
    headers = { 
        'Accept': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/catalog_system/pvt/products/productget/{product_id}'.format(product_id=1),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_productby_ref_id(client):
    """Test case for productby_ref_id

    Get Product by RefId
    """
    headers = { 
        'Accept': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/catalog_system/pvt/products/productgetbyrefid/{ref_id}'.format(ref_id='ref_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_review_rate_product(client):
    """Test case for review_rate_product

    Get Product Review Rate by Product ID
    """
    headers = { 
        'Accept': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/addon/pvt/review/GetProductRate/{product_id}'.format(product_id=1),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

