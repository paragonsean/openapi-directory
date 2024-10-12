# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.virtual_network_peering import VirtualNetworkPeering
from openapi_server.models.virtual_network_peering_list_result import VirtualNetworkPeeringListResult


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_virtual_network_peerings_create_or_update(client):
    """Test case for virtual_network_peerings_create_or_update

    
    """
    virtual_network_peering_parameters = {"name":"name","etag":"etag","properties":{"remoteVirtualNetwork":{"id":"id"},"allowVirtualNetworkAccess":True,"peeringState":"Initiated","allowGatewayTransit":True,"provisioningState":"provisioningState","allowForwardedTraffic":True,"useRemoteGateways":True}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/virtualNetworks/{virtual_network_name}/virtualNetworkPeerings/{virtual_network_peering_name}'.format(resource_group_name='resource_group_name_example', virtual_network_name='virtual_network_name_example', virtual_network_peering_name='virtual_network_peering_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=virtual_network_peering_parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_network_peerings_delete(client):
    """Test case for virtual_network_peerings_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/virtualNetworks/{virtual_network_name}/virtualNetworkPeerings/{virtual_network_peering_name}'.format(resource_group_name='resource_group_name_example', virtual_network_name='virtual_network_name_example', virtual_network_peering_name='virtual_network_peering_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_network_peerings_get(client):
    """Test case for virtual_network_peerings_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/virtualNetworks/{virtual_network_name}/virtualNetworkPeerings/{virtual_network_peering_name}'.format(resource_group_name='resource_group_name_example', virtual_network_name='virtual_network_name_example', virtual_network_peering_name='virtual_network_peering_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_network_peerings_list(client):
    """Test case for virtual_network_peerings_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/virtualNetworks/{virtual_network_name}/virtualNetworkPeerings'.format(resource_group_name='resource_group_name_example', virtual_network_name='virtual_network_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

