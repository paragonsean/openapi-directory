# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.backup_resource_vault_config_resource import BackupResourceVaultConfigResource


pytestmark = pytest.mark.asyncio

async def test_backup_resource_vault_configs_get(client):
    """Test case for backup_resource_vault_configs_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/Subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.RecoveryServices/vaults/{vault_name}/backupconfig/vaultconfig'.format(vault_name='vault_name_example', resource_group_name='resource_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_backup_resource_vault_configs_update(client):
    """Test case for backup_resource_vault_configs_update

    
    """
    parameters = {"properties":{"enhancedSecurityState":"Invalid","storageModelType":"Invalid","storageType":"Invalid","softDeleteFeatureState":"Invalid","storageTypeState":"Invalid"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/Subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.RecoveryServices/vaults/{vault_name}/backupconfig/vaultconfig'.format(vault_name='vault_name_example', resource_group_name='resource_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

