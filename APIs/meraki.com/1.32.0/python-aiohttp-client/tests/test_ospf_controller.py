# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.update_network_switch_routing_ospf_request import UpdateNetworkSwitchRoutingOspfRequest


pytestmark = pytest.mark.asyncio

async def test_get_network_switch_routing_ospf_2(client):
    """Test case for get_network_switch_routing_ospf_2

    Return layer 3 OSPF routing configuration
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/switch/routing/ospf'.format(network_id='network_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_network_switch_routing_ospf_2(client):
    """Test case for update_network_switch_routing_ospf_2

    Update layer 3 OSPF routing configuration
    """
    body = openapi_server.UpdateNetworkSwitchRoutingOspfRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/networks/{network_id}/switch/routing/ospf'.format(network_id='network_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

