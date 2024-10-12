# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.update_organization_vpn_firewall_rules_request import UpdateOrganizationVpnFirewallRulesRequest


pytestmark = pytest.mark.asyncio

async def test_get_organization_vpn_firewall_rules(client):
    """Test case for get_organization_vpn_firewall_rules

    Return the firewall rules for an organization's site-to-site VPN
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v0/organizations/{organization_id}/vpnFirewallRules'.format(organization_id='organization_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_organization_vpn_firewall_rules(client):
    """Test case for update_organization_vpn_firewall_rules

    Update the firewall rules of an organization's site-to-site VPN
    """
    body = openapi_server.UpdateOrganizationVpnFirewallRulesRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v0/organizations/{organization_id}/vpnFirewallRules'.format(organization_id='organization_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

