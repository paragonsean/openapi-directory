# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_network_switch_dhcp_server_policy_arp_inspection_warnings_by_device200_response_inner import GetNetworkSwitchDhcpServerPolicyArpInspectionWarningsByDevice200ResponseInner
from openapi_server.models.get_organization_devices_power_modules_statuses_by_device200_response_inner import GetOrganizationDevicesPowerModulesStatusesByDevice200ResponseInner
from openapi_server.models.get_organization_devices_uplinks_addresses_by_device200_response_inner import GetOrganizationDevicesUplinksAddressesByDevice200ResponseInner
from openapi_server.models.get_organization_firmware_upgrades_by_device200_response_inner import GetOrganizationFirmwareUpgradesByDevice200ResponseInner


pytestmark = pytest.mark.asyncio

async def test_get_network_switch_dhcp_server_policy_arp_inspection_warnings_by_device_4(client):
    """Test case for get_network_switch_dhcp_server_policy_arp_inspection_warnings_by_device_4

    Return the devices that have a Dynamic ARP Inspection warning and their warnings
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
        path='/api/v1/networks/{network_id}/switch/dhcpServerPolicy/arpInspection/warnings/byDevice'.format(network_id='network_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_devices_power_modules_statuses_by_device_4(client):
    """Test case for get_organization_devices_power_modules_statuses_by_device_4

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

async def test_get_organization_devices_uplinks_addresses_by_device_4(client):
    """Test case for get_organization_devices_uplinks_addresses_by_device_4

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

async def test_get_organization_firmware_upgrades_by_device_3(client):
    """Test case for get_organization_firmware_upgrades_by_device_3

    Get firmware upgrade status for the filtered devices
    """
    params = [('perPage', 56),
                    ('startingAfter', 'starting_after_example'),
                    ('endingBefore', 'ending_before_example'),
                    ('networkIds', ['network_ids_example']),
                    ('serials', ['serials_example']),
                    ('macs', ['macs_example']),
                    ('firmwareUpgradeIds', ['firmware_upgrade_ids_example']),
                    ('firmwareUpgradeBatchIds', ['firmware_upgrade_batch_ids_example'])]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/firmware/upgrades/byDevice'.format(organization_id='organization_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

