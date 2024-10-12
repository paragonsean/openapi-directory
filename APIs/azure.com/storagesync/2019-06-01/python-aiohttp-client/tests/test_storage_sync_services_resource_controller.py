# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.storage_sync_error import StorageSyncError
from openapi_server.models.storage_sync_service import StorageSyncService
from openapi_server.models.storage_sync_service_array import StorageSyncServiceArray
from openapi_server.models.storage_sync_service_create_parameters import StorageSyncServiceCreateParameters
from openapi_server.models.storage_sync_service_update_parameters import StorageSyncServiceUpdateParameters


pytestmark = pytest.mark.asyncio

async def test_storage_sync_services_create(client):
    """Test case for storage_sync_services_create

    
    """
    parameters = {"location":"location","properties":"{}","tags":{"key":"tags"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.StorageSync/storageSyncServices/{storage_sync_service_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', storage_sync_service_name='storage_sync_service_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_storage_sync_services_delete(client):
    """Test case for storage_sync_services_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.StorageSync/storageSyncServices/{storage_sync_service_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', storage_sync_service_name='storage_sync_service_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_storage_sync_services_get(client):
    """Test case for storage_sync_services_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.StorageSync/storageSyncServices/{storage_sync_service_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', storage_sync_service_name='storage_sync_service_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_storage_sync_services_list_by_resource_group(client):
    """Test case for storage_sync_services_list_by_resource_group

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.StorageSync/storageSyncServices'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_storage_sync_services_list_by_subscription(client):
    """Test case for storage_sync_services_list_by_subscription

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.StorageSync/storageSyncServices'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_storage_sync_services_update(client):
    """Test case for storage_sync_services_update

    
    """
    parameters = {"properties":"{}","tags":{"key":"tags"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.StorageSync/storageSyncServices/{storage_sync_service_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', storage_sync_service_name='storage_sync_service_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

