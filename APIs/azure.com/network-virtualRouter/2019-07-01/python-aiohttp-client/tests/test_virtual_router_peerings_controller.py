# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.virtual_router_peering import VirtualRouterPeering
from openapi_server.models.virtual_router_peering_list_result import VirtualRouterPeeringListResult
from openapi_server.models.virtual_routers_list_default_response import VirtualRoutersListDefaultResponse


pytestmark = pytest.mark.asyncio

async def test_virtual_router_peerings_create_or_update(client):
    """Test case for virtual_router_peerings_create_or_update

    
    """
    parameters = {"name":"name","etag":"etag","type":"type","properties":{"peerIp":"peerIp","provisioningState":"Succeeded","peerAsn":343953089}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/virtualRouters/{virtual_router_name}/peerings/{peering_name}'.format(resource_group_name='resource_group_name_example', virtual_router_name='virtual_router_name_example', peering_name='peering_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_router_peerings_delete(client):
    """Test case for virtual_router_peerings_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/virtualRouters/{virtual_router_name}/peerings/{peering_name}'.format(resource_group_name='resource_group_name_example', virtual_router_name='virtual_router_name_example', peering_name='peering_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_router_peerings_get(client):
    """Test case for virtual_router_peerings_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/virtualRouters/{virtual_router_name}/peerings/{peering_name}'.format(resource_group_name='resource_group_name_example', virtual_router_name='virtual_router_name_example', peering_name='peering_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_router_peerings_list(client):
    """Test case for virtual_router_peerings_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/virtualRouters/{virtual_router_name}/peerings'.format(resource_group_name='resource_group_name_example', virtual_router_name='virtual_router_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_router_peerings_update(client):
    """Test case for virtual_router_peerings_update

    
    """
    parameters = {"name":"name","etag":"etag","type":"type","properties":{"peerIp":"peerIp","provisioningState":"Succeeded","peerAsn":343953089}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/virtualRouters/{virtual_router_name}/peerings/{peering_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', virtual_router_name='virtual_router_name_example', peering_name='peering_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

