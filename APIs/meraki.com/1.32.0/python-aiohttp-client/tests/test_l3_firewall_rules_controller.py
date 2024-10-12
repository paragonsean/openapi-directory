# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.update_network_appliance_firewall_inbound_firewall_rules_request import UpdateNetworkApplianceFirewallInboundFirewallRulesRequest
from openapi_server.models.update_network_wireless_ssid_firewall_l3_firewall_rules_request import UpdateNetworkWirelessSsidFirewallL3FirewallRulesRequest


pytestmark = pytest.mark.asyncio

async def test_get_network_appliance_firewall_l3_firewall_rules_2(client):
    """Test case for get_network_appliance_firewall_l3_firewall_rules_2

    Return the L3 firewall rules for an MX network
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/appliance/firewall/l3FirewallRules'.format(network_id='network_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_wireless_ssid_firewall_l3_firewall_rules_3(client):
    """Test case for get_network_wireless_ssid_firewall_l3_firewall_rules_3

    Return the L3 firewall rules for an SSID on an MR network
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/wireless/ssids/{number}/firewall/l3FirewallRules'.format(network_id='network_id_example', number='number_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_network_appliance_firewall_l3_firewall_rules_2(client):
    """Test case for update_network_appliance_firewall_l3_firewall_rules_2

    Update the L3 firewall rules of an MX network
    """
    body = openapi_server.UpdateNetworkApplianceFirewallInboundFirewallRulesRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/networks/{network_id}/appliance/firewall/l3FirewallRules'.format(network_id='network_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_network_wireless_ssid_firewall_l3_firewall_rules_3(client):
    """Test case for update_network_wireless_ssid_firewall_l3_firewall_rules_3

    Update the L3 firewall rules of an SSID on an MR network
    """
    body = openapi_server.UpdateNetworkWirelessSsidFirewallL3FirewallRulesRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/networks/{network_id}/wireless/ssids/{number}/firewall/l3FirewallRules'.format(network_id='network_id_example', number='number_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

