# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.endpoint_keys_dto import EndpointKeysDTO
from openapi_server.models.endpoint_settings_dto import EndpointSettingsDTO
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_endpoint_keys_get_keys(client):
    """Test case for endpoint_keys_get_keys

    Gets endpoint keys for an endpoint
    """
    headers = { 
        'Accept': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/endpointkeys',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_endpoint_settings_get_settings(client):
    """Test case for endpoint_settings_get_settings

    Gets endpoint settings for an endpoint.
    """
    headers = { 
        'Accept': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/endpointSettings',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

