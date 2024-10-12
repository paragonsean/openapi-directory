# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.update_network_appliance_firewall_cellular_firewall_rules_request import UpdateNetworkApplianceFirewallCellularFirewallRulesRequest


pytestmark = pytest.mark.asyncio

async def test_get_network_appliance_firewall_inbound_cellular_firewall_rules_2(client):
    """Test case for get_network_appliance_firewall_inbound_cellular_firewall_rules_2

    Return the inbound cellular firewall rules for an MX network
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/appliance/firewall/inboundCellularFirewallRules'.format(network_id='network_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_network_appliance_firewall_inbound_cellular_firewall_rules_2(client):
    """Test case for update_network_appliance_firewall_inbound_cellular_firewall_rules_2

    Update the inbound cellular firewall rules of an MX network
    """
    body = openapi_server.UpdateNetworkApplianceFirewallCellularFirewallRulesRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/networks/{network_id}/appliance/firewall/inboundCellularFirewallRules'.format(network_id='network_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

