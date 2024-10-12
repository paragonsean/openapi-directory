# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_network_wireless_failed_connections200_response_inner import GetNetworkWirelessFailedConnections200ResponseInner


pytestmark = pytest.mark.asyncio

async def test_get_network_wireless_failed_connections_1(client):
    """Test case for get_network_wireless_failed_connections_1

    List of all failed client connection events on this network in a given time range
    """
    params = [('t0', 't0_example'),
                    ('t1', 't1_example'),
                    ('timespan', 3.4),
                    ('band', 'band_example'),
                    ('ssid', 56),
                    ('vlan', 56),
                    ('apTag', 'ap_tag_example'),
                    ('serial', 'serial_example'),
                    ('clientId', 'client_id_example')]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/wireless/failedConnections'.format(network_id='network_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

