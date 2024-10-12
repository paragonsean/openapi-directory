# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_catalog_pvt_product_product_id_similarcategory_category_id_post200_response import ApiCatalogPvtProductProductIdSimilarcategoryCategoryIdPost200Response
from openapi_server.models.api_catalog_pvt_product_product_id_similarcategory_get200_response_inner import ApiCatalogPvtProductProductIdSimilarcategoryGet200ResponseInner


pytestmark = pytest.mark.asyncio

async def test_api_catalog_pvt_product_product_id_similarcategory_category_id_delete(client):
    """Test case for api_catalog_pvt_product_product_id_similarcategory_category_id_delete

    Delete Similar Category
    """
    headers = { 
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/catalog/pvt/product/{product_id}/similarcategory/{category_id}'.format(product_id=1, category_id=1),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_catalog_pvt_product_product_id_similarcategory_category_id_post(client):
    """Test case for api_catalog_pvt_product_product_id_similarcategory_category_id_post

    Add Similar Category
    """
    headers = { 
        'Accept': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/catalog/pvt/product/{product_id}/similarcategory/{category_id}'.format(product_id=1, category_id=1),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_catalog_pvt_product_product_id_similarcategory_get(client):
    """Test case for api_catalog_pvt_product_product_id_similarcategory_get

    Get Similar Categories
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
        path='/api/catalog/pvt/product/{product_id}/similarcategory'.format(product_id=1),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

