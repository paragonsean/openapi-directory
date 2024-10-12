from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_device_wireless_bluetooth_settings200_response import GetDeviceWirelessBluetoothSettings200Response
from openapi_server.models.get_network_wireless_bluetooth_settings200_response import GetNetworkWirelessBluetoothSettings200Response
from openapi_server.models.update_device_wireless_bluetooth_settings_request import UpdateDeviceWirelessBluetoothSettingsRequest
from openapi_server.models.update_network_wireless_bluetooth_settings_request import UpdateNetworkWirelessBluetoothSettingsRequest
from openapi_server import util


async def get_device_wireless_bluetooth_settings_1(request: web.Request, serial) -> web.Response:
    """Return the bluetooth settings for a wireless device

    Return the bluetooth settings for a wireless device

    :param serial: 
    :type serial: str

    """
    return web.Response(status=200)


async def get_network_wireless_bluetooth_settings_1(request: web.Request, network_id) -> web.Response:
    """Return the Bluetooth settings for a network. &lt;a href&#x3D;\&quot;https://documentation.meraki.com/MR/Bluetooth/Bluetooth_Low_Energy_(BLE)\&quot;&gt;Bluetooth settings&lt;/a&gt; must be enabled on the network.

    Return the Bluetooth settings for a network. &lt;a href&#x3D;\&quot;https://documentation.meraki.com/MR/Bluetooth/Bluetooth_Low_Energy_(BLE)\&quot;&gt;Bluetooth settings&lt;/a&gt; must be enabled on the network.

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def update_device_wireless_bluetooth_settings_1(request: web.Request, serial, body=None) -> web.Response:
    """Update the bluetooth settings for a wireless device

    Update the bluetooth settings for a wireless device

    :param serial: 
    :type serial: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateDeviceWirelessBluetoothSettingsRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_wireless_bluetooth_settings_1(request: web.Request, network_id, body=None) -> web.Response:
    """Update the Bluetooth settings for a network

    Update the Bluetooth settings for a network. See the docs page for &lt;a href&#x3D;\&quot;https://documentation.meraki.com/MR/Bluetooth/Bluetooth_Low_Energy_(BLE)\&quot;&gt;Bluetooth settings&lt;/a&gt;.

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkWirelessBluetoothSettingsRequest.from_dict(body)
    return web.Response(status=200)
