# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.app_store_version_submission_create_request import AppStoreVersionSubmissionCreateRequest
from openapi_server.models.app_store_version_submission_response import AppStoreVersionSubmissionResponse
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_app_store_version_submissions_create_instance(client):
    """Test case for app_store_version_submissions_create_instance

    
    """
    body = {"data":{"relationships":{"appStoreVersion":{"data":{"id":"id","type":"appStoreVersions"}}},"type":"appStoreVersionSubmissions"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/appStoreVersionSubmissions',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_app_store_version_submissions_delete_instance(client):
    """Test case for app_store_version_submissions_delete_instance

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/appStoreVersionSubmissions/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

