# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_device_code_request import CreateDeviceCodeRequest
from openapi_server.models.create_device_code_response import CreateDeviceCodeResponse
from openapi_server.models.get_device_code_response import GetDeviceCodeResponse
from openapi_server.models.list_device_codes_response import ListDeviceCodesResponse


pytestmark = pytest.mark.asyncio

async def test_create_device_code(client):
    """Test case for create_device_code

    CreateDeviceCode
    """
    body = {"request_body":{"device_code":{"location_id":"B5E4484SHHNYH","name":"Counter 1","product_type":"TERMINAL_API"},"idempotency_key":"01bb00a6-0c86-4770-94ed-f5fca973cd56"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/devices/codes',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_device_code(client):
    """Test case for get_device_code

    GetDeviceCode
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/devices/codes/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_device_codes(client):
    """Test case for list_device_codes

    ListDeviceCodes
    """
    params = [('cursor', 'cursor_example'),
                    ('location_id', 'location_id_example'),
                    ('product_type', 'product_type_example'),
                    ('status', 'status_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/devices/codes',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

