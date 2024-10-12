# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.update_network_appliance_firewall_firewalled_service_request import UpdateNetworkApplianceFirewallFirewalledServiceRequest


pytestmark = pytest.mark.asyncio

async def test_get_network_appliance_firewall_firewalled_service_2(client):
    """Test case for get_network_appliance_firewall_firewalled_service_2

    Return the accessibility settings of the given service ('ICMP', 'web', or 'SNMP')
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/appliance/firewall/firewalledServices/{service}'.format(network_id='network_id_example', service='service_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_appliance_firewall_firewalled_services_2(client):
    """Test case for get_network_appliance_firewall_firewalled_services_2

    List the appliance services and their accessibility rules
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/appliance/firewall/firewalledServices'.format(network_id='network_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_network_appliance_firewall_firewalled_service_2(client):
    """Test case for update_network_appliance_firewall_firewalled_service_2

    Updates the accessibility settings for the given service ('ICMP', 'web', or 'SNMP')
    """
    body = openapi_server.UpdateNetworkApplianceFirewallFirewalledServiceRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/networks/{network_id}/appliance/firewall/firewalledServices/{service}'.format(network_id='network_id_example', service='service_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

