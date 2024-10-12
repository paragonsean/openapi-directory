# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.express_route_circuit_peering import ExpressRouteCircuitPeering
from openapi_server.models.express_route_circuit_peering_list_result import ExpressRouteCircuitPeeringListResult


pytestmark = pytest.mark.asyncio

async def test_express_route_circuit_peerings_create_or_update(client):
    """Test case for express_route_circuit_peerings_create_or_update

    
    """
    peering_parameters = {"name":"name","etag":"etag","type":"type","properties":{"routeFilter":{"id":"id"},"sharedKey":"sharedKey","primaryAzurePort":"primaryAzurePort","ipv6PeeringConfig":{"routeFilter":{"id":"id"},"microsoftPeeringConfig":{"advertisedCommunities":["advertisedCommunities","advertisedCommunities"],"routingRegistryName":"routingRegistryName","legacyMode":5,"advertisedPublicPrefixes":["advertisedPublicPrefixes","advertisedPublicPrefixes"],"advertisedPublicPrefixesState":"NotConfigured","customerASN":1},"primaryPeerAddressPrefix":"primaryPeerAddressPrefix","state":"Disabled","secondaryPeerAddressPrefix":"secondaryPeerAddressPrefix"},"secondaryAzurePort":"secondaryAzurePort","vlanId":2,"lastModifiedBy":"lastModifiedBy","peeredConnections":[{"name":"name","etag":"etag","type":"type","properties":{"expressRouteCircuitPeering":{"id":"id"},"addressPrefix":"addressPrefix","peerExpressRouteCircuitPeering":{"id":"id"},"connectionName":"connectionName","provisioningState":"provisioningState","authResourceGuid":"authResourceGuid"}},{"name":"name","etag":"etag","type":"type","properties":{"expressRouteCircuitPeering":{"id":"id"},"addressPrefix":"addressPrefix","peerExpressRouteCircuitPeering":{"id":"id"},"connectionName":"connectionName","provisioningState":"provisioningState","authResourceGuid":"authResourceGuid"}}],"azureASN":6,"provisioningState":"provisioningState","peerASN":2421234837,"secondaryPeerAddressPrefix":"secondaryPeerAddressPrefix","stats":{"primarybytesOut":7,"primarybytesIn":2,"secondarybytesOut":3,"secondarybytesIn":9},"gatewayManagerEtag":"gatewayManagerEtag","microsoftPeeringConfig":{"advertisedCommunities":["advertisedCommunities","advertisedCommunities"],"routingRegistryName":"routingRegistryName","legacyMode":5,"advertisedPublicPrefixes":["advertisedPublicPrefixes","advertisedPublicPrefixes"],"advertisedPublicPrefixesState":"NotConfigured","customerASN":1},"primaryPeerAddressPrefix":"primaryPeerAddressPrefix","state":"Disabled","expressRouteConnection":{"id":"id"},"connections":[{"name":"name","etag":"etag","type":"type","properties":{"authorizationKey":"authorizationKey","expressRouteCircuitPeering":{"id":"id"},"addressPrefix":"addressPrefix","peerExpressRouteCircuitPeering":{"id":"id"},"provisioningState":"provisioningState","circuitConnectionStatus":"Connected"}},{"name":"name","etag":"etag","type":"type","properties":{"authorizationKey":"authorizationKey","expressRouteCircuitPeering":{"id":"id"},"addressPrefix":"addressPrefix","peerExpressRouteCircuitPeering":{"id":"id"},"provisioningState":"provisioningState","circuitConnectionStatus":"Connected"}}],"peeringType":"AzurePublicPeering"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/expressRouteCircuits/{circuit_name}/peerings/{peering_name}'.format(resource_group_name='resource_group_name_example', circuit_name='circuit_name_example', peering_name='peering_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=peering_parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_express_route_circuit_peerings_delete(client):
    """Test case for express_route_circuit_peerings_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/expressRouteCircuits/{circuit_name}/peerings/{peering_name}'.format(resource_group_name='resource_group_name_example', circuit_name='circuit_name_example', peering_name='peering_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_express_route_circuit_peerings_get(client):
    """Test case for express_route_circuit_peerings_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/expressRouteCircuits/{circuit_name}/peerings/{peering_name}'.format(resource_group_name='resource_group_name_example', circuit_name='circuit_name_example', peering_name='peering_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_express_route_circuit_peerings_list(client):
    """Test case for express_route_circuit_peerings_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/expressRouteCircuits/{circuit_name}/peerings'.format(resource_group_name='resource_group_name_example', circuit_name='circuit_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

