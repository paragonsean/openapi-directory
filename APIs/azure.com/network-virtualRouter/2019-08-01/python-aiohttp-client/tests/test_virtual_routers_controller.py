# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.virtual_router import VirtualRouter
from openapi_server.models.virtual_router_list_result import VirtualRouterListResult
from openapi_server.models.virtual_routers_list_default_response import VirtualRoutersListDefaultResponse
from openapi_server.models.virtual_routers_update_request import VirtualRoutersUpdateRequest


pytestmark = pytest.mark.asyncio

async def test_virtual_routers_create_or_update(client):
    """Test case for virtual_routers_create_or_update

    
    """
    parameters = {"etag":"etag","properties":{"hostedGateway":{"id":"id"},"virtualRouterAsn":343953089,"virtualRouterIps":["virtualRouterIps","virtualRouterIps"],"peerings":[{"id":"id"},{"id":"id"}],"provisioningState":"Succeeded","hostedSubnet":{"id":"id"}}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/virtualRouters/{virtual_router_name}'.format(resource_group_name='resource_group_name_example', virtual_router_name='virtual_router_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_routers_delete(client):
    """Test case for virtual_routers_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/virtualRouters/{virtual_router_name}'.format(resource_group_name='resource_group_name_example', virtual_router_name='virtual_router_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_routers_get(client):
    """Test case for virtual_routers_get

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$expand', 'expand_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/virtualRouters/{virtual_router_name}'.format(resource_group_name='resource_group_name_example', virtual_router_name='virtual_router_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_routers_list(client):
    """Test case for virtual_routers_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Network/virtualRouters'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_routers_list_by_resource_group(client):
    """Test case for virtual_routers_list_by_resource_group

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/virtualRouters'.format(resource_group_name='resource_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_routers_update(client):
    """Test case for virtual_routers_update

    
    """
    parameters = openapi_server.VirtualRoutersUpdateRequest()
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/virtualRouters/{virtual_router_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', virtual_router_name='virtual_router_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

