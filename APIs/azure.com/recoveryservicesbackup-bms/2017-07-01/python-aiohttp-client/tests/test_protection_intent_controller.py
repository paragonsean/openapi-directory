# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.pre_validate_enable_backup_request import PreValidateEnableBackupRequest
from openapi_server.models.pre_validate_enable_backup_response import PreValidateEnableBackupResponse
from openapi_server.models.protection_intent_resource import ProtectionIntentResource


pytestmark = pytest.mark.asyncio

async def test_protection_intent_create_or_update(client):
    """Test case for protection_intent_create_or_update

    
    """
    parameters = {"properties":{"backupManagementType":"Invalid","itemId":"itemId","policyId":"policyId","protectionIntentItemType":"protectionIntentItemType","protectionState":"Invalid","sourceResourceId":"sourceResourceId"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/Subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.RecoveryServices/vaults/{vault_name}/backupFabrics/{fabric_name}/backupProtectionIntent/{intent_object_name}'.format(vault_name='vault_name_example', resource_group_name='resource_group_name_example', subscription_id='subscription_id_example', fabric_name='fabric_name_example', intent_object_name='intent_object_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_protection_intent_delete(client):
    """Test case for protection_intent_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/Subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.RecoveryServices/vaults/{vault_name}/backupFabrics/{fabric_name}/backupProtectionIntent/{intent_object_name}'.format(vault_name='vault_name_example', resource_group_name='resource_group_name_example', subscription_id='subscription_id_example', fabric_name='fabric_name_example', intent_object_name='intent_object_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_protection_intent_get(client):
    """Test case for protection_intent_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/Subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.RecoveryServices/vaults/{vault_name}/backupFabrics/{fabric_name}/backupProtectionIntent/{intent_object_name}'.format(vault_name='vault_name_example', resource_group_name='resource_group_name_example', subscription_id='subscription_id_example', fabric_name='fabric_name_example', intent_object_name='intent_object_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_protection_intent_validate(client):
    """Test case for protection_intent_validate

    It will validate followings  1. Vault capacity  2. VM is already protected  3. Any VM related configuration passed in properties.
    """
    parameters = {"resourceId":"resourceId","vaultId":"vaultId","properties":"properties","resourceType":"Invalid"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/Subscriptions/{subscription_id}/providers/Microsoft.RecoveryServices/locations/{azure_region}/backupPreValidateProtection'.format(azure_region='azure_region_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

