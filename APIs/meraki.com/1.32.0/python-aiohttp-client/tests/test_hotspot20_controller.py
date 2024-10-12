# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.update_network_wireless_ssid_hotspot20_request import UpdateNetworkWirelessSsidHotspot20Request


pytestmark = pytest.mark.asyncio

async def test_get_network_wireless_ssid_hotspot20_2(client):
    """Test case for get_network_wireless_ssid_hotspot20_2

    Return the Hotspot 2.0 settings for an SSID
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/wireless/ssids/{number}/hotspot20'.format(network_id='network_id_example', number='number_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_network_wireless_ssid_hotspot20_2(client):
    """Test case for update_network_wireless_ssid_hotspot20_2

    Update the Hotspot 2.0 settings of an SSID
    """
    body = openapi_server.UpdateNetworkWirelessSsidHotspot20Request()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/networks/{network_id}/wireless/ssids/{number}/hotspot20'.format(network_id='network_id_example', number='number_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

