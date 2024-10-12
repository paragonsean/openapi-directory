# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.express_route_circuit_peering import ExpressRouteCircuitPeering
from openapi_server.models.express_route_circuit_peering_list_result import ExpressRouteCircuitPeeringListResult


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_express_route_circuit_peerings_create_or_update(client):
    """Test case for express_route_circuit_peerings_create_or_update

    
    """
    peering_parameters = {"name":"name","etag":"etag","properties":{"sharedKey":"sharedKey","primaryAzurePort":"primaryAzurePort","secondaryAzurePort":"secondaryAzurePort","vlanId":9,"lastModifiedBy":"lastModifiedBy","azureASN":0,"provisioningState":"provisioningState","peerASN":1,"secondaryPeerAddressPrefix":"secondaryPeerAddressPrefix","stats":{"primarybytesOut":5,"primarybytesIn":5,"secondarybytesOut":7,"secondarybytesIn":2},"gatewayManagerEtag":"gatewayManagerEtag","microsoftPeeringConfig":{"routingRegistryName":"routingRegistryName","advertisedPublicPrefixes":["advertisedPublicPrefixes","advertisedPublicPrefixes"],"advertisedPublicPrefixesState":"NotConfigured","customerASN":6},"primaryPeerAddressPrefix":"primaryPeerAddressPrefix","state":"Disabled","peeringType":"AzurePublicPeering"}}
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

