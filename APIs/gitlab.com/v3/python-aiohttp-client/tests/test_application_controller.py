# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.application_setting import ApplicationSetting
from openapi_server.models.put_v3_application_settings_request import PutV3ApplicationSettingsRequest


pytestmark = pytest.mark.asyncio

async def test_get_v3_application_settings(client):
    """Test case for get_v3_application_settings

    Get the current application settings
    """
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/application/settings',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_v3_application_settings(client):
    """Test case for put_v3_application_settings

    Modify application settings
    """
    body = openapi_server.PutV3ApplicationSettingsRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/application/settings',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

