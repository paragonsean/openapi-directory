# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.patch_route_filter import PatchRouteFilter
from openapi_server.models.route_filter import RouteFilter
from openapi_server.models.route_filter_list_result import RouteFilterListResult


pytestmark = pytest.mark.asyncio

async def test_route_filters_create_or_update(client):
    """Test case for route_filters_create_or_update

    
    """
    route_filter_parameters = {"etag":"etag","properties":{"ipv6Peerings":[{"name":"name","etag":"etag","type":"type","properties":{"routeFilter":{"id":"id"},"sharedKey":"sharedKey","primaryAzurePort":"primaryAzurePort","ipv6PeeringConfig":{"routeFilter":{"id":"id"},"microsoftPeeringConfig":{"advertisedCommunities":["advertisedCommunities","advertisedCommunities"],"routingRegistryName":"routingRegistryName","legacyMode":1,"advertisedPublicPrefixes":["advertisedPublicPrefixes","advertisedPublicPrefixes"],"advertisedPublicPrefixesState":"NotConfigured","customerASN":6},"primaryPeerAddressPrefix":"primaryPeerAddressPrefix","state":"Disabled","secondaryPeerAddressPrefix":"secondaryPeerAddressPrefix"},"secondaryAzurePort":"secondaryAzurePort","vlanId":3,"lastModifiedBy":"lastModifiedBy","peeredConnections":[{"name":"name","etag":"etag","type":"type","properties":{"expressRouteCircuitPeering":{"id":"id"},"addressPrefix":"addressPrefix","peerExpressRouteCircuitPeering":{"id":"id"},"connectionName":"connectionName","provisioningState":"Succeeded","authResourceGuid":"authResourceGuid","circuitConnectionStatus":"Connected"}},{"name":"name","etag":"etag","type":"type","properties":{"expressRouteCircuitPeering":{"id":"id"},"addressPrefix":"addressPrefix","peerExpressRouteCircuitPeering":{"id":"id"},"connectionName":"connectionName","provisioningState":"Succeeded","authResourceGuid":"authResourceGuid","circuitConnectionStatus":"Connected"}}],"azureASN":0,"provisioningState":"Succeeded","peerASN":2560717018,"secondaryPeerAddressPrefix":"secondaryPeerAddressPrefix","stats":{"primarybytesOut":2,"primarybytesIn":5,"secondarybytesOut":9,"secondarybytesIn":7},"gatewayManagerEtag":"gatewayManagerEtag","microsoftPeeringConfig":{"advertisedCommunities":["advertisedCommunities","advertisedCommunities"],"routingRegistryName":"routingRegistryName","legacyMode":1,"advertisedPublicPrefixes":["advertisedPublicPrefixes","advertisedPublicPrefixes"],"advertisedPublicPrefixesState":"NotConfigured","customerASN":6},"primaryPeerAddressPrefix":"primaryPeerAddressPrefix","state":"Disabled","expressRouteConnection":{"id":"id"},"connections":[{"name":"name","etag":"etag","type":"type","properties":{"authorizationKey":"authorizationKey","expressRouteCircuitPeering":{"id":"id"},"addressPrefix":"addressPrefix","peerExpressRouteCircuitPeering":{"id":"id"},"provisioningState":"Succeeded","circuitConnectionStatus":"Connected"}},{"name":"name","etag":"etag","type":"type","properties":{"authorizationKey":"authorizationKey","expressRouteCircuitPeering":{"id":"id"},"addressPrefix":"addressPrefix","peerExpressRouteCircuitPeering":{"id":"id"},"provisioningState":"Succeeded","circuitConnectionStatus":"Connected"}}],"peeringType":"AzurePublicPeering"}},{"name":"name","etag":"etag","type":"type","properties":{"routeFilter":{"id":"id"},"sharedKey":"sharedKey","primaryAzurePort":"primaryAzurePort","ipv6PeeringConfig":{"routeFilter":{"id":"id"},"microsoftPeeringConfig":{"advertisedCommunities":["advertisedCommunities","advertisedCommunities"],"routingRegistryName":"routingRegistryName","legacyMode":1,"advertisedPublicPrefixes":["advertisedPublicPrefixes","advertisedPublicPrefixes"],"advertisedPublicPrefixesState":"NotConfigured","customerASN":6},"primaryPeerAddressPrefix":"primaryPeerAddressPrefix","state":"Disabled","secondaryPeerAddressPrefix":"secondaryPeerAddressPrefix"},"secondaryAzurePort":"secondaryAzurePort","vlanId":3,"lastModifiedBy":"lastModifiedBy","peeredConnections":[{"name":"name","etag":"etag","type":"type","properties":{"expressRouteCircuitPeering":{"id":"id"},"addressPrefix":"addressPrefix","peerExpressRouteCircuitPeering":{"id":"id"},"connectionName":"connectionName","provisioningState":"Succeeded","authResourceGuid":"authResourceGuid","circuitConnectionStatus":"Connected"}},{"name":"name","etag":"etag","type":"type","properties":{"expressRouteCircuitPeering":{"id":"id"},"addressPrefix":"addressPrefix","peerExpressRouteCircuitPeering":{"id":"id"},"connectionName":"connectionName","provisioningState":"Succeeded","authResourceGuid":"authResourceGuid","circuitConnectionStatus":"Connected"}}],"azureASN":0,"provisioningState":"Succeeded","peerASN":2560717018,"secondaryPeerAddressPrefix":"secondaryPeerAddressPrefix","stats":{"primarybytesOut":2,"primarybytesIn":5,"secondarybytesOut":9,"secondarybytesIn":7},"gatewayManagerEtag":"gatewayManagerEtag","microsoftPeeringConfig":{"advertisedCommunities":["advertisedCommunities","advertisedCommunities"],"routingRegistryName":"routingRegistryName","legacyMode":1,"advertisedPublicPrefixes":["advertisedPublicPrefixes","advertisedPublicPrefixes"],"advertisedPublicPrefixesState":"NotConfigured","customerASN":6},"primaryPeerAddressPrefix":"primaryPeerAddressPrefix","state":"Disabled","expressRouteConnection":{"id":"id"},"connections":[{"name":"name","etag":"etag","type":"type","properties":{"authorizationKey":"authorizationKey","expressRouteCircuitPeering":{"id":"id"},"addressPrefix":"addressPrefix","peerExpressRouteCircuitPeering":{"id":"id"},"provisioningState":"Succeeded","circuitConnectionStatus":"Connected"}},{"name":"name","etag":"etag","type":"type","properties":{"authorizationKey":"authorizationKey","expressRouteCircuitPeering":{"id":"id"},"addressPrefix":"addressPrefix","peerExpressRouteCircuitPeering":{"id":"id"},"provisioningState":"Succeeded","circuitConnectionStatus":"Connected"}}],"peeringType":"AzurePublicPeering"}}],"peerings":[{"name":"name","etag":"etag","type":"type","properties":{"routeFilter":{"id":"id"},"sharedKey":"sharedKey","primaryAzurePort":"primaryAzurePort","ipv6PeeringConfig":{"routeFilter":{"id":"id"},"microsoftPeeringConfig":{"advertisedCommunities":["advertisedCommunities","advertisedCommunities"],"routingRegistryName":"routingRegistryName","legacyMode":1,"advertisedPublicPrefixes":["advertisedPublicPrefixes","advertisedPublicPrefixes"],"advertisedPublicPrefixesState":"NotConfigured","customerASN":6},"primaryPeerAddressPrefix":"primaryPeerAddressPrefix","state":"Disabled","secondaryPeerAddressPrefix":"secondaryPeerAddressPrefix"},"secondaryAzurePort":"secondaryAzurePort","vlanId":3,"lastModifiedBy":"lastModifiedBy","peeredConnections":[{"name":"name","etag":"etag","type":"type","properties":{"expressRouteCircuitPeering":{"id":"id"},"addressPrefix":"addressPrefix","peerExpressRouteCircuitPeering":{"id":"id"},"connectionName":"connectionName","provisioningState":"Succeeded","authResourceGuid":"authResourceGuid","circuitConnectionStatus":"Connected"}},{"name":"name","etag":"etag","type":"type","properties":{"expressRouteCircuitPeering":{"id":"id"},"addressPrefix":"addressPrefix","peerExpressRouteCircuitPeering":{"id":"id"},"connectionName":"connectionName","provisioningState":"Succeeded","authResourceGuid":"authResourceGuid","circuitConnectionStatus":"Connected"}}],"azureASN":0,"provisioningState":"Succeeded","peerASN":2560717018,"secondaryPeerAddressPrefix":"secondaryPeerAddressPrefix","stats":{"primarybytesOut":2,"primarybytesIn":5,"secondarybytesOut":9,"secondarybytesIn":7},"gatewayManagerEtag":"gatewayManagerEtag","microsoftPeeringConfig":{"advertisedCommunities":["advertisedCommunities","advertisedCommunities"],"routingRegistryName":"routingRegistryName","legacyMode":1,"advertisedPublicPrefixes":["advertisedPublicPrefixes","advertisedPublicPrefixes"],"advertisedPublicPrefixesState":"NotConfigured","customerASN":6},"primaryPeerAddressPrefix":"primaryPeerAddressPrefix","state":"Disabled","expressRouteConnection":{"id":"id"},"connections":[{"name":"name","etag":"etag","type":"type","properties":{"authorizationKey":"authorizationKey","expressRouteCircuitPeering":{"id":"id"},"addressPrefix":"addressPrefix","peerExpressRouteCircuitPeering":{"id":"id"},"provisioningState":"Succeeded","circuitConnectionStatus":"Connected"}},{"name":"name","etag":"etag","type":"type","properties":{"authorizationKey":"authorizationKey","expressRouteCircuitPeering":{"id":"id"},"addressPrefix":"addressPrefix","peerExpressRouteCircuitPeering":{"id":"id"},"provisioningState":"Succeeded","circuitConnectionStatus":"Connected"}}],"peeringType":"AzurePublicPeering"}},{"name":"name","etag":"etag","type":"type","properties":{"routeFilter":{"id":"id"},"sharedKey":"sharedKey","primaryAzurePort":"primaryAzurePort","ipv6PeeringConfig":{"routeFilter":{"id":"id"},"microsoftPeeringConfig":{"advertisedCommunities":["advertisedCommunities","advertisedCommunities"],"routingRegistryName":"routingRegistryName","legacyMode":1,"advertisedPublicPrefixes":["advertisedPublicPrefixes","advertisedPublicPrefixes"],"advertisedPublicPrefixesState":"NotConfigured","customerASN":6},"primaryPeerAddressPrefix":"primaryPeerAddressPrefix","state":"Disabled","secondaryPeerAddressPrefix":"secondaryPeerAddressPrefix"},"secondaryAzurePort":"secondaryAzurePort","vlanId":3,"lastModifiedBy":"lastModifiedBy","peeredConnections":[{"name":"name","etag":"etag","type":"type","properties":{"expressRouteCircuitPeering":{"id":"id"},"addressPrefix":"addressPrefix","peerExpressRouteCircuitPeering":{"id":"id"},"connectionName":"connectionName","provisioningState":"Succeeded","authResourceGuid":"authResourceGuid","circuitConnectionStatus":"Connected"}},{"name":"name","etag":"etag","type":"type","properties":{"expressRouteCircuitPeering":{"id":"id"},"addressPrefix":"addressPrefix","peerExpressRouteCircuitPeering":{"id":"id"},"connectionName":"connectionName","provisioningState":"Succeeded","authResourceGuid":"authResourceGuid","circuitConnectionStatus":"Connected"}}],"azureASN":0,"provisioningState":"Succeeded","peerASN":2560717018,"secondaryPeerAddressPrefix":"secondaryPeerAddressPrefix","stats":{"primarybytesOut":2,"primarybytesIn":5,"secondarybytesOut":9,"secondarybytesIn":7},"gatewayManagerEtag":"gatewayManagerEtag","microsoftPeeringConfig":{"advertisedCommunities":["advertisedCommunities","advertisedCommunities"],"routingRegistryName":"routingRegistryName","legacyMode":1,"advertisedPublicPrefixes":["advertisedPublicPrefixes","advertisedPublicPrefixes"],"advertisedPublicPrefixesState":"NotConfigured","customerASN":6},"primaryPeerAddressPrefix":"primaryPeerAddressPrefix","state":"Disabled","expressRouteConnection":{"id":"id"},"connections":[{"name":"name","etag":"etag","type":"type","properties":{"authorizationKey":"authorizationKey","expressRouteCircuitPeering":{"id":"id"},"addressPrefix":"addressPrefix","peerExpressRouteCircuitPeering":{"id":"id"},"provisioningState":"Succeeded","circuitConnectionStatus":"Connected"}},{"name":"name","etag":"etag","type":"type","properties":{"authorizationKey":"authorizationKey","expressRouteCircuitPeering":{"id":"id"},"addressPrefix":"addressPrefix","peerExpressRouteCircuitPeering":{"id":"id"},"provisioningState":"Succeeded","circuitConnectionStatus":"Connected"}}],"peeringType":"AzurePublicPeering"}}],"rules":[{"name":"name","etag":"etag","location":"location","properties":{"access":"Allow","routeFilterRuleType":"Community","provisioningState":"Succeeded","communities":["communities","communities"]}},{"name":"name","etag":"etag","location":"location","properties":{"access":"Allow","routeFilterRuleType":"Community","provisioningState":"Succeeded","communities":["communities","communities"]}}],"provisioningState":"Succeeded"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/routeFilters/{route_filter_name}'.format(resource_group_name='resource_group_name_example', route_filter_name='route_filter_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=route_filter_parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_route_filters_delete(client):
    """Test case for route_filters_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/routeFilters/{route_filter_name}'.format(resource_group_name='resource_group_name_example', route_filter_name='route_filter_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_route_filters_get(client):
    """Test case for route_filters_get

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$expand', 'expand_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/routeFilters/{route_filter_name}'.format(resource_group_name='resource_group_name_example', route_filter_name='route_filter_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_route_filters_list(client):
    """Test case for route_filters_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Network/routeFilters'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_route_filters_list_by_resource_group(client):
    """Test case for route_filters_list_by_resource_group

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/routeFilters'.format(resource_group_name='resource_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_route_filters_update(client):
    """Test case for route_filters_update

    
    """
    route_filter_parameters = {"name":"name","etag":"etag","type":"type","properties":{"ipv6Peerings":[{"name":"name","etag":"etag","type":"type","properties":{"routeFilter":{"id":"id"},"sharedKey":"sharedKey","primaryAzurePort":"primaryAzurePort","ipv6PeeringConfig":{"routeFilter":{"id":"id"},"microsoftPeeringConfig":{"advertisedCommunities":["advertisedCommunities","advertisedCommunities"],"routingRegistryName":"routingRegistryName","legacyMode":1,"advertisedPublicPrefixes":["advertisedPublicPrefixes","advertisedPublicPrefixes"],"advertisedPublicPrefixesState":"NotConfigured","customerASN":6},"primaryPeerAddressPrefix":"primaryPeerAddressPrefix","state":"Disabled","secondaryPeerAddressPrefix":"secondaryPeerAddressPrefix"},"secondaryAzurePort":"secondaryAzurePort","vlanId":3,"lastModifiedBy":"lastModifiedBy","peeredConnections":[{"name":"name","etag":"etag","type":"type","properties":{"expressRouteCircuitPeering":{"id":"id"},"addressPrefix":"addressPrefix","peerExpressRouteCircuitPeering":{"id":"id"},"connectionName":"connectionName","provisioningState":"Succeeded","authResourceGuid":"authResourceGuid","circuitConnectionStatus":"Connected"}},{"name":"name","etag":"etag","type":"type","properties":{"expressRouteCircuitPeering":{"id":"id"},"addressPrefix":"addressPrefix","peerExpressRouteCircuitPeering":{"id":"id"},"connectionName":"connectionName","provisioningState":"Succeeded","authResourceGuid":"authResourceGuid","circuitConnectionStatus":"Connected"}}],"azureASN":0,"provisioningState":"Succeeded","peerASN":2560717018,"secondaryPeerAddressPrefix":"secondaryPeerAddressPrefix","stats":{"primarybytesOut":2,"primarybytesIn":5,"secondarybytesOut":9,"secondarybytesIn":7},"gatewayManagerEtag":"gatewayManagerEtag","microsoftPeeringConfig":{"advertisedCommunities":["advertisedCommunities","advertisedCommunities"],"routingRegistryName":"routingRegistryName","legacyMode":1,"advertisedPublicPrefixes":["advertisedPublicPrefixes","advertisedPublicPrefixes"],"advertisedPublicPrefixesState":"NotConfigured","customerASN":6},"primaryPeerAddressPrefix":"primaryPeerAddressPrefix","state":"Disabled","expressRouteConnection":{"id":"id"},"connections":[{"name":"name","etag":"etag","type":"type","properties":{"authorizationKey":"authorizationKey","expressRouteCircuitPeering":{"id":"id"},"addressPrefix":"addressPrefix","peerExpressRouteCircuitPeering":{"id":"id"},"provisioningState":"Succeeded","circuitConnectionStatus":"Connected"}},{"name":"name","etag":"etag","type":"type","properties":{"authorizationKey":"authorizationKey","expressRouteCircuitPeering":{"id":"id"},"addressPrefix":"addressPrefix","peerExpressRouteCircuitPeering":{"id":"id"},"provisioningState":"Succeeded","circuitConnectionStatus":"Connected"}}],"peeringType":"AzurePublicPeering"}},{"name":"name","etag":"etag","type":"type","properties":{"routeFilter":{"id":"id"},"sharedKey":"sharedKey","primaryAzurePort":"primaryAzurePort","ipv6PeeringConfig":{"routeFilter":{"id":"id"},"microsoftPeeringConfig":{"advertisedCommunities":["advertisedCommunities","advertisedCommunities"],"routingRegistryName":"routingRegistryName","legacyMode":1,"advertisedPublicPrefixes":["advertisedPublicPrefixes","advertisedPublicPrefixes"],"advertisedPublicPrefixesState":"NotConfigured","customerASN":6},"primaryPeerAddressPrefix":"primaryPeerAddressPrefix","state":"Disabled","secondaryPeerAddressPrefix":"secondaryPeerAddressPrefix"},"secondaryAzurePort":"secondaryAzurePort","vlanId":3,"lastModifiedBy":"lastModifiedBy","peeredConnections":[{"name":"name","etag":"etag","type":"type","properties":{"expressRouteCircuitPeering":{"id":"id"},"addressPrefix":"addressPrefix","peerExpressRouteCircuitPeering":{"id":"id"},"connectionName":"connectionName","provisioningState":"Succeeded","authResourceGuid":"authResourceGuid","circuitConnectionStatus":"Connected"}},{"name":"name","etag":"etag","type":"type","properties":{"expressRouteCircuitPeering":{"id":"id"},"addressPrefix":"addressPrefix","peerExpressRouteCircuitPeering":{"id":"id"},"connectionName":"connectionName","provisioningState":"Succeeded","authResourceGuid":"authResourceGuid","circuitConnectionStatus":"Connected"}}],"azureASN":0,"provisioningState":"Succeeded","peerASN":2560717018,"secondaryPeerAddressPrefix":"secondaryPeerAddressPrefix","stats":{"primarybytesOut":2,"primarybytesIn":5,"secondarybytesOut":9,"secondarybytesIn":7},"gatewayManagerEtag":"gatewayManagerEtag","microsoftPeeringConfig":{"advertisedCommunities":["advertisedCommunities","advertisedCommunities"],"routingRegistryName":"routingRegistryName","legacyMode":1,"advertisedPublicPrefixes":["advertisedPublicPrefixes","advertisedPublicPrefixes"],"advertisedPublicPrefixesState":"NotConfigured","customerASN":6},"primaryPeerAddressPrefix":"primaryPeerAddressPrefix","state":"Disabled","expressRouteConnection":{"id":"id"},"connections":[{"name":"name","etag":"etag","type":"type","properties":{"authorizationKey":"authorizationKey","expressRouteCircuitPeering":{"id":"id"},"addressPrefix":"addressPrefix","peerExpressRouteCircuitPeering":{"id":"id"},"provisioningState":"Succeeded","circuitConnectionStatus":"Connected"}},{"name":"name","etag":"etag","type":"type","properties":{"authorizationKey":"authorizationKey","expressRouteCircuitPeering":{"id":"id"},"addressPrefix":"addressPrefix","peerExpressRouteCircuitPeering":{"id":"id"},"provisioningState":"Succeeded","circuitConnectionStatus":"Connected"}}],"peeringType":"AzurePublicPeering"}}],"peerings":[{"name":"name","etag":"etag","type":"type","properties":{"routeFilter":{"id":"id"},"sharedKey":"sharedKey","primaryAzurePort":"primaryAzurePort","ipv6PeeringConfig":{"routeFilter":{"id":"id"},"microsoftPeeringConfig":{"advertisedCommunities":["advertisedCommunities","advertisedCommunities"],"routingRegistryName":"routingRegistryName","legacyMode":1,"advertisedPublicPrefixes":["advertisedPublicPrefixes","advertisedPublicPrefixes"],"advertisedPublicPrefixesState":"NotConfigured","customerASN":6},"primaryPeerAddressPrefix":"primaryPeerAddressPrefix","state":"Disabled","secondaryPeerAddressPrefix":"secondaryPeerAddressPrefix"},"secondaryAzurePort":"secondaryAzurePort","vlanId":3,"lastModifiedBy":"lastModifiedBy","peeredConnections":[{"name":"name","etag":"etag","type":"type","properties":{"expressRouteCircuitPeering":{"id":"id"},"addressPrefix":"addressPrefix","peerExpressRouteCircuitPeering":{"id":"id"},"connectionName":"connectionName","provisioningState":"Succeeded","authResourceGuid":"authResourceGuid","circuitConnectionStatus":"Connected"}},{"name":"name","etag":"etag","type":"type","properties":{"expressRouteCircuitPeering":{"id":"id"},"addressPrefix":"addressPrefix","peerExpressRouteCircuitPeering":{"id":"id"},"connectionName":"connectionName","provisioningState":"Succeeded","authResourceGuid":"authResourceGuid","circuitConnectionStatus":"Connected"}}],"azureASN":0,"provisioningState":"Succeeded","peerASN":2560717018,"secondaryPeerAddressPrefix":"secondaryPeerAddressPrefix","stats":{"primarybytesOut":2,"primarybytesIn":5,"secondarybytesOut":9,"secondarybytesIn":7},"gatewayManagerEtag":"gatewayManagerEtag","microsoftPeeringConfig":{"advertisedCommunities":["advertisedCommunities","advertisedCommunities"],"routingRegistryName":"routingRegistryName","legacyMode":1,"advertisedPublicPrefixes":["advertisedPublicPrefixes","advertisedPublicPrefixes"],"advertisedPublicPrefixesState":"NotConfigured","customerASN":6},"primaryPeerAddressPrefix":"primaryPeerAddressPrefix","state":"Disabled","expressRouteConnection":{"id":"id"},"connections":[{"name":"name","etag":"etag","type":"type","properties":{"authorizationKey":"authorizationKey","expressRouteCircuitPeering":{"id":"id"},"addressPrefix":"addressPrefix","peerExpressRouteCircuitPeering":{"id":"id"},"provisioningState":"Succeeded","circuitConnectionStatus":"Connected"}},{"name":"name","etag":"etag","type":"type","properties":{"authorizationKey":"authorizationKey","expressRouteCircuitPeering":{"id":"id"},"addressPrefix":"addressPrefix","peerExpressRouteCircuitPeering":{"id":"id"},"provisioningState":"Succeeded","circuitConnectionStatus":"Connected"}}],"peeringType":"AzurePublicPeering"}},{"name":"name","etag":"etag","type":"type","properties":{"routeFilter":{"id":"id"},"sharedKey":"sharedKey","primaryAzurePort":"primaryAzurePort","ipv6PeeringConfig":{"routeFilter":{"id":"id"},"microsoftPeeringConfig":{"advertisedCommunities":["advertisedCommunities","advertisedCommunities"],"routingRegistryName":"routingRegistryName","legacyMode":1,"advertisedPublicPrefixes":["advertisedPublicPrefixes","advertisedPublicPrefixes"],"advertisedPublicPrefixesState":"NotConfigured","customerASN":6},"primaryPeerAddressPrefix":"primaryPeerAddressPrefix","state":"Disabled","secondaryPeerAddressPrefix":"secondaryPeerAddressPrefix"},"secondaryAzurePort":"secondaryAzurePort","vlanId":3,"lastModifiedBy":"lastModifiedBy","peeredConnections":[{"name":"name","etag":"etag","type":"type","properties":{"expressRouteCircuitPeering":{"id":"id"},"addressPrefix":"addressPrefix","peerExpressRouteCircuitPeering":{"id":"id"},"connectionName":"connectionName","provisioningState":"Succeeded","authResourceGuid":"authResourceGuid","circuitConnectionStatus":"Connected"}},{"name":"name","etag":"etag","type":"type","properties":{"expressRouteCircuitPeering":{"id":"id"},"addressPrefix":"addressPrefix","peerExpressRouteCircuitPeering":{"id":"id"},"connectionName":"connectionName","provisioningState":"Succeeded","authResourceGuid":"authResourceGuid","circuitConnectionStatus":"Connected"}}],"azureASN":0,"provisioningState":"Succeeded","peerASN":2560717018,"secondaryPeerAddressPrefix":"secondaryPeerAddressPrefix","stats":{"primarybytesOut":2,"primarybytesIn":5,"secondarybytesOut":9,"secondarybytesIn":7},"gatewayManagerEtag":"gatewayManagerEtag","microsoftPeeringConfig":{"advertisedCommunities":["advertisedCommunities","advertisedCommunities"],"routingRegistryName":"routingRegistryName","legacyMode":1,"advertisedPublicPrefixes":["advertisedPublicPrefixes","advertisedPublicPrefixes"],"advertisedPublicPrefixesState":"NotConfigured","customerASN":6},"primaryPeerAddressPrefix":"primaryPeerAddressPrefix","state":"Disabled","expressRouteConnection":{"id":"id"},"connections":[{"name":"name","etag":"etag","type":"type","properties":{"authorizationKey":"authorizationKey","expressRouteCircuitPeering":{"id":"id"},"addressPrefix":"addressPrefix","peerExpressRouteCircuitPeering":{"id":"id"},"provisioningState":"Succeeded","circuitConnectionStatus":"Connected"}},{"name":"name","etag":"etag","type":"type","properties":{"authorizationKey":"authorizationKey","expressRouteCircuitPeering":{"id":"id"},"addressPrefix":"addressPrefix","peerExpressRouteCircuitPeering":{"id":"id"},"provisioningState":"Succeeded","circuitConnectionStatus":"Connected"}}],"peeringType":"AzurePublicPeering"}}],"rules":[{"name":"name","etag":"etag","location":"location","properties":{"access":"Allow","routeFilterRuleType":"Community","provisioningState":"Succeeded","communities":["communities","communities"]}},{"name":"name","etag":"etag","location":"location","properties":{"access":"Allow","routeFilterRuleType":"Community","provisioningState":"Succeeded","communities":["communities","communities"]}}],"provisioningState":"Succeeded"},"tags":{"key":"tags"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/routeFilters/{route_filter_name}'.format(resource_group_name='resource_group_name_example', route_filter_name='route_filter_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=route_filter_parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

