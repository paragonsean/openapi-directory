# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.scoped_resource import ScopedResource
from openapi_server.models.scoped_resource_list_result import ScopedResourceListResult


pytestmark = pytest.mark.asyncio

async def test_private_link_scoped_resources_create_or_update(client):
    """Test case for private_link_scoped_resources_create_or_update

    
    """
    parameters = {"properties":{"linkedResourceId":"linkedResourceId","provisioningState":"provisioningState"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Insights/privateLinkScopes/{scope_name}/scopedResources/{name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', scope_name='scope_name_example', name='name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_private_link_scoped_resources_delete(client):
    """Test case for private_link_scoped_resources_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Insights/privateLinkScopes/{scope_name}/scopedResources/{name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', scope_name='scope_name_example', name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_private_link_scoped_resources_get(client):
    """Test case for private_link_scoped_resources_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Insights/privateLinkScopes/{scope_name}/scopedResources/{name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', scope_name='scope_name_example', name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_private_link_scoped_resources_list_by_private_link_scope(client):
    """Test case for private_link_scoped_resources_list_by_private_link_scope

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Insights/privateLinkScopes/{scope_name}/scopedResources'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', scope_name='scope_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

