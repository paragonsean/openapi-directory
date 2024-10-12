# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.update_network_appliance_port_request import UpdateNetworkAppliancePortRequest


pytestmark = pytest.mark.asyncio

async def test_get_network_appliance_port(client):
    """Test case for get_network_appliance_port

    Return per-port VLAN settings for a single MX port.
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v0/networks/{network_id}/appliancePorts/{appliance_port_id}'.format(network_id='network_id_example', appliance_port_id='appliance_port_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_appliance_ports(client):
    """Test case for get_network_appliance_ports

    List per-port VLAN settings for all ports of a MX.
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v0/networks/{network_id}/appliancePorts'.format(network_id='network_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_network_appliance_port(client):
    """Test case for update_network_appliance_port

    Update the per-port VLAN settings for a single MX port.
    """
    body = openapi_server.UpdateNetworkAppliancePortRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v0/networks/{network_id}/appliancePorts/{appliance_port_id}'.format(network_id='network_id_example', appliance_port_id='appliance_port_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

