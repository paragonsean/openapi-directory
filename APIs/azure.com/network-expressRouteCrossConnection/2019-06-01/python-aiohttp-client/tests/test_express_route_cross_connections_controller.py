# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.express_route_cross_connection import ExpressRouteCrossConnection
from openapi_server.models.express_route_cross_connection_list_result import ExpressRouteCrossConnectionListResult
from openapi_server.models.express_route_cross_connections_update_tags_request import ExpressRouteCrossConnectionsUpdateTagsRequest


pytestmark = pytest.mark.asyncio

async def test_express_route_cross_connections_create_or_update(client):
    """Test case for express_route_cross_connections_create_or_update

    
    """
    parameters = {"etag":"etag","properties":{"primaryAzurePort":"primaryAzurePort","sTag":7,"secondaryAzurePort":"secondaryAzurePort","bandwidthInMbps":0,"serviceProviderNotes":"serviceProviderNotes","peerings":[{"name":"name","etag":"etag","properties":{"sharedKey":"sharedKey","primaryAzurePort":"primaryAzurePort","ipv6PeeringConfig":{"routeFilter":{"id":"id"},"microsoftPeeringConfig":{"advertisedCommunities":["advertisedCommunities","advertisedCommunities"],"routingRegistryName":"routingRegistryName","legacyMode":5,"advertisedPublicPrefixes":["advertisedPublicPrefixes","advertisedPublicPrefixes"],"advertisedPublicPrefixesState":"NotConfigured","customerASN":1},"primaryPeerAddressPrefix":"primaryPeerAddressPrefix","state":"Disabled","secondaryPeerAddressPrefix":"secondaryPeerAddressPrefix"},"secondaryAzurePort":"secondaryAzurePort","vlanId":2,"lastModifiedBy":"lastModifiedBy","azureASN":6,"provisioningState":"provisioningState","peerASN":2421234837,"secondaryPeerAddressPrefix":"secondaryPeerAddressPrefix","gatewayManagerEtag":"gatewayManagerEtag","microsoftPeeringConfig":{"advertisedCommunities":["advertisedCommunities","advertisedCommunities"],"routingRegistryName":"routingRegistryName","legacyMode":5,"advertisedPublicPrefixes":["advertisedPublicPrefixes","advertisedPublicPrefixes"],"advertisedPublicPrefixesState":"NotConfigured","customerASN":1},"primaryPeerAddressPrefix":"primaryPeerAddressPrefix","state":"Disabled","peeringType":"AzurePublicPeering"}},{"name":"name","etag":"etag","properties":{"sharedKey":"sharedKey","primaryAzurePort":"primaryAzurePort","ipv6PeeringConfig":{"routeFilter":{"id":"id"},"microsoftPeeringConfig":{"advertisedCommunities":["advertisedCommunities","advertisedCommunities"],"routingRegistryName":"routingRegistryName","legacyMode":5,"advertisedPublicPrefixes":["advertisedPublicPrefixes","advertisedPublicPrefixes"],"advertisedPublicPrefixesState":"NotConfigured","customerASN":1},"primaryPeerAddressPrefix":"primaryPeerAddressPrefix","state":"Disabled","secondaryPeerAddressPrefix":"secondaryPeerAddressPrefix"},"secondaryAzurePort":"secondaryAzurePort","vlanId":2,"lastModifiedBy":"lastModifiedBy","azureASN":6,"provisioningState":"provisioningState","peerASN":2421234837,"secondaryPeerAddressPrefix":"secondaryPeerAddressPrefix","gatewayManagerEtag":"gatewayManagerEtag","microsoftPeeringConfig":{"advertisedCommunities":["advertisedCommunities","advertisedCommunities"],"routingRegistryName":"routingRegistryName","legacyMode":5,"advertisedPublicPrefixes":["advertisedPublicPrefixes","advertisedPublicPrefixes"],"advertisedPublicPrefixesState":"NotConfigured","customerASN":1},"primaryPeerAddressPrefix":"primaryPeerAddressPrefix","state":"Disabled","peeringType":"AzurePublicPeering"}}],"provisioningState":"provisioningState","serviceProviderProvisioningState":"NotProvisioned","expressRouteCircuit":{"id":"id"},"peeringLocation":"peeringLocation"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/expressRouteCrossConnections/{cross_connection_name}'.format(resource_group_name='resource_group_name_example', cross_connection_name='cross_connection_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_express_route_cross_connections_get(client):
    """Test case for express_route_cross_connections_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/expressRouteCrossConnections/{cross_connection_name}'.format(resource_group_name='resource_group_name_example', cross_connection_name='cross_connection_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_express_route_cross_connections_list(client):
    """Test case for express_route_cross_connections_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Network/expressRouteCrossConnections'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_express_route_cross_connections_list_by_resource_group(client):
    """Test case for express_route_cross_connections_list_by_resource_group

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/expressRouteCrossConnections'.format(resource_group_name='resource_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_express_route_cross_connections_update_tags(client):
    """Test case for express_route_cross_connections_update_tags

    
    """
    cross_connection_parameters = openapi_server.ExpressRouteCrossConnectionsUpdateTagsRequest()
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/expressRouteCrossConnections/{cross_connection_name}'.format(resource_group_name='resource_group_name_example', cross_connection_name='cross_connection_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=cross_connection_parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

