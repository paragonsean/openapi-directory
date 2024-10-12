# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_network_switch_dhcp_server_policy_arp_inspection_warnings_by_device200_response_inner import GetNetworkSwitchDhcpServerPolicyArpInspectionWarningsByDevice200ResponseInner


pytestmark = pytest.mark.asyncio

async def test_get_network_switch_dhcp_server_policy_arp_inspection_warnings_by_device_3(client):
    """Test case for get_network_switch_dhcp_server_policy_arp_inspection_warnings_by_device_3

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

