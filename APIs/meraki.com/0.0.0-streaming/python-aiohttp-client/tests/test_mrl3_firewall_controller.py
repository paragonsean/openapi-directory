# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.update_network_ssid_l3_firewall_rules_request import UpdateNetworkSsidL3FirewallRulesRequest


pytestmark = pytest.mark.asyncio

async def test_get_network_ssid_l3_firewall_rules(client):
    """Test case for get_network_ssid_l3_firewall_rules

    Return the L3 firewall rules for an SSID on an MR network
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v0/networks/{network_id}/ssids/{number}/l3FirewallRules'.format(network_id='network_id_example', number='number_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_network_ssid_l3_firewall_rules(client):
    """Test case for update_network_ssid_l3_firewall_rules

    Update the L3 firewall rules of an SSID on an MR network
    """
    body = openapi_server.UpdateNetworkSsidL3FirewallRulesRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v0/networks/{network_id}/ssids/{number}/l3FirewallRules'.format(network_id='network_id_example', number='number_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

