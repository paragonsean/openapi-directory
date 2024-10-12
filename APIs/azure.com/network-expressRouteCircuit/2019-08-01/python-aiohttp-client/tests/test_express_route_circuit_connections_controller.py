# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.express_route_circuit_connection import ExpressRouteCircuitConnection
from openapi_server.models.express_route_circuit_connection_list_result import ExpressRouteCircuitConnectionListResult


pytestmark = pytest.mark.asyncio

async def test_express_route_circuit_connections_create_or_update(client):
    """Test case for express_route_circuit_connections_create_or_update

    
    """
    express_route_circuit_connection_parameters = {"name":"name","etag":"etag","type":"type","properties":{"authorizationKey":"authorizationKey","expressRouteCircuitPeering":{"id":"id"},"addressPrefix":"addressPrefix","peerExpressRouteCircuitPeering":{"id":"id"},"provisioningState":"Succeeded","circuitConnectionStatus":"Connected"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/expressRouteCircuits/{circuit_name}/peerings/{peering_name}/connections/{connection_name}'.format(resource_group_name='resource_group_name_example', circuit_name='circuit_name_example', peering_name='peering_name_example', connection_name='connection_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=express_route_circuit_connection_parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_express_route_circuit_connections_delete(client):
    """Test case for express_route_circuit_connections_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/expressRouteCircuits/{circuit_name}/peerings/{peering_name}/connections/{connection_name}'.format(resource_group_name='resource_group_name_example', circuit_name='circuit_name_example', peering_name='peering_name_example', connection_name='connection_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_express_route_circuit_connections_get(client):
    """Test case for express_route_circuit_connections_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/expressRouteCircuits/{circuit_name}/peerings/{peering_name}/connections/{connection_name}'.format(resource_group_name='resource_group_name_example', circuit_name='circuit_name_example', peering_name='peering_name_example', connection_name='connection_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_express_route_circuit_connections_list(client):
    """Test case for express_route_circuit_connections_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/expressRouteCircuits/{circuit_name}/peerings/{peering_name}/connections'.format(resource_group_name='resource_group_name_example', circuit_name='circuit_name_example', peering_name='peering_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

