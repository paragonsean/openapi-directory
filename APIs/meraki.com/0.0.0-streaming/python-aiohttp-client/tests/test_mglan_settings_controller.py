# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.update_device_cellular_gateway_settings_request import UpdateDeviceCellularGatewaySettingsRequest


pytestmark = pytest.mark.asyncio

async def test_get_device_cellular_gateway_settings(client):
    """Test case for get_device_cellular_gateway_settings

    Show the LAN Settings of a MG
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v0/devices/{serial}/cellularGateway/settings'.format(serial='serial_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_device_cellular_gateway_settings(client):
    """Test case for update_device_cellular_gateway_settings

    Update the LAN Settings for a single MG.
    """
    body = openapi_server.UpdateDeviceCellularGatewaySettingsRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v0/devices/{serial}/cellularGateway/settings'.format(serial='serial_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

