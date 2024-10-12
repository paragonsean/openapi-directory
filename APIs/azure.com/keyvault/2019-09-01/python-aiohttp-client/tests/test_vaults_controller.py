# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.check_name_availability_result import CheckNameAvailabilityResult
from openapi_server.models.deleted_vault import DeletedVault
from openapi_server.models.deleted_vault_list_result import DeletedVaultListResult
from openapi_server.models.resource_list_result import ResourceListResult
from openapi_server.models.vault import Vault
from openapi_server.models.vault_access_policy_parameters import VaultAccessPolicyParameters
from openapi_server.models.vault_check_name_availability_parameters import VaultCheckNameAvailabilityParameters
from openapi_server.models.vault_create_or_update_parameters import VaultCreateOrUpdateParameters
from openapi_server.models.vault_list_result import VaultListResult
from openapi_server.models.vault_patch_parameters import VaultPatchParameters


pytestmark = pytest.mark.asyncio

async def test_vaults_check_name_availability(client):
    """Test case for vaults_check_name_availability

    
    """
    vault_name = {"name":"name","type":"Microsoft.KeyVault/vaults"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/providers/Microsoft.KeyVault/checkNameAvailability'.format(subscription_id='subscription_id_example'),
        headers=headers,
        json=vault_name,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_vaults_create_or_update(client):
    """Test case for vaults_create_or_update

    
    """
    parameters = {"location":"location","properties":{"enablePurgeProtection":True,"privateEndpointConnections":[{"properties":{"privateLinkServiceConnectionState":{"actionRequired":"actionRequired","description":"description","status":"Pending"},"privateEndpoint":{"id":"id"},"provisioningState":"Succeeded"}},{"properties":{"privateLinkServiceConnectionState":{"actionRequired":"actionRequired","description":"description","status":"Pending"},"privateEndpoint":{"id":"id"},"provisioningState":"Succeeded"}}],"enabledForDeployment":True,"accessPolicies":[{"permissions":{"certificates":["get","get"],"keys":["encrypt","encrypt"],"storage":["get","get"],"secrets":["get","get"]},"tenantId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","applicationId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","objectId":"objectId"},{"permissions":{"certificates":["get","get"],"keys":["encrypt","encrypt"],"storage":["get","get"],"secrets":["get","get"]},"tenantId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","applicationId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","objectId":"objectId"}],"enabledForDiskEncryption":True,"createMode":"recover","enabledForTemplateDeployment":True,"tenantId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","enableSoftDelete":True,"networkAcls":{"bypass":"AzureServices","defaultAction":"Allow","ipRules":[{"value":"value"},{"value":"value"}],"virtualNetworkRules":[{"id":"id"},{"id":"id"}]},"sku":{"name":"standard","family":"A"},"vaultUri":"vaultUri"},"tags":{"key":"tags"}}
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

async def test_vaults_get_deleted(client):
    """Test case for vaults_get_deleted

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.KeyVault/locations/{location}/deletedVaults/{vault_name}'.format(vault_name='vault_name_example', location='location_example', subscription_id='subscription_id_example'),
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


pytestmark = pytest.mark.asyncio

async def test_vaults_list_by_subscription(client):
    """Test case for vaults_list_by_subscription

    
    """
    params = [('$top', 56),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.KeyVault/vaults'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_vaults_list_deleted(client):
    """Test case for vaults_list_deleted

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.KeyVault/deletedVaults'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_vaults_purge_deleted(client):
    """Test case for vaults_purge_deleted

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/providers/Microsoft.KeyVault/locations/{location}/deletedVaults/{vault_name}/purge'.format(vault_name='vault_name_example', location='location_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_vaults_update(client):
    """Test case for vaults_update

    
    """
    parameters = {"properties":{"enablePurgeProtection":True,"enabledForDeployment":True,"accessPolicies":[{"permissions":{"certificates":["get","get"],"keys":["encrypt","encrypt"],"storage":["get","get"],"secrets":["get","get"]},"tenantId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","applicationId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","objectId":"objectId"},{"permissions":{"certificates":["get","get"],"keys":["encrypt","encrypt"],"storage":["get","get"],"secrets":["get","get"]},"tenantId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","applicationId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","objectId":"objectId"}],"enabledForDiskEncryption":True,"createMode":"recover","enabledForTemplateDeployment":True,"tenantId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","enableSoftDelete":True,"networkAcls":{"bypass":"AzureServices","defaultAction":"Allow","ipRules":[{"value":"value"},{"value":"value"}],"virtualNetworkRules":[{"id":"id"},{"id":"id"}]},"sku":{"name":"standard","family":"A"}},"tags":{"key":"tags"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.KeyVault/vaults/{vault_name}'.format(resource_group_name='resource_group_name_example', vault_name='vault_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_vaults_update_access_policy(client):
    """Test case for vaults_update_access_policy

    
    """
    parameters = {"name":"name","location":"location","id":"id","type":"type","properties":{"accessPolicies":[{"permissions":{"certificates":["get","get"],"keys":["encrypt","encrypt"],"storage":["get","get"],"secrets":["get","get"]},"tenantId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","applicationId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","objectId":"objectId"},{"permissions":{"certificates":["get","get"],"keys":["encrypt","encrypt"],"storage":["get","get"],"secrets":["get","get"]},"tenantId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","applicationId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","objectId":"objectId"}]}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.KeyVault/vaults/{vault_name}/accessPolicies/{operation_kind}'.format(resource_group_name='resource_group_name_example', vault_name='vault_name_example', operation_kind='operation_kind_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

