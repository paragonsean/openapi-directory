# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_catalog_pvt_skuattachment_post200_response import ApiCatalogPvtSkuattachmentPost200Response
from openapi_server.models.associateattachmentsto_sku_request import AssociateattachmentstoSKURequest
from openapi_server.models.request_body1 import RequestBody1


pytestmark = pytest.mark.asyncio

async def test_api_catalog_pvt_skuattachment_delete(client):
    """Test case for api_catalog_pvt_skuattachment_delete

    Dissociate attachments and SKUs
    """
    params = [('skuId', 1),
                    ('attachmentId', 1)]
    headers = { 
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/catalog/pvt/skuattachment',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_catalog_pvt_skuattachment_post(client):
    """Test case for api_catalog_pvt_skuattachment_post

    Associate SKU Attachment
    """
    body = openapi_server.RequestBody1()
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
        path='/api/catalog/pvt/skuattachment',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_catalog_pvt_skuattachment_sku_attachment_association_id_delete(client):
    """Test case for api_catalog_pvt_skuattachment_sku_attachment_association_id_delete

    Delete SKU Attachment by Attachment Association ID
    """
    headers = { 
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/catalog/pvt/skuattachment/{sku_attachment_association_id}'.format(sku_attachment_association_id=1),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_catalog_pvt_stockkeepingunit_sku_id_attachment_get(client):
    """Test case for api_catalog_pvt_stockkeepingunit_sku_id_attachment_get

    Get SKU Attachments by SKU ID
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
        path='/api/catalog/pvt/stockkeepingunit/{sku_id}/attachment'.format(sku_id=1),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_associateattachmentsto_sku(client):
    """Test case for associateattachmentsto_sku

    Associate attachments to an SKU
    """
    body = {"AttachmentNames":["T-Shirt Customization"],"SkuId":1}
    headers = { 
        'Content-Type': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/catalog_system/pvt/sku/associateattachments',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

