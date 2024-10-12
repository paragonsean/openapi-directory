# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_device_appliance_uplinks_settings200_response import GetDeviceApplianceUplinksSettings200Response
from openapi_server.models.get_organization_devices_uplinks_addresses_by_device200_response_inner import GetOrganizationDevicesUplinksAddressesByDevice200ResponseInner
from openapi_server.models.get_organization_devices_uplinks_loss_and_latency200_response_inner import GetOrganizationDevicesUplinksLossAndLatency200ResponseInner
from openapi_server.models.get_organization_uplinks_statuses200_response_inner import GetOrganizationUplinksStatuses200ResponseInner
from openapi_server.models.update_device_appliance_uplinks_settings_request import UpdateDeviceApplianceUplinksSettingsRequest


pytestmark = pytest.mark.asyncio

async def test_get_device_appliance_uplinks_settings_1(client):
    """Test case for get_device_appliance_uplinks_settings_1

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

async def test_get_device_loss_and_latency_history_1(client):
    """Test case for get_device_loss_and_latency_history_1

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

async def test_get_network_appliance_uplinks_usage_history_1(client):
    """Test case for get_network_appliance_uplinks_usage_history_1

    Get the sent and received bytes for each uplink of a network.
    """
    params = [('t0', 't0_example'),
                    ('t1', 't1_example'),
                    ('timespan', 3.4),
                    ('resolution', 56)]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/appliance/uplinks/usageHistory'.format(network_id='network_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_appliance_uplink_statuses_1(client):
    """Test case for get_organization_appliance_uplink_statuses_1

    List the uplink status of every Meraki MX and Z series appliances in the organization
    """
    params = [('perPage', 56),
                    ('startingAfter', 'starting_after_example'),
                    ('endingBefore', 'ending_before_example'),
                    ('networkIds', ['network_ids_example']),
                    ('serials', ['serials_example']),
                    ('iccids', ['iccids_example'])]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/appliance/uplink/statuses'.format(organization_id='organization_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_devices_uplinks_addresses_by_device_2(client):
    """Test case for get_organization_devices_uplinks_addresses_by_device_2

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

async def test_get_organization_devices_uplinks_loss_and_latency_2(client):
    """Test case for get_organization_devices_uplinks_loss_and_latency_2

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

async def test_get_organization_uplinks_statuses_1(client):
    """Test case for get_organization_uplinks_statuses_1

    List the uplink status of every Meraki MX, MG and Z series devices in the organization
    """
    params = [('perPage', 56),
                    ('startingAfter', 'starting_after_example'),
                    ('endingBefore', 'ending_before_example'),
                    ('networkIds', ['network_ids_example']),
                    ('serials', ['serials_example']),
                    ('iccids', ['iccids_example'])]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/uplinks/statuses'.format(organization_id='organization_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_device_appliance_uplinks_settings_1(client):
    """Test case for update_device_appliance_uplinks_settings_1

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

