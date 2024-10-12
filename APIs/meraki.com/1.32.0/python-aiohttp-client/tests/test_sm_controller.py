# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.checkin_network_sm_devices200_response import CheckinNetworkSmDevices200Response
from openapi_server.models.checkin_network_sm_devices_request import CheckinNetworkSmDevicesRequest
from openapi_server.models.create_network_sm_bypass_activation_lock_attempt_request import CreateNetworkSmBypassActivationLockAttemptRequest
from openapi_server.models.create_network_sm_target_group_request import CreateNetworkSmTargetGroupRequest
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
from openapi_server.models.get_network_sm_profiles200_response_inner import GetNetworkSmProfiles200ResponseInner
from openapi_server.models.get_network_sm_trusted_access_configs200_response_inner import GetNetworkSmTrustedAccessConfigs200ResponseInner
from openapi_server.models.get_network_sm_user_access_devices200_response_inner import GetNetworkSmUserAccessDevices200ResponseInner
from openapi_server.models.get_network_sm_users200_response_inner import GetNetworkSmUsers200ResponseInner
from openapi_server.models.get_organization_sm_apns_cert200_response import GetOrganizationSmApnsCert200Response
from openapi_server.models.get_organization_sm_vpp_accounts200_response_inner import GetOrganizationSmVppAccounts200ResponseInner
from openapi_server.models.lock_network_sm_devices_request import LockNetworkSmDevicesRequest
from openapi_server.models.modify_network_sm_devices_tags200_response_inner import ModifyNetworkSmDevicesTags200ResponseInner
from openapi_server.models.modify_network_sm_devices_tags_request import ModifyNetworkSmDevicesTagsRequest
from openapi_server.models.move_network_sm_devices200_response import MoveNetworkSmDevices200Response
from openapi_server.models.move_network_sm_devices_request import MoveNetworkSmDevicesRequest
from openapi_server.models.update_network_sm_devices_fields200_response_inner import UpdateNetworkSmDevicesFields200ResponseInner
from openapi_server.models.update_network_sm_devices_fields_request import UpdateNetworkSmDevicesFieldsRequest
from openapi_server.models.wipe_network_sm_devices200_response import WipeNetworkSmDevices200Response
from openapi_server.models.wipe_network_sm_devices_request import WipeNetworkSmDevicesRequest


pytestmark = pytest.mark.asyncio

async def test_checkin_network_sm_devices(client):
    """Test case for checkin_network_sm_devices

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

async def test_create_network_sm_bypass_activation_lock_attempt(client):
    """Test case for create_network_sm_bypass_activation_lock_attempt

    Bypass activation lock attempt
    """
    body = openapi_server.CreateNetworkSmBypassActivationLockAttemptRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/networks/{network_id}/sm/bypassActivationLockAttempts'.format(network_id='network_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_network_sm_target_group(client):
    """Test case for create_network_sm_target_group

    Add a target group
    """
    body = openapi_server.CreateNetworkSmTargetGroupRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/networks/{network_id}/sm/targetGroups'.format(network_id='network_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_network_sm_target_group(client):
    """Test case for delete_network_sm_target_group

    Delete a target group from a network
    """
    headers = { 
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/networks/{network_id}/sm/targetGroups/{target_group_id}'.format(network_id='network_id_example', target_group_id='target_group_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_network_sm_user_access_device(client):
    """Test case for delete_network_sm_user_access_device

    Delete a User Access Device
    """
    headers = { 
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/networks/{network_id}/sm/userAccessDevices/{user_access_device_id}'.format(network_id='network_id_example', user_access_device_id='user_access_device_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_sm_bypass_activation_lock_attempt(client):
    """Test case for get_network_sm_bypass_activation_lock_attempt

    Bypass activation lock attempt status
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/sm/bypassActivationLockAttempts/{attempt_id}'.format(network_id='network_id_example', attempt_id='attempt_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_sm_device_cellular_usage_history(client):
    """Test case for get_network_sm_device_cellular_usage_history

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

async def test_get_network_sm_device_certs(client):
    """Test case for get_network_sm_device_certs

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

async def test_get_network_sm_device_connectivity(client):
    """Test case for get_network_sm_device_connectivity

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

async def test_get_network_sm_device_desktop_logs(client):
    """Test case for get_network_sm_device_desktop_logs

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

async def test_get_network_sm_device_device_command_logs(client):
    """Test case for get_network_sm_device_device_command_logs

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

async def test_get_network_sm_device_device_profiles(client):
    """Test case for get_network_sm_device_device_profiles

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

async def test_get_network_sm_device_network_adapters(client):
    """Test case for get_network_sm_device_network_adapters

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

async def test_get_network_sm_device_performance_history(client):
    """Test case for get_network_sm_device_performance_history

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

async def test_get_network_sm_device_restrictions(client):
    """Test case for get_network_sm_device_restrictions

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

async def test_get_network_sm_device_security_centers(client):
    """Test case for get_network_sm_device_security_centers

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

async def test_get_network_sm_device_softwares(client):
    """Test case for get_network_sm_device_softwares

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

async def test_get_network_sm_device_wlan_lists(client):
    """Test case for get_network_sm_device_wlan_lists

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

async def test_get_network_sm_devices(client):
    """Test case for get_network_sm_devices

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

async def test_get_network_sm_profiles(client):
    """Test case for get_network_sm_profiles

    List all profiles in a network
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/sm/profiles'.format(network_id='network_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_sm_target_group(client):
    """Test case for get_network_sm_target_group

    Return a target group
    """
    params = [('withDetails', True)]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/sm/targetGroups/{target_group_id}'.format(network_id='network_id_example', target_group_id='target_group_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_sm_target_groups(client):
    """Test case for get_network_sm_target_groups

    List the target groups in this network
    """
    params = [('withDetails', True)]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/sm/targetGroups'.format(network_id='network_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_sm_trusted_access_configs(client):
    """Test case for get_network_sm_trusted_access_configs

    List Trusted Access Configs
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
        path='/api/v1/networks/{network_id}/sm/trustedAccessConfigs'.format(network_id='network_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_sm_user_access_devices(client):
    """Test case for get_network_sm_user_access_devices

    List User Access Devices and its Trusted Access Connections
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
        path='/api/v1/networks/{network_id}/sm/userAccessDevices'.format(network_id='network_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_sm_user_device_profiles(client):
    """Test case for get_network_sm_user_device_profiles

    Get the profiles associated with a user
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/sm/users/{user_id}/deviceProfiles'.format(network_id='network_id_example', user_id='user_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_sm_user_softwares(client):
    """Test case for get_network_sm_user_softwares

    Get a list of softwares associated with a user
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/sm/users/{user_id}/softwares'.format(network_id='network_id_example', user_id='user_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_sm_users(client):
    """Test case for get_network_sm_users

    List the owners in an SM network with various specified fields and filters
    """
    params = [('ids', ['ids_example']),
                    ('usernames', ['usernames_example']),
                    ('emails', ['emails_example']),
                    ('scope', ['scope_example'])]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/sm/users'.format(network_id='network_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_sm_apns_cert(client):
    """Test case for get_organization_sm_apns_cert

    Get the organization's APNS certificate
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/sm/apnsCert'.format(organization_id='organization_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_sm_vpp_account(client):
    """Test case for get_organization_sm_vpp_account

    Get a hash containing the unparsed token of the VPP account with the given ID
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/sm/vppAccounts/{vpp_account_id}'.format(organization_id='organization_id_example', vpp_account_id='vpp_account_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_sm_vpp_accounts(client):
    """Test case for get_organization_sm_vpp_accounts

    List the VPP accounts in the organization
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/sm/vppAccounts'.format(organization_id='organization_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_lock_network_sm_devices(client):
    """Test case for lock_network_sm_devices

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

async def test_modify_network_sm_devices_tags(client):
    """Test case for modify_network_sm_devices_tags

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

async def test_move_network_sm_devices(client):
    """Test case for move_network_sm_devices

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

async def test_refresh_network_sm_device_details(client):
    """Test case for refresh_network_sm_device_details

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

async def test_unenroll_network_sm_device(client):
    """Test case for unenroll_network_sm_device

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

async def test_update_network_sm_devices_fields(client):
    """Test case for update_network_sm_devices_fields

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

async def test_update_network_sm_target_group(client):
    """Test case for update_network_sm_target_group

    Update a target group
    """
    body = openapi_server.CreateNetworkSmTargetGroupRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/networks/{network_id}/sm/targetGroups/{target_group_id}'.format(network_id='network_id_example', target_group_id='target_group_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_wipe_network_sm_devices(client):
    """Test case for wipe_network_sm_devices

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

