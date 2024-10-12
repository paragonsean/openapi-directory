# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.storage_target import StorageTarget
from openapi_server.models.storage_targets_result import StorageTargetsResult


pytestmark = pytest.mark.asyncio

async def test_storage_targets_create_or_update(client):
    """Test case for storage_targets_create_or_update

    
    """
    storagetarget = {"name":"name","id":"id","type":"type","properties":{"clfs":{"target":"target"},"targetType":"nfs3","nfs3":{"usageModel":"usageModel","target":"target"},"provisioningState":"Succeeded","junctions":[{"nfsExport":"nfsExport","namespacePath":"namespacePath","targetPath":"targetPath"},{"nfsExport":"nfsExport","namespacePath":"namespacePath","targetPath":"targetPath"}],"unknown":{"unknownMap":{"key":"unknownMap"}}}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.StorageCache/caches/{cache_name}/storageTargets/{storage_target_name}'.format(resource_group_name='resource_group_name_example', subscription_id='subscription_id_example', cache_name='cache_name_example', storage_target_name='storage_target_name_example'),
        headers=headers,
        json=storagetarget,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_storage_targets_delete(client):
    """Test case for storage_targets_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.StorageCache/caches/{cache_name}/storageTargets/{storage_target_name}'.format(resource_group_name='resource_group_name_example', subscription_id='subscription_id_example', cache_name='cache_name_example', storage_target_name='storage_target_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_storage_targets_get(client):
    """Test case for storage_targets_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.StorageCache/caches/{cache_name}/storageTargets/{storage_target_name}'.format(resource_group_name='resource_group_name_example', subscription_id='subscription_id_example', cache_name='cache_name_example', storage_target_name='storage_target_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_storage_targets_list_by_cache(client):
    """Test case for storage_targets_list_by_cache

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.StorageCache/caches/{cache_name}/storageTargets'.format(resource_group_name='resource_group_name_example', subscription_id='subscription_id_example', cache_name='cache_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

