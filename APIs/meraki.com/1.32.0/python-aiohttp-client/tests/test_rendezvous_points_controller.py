# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_network_switch_routing_multicast_rendezvous_point_request import CreateNetworkSwitchRoutingMulticastRendezvousPointRequest
from openapi_server.models.update_network_switch_routing_multicast_rendezvous_point_request import UpdateNetworkSwitchRoutingMulticastRendezvousPointRequest


pytestmark = pytest.mark.asyncio

async def test_create_network_switch_routing_multicast_rendezvous_point_3(client):
    """Test case for create_network_switch_routing_multicast_rendezvous_point_3

    Create a multicast rendezvous point
    """
    body = openapi_server.CreateNetworkSwitchRoutingMulticastRendezvousPointRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/networks/{network_id}/switch/routing/multicast/rendezvousPoints'.format(network_id='network_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_network_switch_routing_multicast_rendezvous_point_3(client):
    """Test case for delete_network_switch_routing_multicast_rendezvous_point_3

    Delete a multicast rendezvous point
    """
    headers = { 
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/networks/{network_id}/switch/routing/multicast/rendezvousPoints/{rendezvous_point_id}'.format(network_id='network_id_example', rendezvous_point_id='rendezvous_point_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_switch_routing_multicast_rendezvous_point_3(client):
    """Test case for get_network_switch_routing_multicast_rendezvous_point_3

    Return a multicast rendezvous point
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/switch/routing/multicast/rendezvousPoints/{rendezvous_point_id}'.format(network_id='network_id_example', rendezvous_point_id='rendezvous_point_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_switch_routing_multicast_rendezvous_points_3(client):
    """Test case for get_network_switch_routing_multicast_rendezvous_points_3

    List multicast rendezvous points
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/switch/routing/multicast/rendezvousPoints'.format(network_id='network_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_network_switch_routing_multicast_rendezvous_point_3(client):
    """Test case for update_network_switch_routing_multicast_rendezvous_point_3

    Update a multicast rendezvous point
    """
    body = openapi_server.UpdateNetworkSwitchRoutingMulticastRendezvousPointRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/networks/{network_id}/switch/routing/multicast/rendezvousPoints/{rendezvous_point_id}'.format(network_id='network_id_example', rendezvous_point_id='rendezvous_point_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

