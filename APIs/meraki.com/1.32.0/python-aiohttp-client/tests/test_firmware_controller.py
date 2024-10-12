# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_organization_firmware_upgrades200_response_inner import GetOrganizationFirmwareUpgrades200ResponseInner
from openapi_server.models.get_organization_firmware_upgrades_by_device200_response_inner import GetOrganizationFirmwareUpgradesByDevice200ResponseInner


pytestmark = pytest.mark.asyncio

async def test_get_organization_firmware_upgrades_1(client):
    """Test case for get_organization_firmware_upgrades_1

    Get firmware upgrade information for an organization
    """
    params = [('status', ['status_example']),
                    ('productType', ['product_type_example'])]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/firmware/upgrades'.format(organization_id='organization_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_firmware_upgrades_by_device_1(client):
    """Test case for get_organization_firmware_upgrades_by_device_1

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

