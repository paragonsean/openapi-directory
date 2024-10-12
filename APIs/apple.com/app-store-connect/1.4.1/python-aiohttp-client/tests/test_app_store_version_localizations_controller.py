# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.app_preview_sets_response import AppPreviewSetsResponse
from openapi_server.models.app_screenshot_sets_response import AppScreenshotSetsResponse
from openapi_server.models.app_store_version_localization_create_request import AppStoreVersionLocalizationCreateRequest
from openapi_server.models.app_store_version_localization_response import AppStoreVersionLocalizationResponse
from openapi_server.models.app_store_version_localization_update_request import AppStoreVersionLocalizationUpdateRequest
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_app_store_version_localizations_app_preview_sets_get_to_many_related(client):
    """Test case for app_store_version_localizations_app_preview_sets_get_to_many_related

    
    """
    params = [('filter[previewType]', ['filter_preview_type_example']),
                    ('fields[appStoreVersionLocalizations]', ['fields_app_store_version_localizations_example']),
                    ('fields[appPreviews]', ['fields_app_previews_example']),
                    ('fields[appPreviewSets]', ['fields_app_preview_sets_example']),
                    ('limit', 56),
                    ('include', ['include_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/appStoreVersionLocalizations/{id}/appPreviewSets'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_app_store_version_localizations_app_screenshot_sets_get_to_many_related(client):
    """Test case for app_store_version_localizations_app_screenshot_sets_get_to_many_related

    
    """
    params = [('filter[screenshotDisplayType]', ['filter_screenshot_display_type_example']),
                    ('fields[appStoreVersionLocalizations]', ['fields_app_store_version_localizations_example']),
                    ('fields[appScreenshotSets]', ['fields_app_screenshot_sets_example']),
                    ('fields[appScreenshots]', ['fields_app_screenshots_example']),
                    ('limit', 56),
                    ('include', ['include_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/appStoreVersionLocalizations/{id}/appScreenshotSets'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_app_store_version_localizations_create_instance(client):
    """Test case for app_store_version_localizations_create_instance

    
    """
    body = {"data":{"relationships":{"appStoreVersion":{"data":{"id":"id","type":"appStoreVersions"}}},"attributes":{"whatsNew":"whatsNew","keywords":"keywords","marketingUrl":"https://openapi-generator.tech","supportUrl":"https://openapi-generator.tech","description":"description","locale":"locale","promotionalText":"promotionalText"},"type":"appStoreVersionLocalizations"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/appStoreVersionLocalizations',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_app_store_version_localizations_delete_instance(client):
    """Test case for app_store_version_localizations_delete_instance

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/appStoreVersionLocalizations/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_app_store_version_localizations_get_instance(client):
    """Test case for app_store_version_localizations_get_instance

    
    """
    params = [('fields[appStoreVersionLocalizations]', ['fields_app_store_version_localizations_example']),
                    ('include', ['include_example']),
                    ('fields[appScreenshotSets]', ['fields_app_screenshot_sets_example']),
                    ('fields[appPreviewSets]', ['fields_app_preview_sets_example']),
                    ('limit[appPreviewSets]', 56),
                    ('limit[appScreenshotSets]', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/appStoreVersionLocalizations/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_app_store_version_localizations_update_instance(client):
    """Test case for app_store_version_localizations_update_instance

    
    """
    body = {"data":{"attributes":{"whatsNew":"whatsNew","keywords":"keywords","marketingUrl":"https://openapi-generator.tech","supportUrl":"https://openapi-generator.tech","description":"description","promotionalText":"promotionalText"},"id":"id","type":"appStoreVersionLocalizations"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v1/appStoreVersionLocalizations/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

