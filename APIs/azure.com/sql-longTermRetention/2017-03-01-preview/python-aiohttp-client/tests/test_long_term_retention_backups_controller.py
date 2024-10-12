# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.long_term_retention_backup import LongTermRetentionBackup
from openapi_server.models.long_term_retention_backup_list_result import LongTermRetentionBackupListResult


pytestmark = pytest.mark.asyncio

async def test_long_term_retention_backups_delete(client):
    """Test case for long_term_retention_backups_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Sql/locations/{location_name}/longTermRetentionServers/{long_term_retention_server_name}/longTermRetentionDatabases/{long_term_retention_database_name}/longTermRetentionBackups/{backup_name}'.format(location_name='location_name_example', long_term_retention_server_name='long_term_retention_server_name_example', long_term_retention_database_name='long_term_retention_database_name_example', backup_name='backup_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_long_term_retention_backups_delete_by_resource_group(client):
    """Test case for long_term_retention_backups_delete_by_resource_group

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/locations/{location_name}/longTermRetentionServers/{long_term_retention_server_name}/longTermRetentionDatabases/{long_term_retention_database_name}/longTermRetentionBackups/{backup_name}'.format(resource_group_name='resource_group_name_example', location_name='location_name_example', long_term_retention_server_name='long_term_retention_server_name_example', long_term_retention_database_name='long_term_retention_database_name_example', backup_name='backup_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_long_term_retention_backups_get(client):
    """Test case for long_term_retention_backups_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Sql/locations/{location_name}/longTermRetentionServers/{long_term_retention_server_name}/longTermRetentionDatabases/{long_term_retention_database_name}/longTermRetentionBackups/{backup_name}'.format(location_name='location_name_example', long_term_retention_server_name='long_term_retention_server_name_example', long_term_retention_database_name='long_term_retention_database_name_example', backup_name='backup_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_long_term_retention_backups_get_by_resource_group(client):
    """Test case for long_term_retention_backups_get_by_resource_group

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/locations/{location_name}/longTermRetentionServers/{long_term_retention_server_name}/longTermRetentionDatabases/{long_term_retention_database_name}/longTermRetentionBackups/{backup_name}'.format(resource_group_name='resource_group_name_example', location_name='location_name_example', long_term_retention_server_name='long_term_retention_server_name_example', long_term_retention_database_name='long_term_retention_database_name_example', backup_name='backup_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_long_term_retention_backups_list_by_database(client):
    """Test case for long_term_retention_backups_list_by_database

    
    """
    params = [('onlyLatestPerDatabase', True),
                    ('databaseState', 'database_state_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Sql/locations/{location_name}/longTermRetentionServers/{long_term_retention_server_name}/longTermRetentionDatabases/{long_term_retention_database_name}/longTermRetentionBackups'.format(location_name='location_name_example', long_term_retention_server_name='long_term_retention_server_name_example', long_term_retention_database_name='long_term_retention_database_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_long_term_retention_backups_list_by_location(client):
    """Test case for long_term_retention_backups_list_by_location

    
    """
    params = [('onlyLatestPerDatabase', True),
                    ('databaseState', 'database_state_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Sql/locations/{location_name}/longTermRetentionBackups'.format(location_name='location_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_long_term_retention_backups_list_by_resource_group_database(client):
    """Test case for long_term_retention_backups_list_by_resource_group_database

    
    """
    params = [('onlyLatestPerDatabase', True),
                    ('databaseState', 'database_state_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/locations/{location_name}/longTermRetentionServers/{long_term_retention_server_name}/longTermRetentionDatabases/{long_term_retention_database_name}/longTermRetentionBackups'.format(resource_group_name='resource_group_name_example', location_name='location_name_example', long_term_retention_server_name='long_term_retention_server_name_example', long_term_retention_database_name='long_term_retention_database_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_long_term_retention_backups_list_by_resource_group_location(client):
    """Test case for long_term_retention_backups_list_by_resource_group_location

    
    """
    params = [('onlyLatestPerDatabase', True),
                    ('databaseState', 'database_state_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/locations/{location_name}/longTermRetentionBackups'.format(resource_group_name='resource_group_name_example', location_name='location_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_long_term_retention_backups_list_by_resource_group_server(client):
    """Test case for long_term_retention_backups_list_by_resource_group_server

    
    """
    params = [('onlyLatestPerDatabase', True),
                    ('databaseState', 'database_state_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/locations/{location_name}/longTermRetentionServers/{long_term_retention_server_name}/longTermRetentionBackups'.format(resource_group_name='resource_group_name_example', location_name='location_name_example', long_term_retention_server_name='long_term_retention_server_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_long_term_retention_backups_list_by_server(client):
    """Test case for long_term_retention_backups_list_by_server

    
    """
    params = [('onlyLatestPerDatabase', True),
                    ('databaseState', 'database_state_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Sql/locations/{location_name}/longTermRetentionServers/{long_term_retention_server_name}/longTermRetentionBackups'.format(location_name='location_name_example', long_term_retention_server_name='long_term_retention_server_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

