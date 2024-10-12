# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.disk_encryption_set import DiskEncryptionSet
from openapi_server.models.disk_encryption_set_list import DiskEncryptionSetList
from openapi_server.models.disk_encryption_set_update import DiskEncryptionSetUpdate


pytestmark = pytest.mark.asyncio

async def test_disk_encryption_sets_create_or_update(client):
    """Test case for disk_encryption_sets_create_or_update

    
    """
    disk_encryption_set = {"identity":{"tenantId":"tenantId","principalId":"principalId","type":"SystemAssigned"},"properties":{"previousKeys":[{"sourceVault":{"id":"id"},"keyUrl":"keyUrl"},{"sourceVault":{"id":"id"},"keyUrl":"keyUrl"}],"activeKey":{"sourceVault":{"id":"id"},"keyUrl":"keyUrl"},"provisioningState":"provisioningState"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Compute/diskEncryptionSets/{disk_encryption_set_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', disk_encryption_set_name='disk_encryption_set_name_example'),
        headers=headers,
        json=disk_encryption_set,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_disk_encryption_sets_delete(client):
    """Test case for disk_encryption_sets_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Compute/diskEncryptionSets/{disk_encryption_set_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', disk_encryption_set_name='disk_encryption_set_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_disk_encryption_sets_get(client):
    """Test case for disk_encryption_sets_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Compute/diskEncryptionSets/{disk_encryption_set_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', disk_encryption_set_name='disk_encryption_set_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_disk_encryption_sets_list(client):
    """Test case for disk_encryption_sets_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Compute/diskEncryptionSets'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_disk_encryption_sets_list_by_resource_group(client):
    """Test case for disk_encryption_sets_list_by_resource_group

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Compute/diskEncryptionSets'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_disk_encryption_sets_update(client):
    """Test case for disk_encryption_sets_update

    
    """
    disk_encryption_set = {"properties":{"activeKey":{"sourceVault":{"id":"id"},"keyUrl":"keyUrl"}},"tags":{"key":"tags"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Compute/diskEncryptionSets/{disk_encryption_set_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', disk_encryption_set_name='disk_encryption_set_name_example'),
        headers=headers,
        json=disk_encryption_set,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

