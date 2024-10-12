# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.blink_device_leds_request import BlinkDeviceLedsRequest
from openapi_server.models.checkin_network_sm_devices200_response import CheckinNetworkSmDevices200Response
from openapi_server.models.checkin_network_sm_devices_request import CheckinNetworkSmDevicesRequest
from openapi_server.models.claim_network_devices_request import ClaimNetworkDevicesRequest
from openapi_server.models.clone_organization_switch_devices_request import CloneOrganizationSwitchDevicesRequest
from openapi_server.models.create_device_live_tools_ping201_response import CreateDeviceLiveToolsPing201Response
from openapi_server.models.create_device_live_tools_ping_device_request import CreateDeviceLiveToolsPingDeviceRequest
from openapi_server.models.create_device_live_tools_ping_request import CreateDeviceLiveToolsPingRequest
from openapi_server.models.get_device_live_tools_ping200_response import GetDeviceLiveToolsPing200Response
from openapi_server.models.get_device_wireless_connection_stats200_response import GetDeviceWirelessConnectionStats200Response
from openapi_server.models.get_network_sm_device_cellular_usage_history200_response_inner import GetNetworkSmDeviceCellularUsageHistory200ResponseInner
from openapi_server.models.get_network_sm_device_certs200_response_inner import GetNetworkSmDeviceCerts200ResponseInner
from openapi_server.models.get_network_sm_device_connectivity200_response_inner import GetNetworkSmDeviceConnectivity200ResponseInner
from openapi_server.models.get_network_sm_device_desktop_logs200_response_inner import GetNetworkSmDeviceDesktopLogs200ResponseInner
from openapi_server.models.get_network_sm_device_device_command_logs200_response_inner import GetNetworkSmDeviceDeviceCommandLogs200ResponseInner
from openapi_server.models.get_network_sm_device_device_profiles200_response_inner import GetNetworkSmDeviceDeviceProfiles200ResponseInner
from openapi_server.models.get_network_sm_device_network_adapters200_response_inner import GetNetworkSmDeviceNetworkAdapters200ResponseInner
from openapi_server.models.get_network_sm_device_performance_history200_response_inner import GetNetworkSmDevicePerformanceHistory200ResponseInner
from openapi_server.models.get_network_sm_device_security_centers200_response_inner import GetNetworkSmDeviceSecurityCenters200ResponseInner
from openapi_server.models.get_network_sm_device_softwares200_response_inner import GetNetworkSmDeviceSoftwares200ResponseInner
from openapi_server.models.get_network_sm_device_wlan_lists200_response_inner import GetNetworkSmDeviceWlanLists200ResponseInner
from openapi_server.models.get_network_sm_devices200_response_inner import GetNetworkSmDevices200ResponseInner
from openapi_server.models.get_organization_devices200_response_inner import GetOrganizationDevices200ResponseInner
from openapi_server.models.get_organization_devices_availabilities200_response_inner import GetOrganizationDevicesAvailabilities200ResponseInner
from openapi_server.models.get_organization_devices_power_modules_statuses_by_device200_response_inner import GetOrganizationDevicesPowerModulesStatusesByDevice200ResponseInner
from openapi_server.models.get_organization_devices_statuses200_response import GetOrganizationDevicesStatuses200Response
from openapi_server.models.get_organization_devices_statuses_overview200_response import GetOrganizationDevicesStatusesOverview200Response
from openapi_server.models.get_organization_devices_uplinks_addresses_by_device200_response_inner import GetOrganizationDevicesUplinksAddressesByDevice200ResponseInner
from openapi_server.models.get_organization_devices_uplinks_loss_and_latency200_response_inner import GetOrganizationDevicesUplinksLossAndLatency200ResponseInner
from openapi_server.models.get_organization_inventory_devices200_response_inner import GetOrganizationInventoryDevices200ResponseInner
from openapi_server.models.get_organization_summary_top_devices_by_usage200_response_inner import GetOrganizationSummaryTopDevicesByUsage200ResponseInner
from openapi_server.models.get_organization_summary_top_devices_models_by_usage200_response_inner import GetOrganizationSummaryTopDevicesModelsByUsage200ResponseInner
from openapi_server.models.get_organization_wireless_devices_ethernet_statuses200_response_inner import GetOrganizationWirelessDevicesEthernetStatuses200ResponseInner
from openapi_server.models.lock_network_sm_devices_request import LockNetworkSmDevicesRequest
from openapi_server.models.modify_network_sm_devices_tags200_response_inner import ModifyNetworkSmDevicesTags200ResponseInner
from openapi_server.models.modify_network_sm_devices_tags_request import ModifyNetworkSmDevicesTagsRequest
from openapi_server.models.move_network_sm_devices200_response import MoveNetworkSmDevices200Response
from openapi_server.models.move_network_sm_devices_request import MoveNetworkSmDevicesRequest
from openapi_server.models.remove_network_devices_request import RemoveNetworkDevicesRequest
from openapi_server.models.update_device_cellular_sims_request import UpdateDeviceCellularSimsRequest
from openapi_server.models.update_device_management_interface_request import UpdateDeviceManagementInterfaceRequest
from openapi_server.models.update_device_request import UpdateDeviceRequest
from openapi_server.models.update_network_sm_devices_fields200_response_inner import UpdateNetworkSmDevicesFields200ResponseInner
from openapi_server.models.update_network_sm_devices_fields_request import UpdateNetworkSmDevicesFieldsRequest
from openapi_server.models.vmx_network_devices_claim_request import VmxNetworkDevicesClaimRequest
from openapi_server.models.wipe_network_sm_devices200_response import WipeNetworkSmDevices200Response
from openapi_server.models.wipe_network_sm_devices_request import WipeNetworkSmDevicesRequest


pytestmark = pytest.mark.asyncio

async def test_blink_device_leds(client):
    """Test case for blink_device_leds

    Blink the LEDs on a device
    """
    body = openapi_server.BlinkDeviceLedsRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/devices/{serial}/blinkLeds'.format(serial='serial_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_checkin_network_sm_devices_1(client):
    """Test case for checkin_network_sm_devices_1

    Force check-in a set of devices
    """
    body = openapi_server.CheckinNetworkSmDevicesRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/networks/{network_id}/sm/devices/checkin'.format(network_id='network_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_claim_network_devices_1(client):
    """Test case for claim_network_devices_1

    Claim devices into a network. (Note: for recently claimed devices, it may take a few minutes for API requsts against that device to succeed)
    """
    body = openapi_server.ClaimNetworkDevicesRequest()
    headers = { 
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/networks/{network_id}/devices/claim'.format(network_id='network_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_clone_organization_switch_devices_1(client):
    """Test case for clone_organization_switch_devices_1

    Clone port-level and some switch-level configuration settings from a source switch to one or more target switches
    """
    body = openapi_server.CloneOrganizationSwitchDevicesRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/organizations/{organization_id}/switch/devices/clone'.format(organization_id='organization_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_device_live_tools_ping(client):
    """Test case for create_device_live_tools_ping

    Enqueue a job to ping a target host from the device
    """
    body = openapi_server.CreateDeviceLiveToolsPingRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/devices/{serial}/liveTools/ping'.format(serial='serial_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_device_live_tools_ping_device(client):
    """Test case for create_device_live_tools_ping_device

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

async def test_get_device(client):
    """Test case for get_device

    Return a single device
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/devices/{serial}'.format(serial='serial_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_device_cellular_sims(client):
    """Test case for get_device_cellular_sims

    Return the SIM and APN configurations for a cellular device.
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/devices/{serial}/cellular/sims'.format(serial='serial_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_device_clients(client):
    """Test case for get_device_clients

    List the clients of a device, up to a maximum of a month ago
    """
    params = [('t0', 't0_example'),
                    ('timespan', 3.4)]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/devices/{serial}/clients'.format(serial='serial_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_device_live_tools_ping(client):
    """Test case for get_device_live_tools_ping

    Return a ping job
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/devices/{serial}/liveTools/ping/{id}'.format(serial='serial_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_device_live_tools_ping_device(client):
    """Test case for get_device_live_tools_ping_device

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


pytestmark = pytest.mark.asyncio

async def test_get_device_lldp_cdp(client):
    """Test case for get_device_lldp_cdp

    List LLDP and CDP information for a device
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/devices/{serial}/lldpCdp'.format(serial='serial_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_device_loss_and_latency_history(client):
    """Test case for get_device_loss_and_latency_history

    Get the uplink loss percentage and latency in milliseconds, and goodput in kilobits per second for a wired network device.
    """
    params = [('t0', 't0_example'),
                    ('t1', 't1_example'),
                    ('timespan', 3.4),
                    ('resolution', 56),
                    ('uplink', 'uplink_example'),
                    ('ip', 'ip_example')]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/devices/{serial}/lossAndLatencyHistory'.format(serial='serial_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_device_management_interface(client):
    """Test case for get_device_management_interface

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

async def test_get_network_devices_1(client):
    """Test case for get_network_devices_1

    List the devices in a network
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/devices'.format(network_id='network_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_sm_device_cellular_usage_history_1(client):
    """Test case for get_network_sm_device_cellular_usage_history_1

    Return the client's daily cellular data usage history
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/sm/devices/{device_id}/cellularUsageHistory'.format(network_id='network_id_example', device_id='device_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_sm_device_certs_1(client):
    """Test case for get_network_sm_device_certs_1

    List the certs on a device
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/sm/devices/{device_id}/certs'.format(network_id='network_id_example', device_id='device_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_sm_device_connectivity_1(client):
    """Test case for get_network_sm_device_connectivity_1

    Returns historical connectivity data (whether a device is regularly checking in to Dashboard).
    """
    params = [('perPage', 56),
                    ('startingAfter', 'starting_after_example'),
                    ('endingBefore', 'ending_before_example')]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/sm/devices/{device_id}/connectivity'.format(network_id='network_id_example', device_id='device_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_sm_device_desktop_logs_1(client):
    """Test case for get_network_sm_device_desktop_logs_1

    Return historical records of various Systems Manager network connection details for desktop devices.
    """
    params = [('perPage', 56),
                    ('startingAfter', 'starting_after_example'),
                    ('endingBefore', 'ending_before_example')]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/sm/devices/{device_id}/desktopLogs'.format(network_id='network_id_example', device_id='device_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_sm_device_device_command_logs_1(client):
    """Test case for get_network_sm_device_device_command_logs_1

    Return historical records of commands sent to Systems Manager devices
    """
    params = [('perPage', 56),
                    ('startingAfter', 'starting_after_example'),
                    ('endingBefore', 'ending_before_example')]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/sm/devices/{device_id}/deviceCommandLogs'.format(network_id='network_id_example', device_id='device_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_sm_device_device_profiles_1(client):
    """Test case for get_network_sm_device_device_profiles_1

    Get the installed profiles associated with a device
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/sm/devices/{device_id}/deviceProfiles'.format(network_id='network_id_example', device_id='device_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_sm_device_network_adapters_1(client):
    """Test case for get_network_sm_device_network_adapters_1

    List the network adapters of a device
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/sm/devices/{device_id}/networkAdapters'.format(network_id='network_id_example', device_id='device_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_sm_device_performance_history_1(client):
    """Test case for get_network_sm_device_performance_history_1

    Return historical records of various Systems Manager client metrics for desktop devices.
    """
    params = [('perPage', 56),
                    ('startingAfter', 'starting_after_example'),
                    ('endingBefore', 'ending_before_example')]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/sm/devices/{device_id}/performanceHistory'.format(network_id='network_id_example', device_id='device_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_sm_device_restrictions_1(client):
    """Test case for get_network_sm_device_restrictions_1

    List the restrictions on a device
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/sm/devices/{device_id}/restrictions'.format(network_id='network_id_example', device_id='device_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_sm_device_security_centers_1(client):
    """Test case for get_network_sm_device_security_centers_1

    List the security centers on a device
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/sm/devices/{device_id}/securityCenters'.format(network_id='network_id_example', device_id='device_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_sm_device_softwares_1(client):
    """Test case for get_network_sm_device_softwares_1

    Get a list of softwares associated with a device
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/sm/devices/{device_id}/softwares'.format(network_id='network_id_example', device_id='device_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_sm_device_wlan_lists_1(client):
    """Test case for get_network_sm_device_wlan_lists_1

    List the saved SSID names on a device
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/sm/devices/{device_id}/wlanLists'.format(network_id='network_id_example', device_id='device_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_sm_devices_1(client):
    """Test case for get_network_sm_devices_1

    List the devices enrolled in an SM network with various specified fields and filters
    """
    params = [('fields', ['fields_example']),
                    ('wifiMacs', ['wifi_macs_example']),
                    ('serials', ['serials_example']),
                    ('ids', ['ids_example']),
                    ('scope', ['scope_example']),
                    ('perPage', 56),
                    ('startingAfter', 'starting_after_example'),
                    ('endingBefore', 'ending_before_example')]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/sm/devices'.format(network_id='network_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_wireless_devices_connection_stats_1(client):
    """Test case for get_network_wireless_devices_connection_stats_1

    Aggregated connectivity info for this network, grouped by node
    """
    params = [('t0', 't0_example'),
                    ('t1', 't1_example'),
                    ('timespan', 3.4),
                    ('band', 'band_example'),
                    ('ssid', 56),
                    ('vlan', 56),
                    ('apTag', 'ap_tag_example')]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/wireless/devices/connectionStats'.format(network_id='network_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_wireless_devices_latency_stats_1(client):
    """Test case for get_network_wireless_devices_latency_stats_1

    Aggregated latency info for this network, grouped by node
    """
    params = [('t0', 't0_example'),
                    ('t1', 't1_example'),
                    ('timespan', 3.4),
                    ('band', 'band_example'),
                    ('ssid', 56),
                    ('vlan', 56),
                    ('apTag', 'ap_tag_example'),
                    ('fields', 'fields_example')]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/wireless/devices/latencyStats'.format(network_id='network_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_devices_1(client):
    """Test case for get_organization_devices_1

    List the devices in an organization
    """
    params = [('perPage', 56),
                    ('startingAfter', 'starting_after_example'),
                    ('endingBefore', 'ending_before_example'),
                    ('configurationUpdatedAfter', 'configuration_updated_after_example'),
                    ('networkIds', ['network_ids_example']),
                    ('productTypes', ['product_types_example']),
                    ('tags', ['tags_example']),
                    ('tagsFilterType', 'tags_filter_type_example'),
                    ('name', 'name_example'),
                    ('mac', 'mac_example'),
                    ('serial', 'serial_example'),
                    ('model', 'model_example'),
                    ('macs', ['macs_example']),
                    ('serials', ['serials_example']),
                    ('sensorMetrics', ['sensor_metrics_example']),
                    ('sensorAlertProfileIds', ['sensor_alert_profile_ids_example']),
                    ('models', ['models_example'])]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/devices'.format(organization_id='organization_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_devices_availabilities_1(client):
    """Test case for get_organization_devices_availabilities_1

    List the availability information for devices in an organization
    """
    params = [('perPage', 56),
                    ('startingAfter', 'starting_after_example'),
                    ('endingBefore', 'ending_before_example'),
                    ('networkIds', ['network_ids_example']),
                    ('productTypes', ['product_types_example']),
                    ('serials', ['serials_example']),
                    ('tags', ['tags_example']),
                    ('tagsFilterType', 'tags_filter_type_example')]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/devices/availabilities'.format(organization_id='organization_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_devices_power_modules_statuses_by_device_1(client):
    """Test case for get_organization_devices_power_modules_statuses_by_device_1

    List the power status information for devices in an organization
    """
    params = [('perPage', 56),
                    ('startingAfter', 'starting_after_example'),
                    ('endingBefore', 'ending_before_example'),
                    ('networkIds', ['network_ids_example']),
                    ('productTypes', ['product_types_example']),
                    ('serials', ['serials_example']),
                    ('tags', ['tags_example']),
                    ('tagsFilterType', 'tags_filter_type_example')]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/devices/powerModules/statuses/byDevice'.format(organization_id='organization_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_devices_statuses_1(client):
    """Test case for get_organization_devices_statuses_1

    List the status of every Meraki device in the organization
    """
    params = [('perPage', 56),
                    ('startingAfter', 'starting_after_example'),
                    ('endingBefore', 'ending_before_example'),
                    ('networkIds', ['network_ids_example']),
                    ('serials', ['serials_example']),
                    ('statuses', ['statuses_example']),
                    ('productTypes', ['product_types_example']),
                    ('models', ['models_example']),
                    ('tags', ['tags_example']),
                    ('tagsFilterType', 'tags_filter_type_example')]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/devices/statuses'.format(organization_id='organization_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_devices_statuses_overview_1(client):
    """Test case for get_organization_devices_statuses_overview_1

    Return an overview of current device statuses
    """
    params = [('productTypes', ['product_types_example']),
                    ('networkIds', ['network_ids_example'])]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/devices/statuses/overview'.format(organization_id='organization_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_devices_uplinks_addresses_by_device_1(client):
    """Test case for get_organization_devices_uplinks_addresses_by_device_1

    List the current uplink addresses for devices in an organization.
    """
    params = [('perPage', 56),
                    ('startingAfter', 'starting_after_example'),
                    ('endingBefore', 'ending_before_example'),
                    ('networkIds', ['network_ids_example']),
                    ('productTypes', ['product_types_example']),
                    ('serials', ['serials_example']),
                    ('tags', ['tags_example']),
                    ('tagsFilterType', 'tags_filter_type_example')]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/devices/uplinks/addresses/byDevice'.format(organization_id='organization_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_devices_uplinks_loss_and_latency_1(client):
    """Test case for get_organization_devices_uplinks_loss_and_latency_1

    Return the uplink loss and latency for every MX in the organization from at latest 2 minutes ago
    """
    params = [('t0', 't0_example'),
                    ('t1', 't1_example'),
                    ('timespan', 3.4),
                    ('uplink', 'uplink_example'),
                    ('ip', 'ip_example')]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/devices/uplinksLossAndLatency'.format(organization_id='organization_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_inventory_device_2(client):
    """Test case for get_organization_inventory_device_2

    Return a single device from the inventory of an organization
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/inventory/devices/{serial}'.format(organization_id='organization_id_example', serial='serial_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_inventory_devices_2(client):
    """Test case for get_organization_inventory_devices_2

    Return the device inventory for an organization
    """
    params = [('perPage', 56),
                    ('startingAfter', 'starting_after_example'),
                    ('endingBefore', 'ending_before_example'),
                    ('usedState', 'used_state_example'),
                    ('search', 'search_example'),
                    ('macs', ['macs_example']),
                    ('networkIds', ['network_ids_example']),
                    ('serials', ['serials_example']),
                    ('models', ['models_example']),
                    ('orderNumbers', ['order_numbers_example']),
                    ('tags', ['tags_example']),
                    ('tagsFilterType', 'tags_filter_type_example'),
                    ('productTypes', ['product_types_example'])]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/inventory/devices'.format(organization_id='organization_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_summary_top_devices_by_usage_3(client):
    """Test case for get_organization_summary_top_devices_by_usage_3

    Return metrics for organization's top 10 devices sorted by data usage over given time range
    """
    params = [('t0', 't0_example'),
                    ('t1', 't1_example'),
                    ('timespan', 3.4)]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/summary/top/devices/byUsage'.format(organization_id='organization_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_summary_top_devices_models_by_usage_3(client):
    """Test case for get_organization_summary_top_devices_models_by_usage_3

    Return metrics for organization's top 10 device models sorted by data usage over given time range
    """
    params = [('t0', 't0_example'),
                    ('t1', 't1_example'),
                    ('timespan', 3.4)]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/summary/top/devices/models/byUsage'.format(organization_id='organization_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_wireless_devices_ethernet_statuses_1(client):
    """Test case for get_organization_wireless_devices_ethernet_statuses_1

    Endpoint to see power status for wireless devices
    """
    params = [('perPage', 56),
                    ('startingAfter', 'starting_after_example'),
                    ('endingBefore', 'ending_before_example'),
                    ('networkIds', ['network_ids_example'])]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/wireless/devices/ethernet/statuses'.format(organization_id='organization_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_lock_network_sm_devices_1(client):
    """Test case for lock_network_sm_devices_1

    Lock a set of devices
    """
    body = openapi_server.LockNetworkSmDevicesRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/networks/{network_id}/sm/devices/lock'.format(network_id='network_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_modify_network_sm_devices_tags_1(client):
    """Test case for modify_network_sm_devices_tags_1

    Add, delete, or update the tags of a set of devices
    """
    body = openapi_server.ModifyNetworkSmDevicesTagsRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/networks/{network_id}/sm/devices/modifyTags'.format(network_id='network_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_move_network_sm_devices_1(client):
    """Test case for move_network_sm_devices_1

    Move a set of devices to a new network
    """
    body = openapi_server.MoveNetworkSmDevicesRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/networks/{network_id}/sm/devices/move'.format(network_id='network_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reboot_device(client):
    """Test case for reboot_device

    Reboot a device
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/devices/{serial}/reboot'.format(serial='serial_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_refresh_network_sm_device_details_1(client):
    """Test case for refresh_network_sm_device_details_1

    Refresh the details of a device
    """
    headers = { 
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/networks/{network_id}/sm/devices/{device_id}/refreshDetails'.format(network_id='network_id_example', device_id='device_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_network_devices_1(client):
    """Test case for remove_network_devices_1

    Remove a single device
    """
    body = openapi_server.RemoveNetworkDevicesRequest()
    headers = { 
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/networks/{network_id}/devices/remove'.format(network_id='network_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_unenroll_network_sm_device_1(client):
    """Test case for unenroll_network_sm_device_1

    Unenroll a device
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/networks/{network_id}/sm/devices/{device_id}/unenroll'.format(network_id='network_id_example', device_id='device_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_device(client):
    """Test case for update_device

    Update the attributes of a device
    """
    body = openapi_server.UpdateDeviceRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/devices/{serial}'.format(serial='serial_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_device_cellular_sims(client):
    """Test case for update_device_cellular_sims

    Updates the SIM and APN configurations for a cellular device.
    """
    body = openapi_server.UpdateDeviceCellularSimsRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/devices/{serial}/cellular/sims'.format(serial='serial_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_device_management_interface(client):
    """Test case for update_device_management_interface

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


pytestmark = pytest.mark.asyncio

async def test_update_network_sm_devices_fields_1(client):
    """Test case for update_network_sm_devices_fields_1

    Modify the fields of a device
    """
    body = openapi_server.UpdateNetworkSmDevicesFieldsRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/networks/{network_id}/sm/devices/fields'.format(network_id='network_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_vmx_network_devices_claim_1(client):
    """Test case for vmx_network_devices_claim_1

    Claim a vMX into a network
    """
    body = openapi_server.VmxNetworkDevicesClaimRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/networks/{network_id}/devices/claim/vmx'.format(network_id='network_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_wipe_network_sm_devices_1(client):
    """Test case for wipe_network_sm_devices_1

    Wipe a device
    """
    body = openapi_server.WipeNetworkSmDevicesRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/networks/{network_id}/sm/devices/wipe'.format(network_id='network_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

