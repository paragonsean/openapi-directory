# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.update_network_switch_alternate_management_interface_request import UpdateNetworkSwitchAlternateManagementInterfaceRequest
from openapi_server.models.update_network_wireless_alternate_management_interface_request import UpdateNetworkWirelessAlternateManagementInterfaceRequest


pytestmark = pytest.mark.asyncio

async def test_get_network_switch_alternate_management_interface_1(client):
    """Test case for get_network_switch_alternate_management_interface_1

    Return the switch alternate management interface for the network
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/switch/alternateManagementInterface'.format(network_id='network_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_wireless_alternate_management_interface_1(client):
    """Test case for get_network_wireless_alternate_management_interface_1

    Return alternate management interface and devices with IP assigned
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/wireless/alternateManagementInterface'.format(network_id='network_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_network_switch_alternate_management_interface_1(client):
    """Test case for update_network_switch_alternate_management_interface_1

    Update the switch alternate management interface for the network
    """
    body = openapi_server.UpdateNetworkSwitchAlternateManagementInterfaceRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/networks/{network_id}/switch/alternateManagementInterface'.format(network_id='network_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_network_wireless_alternate_management_interface_1(client):
    """Test case for update_network_wireless_alternate_management_interface_1

    Update alternate management interface and device static IP
    """
    body = openapi_server.UpdateNetworkWirelessAlternateManagementInterfaceRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/networks/{network_id}/wireless/alternateManagementInterface'.format(network_id='network_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

