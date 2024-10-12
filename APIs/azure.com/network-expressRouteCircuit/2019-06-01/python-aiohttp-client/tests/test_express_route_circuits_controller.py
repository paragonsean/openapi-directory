# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.express_route_circuit import ExpressRouteCircuit
from openapi_server.models.express_route_circuit_list_result import ExpressRouteCircuitListResult
from openapi_server.models.express_route_circuits_update_tags_request import ExpressRouteCircuitsUpdateTagsRequest


pytestmark = pytest.mark.asyncio

async def test_express_route_circuits_create_or_update(client):
    """Test case for express_route_circuits_create_or_update

    
    """
    parameters = {"etag":"etag","sku":{"tier":"Standard","name":"name","family":"UnlimitedData"},"properties":{"bandwidthInGbps":0.8008281904610115,"authorizations":[{"name":"name","etag":"etag","type":"type","properties":{"authorizationUseStatus":"Available","authorizationKey":"authorizationKey","provisioningState":"provisioningState"}},{"name":"name","etag":"etag","type":"type","properties":{"authorizationUseStatus":"Available","authorizationKey":"authorizationKey","provisioningState":"provisioningState"}}],"serviceProviderNotes":"serviceProviderNotes","globalReachEnabled":True,"provisioningState":"provisioningState","serviceProviderProvisioningState":"NotProvisioned","stag":7,"circuitProvisioningState":"circuitProvisioningState","gatewayManagerEtag":"gatewayManagerEtag","peerings":[{"name":"name","etag":"etag","type":"type","properties":{"routeFilter":{"id":"id"},"sharedKey":"sharedKey","primaryAzurePort":"primaryAzurePort","ipv6PeeringConfig":{"routeFilter":{"id":"id"},"microsoftPeeringConfig":{"advertisedCommunities":["advertisedCommunities","advertisedCommunities"],"routingRegistryName":"routingRegistryName","legacyMode":5,"advertisedPublicPrefixes":["advertisedPublicPrefixes","advertisedPublicPrefixes"],"advertisedPublicPrefixesState":"NotConfigured","customerASN":1},"primaryPeerAddressPrefix":"primaryPeerAddressPrefix","state":"Disabled","secondaryPeerAddressPrefix":"secondaryPeerAddressPrefix"},"secondaryAzurePort":"secondaryAzurePort","vlanId":2,"lastModifiedBy":"lastModifiedBy","peeredConnections":[{"name":"name","etag":"etag","type":"type","properties":{"expressRouteCircuitPeering":{"id":"id"},"addressPrefix":"addressPrefix","peerExpressRouteCircuitPeering":{"id":"id"},"connectionName":"connectionName","provisioningState":"provisioningState","authResourceGuid":"authResourceGuid"}},{"name":"name","etag":"etag","type":"type","properties":{"expressRouteCircuitPeering":{"id":"id"},"addressPrefix":"addressPrefix","peerExpressRouteCircuitPeering":{"id":"id"},"connectionName":"connectionName","provisioningState":"provisioningState","authResourceGuid":"authResourceGuid"}}],"azureASN":6,"provisioningState":"provisioningState","peerASN":2421234837,"secondaryPeerAddressPrefix":"secondaryPeerAddressPrefix","stats":{"primarybytesOut":7,"primarybytesIn":2,"secondarybytesOut":3,"secondarybytesIn":9},"gatewayManagerEtag":"gatewayManagerEtag","microsoftPeeringConfig":{"advertisedCommunities":["advertisedCommunities","advertisedCommunities"],"routingRegistryName":"routingRegistryName","legacyMode":5,"advertisedPublicPrefixes":["advertisedPublicPrefixes","advertisedPublicPrefixes"],"advertisedPublicPrefixesState":"NotConfigured","customerASN":1},"primaryPeerAddressPrefix":"primaryPeerAddressPrefix","state":"Disabled","expressRouteConnection":{"id":"id"},"connections":[{"name":"name","etag":"etag","type":"type","properties":{"authorizationKey":"authorizationKey","expressRouteCircuitPeering":{"id":"id"},"addressPrefix":"addressPrefix","peerExpressRouteCircuitPeering":{"id":"id"},"provisioningState":"provisioningState","circuitConnectionStatus":"Connected"}},{"name":"name","etag":"etag","type":"type","properties":{"authorizationKey":"authorizationKey","expressRouteCircuitPeering":{"id":"id"},"addressPrefix":"addressPrefix","peerExpressRouteCircuitPeering":{"id":"id"},"provisioningState":"provisioningState","circuitConnectionStatus":"Connected"}}],"peeringType":"AzurePublicPeering"}},{"name":"name","etag":"etag","type":"type","properties":{"routeFilter":{"id":"id"},"sharedKey":"sharedKey","primaryAzurePort":"primaryAzurePort","ipv6PeeringConfig":{"routeFilter":{"id":"id"},"microsoftPeeringConfig":{"advertisedCommunities":["advertisedCommunities","advertisedCommunities"],"routingRegistryName":"routingRegistryName","legacyMode":5,"advertisedPublicPrefixes":["advertisedPublicPrefixes","advertisedPublicPrefixes"],"advertisedPublicPrefixesState":"NotConfigured","customerASN":1},"primaryPeerAddressPrefix":"primaryPeerAddressPrefix","state":"Disabled","secondaryPeerAddressPrefix":"secondaryPeerAddressPrefix"},"secondaryAzurePort":"secondaryAzurePort","vlanId":2,"lastModifiedBy":"lastModifiedBy","peeredConnections":[{"name":"name","etag":"etag","type":"type","properties":{"expressRouteCircuitPeering":{"id":"id"},"addressPrefix":"addressPrefix","peerExpressRouteCircuitPeering":{"id":"id"},"connectionName":"connectionName","provisioningState":"provisioningState","authResourceGuid":"authResourceGuid"}},{"name":"name","etag":"etag","type":"type","properties":{"expressRouteCircuitPeering":{"id":"id"},"addressPrefix":"addressPrefix","peerExpressRouteCircuitPeering":{"id":"id"},"connectionName":"connectionName","provisioningState":"provisioningState","authResourceGuid":"authResourceGuid"}}],"azureASN":6,"provisioningState":"provisioningState","peerASN":2421234837,"secondaryPeerAddressPrefix":"secondaryPeerAddressPrefix","stats":{"primarybytesOut":7,"primarybytesIn":2,"secondarybytesOut":3,"secondarybytesIn":9},"gatewayManagerEtag":"gatewayManagerEtag","microsoftPeeringConfig":{"advertisedCommunities":["advertisedCommunities","advertisedCommunities"],"routingRegistryName":"routingRegistryName","legacyMode":5,"advertisedPublicPrefixes":["advertisedPublicPrefixes","advertisedPublicPrefixes"],"advertisedPublicPrefixesState":"NotConfigured","customerASN":1},"primaryPeerAddressPrefix":"primaryPeerAddressPrefix","state":"Disabled","expressRouteConnection":{"id":"id"},"connections":[{"name":"name","etag":"etag","type":"type","properties":{"authorizationKey":"authorizationKey","expressRouteCircuitPeering":{"id":"id"},"addressPrefix":"addressPrefix","peerExpressRouteCircuitPeering":{"id":"id"},"provisioningState":"provisioningState","circuitConnectionStatus":"Connected"}},{"name":"name","etag":"etag","type":"type","properties":{"authorizationKey":"authorizationKey","expressRouteCircuitPeering":{"id":"id"},"addressPrefix":"addressPrefix","peerExpressRouteCircuitPeering":{"id":"id"},"provisioningState":"provisioningState","circuitConnectionStatus":"Connected"}}],"peeringType":"AzurePublicPeering"}}],"serviceKey":"serviceKey","allowClassicOperations":True,"expressRoutePort":{"id":"id"},"serviceProviderProperties":{"bandwidthInMbps":4,"serviceProviderName":"serviceProviderName","peeringLocation":"peeringLocation"}}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/expressRouteCircuits/{circuit_name}'.format(resource_group_name='resource_group_name_example', circuit_name='circuit_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_express_route_circuits_delete(client):
    """Test case for express_route_circuits_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/expressRouteCircuits/{circuit_name}'.format(resource_group_name='resource_group_name_example', circuit_name='circuit_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_express_route_circuits_get(client):
    """Test case for express_route_circuits_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/expressRouteCircuits/{circuit_name}'.format(resource_group_name='resource_group_name_example', circuit_name='circuit_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_express_route_circuits_list(client):
    """Test case for express_route_circuits_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/expressRouteCircuits'.format(resource_group_name='resource_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_express_route_circuits_list_all(client):
    """Test case for express_route_circuits_list_all

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Network/expressRouteCircuits'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_express_route_circuits_update_tags(client):
    """Test case for express_route_circuits_update_tags

    
    """
    parameters = openapi_server.ExpressRouteCircuitsUpdateTagsRequest()
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/expressRouteCircuits/{circuit_name}'.format(resource_group_name='resource_group_name_example', circuit_name='circuit_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

