# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.endpoint_keys_dto import EndpointKeysDTO
from openapi_server.models.endpoint_settings_dto import EndpointSettingsDTO
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_endpoint_keys_refresh_keys(client):
    """Test case for endpoint_keys_refresh_keys

    Re-generates an endpoint key.
    """
    headers = { 
        'Accept': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/endpointkeys/{key_type}'.format(key_type='key_type_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_endpoint_settings_update_settings(client):
    """Test case for endpoint_settings_update_settings

    Updates endpoint settings for an endpoint.
    """
    endpoint_settings_payload = {"activeLearning":"{}"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/endpointSettings',
        headers=headers,
        json=endpoint_settings_payload,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

