# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.update_device_cellular_gateway_lan_request import UpdateDeviceCellularGatewayLanRequest


pytestmark = pytest.mark.asyncio

async def test_get_device_cellular_gateway_lan_1(client):
    """Test case for get_device_cellular_gateway_lan_1

    Show the LAN Settings of a MG
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/devices/{serial}/cellularGateway/lan'.format(serial='serial_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_device_cellular_gateway_lan_1(client):
    """Test case for update_device_cellular_gateway_lan_1

    Update the LAN Settings for a single MG.
    """
    body = openapi_server.UpdateDeviceCellularGatewayLanRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/devices/{serial}/cellularGateway/lan'.format(serial='serial_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

