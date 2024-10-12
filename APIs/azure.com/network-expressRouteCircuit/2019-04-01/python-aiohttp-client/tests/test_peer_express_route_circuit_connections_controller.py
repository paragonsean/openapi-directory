# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.peer_express_route_circuit_connection import PeerExpressRouteCircuitConnection
from openapi_server.models.peer_express_route_circuit_connection_list_result import PeerExpressRouteCircuitConnectionListResult


pytestmark = pytest.mark.asyncio

async def test_peer_express_route_circuit_connections_get(client):
    """Test case for peer_express_route_circuit_connections_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/expressRouteCircuits/{circuit_name}/peerings/{peering_name}/peerConnections/{connection_name}'.format(resource_group_name='resource_group_name_example', circuit_name='circuit_name_example', peering_name='peering_name_example', connection_name='connection_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_peer_express_route_circuit_connections_list(client):
    """Test case for peer_express_route_circuit_connections_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/expressRouteCircuits/{circuit_name}/peerings/{peering_name}/peerConnections'.format(resource_group_name='resource_group_name_example', circuit_name='circuit_name_example', peering_name='peering_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

