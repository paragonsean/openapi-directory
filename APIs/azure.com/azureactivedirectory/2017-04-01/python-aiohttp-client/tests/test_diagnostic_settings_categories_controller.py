# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.diagnostic_settings_category_resource_collection import DiagnosticSettingsCategoryResourceCollection
from openapi_server.models.error_response import ErrorResponse


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
        path='/providers/microsoft.aadiam/diagnosticSettingsCategories',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

