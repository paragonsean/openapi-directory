# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.backup_long_term_retention_vault import BackupLongTermRetentionVault
from openapi_server.models.backup_long_term_retention_vault_list_result import BackupLongTermRetentionVaultListResult


pytestmark = pytest.mark.asyncio

async def test_backup_long_term_retention_vaults_create_or_update(client):
    """Test case for backup_long_term_retention_vaults_create_or_update

    
    """
    parameters = {"location":"location","properties":{"recoveryServicesVaultResourceId":"recoveryServicesVaultResourceId"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/servers/{server_name}/backupLongTermRetentionVaults/{backup_long_term_retention_vault_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', server_name='server_name_example', backup_long_term_retention_vault_name='backup_long_term_retention_vault_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_backup_long_term_retention_vaults_get(client):
    """Test case for backup_long_term_retention_vaults_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/servers/{server_name}/backupLongTermRetentionVaults/{backup_long_term_retention_vault_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', server_name='server_name_example', backup_long_term_retention_vault_name='backup_long_term_retention_vault_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_backup_long_term_retention_vaults_list_by_server(client):
    """Test case for backup_long_term_retention_vaults_list_by_server

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/servers/{server_name}/backupLongTermRetentionVaults'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', server_name='server_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

