# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.custom_rp_manifest import CustomRPManifest
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.list_by_custom_rp_manifest import ListByCustomRPManifest
from openapi_server.models.resource_providers_update import ResourceProvidersUpdate


pytestmark = pytest.mark.asyncio

async def test_custom_resource_provider_create_or_update(client):
    """Test case for custom_resource_provider_create_or_update

    
    """
    resource_provider = {"properties":"{}"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.CustomProviders/resourceProviders/{resource_provider_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', resource_provider_name='resource_provider_name_example'),
        headers=headers,
        json=resource_provider,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_custom_resource_provider_delete(client):
    """Test case for custom_resource_provider_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.CustomProviders/resourceProviders/{resource_provider_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', resource_provider_name='resource_provider_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_custom_resource_provider_get(client):
    """Test case for custom_resource_provider_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.CustomProviders/resourceProviders/{resource_provider_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', resource_provider_name='resource_provider_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_custom_resource_provider_list_by_resource_group(client):
    """Test case for custom_resource_provider_list_by_resource_group

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.CustomProviders/resourceProviders'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_custom_resource_provider_list_by_subscription(client):
    """Test case for custom_resource_provider_list_by_subscription

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.CustomProviders/resourceProviders'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_custom_resource_provider_update(client):
    """Test case for custom_resource_provider_update

    
    """
    patchable_resource = {"tags":{"key":"tags"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.CustomProviders/resourceProviders/{resource_provider_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', resource_provider_name='resource_provider_name_example'),
        headers=headers,
        json=patchable_resource,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

