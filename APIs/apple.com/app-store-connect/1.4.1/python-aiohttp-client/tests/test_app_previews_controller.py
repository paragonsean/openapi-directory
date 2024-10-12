# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.app_preview_create_request import AppPreviewCreateRequest
from openapi_server.models.app_preview_response import AppPreviewResponse
from openapi_server.models.app_preview_update_request import AppPreviewUpdateRequest
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_app_previews_create_instance(client):
    """Test case for app_previews_create_instance

    
    """
    body = {"data":{"relationships":{"appPreviewSet":{"data":{"id":"id","type":"appPreviewSets"}}},"attributes":{"fileName":"fileName","fileSize":0,"mimeType":"mimeType","previewFrameTimeCode":"previewFrameTimeCode"},"type":"appPreviews"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/appPreviews',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_app_previews_delete_instance(client):
    """Test case for app_previews_delete_instance

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/appPreviews/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_app_previews_get_instance(client):
    """Test case for app_previews_get_instance

    
    """
    params = [('fields[appPreviews]', ['fields_app_previews_example']),
                    ('include', ['include_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/appPreviews/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_app_previews_update_instance(client):
    """Test case for app_previews_update_instance

    
    """
    body = {"data":{"attributes":{"uploaded":True,"previewFrameTimeCode":"previewFrameTimeCode","sourceFileChecksum":"sourceFileChecksum"},"id":"id","type":"appPreviews"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v1/appPreviews/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

