# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.update_network_appliance_vpn_bgp_request import UpdateNetworkApplianceVpnBgpRequest


pytestmark = pytest.mark.asyncio

async def test_get_network_appliance_vpn_bgp_2(client):
    """Test case for get_network_appliance_vpn_bgp_2

    Return a Hub BGP Configuration
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/appliance/vpn/bgp'.format(network_id='network_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_network_appliance_vpn_bgp_2(client):
    """Test case for update_network_appliance_vpn_bgp_2

    Update a Hub BGP Configuration
    """
    body = openapi_server.UpdateNetworkApplianceVpnBgpRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/networks/{network_id}/appliance/vpn/bgp'.format(network_id='network_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

