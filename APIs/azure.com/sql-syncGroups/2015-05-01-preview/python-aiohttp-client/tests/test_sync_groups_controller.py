# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.sync_database_id_list_result import SyncDatabaseIdListResult
from openapi_server.models.sync_full_schema_properties_list_result import SyncFullSchemaPropertiesListResult
from openapi_server.models.sync_group import SyncGroup
from openapi_server.models.sync_group_list_result import SyncGroupListResult
from openapi_server.models.sync_group_log_list_result import SyncGroupLogListResult


pytestmark = pytest.mark.asyncio

async def test_sync_groups_cancel_sync(client):
    """Test case for sync_groups_cancel_sync

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/servers/{server_name}/databases/{database_name}/syncGroups/{sync_group_name}/cancelSync'.format(resource_group_name='resource_group_name_example', server_name='server_name_example', database_name='database_name_example', sync_group_name='sync_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sync_groups_create_or_update(client):
    """Test case for sync_groups_create_or_update

    
    """
    parameters = {"properties":{"schema":{"tables":[{"quotedName":"quotedName","columns":[{"quotedName":"quotedName","dataType":"dataType","dataSize":"dataSize"},{"quotedName":"quotedName","dataType":"dataType","dataSize":"dataSize"}]},{"quotedName":"quotedName","columns":[{"quotedName":"quotedName","dataType":"dataType","dataSize":"dataSize"},{"quotedName":"quotedName","dataType":"dataType","dataSize":"dataSize"}]}],"masterSyncMemberName":"masterSyncMemberName"},"lastSyncTime":"2000-01-23T04:56:07.000+00:00","syncDatabaseId":"syncDatabaseId","hubDatabasePassword":"hubDatabasePassword","syncState":"NotReady","hubDatabaseUserName":"hubDatabaseUserName","interval":0,"conflictResolutionPolicy":"HubWin"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/servers/{server_name}/databases/{database_name}/syncGroups/{sync_group_name}'.format(resource_group_name='resource_group_name_example', server_name='server_name_example', database_name='database_name_example', sync_group_name='sync_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sync_groups_delete(client):
    """Test case for sync_groups_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/servers/{server_name}/databases/{database_name}/syncGroups/{sync_group_name}'.format(resource_group_name='resource_group_name_example', server_name='server_name_example', database_name='database_name_example', sync_group_name='sync_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sync_groups_get(client):
    """Test case for sync_groups_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/servers/{server_name}/databases/{database_name}/syncGroups/{sync_group_name}'.format(resource_group_name='resource_group_name_example', server_name='server_name_example', database_name='database_name_example', sync_group_name='sync_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sync_groups_list_by_database(client):
    """Test case for sync_groups_list_by_database

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/servers/{server_name}/databases/{database_name}/syncGroups'.format(resource_group_name='resource_group_name_example', server_name='server_name_example', database_name='database_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sync_groups_list_hub_schemas(client):
    """Test case for sync_groups_list_hub_schemas

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/servers/{server_name}/databases/{database_name}/syncGroups/{sync_group_name}/hubSchemas'.format(resource_group_name='resource_group_name_example', server_name='server_name_example', database_name='database_name_example', sync_group_name='sync_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sync_groups_list_logs(client):
    """Test case for sync_groups_list_logs

    
    """
    params = [('startTime', 'start_time_example'),
                    ('endTime', 'end_time_example'),
                    ('type', 'type_example'),
                    ('continuationToken', 'continuation_token_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/servers/{server_name}/databases/{database_name}/syncGroups/{sync_group_name}/logs'.format(resource_group_name='resource_group_name_example', server_name='server_name_example', database_name='database_name_example', sync_group_name='sync_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sync_groups_list_sync_database_ids(client):
    """Test case for sync_groups_list_sync_database_ids

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Sql/locations/{location_name}/syncDatabaseIds'.format(location_name='location_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sync_groups_refresh_hub_schema(client):
    """Test case for sync_groups_refresh_hub_schema

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/servers/{server_name}/databases/{database_name}/syncGroups/{sync_group_name}/refreshHubSchema'.format(resource_group_name='resource_group_name_example', server_name='server_name_example', database_name='database_name_example', sync_group_name='sync_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sync_groups_trigger_sync(client):
    """Test case for sync_groups_trigger_sync

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/servers/{server_name}/databases/{database_name}/syncGroups/{sync_group_name}/triggerSync'.format(resource_group_name='resource_group_name_example', server_name='server_name_example', database_name='database_name_example', sync_group_name='sync_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sync_groups_update(client):
    """Test case for sync_groups_update

    
    """
    parameters = {"properties":{"schema":{"tables":[{"quotedName":"quotedName","columns":[{"quotedName":"quotedName","dataType":"dataType","dataSize":"dataSize"},{"quotedName":"quotedName","dataType":"dataType","dataSize":"dataSize"}]},{"quotedName":"quotedName","columns":[{"quotedName":"quotedName","dataType":"dataType","dataSize":"dataSize"},{"quotedName":"quotedName","dataType":"dataType","dataSize":"dataSize"}]}],"masterSyncMemberName":"masterSyncMemberName"},"lastSyncTime":"2000-01-23T04:56:07.000+00:00","syncDatabaseId":"syncDatabaseId","hubDatabasePassword":"hubDatabasePassword","syncState":"NotReady","hubDatabaseUserName":"hubDatabaseUserName","interval":0,"conflictResolutionPolicy":"HubWin"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/servers/{server_name}/databases/{database_name}/syncGroups/{sync_group_name}'.format(resource_group_name='resource_group_name_example', server_name='server_name_example', database_name='database_name_example', sync_group_name='sync_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

