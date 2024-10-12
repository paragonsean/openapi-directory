# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.resource_list_result import ResourceListResult
from openapi_server.models.vault import Vault
from openapi_server.models.vault_create_or_update_parameters import VaultCreateOrUpdateParameters
from openapi_server.models.vault_list_result import VaultListResult


pytestmark = pytest.mark.asyncio

async def test_vaults_create_or_update(client):
    """Test case for vaults_create_or_update

    
    """
    parameters = {"location":"location","properties":{"enabledForDeployment":True,"accessPolicies":[{"permissions":{"certificates":["all","all"],"keys":["all","all"],"secrets":["all","all"]},"tenantId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","applicationId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","objectId":"objectId"},{"permissions":{"certificates":["all","all"],"keys":["all","all"],"secrets":["all","all"]},"tenantId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","applicationId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","objectId":"objectId"},{"permissions":{"certificates":["all","all"],"keys":["all","all"],"secrets":["all","all"]},"tenantId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","applicationId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","objectId":"objectId"},{"permissions":{"certificates":["all","all"],"keys":["all","all"],"secrets":["all","all"]},"tenantId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","applicationId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","objectId":"objectId"},{"permissions":{"certificates":["all","all"],"keys":["all","all"],"secrets":["all","all"]},"tenantId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","applicationId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","objectId":"objectId"}],"enabledForDiskEncryption":True,"enabledForTemplateDeployment":True,"tenantId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","enableSoftDelete":True,"sku":{"name":"standard","family":"A"},"vaultUri":"vaultUri"},"tags":{"key":"tags"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.KeyVault/vaults/{vault_name}'.format(resource_group_name='resource_group_name_example', vault_name='vault_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_vaults_delete(client):
    """Test case for vaults_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.KeyVault/vaults/{vault_name}'.format(resource_group_name='resource_group_name_example', vault_name='vault_name_example', subscription_id='subscription_id_example'),
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
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.KeyVault/vaults/{vault_name}'.format(resource_group_name='resource_group_name_example', vault_name='vault_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_vaults_list(client):
    """Test case for vaults_list

    
    """
    params = [('$filter', 'filter_example'),
                    ('$top', 56),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resources'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_vaults_list_by_resource_group(client):
    """Test case for vaults_list_by_resource_group

    
    """
    params = [('$top', 56),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.KeyVault/vaults'.format(resource_group_name='resource_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

