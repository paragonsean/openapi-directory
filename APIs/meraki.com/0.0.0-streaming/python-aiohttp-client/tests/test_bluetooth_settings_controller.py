# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_network_bluetooth_settings200_response import GetNetworkBluetoothSettings200Response
from openapi_server.models.update_device_wireless_bluetooth_settings200_response import UpdateDeviceWirelessBluetoothSettings200Response
from openapi_server.models.update_device_wireless_bluetooth_settings_request import UpdateDeviceWirelessBluetoothSettingsRequest
from openapi_server.models.update_network_bluetooth_settings_request import UpdateNetworkBluetoothSettingsRequest


pytestmark = pytest.mark.asyncio

async def test_get_network_bluetooth_settings(client):
    """Test case for get_network_bluetooth_settings

    Return the Bluetooth settings for a network. <a href=\"https://documentation.meraki.com/MR/Bluetooth/Bluetooth_Low_Energy_(BLE)\">Bluetooth settings</a> must be enabled on the network.
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v0/networks/{network_id}/bluetoothSettings'.format(network_id='network_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_device_wireless_bluetooth_settings(client):
    """Test case for update_device_wireless_bluetooth_settings

    Update the bluetooth settings for a wireless device
    """
    body = openapi_server.UpdateDeviceWirelessBluetoothSettingsRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v0/devices/{serial}/wireless/bluetooth/settings'.format(serial='serial_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_network_bluetooth_settings(client):
    """Test case for update_network_bluetooth_settings

    Update the Bluetooth settings for a network
    """
    body = openapi_server.UpdateNetworkBluetoothSettingsRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v0/networks/{network_id}/bluetoothSettings'.format(network_id='network_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

