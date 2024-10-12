# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_network_appliance_vlan201_response import CreateNetworkApplianceVlan201Response
from openapi_server.models.create_network_appliance_vlan_request import CreateNetworkApplianceVlanRequest
from openapi_server.models.get_network_appliance_vlans200_response_inner import GetNetworkApplianceVlans200ResponseInner
from openapi_server.models.update_network_appliance_vlan_request import UpdateNetworkApplianceVlanRequest
from openapi_server.models.update_network_appliance_vlans_settings_request import UpdateNetworkApplianceVlansSettingsRequest


pytestmark = pytest.mark.asyncio

async def test_create_network_appliance_vlan_1(client):
    """Test case for create_network_appliance_vlan_1

    Add a VLAN
    """
    body = openapi_server.CreateNetworkApplianceVlanRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/networks/{network_id}/appliance/vlans'.format(network_id='network_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_network_appliance_vlan_1(client):
    """Test case for delete_network_appliance_vlan_1

    Delete a VLAN from a network
    """
    headers = { 
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/networks/{network_id}/appliance/vlans/{vlan_id}'.format(network_id='network_id_example', vlan_id='vlan_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_appliance_vlan_1(client):
    """Test case for get_network_appliance_vlan_1

    Return a VLAN
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/appliance/vlans/{vlan_id}'.format(network_id='network_id_example', vlan_id='vlan_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_appliance_vlans_1(client):
    """Test case for get_network_appliance_vlans_1

    List the VLANs for an MX network
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/appliance/vlans'.format(network_id='network_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_appliance_vlans_settings_1(client):
    """Test case for get_network_appliance_vlans_settings_1

    Returns the enabled status of VLANs for the network
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/appliance/vlans/settings'.format(network_id='network_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_network_appliance_vlan_1(client):
    """Test case for update_network_appliance_vlan_1

    Update a VLAN
    """
    body = openapi_server.UpdateNetworkApplianceVlanRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/networks/{network_id}/appliance/vlans/{vlan_id}'.format(network_id='network_id_example', vlan_id='vlan_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_network_appliance_vlans_settings_1(client):
    """Test case for update_network_appliance_vlans_settings_1

    Enable/Disable VLANs for the given network
    """
    body = openapi_server.UpdateNetworkApplianceVlansSettingsRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/networks/{network_id}/appliance/vlans/settings'.format(network_id='network_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

