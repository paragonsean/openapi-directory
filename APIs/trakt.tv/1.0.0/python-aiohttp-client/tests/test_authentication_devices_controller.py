# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.generate_new_device_codes_request import GenerateNewDeviceCodesRequest
from openapi_server.models.poll_for_the_access_token_request import PollForTheAccessTokenRequest


pytestmark = pytest.mark.asyncio

async def test_generate_new_device_codes(client):
    """Test case for generate_new_device_codes

    Generate new device codes
    """
    body = openapi_server.GenerateNewDeviceCodesRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/oauth/device/code',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_poll_for_the_access_token(client):
    """Test case for poll_for_the_access_token

    Poll for the access_token
    """
    body = openapi_server.PollForTheAccessTokenRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/oauth/device/token',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

