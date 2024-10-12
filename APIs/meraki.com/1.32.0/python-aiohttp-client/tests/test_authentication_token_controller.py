# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_device_appliance_vmx_authentication_token201_response import CreateDeviceApplianceVmxAuthenticationToken201Response


pytestmark = pytest.mark.asyncio

async def test_create_device_appliance_vmx_authentication_token_2(client):
    """Test case for create_device_appliance_vmx_authentication_token_2

    Generate a new vMX authentication token
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/devices/{serial}/appliance/vmx/authenticationToken'.format(serial='serial_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

