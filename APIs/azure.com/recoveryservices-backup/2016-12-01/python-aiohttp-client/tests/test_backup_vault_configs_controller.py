# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.backup_vault_config import BackupVaultConfig


pytestmark = pytest.mark.asyncio

async def test_backup_vault_configs_get(client):
    """Test case for backup_vault_configs_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/Subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.RecoveryServices/vaults/{vault_name}/backupconfig/vaultconfig'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', vault_name='vault_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_backup_vault_configs_update(client):
    """Test case for backup_vault_configs_update

    
    """
    backup_vault_config = {"properties":{"enhancedSecurityState":"Invalid","storageType":"Invalid","storageTypeState":"Invalid"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/Subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.RecoveryServices/vaults/{vault_name}/backupconfig/vaultconfig'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', vault_name='vault_name_example'),
        headers=headers,
        json=backup_vault_config,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

