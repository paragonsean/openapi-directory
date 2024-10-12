# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_network_wireless_signal_quality_history200_response_inner import GetNetworkWirelessSignalQualityHistory200ResponseInner


pytestmark = pytest.mark.asyncio

async def test_get_network_wireless_signal_quality_history_1(client):
    """Test case for get_network_wireless_signal_quality_history_1

    Return signal quality (SNR/RSSI) over time for a device or network client
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
                    ('ssid', 56)]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/wireless/signalQualityHistory'.format(network_id='network_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

