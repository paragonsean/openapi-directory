# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_device_live_tools_ping201_response import CreateDeviceLiveToolsPing201Response
from openapi_server.models.create_device_live_tools_ping_device_request import CreateDeviceLiveToolsPingDeviceRequest
from openapi_server.models.get_device_live_tools_ping200_response import GetDeviceLiveToolsPing200Response


pytestmark = pytest.mark.asyncio

async def test_create_device_live_tools_ping_device_1(client):
    """Test case for create_device_live_tools_ping_device_1

    Enqueue a job to check connectivity status to the device
    """
    body = openapi_server.CreateDeviceLiveToolsPingDeviceRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/devices/{serial}/liveTools/pingDevice'.format(serial='serial_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_device_live_tools_ping_device_1(client):
    """Test case for get_device_live_tools_ping_device_1

    Return a ping device job
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/devices/{serial}/liveTools/pingDevice/{id}'.format(serial='serial_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

