# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.request_body3 import RequestBody3
from openapi_server.models.request_body4 import RequestBody4
from openapi_server.models.sku_service import SKUService


pytestmark = pytest.mark.asyncio

async def test_api_catalog_pvt_skuservice_post(client):
    """Test case for api_catalog_pvt_skuservice_post

    Associate SKU Service
    """
    body = openapi_server.RequestBody3()
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
        path='/api/catalog/pvt/skuservice',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_catalog_pvt_skuservice_sku_service_id_delete(client):
    """Test case for api_catalog_pvt_skuservice_sku_service_id_delete

    Dissociate SKU Service
    """
    headers = { 
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/catalog/pvt/skuservice/{sku_service_id}'.format(sku_service_id=1),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_catalog_pvt_skuservice_sku_service_id_get(client):
    """Test case for api_catalog_pvt_skuservice_sku_service_id_get

    Get SKU Service
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
        path='/api/catalog/pvt/skuservice/{sku_service_id}'.format(sku_service_id=5),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_catalog_pvt_skuservice_sku_service_id_put(client):
    """Test case for api_catalog_pvt_skuservice_sku_service_id_put

    Update SKU Service
    """
    body = openapi_server.RequestBody4()
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
        path='/api/catalog/pvt/skuservice/{sku_service_id}'.format(sku_service_id=5),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

