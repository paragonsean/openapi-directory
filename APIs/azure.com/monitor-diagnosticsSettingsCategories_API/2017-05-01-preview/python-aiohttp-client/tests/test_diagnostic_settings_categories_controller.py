# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.diagnostic_settings_category_resource import DiagnosticSettingsCategoryResource
from openapi_server.models.diagnostic_settings_category_resource_collection import DiagnosticSettingsCategoryResourceCollection
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_diagnostic_settings_category_get(client):
    """Test case for diagnostic_settings_category_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{resource_uri}/providers/microsoft.insights/diagnosticSettingsCategories/{name}'.format(resource_uri='resource_uri_example', name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_diagnostic_settings_category_list(client):
    """Test case for diagnostic_settings_category_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{resource_uri}/providers/microsoft.insights/diagnosticSettingsCategories'.format(resource_uri='resource_uri_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

