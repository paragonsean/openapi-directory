# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.app_screenshot_create_request import AppScreenshotCreateRequest
from openapi_server.models.app_screenshot_response import AppScreenshotResponse
from openapi_server.models.app_screenshot_update_request import AppScreenshotUpdateRequest
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_app_screenshots_create_instance(client):
    """Test case for app_screenshots_create_instance

    
    """
    body = {"data":{"relationships":{"appScreenshotSet":{"data":{"id":"id","type":"appScreenshotSets"}}},"attributes":{"fileName":"fileName","fileSize":0},"type":"appScreenshots"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/appScreenshots',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_app_screenshots_delete_instance(client):
    """Test case for app_screenshots_delete_instance

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/appScreenshots/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_app_screenshots_get_instance(client):
    """Test case for app_screenshots_get_instance

    
    """
    params = [('fields[appScreenshots]', ['fields_app_screenshots_example']),
                    ('include', ['include_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/appScreenshots/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_app_screenshots_update_instance(client):
    """Test case for app_screenshots_update_instance

    
    """
    body = {"data":{"attributes":{"uploaded":True,"sourceFileChecksum":"sourceFileChecksum"},"id":"id","type":"appScreenshots"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v1/appScreenshots/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

