# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.update_network_alert_settings_request import UpdateNetworkAlertSettingsRequest


pytestmark = pytest.mark.asyncio

async def test_get_network_alert_settings(client):
    """Test case for get_network_alert_settings

    Return the alert configuration for this network
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v0/networks/{network_id}/alertSettings'.format(network_id='network_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_network_alert_settings(client):
    """Test case for update_network_alert_settings

    Update the alert configuration for this network
    """
    body = openapi_server.UpdateNetworkAlertSettingsRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v0/networks/{network_id}/alertSettings'.format(network_id='network_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

