# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_catalog_pvt_skuservicetypeattachment_post200_response import ApiCatalogPvtSkuservicetypeattachmentPost200Response
from openapi_server.models.request_body5 import RequestBody5


pytestmark = pytest.mark.asyncio

async def test_api_catalog_pvt_skuservicetypeattachment_delete(client):
    """Test case for api_catalog_pvt_skuservicetypeattachment_delete

    Dissociate Attachment by Attachment ID or SKU Service Type ID
    """
    params = [('attachmentId', 1),
                    ('skuServiceTypeId', 1)]
    headers = { 
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/catalog/pvt/skuservicetypeattachment',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_catalog_pvt_skuservicetypeattachment_post(client):
    """Test case for api_catalog_pvt_skuservicetypeattachment_post

    Associate SKU Service Attachment
    """
    body = openapi_server.RequestBody5()
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
        path='/api/catalog/pvt/skuservicetypeattachment',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_catalog_pvt_skuservicetypeattachment_sku_service_type_attachment_id_delete(client):
    """Test case for api_catalog_pvt_skuservicetypeattachment_sku_service_type_attachment_id_delete

    Dissociate Attachment from SKU Service Type
    """
    headers = { 
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/catalog/pvt/skuservicetypeattachment/{sku_service_type_attachment_id}'.format(sku_service_type_attachment_id=1),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

