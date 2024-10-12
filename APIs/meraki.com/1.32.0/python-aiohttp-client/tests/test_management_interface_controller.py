# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.update_device_management_interface_request import UpdateDeviceManagementInterfaceRequest


pytestmark = pytest.mark.asyncio

async def test_get_device_management_interface_1(client):
    """Test case for get_device_management_interface_1

    Return the management interface settings for a device
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/devices/{serial}/managementInterface'.format(serial='serial_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_device_management_interface_1(client):
    """Test case for update_device_management_interface_1

    Update the management interface settings for a device
    """
    body = openapi_server.UpdateDeviceManagementInterfaceRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/devices/{serial}/managementInterface'.format(serial='serial_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

