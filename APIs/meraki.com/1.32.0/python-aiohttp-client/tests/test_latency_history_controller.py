# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_network_wireless_latency_history200_response_inner import GetNetworkWirelessLatencyHistory200ResponseInner


pytestmark = pytest.mark.asyncio

async def test_get_network_wireless_client_latency_history_2(client):
    """Test case for get_network_wireless_client_latency_history_2

    Return the latency history for a client
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
        path='/api/v1/networks/{network_id}/wireless/clients/{client_id}/latencyHistory'.format(network_id='network_id_example', client_id='client_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_wireless_latency_history_1(client):
    """Test case for get_network_wireless_latency_history_1

    Return average wireless latency over time for a network, device, or network client
    """
    params = [('t0', 't0_example'),
                    ('t1', 't1_example'),
                    ('timespan', 3.4),
                    ('resolution', 56),
                    ('autoResolution', True),
                    ('clientId', 'client_id_example'),
                    ('deviceSerial', 'device_serial_example'),
                    ('apTag', 'ap_tag_example'),
                    ('band', 'band_example'),
                    ('ssid', 56),
                    ('accessCategory', 'access_category_example')]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/wireless/latencyHistory'.format(network_id='network_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

