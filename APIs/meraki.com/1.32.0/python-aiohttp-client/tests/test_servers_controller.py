# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_network_switch_dhcp_v4_servers_seen200_response_inner import GetNetworkSwitchDhcpV4ServersSeen200ResponseInner


pytestmark = pytest.mark.asyncio

async def test_get_network_switch_dhcp_v4_servers_seen_3(client):
    """Test case for get_network_switch_dhcp_v4_servers_seen_3

    Return the network's DHCPv4 servers seen within the selected timeframe (default 1 day)
    """
    params = [('t0', 't0_example'),
                    ('timespan', 3.4),
                    ('perPage', 56),
                    ('startingAfter', 'starting_after_example'),
                    ('endingBefore', 'ending_before_example')]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/switch/dhcp/v4/servers/seen'.format(network_id='network_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

