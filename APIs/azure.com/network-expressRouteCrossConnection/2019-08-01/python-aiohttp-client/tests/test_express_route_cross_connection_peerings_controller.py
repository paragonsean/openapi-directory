# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.express_route_cross_connection_peering import ExpressRouteCrossConnectionPeering
from openapi_server.models.express_route_cross_connection_peering_list import ExpressRouteCrossConnectionPeeringList


pytestmark = pytest.mark.asyncio

async def test_express_route_cross_connection_peerings_create_or_update(client):
    """Test case for express_route_cross_connection_peerings_create_or_update

    
    """
    peering_parameters = {"name":"name","etag":"etag","properties":{"sharedKey":"sharedKey","primaryAzurePort":"primaryAzurePort","ipv6PeeringConfig":{"routeFilter":{"id":"id"},"microsoftPeeringConfig":{"advertisedCommunities":["advertisedCommunities","advertisedCommunities"],"routingRegistryName":"routingRegistryName","legacyMode":5,"advertisedPublicPrefixes":["advertisedPublicPrefixes","advertisedPublicPrefixes"],"advertisedPublicPrefixesState":"NotConfigured","customerASN":1},"primaryPeerAddressPrefix":"primaryPeerAddressPrefix","state":"Disabled","secondaryPeerAddressPrefix":"secondaryPeerAddressPrefix"},"secondaryAzurePort":"secondaryAzurePort","vlanId":2,"lastModifiedBy":"lastModifiedBy","azureASN":6,"provisioningState":"Succeeded","peerASN":2421234837,"secondaryPeerAddressPrefix":"secondaryPeerAddressPrefix","gatewayManagerEtag":"gatewayManagerEtag","microsoftPeeringConfig":{"advertisedCommunities":["advertisedCommunities","advertisedCommunities"],"routingRegistryName":"routingRegistryName","legacyMode":5,"advertisedPublicPrefixes":["advertisedPublicPrefixes","advertisedPublicPrefixes"],"advertisedPublicPrefixesState":"NotConfigured","customerASN":1},"primaryPeerAddressPrefix":"primaryPeerAddressPrefix","state":"Disabled","peeringType":"AzurePublicPeering"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/expressRouteCrossConnections/{cross_connection_name}/peerings/{peering_name}'.format(resource_group_name='resource_group_name_example', cross_connection_name='cross_connection_name_example', peering_name='peering_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=peering_parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_express_route_cross_connection_peerings_delete(client):
    """Test case for express_route_cross_connection_peerings_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/expressRouteCrossConnections/{cross_connection_name}/peerings/{peering_name}'.format(resource_group_name='resource_group_name_example', cross_connection_name='cross_connection_name_example', peering_name='peering_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_express_route_cross_connection_peerings_get(client):
    """Test case for express_route_cross_connection_peerings_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/expressRouteCrossConnections/{cross_connection_name}/peerings/{peering_name}'.format(resource_group_name='resource_group_name_example', cross_connection_name='cross_connection_name_example', peering_name='peering_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_express_route_cross_connection_peerings_list(client):
    """Test case for express_route_cross_connection_peerings_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/expressRouteCrossConnections/{cross_connection_name}/peerings'.format(resource_group_name='resource_group_name_example', cross_connection_name='cross_connection_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

