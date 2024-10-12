# coding: utf-8

import pytest
import json
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


pytestmark = pytest.mark.asyncio

async def test_get_device_appliance_uplinks_settings_2(client):
    """Test case for get_device_appliance_uplinks_settings_2

    Return the uplink settings for an MX appliance
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/devices/{serial}/appliance/uplinks/settings'.format(serial='serial_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_device_camera_video_settings_2(client):
    """Test case for get_device_camera_video_settings_2

    Returns video settings for the given camera
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/devices/{serial}/camera/video/settings'.format(serial='serial_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_device_wireless_bluetooth_settings_2(client):
    """Test case for get_device_wireless_bluetooth_settings_2

    Return the bluetooth settings for a wireless device
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/devices/{serial}/wireless/bluetooth/settings'.format(serial='serial_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_device_wireless_radio_settings_2(client):
    """Test case for get_device_wireless_radio_settings_2

    Return the radio settings of a device
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/devices/{serial}/wireless/radio/settings'.format(serial='serial_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_alerts_settings_2(client):
    """Test case for get_network_alerts_settings_2

    Return the alert configuration for this network
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/alerts/settings'.format(network_id='network_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_appliance_firewall_settings_2(client):
    """Test case for get_network_appliance_firewall_settings_2

    Return the firewall settings for this network
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/appliance/firewall/settings'.format(network_id='network_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_appliance_settings_1(client):
    """Test case for get_network_appliance_settings_1

    Return the appliance settings for a network
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/appliance/settings'.format(network_id='network_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_appliance_vlans_settings_2(client):
    """Test case for get_network_appliance_vlans_settings_2

    Returns the enabled status of VLANs for the network
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/appliance/vlans/settings'.format(network_id='network_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_settings_1(client):
    """Test case for get_network_settings_1

    Return the settings for a network
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/settings'.format(network_id='network_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_switch_settings_1(client):
    """Test case for get_network_switch_settings_1

    Returns the switch network settings
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/switch/settings'.format(network_id='network_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_wireless_bluetooth_settings_2(client):
    """Test case for get_network_wireless_bluetooth_settings_2

    Return the Bluetooth settings for a network. <a href=\"https://documentation.meraki.com/MR/Bluetooth/Bluetooth_Low_Energy_(BLE)\">Bluetooth settings</a> must be enabled on the network.
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/wireless/bluetooth/settings'.format(network_id='network_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_wireless_settings_1(client):
    """Test case for get_network_wireless_settings_1

    Return the wireless settings for a network
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/wireless/settings'.format(network_id='network_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_wireless_ssid_splash_settings_3(client):
    """Test case for get_network_wireless_ssid_splash_settings_3

    Display the splash page settings for the given SSID
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/wireless/ssids/{number}/splash/settings'.format(network_id='network_id_example', number='number_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_adaptive_policy_settings_2(client):
    """Test case for get_organization_adaptive_policy_settings_2

    Returns global adaptive policy settings in an organization
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/adaptivePolicy/settings'.format(organization_id='organization_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_device_appliance_uplinks_settings_2(client):
    """Test case for update_device_appliance_uplinks_settings_2

    Update the uplink settings for an MX appliance
    """
    body = openapi_server.UpdateDeviceApplianceUplinksSettingsRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/devices/{serial}/appliance/uplinks/settings'.format(serial='serial_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_device_camera_video_settings_2(client):
    """Test case for update_device_camera_video_settings_2

    Update video settings for the given camera
    """
    body = openapi_server.UpdateDeviceCameraVideoSettingsRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/devices/{serial}/camera/video/settings'.format(serial='serial_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_device_wireless_bluetooth_settings_2(client):
    """Test case for update_device_wireless_bluetooth_settings_2

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
        path='/api/v1/devices/{serial}/wireless/bluetooth/settings'.format(serial='serial_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_device_wireless_radio_settings_2(client):
    """Test case for update_device_wireless_radio_settings_2

    Update the radio settings of a device
    """
    body = openapi_server.UpdateDeviceWirelessRadioSettingsRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/devices/{serial}/wireless/radio/settings'.format(serial='serial_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_network_alerts_settings_2(client):
    """Test case for update_network_alerts_settings_2

    Update the alert configuration for this network
    """
    body = openapi_server.UpdateNetworkAlertsSettingsRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/networks/{network_id}/alerts/settings'.format(network_id='network_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_network_appliance_firewall_settings_2(client):
    """Test case for update_network_appliance_firewall_settings_2

    Update the firewall settings for this network
    """
    body = openapi_server.UpdateNetworkApplianceFirewallSettingsRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/networks/{network_id}/appliance/firewall/settings'.format(network_id='network_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_network_appliance_settings_1(client):
    """Test case for update_network_appliance_settings_1

    Update the appliance settings for a network
    """
    body = openapi_server.UpdateNetworkApplianceSettingsRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/networks/{network_id}/appliance/settings'.format(network_id='network_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_network_appliance_vlans_settings_2(client):
    """Test case for update_network_appliance_vlans_settings_2

    Enable/Disable VLANs for the given network
    """
    body = openapi_server.UpdateNetworkApplianceVlansSettingsRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/networks/{network_id}/appliance/vlans/settings'.format(network_id='network_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_network_settings_1(client):
    """Test case for update_network_settings_1

    Update the settings for a network
    """
    body = openapi_server.UpdateNetworkSettingsRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/networks/{network_id}/settings'.format(network_id='network_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_network_switch_settings_1(client):
    """Test case for update_network_switch_settings_1

    Update switch network settings
    """
    body = openapi_server.UpdateNetworkSwitchSettingsRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/networks/{network_id}/switch/settings'.format(network_id='network_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_network_wireless_bluetooth_settings_2(client):
    """Test case for update_network_wireless_bluetooth_settings_2

    Update the Bluetooth settings for a network
    """
    body = openapi_server.UpdateNetworkWirelessBluetoothSettingsRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/networks/{network_id}/wireless/bluetooth/settings'.format(network_id='network_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_network_wireless_settings_1(client):
    """Test case for update_network_wireless_settings_1

    Update the wireless settings for a network
    """
    body = openapi_server.UpdateNetworkWirelessSettingsRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/networks/{network_id}/wireless/settings'.format(network_id='network_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_network_wireless_ssid_splash_settings_3(client):
    """Test case for update_network_wireless_ssid_splash_settings_3

    Modify the splash page settings for the given SSID
    """
    body = openapi_server.UpdateNetworkWirelessSsidSplashSettingsRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/networks/{network_id}/wireless/ssids/{number}/splash/settings'.format(network_id='network_id_example', number='number_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_organization_adaptive_policy_settings_2(client):
    """Test case for update_organization_adaptive_policy_settings_2

    Update global adaptive policy settings
    """
    body = openapi_server.UpdateOrganizationAdaptivePolicySettingsRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/organizations/{organization_id}/adaptivePolicy/settings'.format(organization_id='organization_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

