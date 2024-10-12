from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_device_appliance_uplinks_settings200_response import GetDeviceApplianceUplinksSettings200Response
from openapi_server.models.get_device_wireless_bluetooth_settings200_response import GetDeviceWirelessBluetoothSettings200Response
from openapi_server.models.get_network_appliance_settings200_response import GetNetworkApplianceSettings200Response
from openapi_server.models.get_network_settings200_response import GetNetworkSettings200Response
from openapi_server.models.get_network_switch_settings200_response import GetNetworkSwitchSettings200Response
from openapi_server.models.get_network_wireless_bluetooth_settings200_response import GetNetworkWirelessBluetoothSettings200Response
from openapi_server.models.get_network_wireless_settings200_response import GetNetworkWirelessSettings200Response
from openapi_server.models.get_network_wireless_ssid_splash_settings200_response import GetNetworkWirelessSsidSplashSettings200Response
from openapi_server.models.update_device_appliance_uplinks_settings_request import UpdateDeviceApplianceUplinksSettingsRequest
from openapi_server.models.update_device_camera_video_settings_request import UpdateDeviceCameraVideoSettingsRequest
from openapi_server.models.update_device_wireless_bluetooth_settings_request import UpdateDeviceWirelessBluetoothSettingsRequest
from openapi_server.models.update_device_wireless_radio_settings_request import UpdateDeviceWirelessRadioSettingsRequest
from openapi_server.models.update_network_alerts_settings_request import UpdateNetworkAlertsSettingsRequest
from openapi_server.models.update_network_appliance_firewall_settings_request import UpdateNetworkApplianceFirewallSettingsRequest
from openapi_server.models.update_network_appliance_settings_request import UpdateNetworkApplianceSettingsRequest
from openapi_server.models.update_network_appliance_vlans_settings_request import UpdateNetworkApplianceVlansSettingsRequest
from openapi_server.models.update_network_settings_request import UpdateNetworkSettingsRequest
from openapi_server.models.update_network_switch_settings_request import UpdateNetworkSwitchSettingsRequest
from openapi_server.models.update_network_wireless_bluetooth_settings_request import UpdateNetworkWirelessBluetoothSettingsRequest
from openapi_server.models.update_network_wireless_settings_request import UpdateNetworkWirelessSettingsRequest
from openapi_server.models.update_network_wireless_ssid_splash_settings_request import UpdateNetworkWirelessSsidSplashSettingsRequest
from openapi_server.models.update_organization_adaptive_policy_settings_request import UpdateOrganizationAdaptivePolicySettingsRequest
from openapi_server import util


async def get_device_appliance_uplinks_settings_2(request: web.Request, serial) -> web.Response:
    """Return the uplink settings for an MX appliance

    Return the uplink settings for an MX appliance

    :param serial: 
    :type serial: str

    """
    return web.Response(status=200)


async def get_device_camera_video_settings_2(request: web.Request, serial) -> web.Response:
    """Returns video settings for the given camera

    Returns video settings for the given camera

    :param serial: 
    :type serial: str

    """
    return web.Response(status=200)


async def get_device_wireless_bluetooth_settings_2(request: web.Request, serial) -> web.Response:
    """Return the bluetooth settings for a wireless device

    Return the bluetooth settings for a wireless device

    :param serial: 
    :type serial: str

    """
    return web.Response(status=200)


async def get_device_wireless_radio_settings_2(request: web.Request, serial) -> web.Response:
    """Return the radio settings of a device

    Return the radio settings of a device

    :param serial: 
    :type serial: str

    """
    return web.Response(status=200)


async def get_network_alerts_settings_2(request: web.Request, network_id) -> web.Response:
    """Return the alert configuration for this network

    Return the alert configuration for this network

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_appliance_firewall_settings_2(request: web.Request, network_id) -> web.Response:
    """Return the firewall settings for this network

    Return the firewall settings for this network

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_appliance_settings_1(request: web.Request, network_id) -> web.Response:
    """Return the appliance settings for a network

    Return the appliance settings for a network

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_appliance_vlans_settings_2(request: web.Request, network_id) -> web.Response:
    """Returns the enabled status of VLANs for the network

    Returns the enabled status of VLANs for the network

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_settings_1(request: web.Request, network_id) -> web.Response:
    """Return the settings for a network

    Return the settings for a network

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_switch_settings_1(request: web.Request, network_id) -> web.Response:
    """Returns the switch network settings

    Returns the switch network settings

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_wireless_bluetooth_settings_2(request: web.Request, network_id) -> web.Response:
    """Return the Bluetooth settings for a network. &lt;a href&#x3D;\&quot;https://documentation.meraki.com/MR/Bluetooth/Bluetooth_Low_Energy_(BLE)\&quot;&gt;Bluetooth settings&lt;/a&gt; must be enabled on the network.

    Return the Bluetooth settings for a network. &lt;a href&#x3D;\&quot;https://documentation.meraki.com/MR/Bluetooth/Bluetooth_Low_Energy_(BLE)\&quot;&gt;Bluetooth settings&lt;/a&gt; must be enabled on the network.

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_wireless_settings_1(request: web.Request, network_id) -> web.Response:
    """Return the wireless settings for a network

    Return the wireless settings for a network

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_wireless_ssid_splash_settings_3(request: web.Request, network_id, number) -> web.Response:
    """Display the splash page settings for the given SSID

    Display the splash page settings for the given SSID

    :param network_id: 
    :type network_id: str
    :param number: 
    :type number: str

    """
    return web.Response(status=200)


async def get_organization_adaptive_policy_settings_2(request: web.Request, organization_id) -> web.Response:
    """Returns global adaptive policy settings in an organization

    Returns global adaptive policy settings in an organization

    :param organization_id: 
    :type organization_id: str

    """
    return web.Response(status=200)


async def update_device_appliance_uplinks_settings_2(request: web.Request, serial, body) -> web.Response:
    """Update the uplink settings for an MX appliance

    Update the uplink settings for an MX appliance

    :param serial: 
    :type serial: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateDeviceApplianceUplinksSettingsRequest.from_dict(body)
    return web.Response(status=200)


async def update_device_camera_video_settings_2(request: web.Request, serial, body=None) -> web.Response:
    """Update video settings for the given camera

    Update video settings for the given camera

    :param serial: 
    :type serial: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateDeviceCameraVideoSettingsRequest.from_dict(body)
    return web.Response(status=200)


async def update_device_wireless_bluetooth_settings_2(request: web.Request, serial, body=None) -> web.Response:
    """Update the bluetooth settings for a wireless device

    Update the bluetooth settings for a wireless device

    :param serial: 
    :type serial: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateDeviceWirelessBluetoothSettingsRequest.from_dict(body)
    return web.Response(status=200)


async def update_device_wireless_radio_settings_2(request: web.Request, serial, body=None) -> web.Response:
    """Update the radio settings of a device

    Update the radio settings of a device

    :param serial: 
    :type serial: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateDeviceWirelessRadioSettingsRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_alerts_settings_2(request: web.Request, network_id, body=None) -> web.Response:
    """Update the alert configuration for this network

    Update the alert configuration for this network

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkAlertsSettingsRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_appliance_firewall_settings_2(request: web.Request, network_id, body=None) -> web.Response:
    """Update the firewall settings for this network

    Update the firewall settings for this network

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkApplianceFirewallSettingsRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_appliance_settings_1(request: web.Request, network_id, body=None) -> web.Response:
    """Update the appliance settings for a network

    Update the appliance settings for a network

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkApplianceSettingsRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_appliance_vlans_settings_2(request: web.Request, network_id, body=None) -> web.Response:
    """Enable/Disable VLANs for the given network

    Enable/Disable VLANs for the given network

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkApplianceVlansSettingsRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_settings_1(request: web.Request, network_id, body=None) -> web.Response:
    """Update the settings for a network

    Update the settings for a network

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkSettingsRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_switch_settings_1(request: web.Request, network_id, body=None) -> web.Response:
    """Update switch network settings

    Update switch network settings

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkSwitchSettingsRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_wireless_bluetooth_settings_2(request: web.Request, network_id, body=None) -> web.Response:
    """Update the Bluetooth settings for a network

    Update the Bluetooth settings for a network. See the docs page for &lt;a href&#x3D;\&quot;https://documentation.meraki.com/MR/Bluetooth/Bluetooth_Low_Energy_(BLE)\&quot;&gt;Bluetooth settings&lt;/a&gt;.

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkWirelessBluetoothSettingsRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_wireless_settings_1(request: web.Request, network_id, body=None) -> web.Response:
    """Update the wireless settings for a network

    Update the wireless settings for a network

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkWirelessSettingsRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_wireless_ssid_splash_settings_3(request: web.Request, network_id, number, body=None) -> web.Response:
    """Modify the splash page settings for the given SSID

    Modify the splash page settings for the given SSID

    :param network_id: 
    :type network_id: str
    :param number: 
    :type number: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkWirelessSsidSplashSettingsRequest.from_dict(body)
    return web.Response(status=200)


async def update_organization_adaptive_policy_settings_2(request: web.Request, organization_id, body=None) -> web.Response:
    """Update global adaptive policy settings

    Update global adaptive policy settings

    :param organization_id: 
    :type organization_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateOrganizationAdaptivePolicySettingsRequest.from_dict(body)
    return web.Response(status=200)
