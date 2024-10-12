# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.update_device_cellular_gateway_port_forwarding_rules_request import UpdateDeviceCellularGatewayPortForwardingRulesRequest
from openapi_server.models.update_network_appliance_firewall_port_forwarding_rules_request import UpdateNetworkApplianceFirewallPortForwardingRulesRequest


pytestmark = pytest.mark.asyncio

async def test_get_device_cellular_gateway_port_forwarding_rules_1(client):
    """Test case for get_device_cellular_gateway_port_forwarding_rules_1

    Returns the port forwarding rules for a single MG.
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/devices/{serial}/cellularGateway/portForwardingRules'.format(serial='serial_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_appliance_firewall_port_forwarding_rules_2(client):
    """Test case for get_network_appliance_firewall_port_forwarding_rules_2

    Return the port forwarding rules for an MX network
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/appliance/firewall/portForwardingRules'.format(network_id='network_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_device_cellular_gateway_port_forwarding_rules_1(client):
    """Test case for update_device_cellular_gateway_port_forwarding_rules_1

    Updates the port forwarding rules for a single MG.
    """
    body = openapi_server.UpdateDeviceCellularGatewayPortForwardingRulesRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/devices/{serial}/cellularGateway/portForwardingRules'.format(serial='serial_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_network_appliance_firewall_port_forwarding_rules_2(client):
    """Test case for update_network_appliance_firewall_port_forwarding_rules_2

    Update the port forwarding rules for an MX network
    """
    body = openapi_server.UpdateNetworkApplianceFirewallPortForwardingRulesRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/networks/{network_id}/appliance/firewall/portForwardingRules'.format(network_id='network_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

