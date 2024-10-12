# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_network_switch_dhcp_server_policy_arp_inspection_trusted_server_request import CreateNetworkSwitchDhcpServerPolicyArpInspectionTrustedServerRequest
from openapi_server.models.get_network_switch_dhcp_server_policy_arp_inspection_trusted_servers200_response_inner import GetNetworkSwitchDhcpServerPolicyArpInspectionTrustedServers200ResponseInner
from openapi_server.models.update_network_switch_dhcp_server_policy_arp_inspection_trusted_server_request import UpdateNetworkSwitchDhcpServerPolicyArpInspectionTrustedServerRequest


pytestmark = pytest.mark.asyncio

async def test_create_network_switch_dhcp_server_policy_arp_inspection_trusted_server_3(client):
    """Test case for create_network_switch_dhcp_server_policy_arp_inspection_trusted_server_3

    Add a server to be trusted by Dynamic ARP Inspection on this network
    """
    body = openapi_server.CreateNetworkSwitchDhcpServerPolicyArpInspectionTrustedServerRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/networks/{network_id}/switch/dhcpServerPolicy/arpInspection/trustedServers'.format(network_id='network_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_network_switch_dhcp_server_policy_arp_inspection_trusted_server_3(client):
    """Test case for delete_network_switch_dhcp_server_policy_arp_inspection_trusted_server_3

    Remove a server from being trusted by Dynamic ARP Inspection on this network
    """
    headers = { 
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/networks/{network_id}/switch/dhcpServerPolicy/arpInspection/trustedServers/{trusted_server_id}'.format(network_id='network_id_example', trusted_server_id='trusted_server_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_switch_dhcp_server_policy_arp_inspection_trusted_servers_3(client):
    """Test case for get_network_switch_dhcp_server_policy_arp_inspection_trusted_servers_3

    Return the list of servers trusted by Dynamic ARP Inspection on this network
    """
    params = [('perPage', 56),
                    ('startingAfter', 'starting_after_example'),
                    ('endingBefore', 'ending_before_example')]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/switch/dhcpServerPolicy/arpInspection/trustedServers'.format(network_id='network_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_network_switch_dhcp_server_policy_arp_inspection_trusted_server_3(client):
    """Test case for update_network_switch_dhcp_server_policy_arp_inspection_trusted_server_3

    Update a server that is trusted by Dynamic ARP Inspection on this network
    """
    body = openapi_server.UpdateNetworkSwitchDhcpServerPolicyArpInspectionTrustedServerRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/networks/{network_id}/switch/dhcpServerPolicy/arpInspection/trustedServers/{trusted_server_id}'.format(network_id='network_id_example', trusted_server_id='trusted_server_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

