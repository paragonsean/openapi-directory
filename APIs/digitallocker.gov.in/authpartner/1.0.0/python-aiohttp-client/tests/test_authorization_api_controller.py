# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.device_authorization_code import DeviceAuthorizationCode
from openapi_server.models.device_authorization_code_response import DeviceAuthorizationCodeResponse
from openapi_server.models.get_device_code_id400_response import GetDeviceCodeId400Response
from openapi_server.models.get_device_code_id401_response import GetDeviceCodeId401Response
from openapi_server.models.get_device_code_id500_response import GetDeviceCodeId500Response


pytestmark = pytest.mark.asyncio

async def test_get_device_code_id(client):
    """Test case for get_device_code_id

    Get Device Code
    """
    body = {"response_type":"device_code","dl_mobile":0,"dl_username":"dl_username","client_id":"client_id"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/public/oauth2/1/code',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

