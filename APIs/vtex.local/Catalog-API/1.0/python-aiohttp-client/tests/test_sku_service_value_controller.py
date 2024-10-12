# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.sku_service_value_request import SKUServiceValueRequest
from openapi_server.models.sku_service_value_response import SKUServiceValueResponse


pytestmark = pytest.mark.asyncio

async def test_api_catalog_pvt_skuservicevalue_post(client):
    """Test case for api_catalog_pvt_skuservicevalue_post

    Create SKU Service Value
    """
    body = {"Cost":10.5,"Name":"Test ServiceValue API","SkuServiceTypeId":2,"Value":10.5}
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
        path='/api/catalog/pvt/skuservicevalue',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_catalog_pvt_skuservicevalue_sku_service_value_id_delete(client):
    """Test case for api_catalog_pvt_skuservicevalue_sku_service_value_id_delete

    Delete SKU Service Value
    """
    headers = { 
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/catalog/pvt/skuservicevalue/{sku_service_value_id}'.format(sku_service_value_id=1),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_catalog_pvt_skuservicevalue_sku_service_value_id_get(client):
    """Test case for api_catalog_pvt_skuservicevalue_sku_service_value_id_get

    Get SKU Service Value
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
        path='/api/catalog/pvt/skuservicevalue/{sku_service_value_id}'.format(sku_service_value_id=1),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_catalog_pvt_skuservicevalue_sku_service_value_id_put(client):
    """Test case for api_catalog_pvt_skuservicevalue_sku_service_value_id_put

    Update SKU Service Value
    """
    body = {"Cost":10.5,"Name":"Test ServiceValue API","SkuServiceTypeId":2,"Value":10.5}
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
        path='/api/catalog/pvt/skuservicevalue/{sku_service_value_id}'.format(sku_service_value_id=1),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

