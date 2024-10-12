# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.update_network_cellular_firewall_rules_request import UpdateNetworkCellularFirewallRulesRequest


pytestmark = pytest.mark.asyncio

async def test_get_network_cellular_firewall_rules(client):
    """Test case for get_network_cellular_firewall_rules

    Return the cellular firewall rules for an MX network
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v0/networks/{network_id}/cellularFirewallRules'.format(network_id='network_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_network_cellular_firewall_rules(client):
    """Test case for update_network_cellular_firewall_rules

    Update the cellular firewall rules of an MX network
    """
    body = openapi_server.UpdateNetworkCellularFirewallRulesRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v0/networks/{network_id}/cellularFirewallRules'.format(network_id='network_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

