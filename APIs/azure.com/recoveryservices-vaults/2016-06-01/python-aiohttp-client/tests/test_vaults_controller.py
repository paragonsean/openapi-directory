# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.patch_vault import PatchVault
from openapi_server.models.vault import Vault
from openapi_server.models.vault_list import VaultList


pytestmark = pytest.mark.asyncio

async def test_vaults_create_or_update(client):
    """Test case for vaults_create_or_update

    
    """
    vault = {"sku":{"name":"Standard"},"properties":{"provisioningState":"provisioningState","upgradeDetails":{"lastUpdatedTimeUtc":"2000-01-23T04:56:07.000+00:00","endTimeUtc":"2000-01-23T04:56:07.000+00:00","upgradedResourceId":"upgradedResourceId","previousResourceId":"previousResourceId","operationId":"operationId","triggerType":"UserTriggered","message":"message","startTimeUtc":"2000-01-23T04:56:07.000+00:00","status":"Unknown"}}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.RecoveryServices/vaults/{vault_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', vault_name='vault_name_example'),
        headers=headers,
        json=vault,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_vaults_delete(client):
    """Test case for vaults_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.RecoveryServices/vaults/{vault_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', vault_name='vault_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_vaults_get(client):
    """Test case for vaults_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.RecoveryServices/vaults/{vault_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', vault_name='vault_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_vaults_list_by_resource_group(client):
    """Test case for vaults_list_by_resource_group

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.RecoveryServices/vaults'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_vaults_list_by_subscription_id(client):
    """Test case for vaults_list_by_subscription_id

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.RecoveryServices/vaults'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_vaults_update(client):
    """Test case for vaults_update

    
    """
    vault = {"sku":{"name":"Standard"},"properties":{"provisioningState":"provisioningState","upgradeDetails":{"lastUpdatedTimeUtc":"2000-01-23T04:56:07.000+00:00","endTimeUtc":"2000-01-23T04:56:07.000+00:00","upgradedResourceId":"upgradedResourceId","previousResourceId":"previousResourceId","operationId":"operationId","triggerType":"UserTriggered","message":"message","startTimeUtc":"2000-01-23T04:56:07.000+00:00","status":"Unknown"}}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.RecoveryServices/vaults/{vault_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', vault_name='vault_name_example'),
        headers=headers,
        json=vault,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

