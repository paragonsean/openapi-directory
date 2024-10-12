# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.azure_monitor_private_link_scope import AzureMonitorPrivateLinkScope
from openapi_server.models.azure_monitor_private_link_scope_list_result import AzureMonitorPrivateLinkScopeListResult
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.tags_resource import TagsResource


pytestmark = pytest.mark.asyncio

async def test_private_link_scopes_create_or_update(client):
    """Test case for private_link_scopes_create_or_update

    
    """
    azure_monitor_private_link_scope_payload = {"properties":{"provisioningState":"provisioningState"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/microsoft.insights/privateLinkScopes/{scope_name}'.format(resource_group_name='resource_group_name_example', subscription_id='subscription_id_example', scope_name='scope_name_example'),
        headers=headers,
        json=azure_monitor_private_link_scope_payload,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_private_link_scopes_delete(client):
    """Test case for private_link_scopes_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/microsoft.insights/privateLinkScopes/{scope_name}'.format(resource_group_name='resource_group_name_example', subscription_id='subscription_id_example', scope_name='scope_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_private_link_scopes_get(client):
    """Test case for private_link_scopes_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/microsoft.insights/privateLinkScopes/{scope_name}'.format(resource_group_name='resource_group_name_example', subscription_id='subscription_id_example', scope_name='scope_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_private_link_scopes_list(client):
    """Test case for private_link_scopes_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/microsoft.insights/privateLinkScopes'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_private_link_scopes_list_by_resource_group(client):
    """Test case for private_link_scopes_list_by_resource_group

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/microsoft.insights/privateLinkScopes'.format(resource_group_name='resource_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_private_link_scopes_update_tags(client):
    """Test case for private_link_scopes_update_tags

    
    """
    private_link_scope_tags = {"tags":"{}"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/microsoft.insights/privateLinkScopes/{scope_name}'.format(resource_group_name='resource_group_name_example', subscription_id='subscription_id_example', scope_name='scope_name_example'),
        headers=headers,
        json=private_link_scope_tags,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

