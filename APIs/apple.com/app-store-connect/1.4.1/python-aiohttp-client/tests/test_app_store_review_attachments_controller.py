# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.app_store_review_attachment_create_request import AppStoreReviewAttachmentCreateRequest
from openapi_server.models.app_store_review_attachment_response import AppStoreReviewAttachmentResponse
from openapi_server.models.app_store_review_attachment_update_request import AppStoreReviewAttachmentUpdateRequest
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_app_store_review_attachments_create_instance(client):
    """Test case for app_store_review_attachments_create_instance

    
    """
    body = {"data":{"relationships":{"appStoreReviewDetail":{"data":{"id":"id","type":"appStoreReviewDetails"}}},"attributes":{"fileName":"fileName","fileSize":0},"type":"appStoreReviewAttachments"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/appStoreReviewAttachments',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_app_store_review_attachments_delete_instance(client):
    """Test case for app_store_review_attachments_delete_instance

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/appStoreReviewAttachments/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_app_store_review_attachments_get_instance(client):
    """Test case for app_store_review_attachments_get_instance

    
    """
    params = [('fields[appStoreReviewAttachments]', ['fields_app_store_review_attachments_example']),
                    ('include', ['include_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/appStoreReviewAttachments/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_app_store_review_attachments_update_instance(client):
    """Test case for app_store_review_attachments_update_instance

    
    """
    body = {"data":{"attributes":{"uploaded":True,"sourceFileChecksum":"sourceFileChecksum"},"id":"id","type":"appStoreReviewAttachments"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v1/appStoreReviewAttachments/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

