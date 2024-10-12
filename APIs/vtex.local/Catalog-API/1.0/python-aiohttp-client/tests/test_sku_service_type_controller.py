# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.sku_service_type_request import SKUServiceTypeRequest
from openapi_server.models.sku_service_type_response import SKUServiceTypeResponse


pytestmark = pytest.mark.asyncio

async def test_api_catalog_pvt_skuservicetype_post(client):
    """Test case for api_catalog_pvt_skuservicetype_post

    Create SKU Service Type
    """
    body = {"ShowOnFileUpload":False,"IsRequired":False,"IsActive":True,"IsGiftCard":False,"ShowOnCartFront":False,"ShowOnProductFront":False,"ShowOnAttachmentFront":False,"Name":"Test API Sku Services"}
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
        path='/api/catalog/pvt/skuservicetype',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_catalog_pvt_skuservicetype_sku_service_type_id_delete(client):
    """Test case for api_catalog_pvt_skuservicetype_sku_service_type_id_delete

    Delete SKU Service Type
    """
    headers = { 
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/catalog/pvt/skuservicetype/{sku_service_type_id}'.format(sku_service_type_id=1),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_catalog_pvt_skuservicetype_sku_service_type_id_get(client):
    """Test case for api_catalog_pvt_skuservicetype_sku_service_type_id_get

    Get SKU Service Type
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
        path='/api/catalog/pvt/skuservicetype/{sku_service_type_id}'.format(sku_service_type_id=1),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_catalog_pvt_skuservicetype_sku_service_type_id_put(client):
    """Test case for api_catalog_pvt_skuservicetype_sku_service_type_id_put

    Update SKU Service Type
    """
    body = {"ShowOnFileUpload":False,"IsRequired":False,"IsActive":True,"IsGiftCard":False,"ShowOnCartFront":False,"ShowOnProductFront":False,"ShowOnAttachmentFront":False,"Name":"Test API Sku Services"}
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
        path='/api/catalog/pvt/skuservicetype/{sku_service_type_id}'.format(sku_service_type_id=1),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

