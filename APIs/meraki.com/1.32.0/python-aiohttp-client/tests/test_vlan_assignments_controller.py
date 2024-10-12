# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_get_device_appliance_prefixes_delegated_vlan_assignments_3(client):
    """Test case for get_device_appliance_prefixes_delegated_vlan_assignments_3

    Return prefixes assigned to all IPv6 enabled VLANs on an appliance.
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/devices/{serial}/appliance/prefixes/delegated/vlanAssignments'.format(serial='serial_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

