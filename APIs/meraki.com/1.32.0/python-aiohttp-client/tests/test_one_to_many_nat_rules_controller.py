# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.update_network_appliance_firewall_one_to_many_nat_rules_request import UpdateNetworkApplianceFirewallOneToManyNatRulesRequest


pytestmark = pytest.mark.asyncio

async def test_get_network_appliance_firewall_one_to_many_nat_rules_2(client):
    """Test case for get_network_appliance_firewall_one_to_many_nat_rules_2

    Return the 1:Many NAT mapping rules for an MX network
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/appliance/firewall/oneToManyNatRules'.format(network_id='network_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_network_appliance_firewall_one_to_many_nat_rules_2(client):
    """Test case for update_network_appliance_firewall_one_to_many_nat_rules_2

    Set the 1:Many NAT mapping rules for an MX network
    """
    body = openapi_server.UpdateNetworkApplianceFirewallOneToManyNatRulesRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/networks/{network_id}/appliance/firewall/oneToManyNatRules'.format(network_id='network_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

