# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.backup_short_term_retention_policy import BackupShortTermRetentionPolicy
from openapi_server.models.backup_short_term_retention_policy_list_result import BackupShortTermRetentionPolicyListResult


pytestmark = pytest.mark.asyncio

async def test_backup_short_term_retention_policies_create_or_update(client):
    """Test case for backup_short_term_retention_policies_create_or_update

    
    """
    parameters = {"properties":{"retentionDays":0}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/servers/{server_name}/databases/{database_name}/backupShortTermRetentionPolicies/{policy_name}'.format(resource_group_name='resource_group_name_example', server_name='server_name_example', database_name='database_name_example', policy_name='policy_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_backup_short_term_retention_policies_get(client):
    """Test case for backup_short_term_retention_policies_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/servers/{server_name}/databases/{database_name}/backupShortTermRetentionPolicies/{policy_name}'.format(resource_group_name='resource_group_name_example', server_name='server_name_example', database_name='database_name_example', policy_name='policy_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_backup_short_term_retention_policies_list_by_database(client):
    """Test case for backup_short_term_retention_policies_list_by_database

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/servers/{server_name}/databases/{database_name}/backupShortTermRetentionPolicies'.format(resource_group_name='resource_group_name_example', server_name='server_name_example', database_name='database_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_backup_short_term_retention_policies_update(client):
    """Test case for backup_short_term_retention_policies_update

    
    """
    parameters = {"properties":{"retentionDays":0}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/servers/{server_name}/databases/{database_name}/backupShortTermRetentionPolicies/{policy_name}'.format(resource_group_name='resource_group_name_example', server_name='server_name_example', database_name='database_name_example', policy_name='policy_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

