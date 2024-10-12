# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.update_network_wireless_settings_request import UpdateNetworkWirelessSettingsRequest


pytestmark = pytest.mark.asyncio

async def test_get_network_wireless_settings(client):
    """Test case for get_network_wireless_settings

    Return the wireless settings for a network
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v0/networks/{network_id}/wireless/settings'.format(network_id='network_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_network_wireless_settings(client):
    """Test case for update_network_wireless_settings

    Update the wireless settings for a network
    """
    body = openapi_server.UpdateNetworkWirelessSettingsRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v0/networks/{network_id}/wireless/settings'.format(network_id='network_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

