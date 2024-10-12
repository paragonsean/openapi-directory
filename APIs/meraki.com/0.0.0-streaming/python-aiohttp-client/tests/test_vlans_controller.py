# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_network_vlan_request import CreateNetworkVlanRequest
from openapi_server.models.update_network_vlan_request import UpdateNetworkVlanRequest
from openapi_server.models.update_network_vlans_enabled_state_request import UpdateNetworkVlansEnabledStateRequest


pytestmark = pytest.mark.asyncio

async def test_create_network_vlan(client):
    """Test case for create_network_vlan

    Add a VLAN
    """
    body = openapi_server.CreateNetworkVlanRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v0/networks/{network_id}/vlans'.format(network_id='network_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_network_vlan(client):
    """Test case for delete_network_vlan

    Delete a VLAN from a network
    """
    headers = { 
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v0/networks/{network_id}/vlans/{vlan_id}'.format(network_id='network_id_example', vlan_id='vlan_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_vlan(client):
    """Test case for get_network_vlan

    Return a VLAN
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v0/networks/{network_id}/vlans/{vlan_id}'.format(network_id='network_id_example', vlan_id='vlan_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_vlans(client):
    """Test case for get_network_vlans

    List the VLANs for an MX network
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v0/networks/{network_id}/vlans'.format(network_id='network_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_vlans_enabled_state(client):
    """Test case for get_network_vlans_enabled_state

    Returns the enabled status of VLANs for the network
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v0/networks/{network_id}/vlansEnabledState'.format(network_id='network_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_network_vlan(client):
    """Test case for update_network_vlan

    Update a VLAN
    """
    body = openapi_server.UpdateNetworkVlanRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v0/networks/{network_id}/vlans/{vlan_id}'.format(network_id='network_id_example', vlan_id='vlan_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_network_vlans_enabled_state(client):
    """Test case for update_network_vlans_enabled_state

    Enable/Disable VLANs for the given network
    """
    body = openapi_server.UpdateNetworkVlansEnabledStateRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v0/networks/{network_id}/vlansEnabledState'.format(network_id='network_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

