# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.app_store_review_attachments_response import AppStoreReviewAttachmentsResponse
from openapi_server.models.app_store_review_detail_create_request import AppStoreReviewDetailCreateRequest
from openapi_server.models.app_store_review_detail_response import AppStoreReviewDetailResponse
from openapi_server.models.app_store_review_detail_update_request import AppStoreReviewDetailUpdateRequest
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_app_store_review_details_app_store_review_attachments_get_to_many_related(client):
    """Test case for app_store_review_details_app_store_review_attachments_get_to_many_related

    
    """
    params = [('fields[appStoreReviewDetails]', ['fields_app_store_review_details_example']),
                    ('fields[appStoreReviewAttachments]', ['fields_app_store_review_attachments_example']),
                    ('limit', 56),
                    ('include', ['include_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/appStoreReviewDetails/{id}/appStoreReviewAttachments'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_app_store_review_details_create_instance(client):
    """Test case for app_store_review_details_create_instance

    
    """
    body = {"data":{"relationships":{"appStoreVersion":{"data":{"id":"id","type":"appStoreVersions"}}},"attributes":{"demoAccountPassword":"demoAccountPassword","notes":"notes","contactEmail":"contactEmail","contactFirstName":"contactFirstName","demoAccountRequired":True,"demoAccountName":"demoAccountName","contactLastName":"contactLastName","contactPhone":"contactPhone"},"type":"appStoreReviewDetails"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/appStoreReviewDetails',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_app_store_review_details_get_instance(client):
    """Test case for app_store_review_details_get_instance

    
    """
    params = [('fields[appStoreReviewDetails]', ['fields_app_store_review_details_example']),
                    ('include', ['include_example']),
                    ('fields[appStoreReviewAttachments]', ['fields_app_store_review_attachments_example']),
                    ('limit[appStoreReviewAttachments]', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/appStoreReviewDetails/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_app_store_review_details_update_instance(client):
    """Test case for app_store_review_details_update_instance

    
    """
    body = {"data":{"attributes":{"demoAccountPassword":"demoAccountPassword","notes":"notes","contactEmail":"contactEmail","contactFirstName":"contactFirstName","demoAccountRequired":True,"demoAccountName":"demoAccountName","contactLastName":"contactLastName","contactPhone":"contactPhone"},"id":"id","type":"appStoreReviewDetails"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v1/appStoreReviewDetails/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

