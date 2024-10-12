# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_network_switch_storm_control200_response import GetNetworkSwitchStormControl200Response
from openapi_server.models.update_network_switch_storm_control_request import UpdateNetworkSwitchStormControlRequest


pytestmark = pytest.mark.asyncio

async def test_get_network_switch_storm_control_1(client):
    """Test case for get_network_switch_storm_control_1

    Return the storm control configuration for a switch network
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/switch/stormControl'.format(network_id='network_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_network_switch_storm_control_1(client):
    """Test case for update_network_switch_storm_control_1

    Update the storm control configuration for a switch network
    """
    body = openapi_server.UpdateNetworkSwitchStormControlRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/networks/{network_id}/switch/stormControl'.format(network_id='network_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

