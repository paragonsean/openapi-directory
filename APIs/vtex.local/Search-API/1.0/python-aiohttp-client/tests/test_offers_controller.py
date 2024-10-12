# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_catalog_system_pub_products_offers_product_id_get200_response_inner import ApiCatalogSystemPubProductsOffersProductIdGet200ResponseInner


pytestmark = pytest.mark.asyncio

async def test_api_catalog_system_pub_products_offers_product_id_get(client):
    """Test case for api_catalog_system_pub_products_offers_product_id_get

    Search Product offers
    """
    headers = { 
        'Accept': 'application/json',
        'accept': 'application/json',
        'content_type': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/catalog_system/pub/products/offers/{product_id}'.format(product_id='3'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_catalog_system_pub_products_offers_product_id_sku_sku_id_get(client):
    """Test case for api_catalog_system_pub_products_offers_product_id_sku_sku_id_get

    Search SKU offers
    """
    headers = { 
        'Accept': 'application/json',
        'accept': 'application/json',
        'content_type': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/catalog_system/pub/products/offers/{product_id}/sku/{sku_id}'.format(product_id='3', sku_id='5'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

