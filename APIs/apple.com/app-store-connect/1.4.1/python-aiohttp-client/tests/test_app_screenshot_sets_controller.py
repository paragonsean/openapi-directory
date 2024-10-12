# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.app_screenshot_set_app_screenshots_linkages_request import AppScreenshotSetAppScreenshotsLinkagesRequest
from openapi_server.models.app_screenshot_set_app_screenshots_linkages_response import AppScreenshotSetAppScreenshotsLinkagesResponse
from openapi_server.models.app_screenshot_set_create_request import AppScreenshotSetCreateRequest
from openapi_server.models.app_screenshot_set_response import AppScreenshotSetResponse
from openapi_server.models.app_screenshots_response import AppScreenshotsResponse
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_app_screenshot_sets_app_screenshots_get_to_many_related(client):
    """Test case for app_screenshot_sets_app_screenshots_get_to_many_related

    
    """
    params = [('fields[appScreenshotSets]', ['fields_app_screenshot_sets_example']),
                    ('fields[appScreenshots]', ['fields_app_screenshots_example']),
                    ('limit', 56),
                    ('include', ['include_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/appScreenshotSets/{id}/appScreenshots'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_app_screenshot_sets_app_screenshots_get_to_many_relationship(client):
    """Test case for app_screenshot_sets_app_screenshots_get_to_many_relationship

    
    """
    params = [('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/appScreenshotSets/{id}/relationships/appScreenshots'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_app_screenshot_sets_app_screenshots_replace_to_many_relationship(client):
    """Test case for app_screenshot_sets_app_screenshots_replace_to_many_relationship

    
    """
    body = {"data":[{"id":"id","type":"appScreenshots"},{"id":"id","type":"appScreenshots"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v1/appScreenshotSets/{id}/relationships/appScreenshots'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_app_screenshot_sets_create_instance(client):
    """Test case for app_screenshot_sets_create_instance

    
    """
    body = {"data":{"relationships":{"appStoreVersionLocalization":{"data":{"id":"id","type":"appStoreVersionLocalizations"}}},"attributes":{"screenshotDisplayType":"APP_IPHONE_65"},"type":"appScreenshotSets"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/appScreenshotSets',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_app_screenshot_sets_delete_instance(client):
    """Test case for app_screenshot_sets_delete_instance

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/appScreenshotSets/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_app_screenshot_sets_get_instance(client):
    """Test case for app_screenshot_sets_get_instance

    
    """
    params = [('fields[appScreenshotSets]', ['fields_app_screenshot_sets_example']),
                    ('include', ['include_example']),
                    ('fields[appScreenshots]', ['fields_app_screenshots_example']),
                    ('limit[appScreenshots]', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/appScreenshotSets/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

