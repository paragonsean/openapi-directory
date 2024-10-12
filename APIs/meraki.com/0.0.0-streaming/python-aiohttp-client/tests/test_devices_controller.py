# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.claim_network_devices_request import ClaimNetworkDevicesRequest
from openapi_server.models.cycle_device_switch_ports_request import CycleDeviceSwitchPortsRequest
from openapi_server.models.update_network_device_request import UpdateNetworkDeviceRequest


pytestmark = pytest.mark.asyncio

async def test_claim_network_devices(client):
    """Test case for claim_network_devices

    Claim devices into a network. (Note: for recently claimed devices, it may take a few minutes for API requests against that device to succeed)
    """
    body = openapi_server.ClaimNetworkDevicesRequest()
    headers = { 
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v0/networks/{network_id}/devices/claim'.format(network_id='network_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cycle_device_switch_ports(client):
    """Test case for cycle_device_switch_ports

    Cycle a set of switch ports
    """
    body = openapi_server.CycleDeviceSwitchPortsRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v0/devices/{serial}/switch/ports/cycle'.format(serial='serial_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_device(client):
    """Test case for get_network_device

    Return a single device
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v0/networks/{network_id}/devices/{serial}'.format(network_id='network_id_example', serial='serial_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_device_loss_and_latency_history(client):
    """Test case for get_network_device_loss_and_latency_history

    Get the uplink loss percentage and latency in milliseconds for a wired network device.
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
        path='/api/v0/networks/{network_id}/devices/{serial}/lossAndLatencyHistory'.format(network_id='network_id_example', serial='serial_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_device_performance(client):
    """Test case for get_network_device_performance

    Return the performance score for a single MX
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v0/networks/{network_id}/devices/{serial}/performance'.format(network_id='network_id_example', serial='serial_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_device_uplink(client):
    """Test case for get_network_device_uplink

    Return the uplink information for a device.
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v0/networks/{network_id}/devices/{serial}/uplink'.format(network_id='network_id_example', serial='serial_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_devices(client):
    """Test case for get_network_devices

    List the devices in a network
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v0/networks/{network_id}/devices'.format(network_id='network_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_devices(client):
    """Test case for get_organization_devices

    List the devices in an organization
    """
    params = [('perPage', 56),
                    ('startingAfter', 'starting_after_example'),
                    ('endingBefore', 'ending_before_example'),
                    ('configurationUpdatedAfter', 'configuration_updated_after_example')]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v0/organizations/{organization_id}/devices'.format(organization_id='organization_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reboot_network_device(client):
    """Test case for reboot_network_device

    Reboot a device
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v0/networks/{network_id}/devices/{serial}/reboot'.format(network_id='network_id_example', serial='serial_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_network_device(client):
    """Test case for remove_network_device

    Remove a single device
    """
    headers = { 
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v0/networks/{network_id}/devices/{serial}/remove'.format(network_id='network_id_example', serial='serial_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_network_device(client):
    """Test case for update_network_device

    Update the attributes of a device
    """
    body = openapi_server.UpdateNetworkDeviceRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v0/networks/{network_id}/devices/{serial}'.format(network_id='network_id_example', serial='serial_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

