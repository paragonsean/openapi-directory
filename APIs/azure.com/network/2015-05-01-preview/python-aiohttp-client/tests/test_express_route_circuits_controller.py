# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.express_route_circuit import ExpressRouteCircuit
from openapi_server.models.express_route_circuit_list_result import ExpressRouteCircuitListResult
from openapi_server.models.express_route_circuits_arp_table_list_result import ExpressRouteCircuitsArpTableListResult
from openapi_server.models.express_route_circuits_routes_table_list_result import ExpressRouteCircuitsRoutesTableListResult
from openapi_server.models.express_route_circuits_stats_list_result import ExpressRouteCircuitsStatsListResult


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_express_route_circuits_create_or_update(client):
    """Test case for express_route_circuits_create_or_update

    
    """
    parameters = {"etag":"etag","sku":{"tier":"Standard","name":"name","family":"UnlimitedData"},"properties":{"circuitProvisioningState":"circuitProvisioningState","authorizations":[{"name":"name","etag":"etag","properties":{"authorizationUseStatus":"Available","authorizationKey":"authorizationKey","provisioningState":"provisioningState"}},{"name":"name","etag":"etag","properties":{"authorizationUseStatus":"Available","authorizationKey":"authorizationKey","provisioningState":"provisioningState"}}],"serviceProviderNotes":"serviceProviderNotes","peerings":[{"name":"name","etag":"etag","properties":{"sharedKey":"sharedKey","primaryAzurePort":"primaryAzurePort","secondaryAzurePort":"secondaryAzurePort","vlanId":2,"azureASN":0,"provisioningState":"provisioningState","peerASN":1,"secondaryPeerAddressPrefix":"secondaryPeerAddressPrefix","stats":{"bytesIn":5,"bytesOut":5},"microsoftPeeringConfig":{"routingRegistryName":"routingRegistryName","advertisedPublicPrefixes":["advertisedPublicPrefixes","advertisedPublicPrefixes"],"advertisedPublicPrefixesState":"NotConfigured","customerASN":6},"primaryPeerAddressPrefix":"primaryPeerAddressPrefix","state":"Disabled","peeringType":"AzurePublicPeering"}},{"name":"name","etag":"etag","properties":{"sharedKey":"sharedKey","primaryAzurePort":"primaryAzurePort","secondaryAzurePort":"secondaryAzurePort","vlanId":2,"azureASN":0,"provisioningState":"provisioningState","peerASN":1,"secondaryPeerAddressPrefix":"secondaryPeerAddressPrefix","stats":{"bytesIn":5,"bytesOut":5},"microsoftPeeringConfig":{"routingRegistryName":"routingRegistryName","advertisedPublicPrefixes":["advertisedPublicPrefixes","advertisedPublicPrefixes"],"advertisedPublicPrefixesState":"NotConfigured","customerASN":6},"primaryPeerAddressPrefix":"primaryPeerAddressPrefix","state":"Disabled","peeringType":"AzurePublicPeering"}}],"provisioningState":"provisioningState","serviceKey":"serviceKey","serviceProviderProvisioningState":"NotProvisioned","serviceProviderProperties":{"bandwidthInMbps":7,"serviceProviderName":"serviceProviderName","peeringLocation":"peeringLocation"}}}
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

async def test_express_route_circuits_list_arp_table(client):
    """Test case for express_route_circuits_list_arp_table

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/expressRouteCircuits/{circuit_namearp_tabl}'.format(resource_group_name='resource_group_name_example', circuit_name='circuit_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_express_route_circuits_list_routes_table(client):
    """Test case for express_route_circuits_list_routes_table

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/expressRouteCircuits/{circuit_nameroutes_tabl}'.format(resource_group_name='resource_group_name_example', circuit_name='circuit_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_express_route_circuits_list_stats(client):
    """Test case for express_route_circuits_list_stats

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/expressRouteCircuits/{circuit_namestat}'.format(resource_group_name='resource_group_name_example', circuit_name='circuit_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

