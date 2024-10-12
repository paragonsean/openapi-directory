# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_network_sm_bypass_activation_lock_attempt_request import CreateNetworkSmBypassActivationLockAttemptRequest
from openapi_server.models.lock_network_sm_devices_request import LockNetworkSmDevicesRequest
from openapi_server.models.update_network_sm_device_fields_request import UpdateNetworkSmDeviceFieldsRequest
from openapi_server.models.update_network_sm_devices_tags_request import UpdateNetworkSmDevicesTagsRequest
from openapi_server.models.wipe_network_sm_device_request import WipeNetworkSmDeviceRequest


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
        path='/api/v0/networks/{network_id}/sm/bypassActivationLockAttempts'.format(network_id='network_id_example'),
        headers=headers,
        json=body,
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
        path='/api/v0/networks/{network_id}/sm/bypassActivationLockAttempts/{attempt_id}'.format(network_id='network_id_example', attempt_id='attempt_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_sm_cellular_usage_history(client):
    """Test case for get_network_sm_cellular_usage_history

    Return the client's daily cellular data usage history
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v0/networks/{network_id}/sm/{device_id}/cellularUsageHistory'.format(network_id='network_id_example', device_id='device_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_sm_certs(client):
    """Test case for get_network_sm_certs

    List the certs on a device
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v0/networks/{network_id}/sm/{device_id}/certs'.format(network_id='network_id_example', device_id='device_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_sm_connectivity(client):
    """Test case for get_network_sm_connectivity

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
        path='/api/v0/networks/{network_id}/sm/{id}/connectivity'.format(network_id='network_id_example', id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_sm_desktop_logs(client):
    """Test case for get_network_sm_desktop_logs

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
        path='/api/v0/networks/{network_id}/sm/{id}/desktopLogs'.format(network_id='network_id_example', id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_sm_device_command_logs(client):
    """Test case for get_network_sm_device_command_logs

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
        path='/api/v0/networks/{network_id}/sm/{id}/deviceCommandLogs'.format(network_id='network_id_example', id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_sm_device_profiles(client):
    """Test case for get_network_sm_device_profiles

    Get the profiles associated with a device
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v0/networks/{network_id}/sm/{device_id}/deviceProfiles'.format(network_id='network_id_example', device_id='device_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_sm_devices(client):
    """Test case for get_network_sm_devices

    List the devices enrolled in an SM network with various specified fields and filters
    """
    params = [('fields', 'fields_example'),
                    ('wifiMacs', 'wifi_macs_example'),
                    ('serials', 'serials_example'),
                    ('ids', 'ids_example'),
                    ('scope', 'scope_example'),
                    ('batchSize', 56),
                    ('batchToken', 'batch_token_example')]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v0/networks/{network_id}/sm/devices'.format(network_id='network_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_sm_network_adapters(client):
    """Test case for get_network_sm_network_adapters

    List the network adapters of a device
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v0/networks/{network_id}/sm/{device_id}/networkAdapters'.format(network_id='network_id_example', device_id='device_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_sm_performance_history(client):
    """Test case for get_network_sm_performance_history

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
        path='/api/v0/networks/{network_id}/sm/{id}/performanceHistory'.format(network_id='network_id_example', id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_sm_profiles(client):
    """Test case for get_network_sm_profiles

    List all the profiles in the network
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v0/networks/{network_id}/sm/profiles'.format(network_id='network_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_sm_restrictions(client):
    """Test case for get_network_sm_restrictions

    List the restrictions on a device
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v0/networks/{network_id}/sm/{device_id}/restrictions'.format(network_id='network_id_example', device_id='device_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_sm_security_centers(client):
    """Test case for get_network_sm_security_centers

    List the security centers on a device
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v0/networks/{network_id}/sm/{device_id}/securityCenters'.format(network_id='network_id_example', device_id='device_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_sm_softwares(client):
    """Test case for get_network_sm_softwares

    Get a list of softwares associated with a device
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v0/networks/{network_id}/sm/{device_id}/softwares'.format(network_id='network_id_example', device_id='device_id_example'),
        headers=headers,
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
        path='/api/v0/networks/{network_id}/sm/user/{user_id}/deviceProfiles'.format(network_id='network_id_example', user_id='user_id_example'),
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
        path='/api/v0/networks/{network_id}/sm/user/{user_id}/softwares'.format(network_id='network_id_example', user_id='user_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_sm_users(client):
    """Test case for get_network_sm_users

    List the owners in an SM network with various specified fields and filters
    """
    params = [('ids', 'ids_example'),
                    ('usernames', 'usernames_example'),
                    ('emails', 'emails_example'),
                    ('scope', 'scope_example')]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v0/networks/{network_id}/sm/users'.format(network_id='network_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_sm_wlan_lists(client):
    """Test case for get_network_sm_wlan_lists

    List the saved SSID names on a device
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v0/networks/{network_id}/sm/{device_id}/wlanLists'.format(network_id='network_id_example', device_id='device_id_example'),
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
        method='PUT',
        path='/api/v0/networks/{network_id}/sm/devices/lock'.format(network_id='network_id_example'),
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
        path='/api/v0/networks/{network_id}/sm/device/{device_id}/refreshDetails'.format(network_id='network_id_example', device_id='device_id_example'),
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
        path='/api/v0/networks/{network_id}/sm/devices/{device_id}/unenroll'.format(network_id='network_id_example', device_id='device_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_network_sm_device_fields(client):
    """Test case for update_network_sm_device_fields

    Modify the fields of a device
    """
    body = openapi_server.UpdateNetworkSmDeviceFieldsRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v0/networks/{network_id}/sm/device/fields'.format(network_id='network_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_network_sm_devices_tags(client):
    """Test case for update_network_sm_devices_tags

    Add, delete, or update the tags of a set of devices
    """
    body = openapi_server.UpdateNetworkSmDevicesTagsRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v0/networks/{network_id}/sm/devices/tags'.format(network_id='network_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_wipe_network_sm_device(client):
    """Test case for wipe_network_sm_device

    Wipe a device
    """
    body = openapi_server.WipeNetworkSmDeviceRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v0/networks/{network_id}/sm/device/wipe'.format(network_id='network_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

