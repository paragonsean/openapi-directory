# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_network_wireless_channel_utilization_history200_response_inner import GetNetworkWirelessChannelUtilizationHistory200ResponseInner


pytestmark = pytest.mark.asyncio

async def test_get_network_wireless_channel_utilization_history_1(client):
    """Test case for get_network_wireless_channel_utilization_history_1

    Return AP channel utilization over time for a device or network client
    """
    params = [('t0', 't0_example'),
                    ('t1', 't1_example'),
                    ('timespan', 3.4),
                    ('resolution', 56),
                    ('autoResolution', True),
                    ('clientId', 'client_id_example'),
                    ('deviceSerial', 'device_serial_example'),
                    ('apTag', 'ap_tag_example'),
                    ('band', 'band_example')]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/wireless/channelUtilizationHistory'.format(network_id='network_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

