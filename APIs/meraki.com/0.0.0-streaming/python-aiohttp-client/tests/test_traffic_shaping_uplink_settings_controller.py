# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.update_network_uplink_settings_request import UpdateNetworkUplinkSettingsRequest


pytestmark = pytest.mark.asyncio

async def test_get_network_uplink_settings(client):
    """Test case for get_network_uplink_settings

    Returns the uplink settings for your MX network.
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v0/networks/{network_id}/uplinkSettings'.format(network_id='network_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_network_uplink_settings(client):
    """Test case for update_network_uplink_settings

    Updates the uplink settings for your MX network.
    """
    body = openapi_server.UpdateNetworkUplinkSettingsRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v0/networks/{network_id}/uplinkSettings'.format(network_id='network_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

