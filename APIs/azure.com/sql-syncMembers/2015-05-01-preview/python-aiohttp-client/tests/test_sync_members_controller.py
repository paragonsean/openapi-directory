# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.sync_full_schema_properties_list_result import SyncFullSchemaPropertiesListResult
from openapi_server.models.sync_member import SyncMember
from openapi_server.models.sync_member_list_result import SyncMemberListResult


pytestmark = pytest.mark.asyncio

async def test_sync_members_create_or_update(client):
    """Test case for sync_members_create_or_update

    
    """
    parameters = {"properties":{"databaseType":"AzureSqlDatabase","sqlServerDatabaseId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","password":"password","databaseName":"databaseName","syncDirection":"Bidirectional","syncState":"SyncInProgress","serverName":"serverName","userName":"userName","syncAgentId":"syncAgentId"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/servers/{server_name}/databases/{database_name}/syncGroups/{sync_group_name}/syncMembers/{sync_member_name}'.format(resource_group_name='resource_group_name_example', server_name='server_name_example', database_name='database_name_example', sync_group_name='sync_group_name_example', sync_member_name='sync_member_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sync_members_delete(client):
    """Test case for sync_members_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/servers/{server_name}/databases/{database_name}/syncGroups/{sync_group_name}/syncMembers/{sync_member_name}'.format(resource_group_name='resource_group_name_example', server_name='server_name_example', database_name='database_name_example', sync_group_name='sync_group_name_example', sync_member_name='sync_member_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sync_members_get(client):
    """Test case for sync_members_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/servers/{server_name}/databases/{database_name}/syncGroups/{sync_group_name}/syncMembers/{sync_member_name}'.format(resource_group_name='resource_group_name_example', server_name='server_name_example', database_name='database_name_example', sync_group_name='sync_group_name_example', sync_member_name='sync_member_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sync_members_list_by_sync_group(client):
    """Test case for sync_members_list_by_sync_group

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/servers/{server_name}/databases/{database_name}/syncGroups/{sync_group_name}/syncMembers'.format(resource_group_name='resource_group_name_example', server_name='server_name_example', database_name='database_name_example', sync_group_name='sync_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sync_members_list_member_schemas(client):
    """Test case for sync_members_list_member_schemas

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/servers/{server_name}/databases/{database_name}/syncGroups/{sync_group_name}/syncMembers/{sync_member_name}/schemas'.format(resource_group_name='resource_group_name_example', server_name='server_name_example', database_name='database_name_example', sync_group_name='sync_group_name_example', sync_member_name='sync_member_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sync_members_refresh_member_schema(client):
    """Test case for sync_members_refresh_member_schema

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/servers/{server_name}/databases/{database_name}/syncGroups/{sync_group_name}/syncMembers/{sync_member_name}/refreshSchema'.format(resource_group_name='resource_group_name_example', server_name='server_name_example', database_name='database_name_example', sync_group_name='sync_group_name_example', sync_member_name='sync_member_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sync_members_update(client):
    """Test case for sync_members_update

    
    """
    parameters = {"properties":{"databaseType":"AzureSqlDatabase","sqlServerDatabaseId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","password":"password","databaseName":"databaseName","syncDirection":"Bidirectional","syncState":"SyncInProgress","serverName":"serverName","userName":"userName","syncAgentId":"syncAgentId"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/servers/{server_name}/databases/{database_name}/syncGroups/{sync_group_name}/syncMembers/{sync_member_name}'.format(resource_group_name='resource_group_name_example', server_name='server_name_example', database_name='database_name_example', sync_group_name='sync_group_name_example', sync_member_name='sync_member_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

