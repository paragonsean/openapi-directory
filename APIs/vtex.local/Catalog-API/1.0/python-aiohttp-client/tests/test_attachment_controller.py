# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_catalog_pvt_attachments_get200_response import ApiCatalogPvtAttachmentsGet200Response
from openapi_server.models.attachment_request import AttachmentRequest
from openapi_server.models.attachment_response import AttachmentResponse


pytestmark = pytest.mark.asyncio

async def test_api_catalog_pvt_attachment_attachmentid_delete(client):
    """Test case for api_catalog_pvt_attachment_attachmentid_delete

    Delete attachment
    """
    headers = { 
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/catalog/pvt/attachment/{attachmentid}'.format(attachmentid='vtexcommercestable'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_catalog_pvt_attachment_attachmentid_get(client):
    """Test case for api_catalog_pvt_attachment_attachmentid_get

    Get attachment
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
        path='/api/catalog/pvt/attachment/{attachmentid}'.format(attachmentid='8'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_catalog_pvt_attachment_attachmentid_put(client):
    """Test case for api_catalog_pvt_attachment_attachmentid_put

    Update attachment
    """
    body = {"Domains":[{"DomainValues":"[1-2]#9[1-1][1]basic;#11[0-1][1]basic","FieldName":"Sauce","MaxCaracters":""},{"DomainValues":"[0-10]#8[0-3][0]medium;#9[0-3][0]medium;#10[0-3][0]medium;#11[0-3][0]medium;#36[0-3][0]medium;#37[0-3][0]medium;#38[0-3][0]medium","FieldName":"Toppings","MaxCaracters":""}],"IsActive":True,"IsRequired":True,"Name":"Ingredients"}
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
        path='/api/catalog/pvt/attachment/{attachmentid}'.format(attachmentid='vtexcommercestable'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_catalog_pvt_attachment_post(client):
    """Test case for api_catalog_pvt_attachment_post

    Create attachment
    """
    body = {"Domains":[{"DomainValues":"[1-2]#9[1-1][1]basic;#11[0-1][1]basic","FieldName":"Sauce","MaxCaracters":""},{"DomainValues":"[0-10]#8[0-3][0]medium;#9[0-3][0]medium;#10[0-3][0]medium;#11[0-3][0]medium;#36[0-3][0]medium;#37[0-3][0]medium;#38[0-3][0]medium","FieldName":"Toppings","MaxCaracters":""}],"IsActive":True,"IsRequired":True,"Name":"Ingredients"}
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
        path='/api/catalog/pvt/attachment',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_catalog_pvt_attachments_get(client):
    """Test case for api_catalog_pvt_attachments_get

    Get all attachments
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
        path='/api/catalog/pvt/attachments',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

