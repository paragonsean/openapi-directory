# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.model_settings_response import ModelSettingsResponse
from openapi_server.models.tsi_error import TsiError
from openapi_server.models.update_model_settings_request import UpdateModelSettingsRequest


pytestmark = pytest.mark.asyncio

async def test_model_settings_get(client):
    """Test case for model_settings_get

    
    """
    params = [('api-version', '2018-11-01-preview')]
    headers = { 
        'Accept': 'application/json',
        'x_ms_client_request_id': 'x_ms_client_request_id_example',
        'x_ms_client_session_id': 'x_ms_client_session_id_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/timeseries/modelSettings',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_model_settings_update(client):
    """Test case for model_settings_update

    
    """
    parameters = {"defaultTypeId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","name":"name"}
    params = [('api-version', '2018-11-01-preview')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_ms_client_request_id': 'x_ms_client_request_id_example',
        'x_ms_client_session_id': 'x_ms_client_session_id_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/timeseries/modelSettings',
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

