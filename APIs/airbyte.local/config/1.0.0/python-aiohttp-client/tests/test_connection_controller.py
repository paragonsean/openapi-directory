# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.connection_create import ConnectionCreate
from openapi_server.models.connection_id_request_body import ConnectionIdRequestBody
from openapi_server.models.connection_read import ConnectionRead
from openapi_server.models.connection_read_list import ConnectionReadList
from openapi_server.models.connection_search import ConnectionSearch
from openapi_server.models.connection_update import ConnectionUpdate
from openapi_server.models.invalid_input_exception_info import InvalidInputExceptionInfo
from openapi_server.models.job_info_read import JobInfoRead
from openapi_server.models.not_found_known_exception_info import NotFoundKnownExceptionInfo
from openapi_server.models.workspace_id_request_body import WorkspaceIdRequestBody


pytestmark = pytest.mark.asyncio

async def test_create_connection(client):
    """Test case for create_connection

    Create a connection between a source and a destination
    """
    body = {"sourceId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","sourceCatalogId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","prefix":"prefix","destinationId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","namespaceDefinition":"source","resourceRequirements":{"cpu_limit":"cpu_limit","memory_request":"memory_request","memory_limit":"memory_limit","cpu_request":"cpu_request"},"schedule":{"units":0,"timeUnit":"minutes"},"notifySchemaChanges":True,"scheduleType":"manual","geography":"auto","name":"name","syncCatalog":{"streams":[{"stream":{"sourceDefinedPrimaryKey":[["sourceDefinedPrimaryKey","sourceDefinedPrimaryKey"],["sourceDefinedPrimaryKey","sourceDefinedPrimaryKey"]],"sourceDefinedCursor":True,"supportedSyncModes":[null,null],"jsonSchema":"{}","name":"name","namespace":"namespace","defaultCursorField":["defaultCursorField","defaultCursorField"]},"config":{"aliasName":"aliasName","suggested":True,"fieldSelectionEnabled":True,"syncMode":"full_refresh","destinationSyncMode":"append","selectedFields":[{"fieldPath":["fieldPath","fieldPath"]},{"fieldPath":["fieldPath","fieldPath"]}],"cursorField":["cursorField","cursorField"],"selected":True,"primaryKey":[["primaryKey","primaryKey"],["primaryKey","primaryKey"]]}},{"stream":{"sourceDefinedPrimaryKey":[["sourceDefinedPrimaryKey","sourceDefinedPrimaryKey"],["sourceDefinedPrimaryKey","sourceDefinedPrimaryKey"]],"sourceDefinedCursor":True,"supportedSyncModes":[null,null],"jsonSchema":"{}","name":"name","namespace":"namespace","defaultCursorField":["defaultCursorField","defaultCursorField"]},"config":{"aliasName":"aliasName","suggested":True,"fieldSelectionEnabled":True,"syncMode":"full_refresh","destinationSyncMode":"append","selectedFields":[{"fieldPath":["fieldPath","fieldPath"]},{"fieldPath":["fieldPath","fieldPath"]}],"cursorField":["cursorField","cursorField"],"selected":True,"primaryKey":[["primaryKey","primaryKey"],["primaryKey","primaryKey"]]}}]},"namespaceFormat":"${SOURCE_NAMESPACE}","operationIds":[null,null],"scheduleData":{"cron":{"cronExpression":"cronExpression","cronTimeZone":"cronTimeZone"},"basicSchedule":{"units":6,"timeUnit":"minutes"}},"nonBreakingChangesPreference":"ignore","status":"active"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/connections/create',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_connection(client):
    """Test case for delete_connection

    Delete a connection
    """
    body = {"connectionId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/connections/delete',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_connection(client):
    """Test case for get_connection

    Get a connection
    """
    body = {"connectionId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/connections/get',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_all_connections_for_workspace(client):
    """Test case for list_all_connections_for_workspace

    Returns all connections for a workspace, including deleted connections.
    """
    body = {"workspaceId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/connections/list_all',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_connections_for_workspace(client):
    """Test case for list_connections_for_workspace

    Returns all connections for a workspace.
    """
    body = {"workspaceId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/connections/list',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reset_connection(client):
    """Test case for reset_connection

    Reset the data for the connection. Deletes data generated by the connection in the destination. Resets any cursors back to initial state.
    """
    body = {"connectionId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/connections/reset',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_connections(client):
    """Test case for search_connections

    Search connections
    """
    body = {"sourceId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","prefix":"prefix","destination":{"connectionConfiguration":{"user":"charles"},"destinationName":"destinationName","name":"name","destinationDefinitionId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","destinationId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","workspaceId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"},"source":{"sourceId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","connectionConfiguration":{"user":"charles"},"name":"name","sourceDefinitionId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","sourceName":"sourceName","workspaceId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"},"destinationId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","namespaceDefinition":"source","schedule":{"units":0,"timeUnit":"minutes"},"scheduleType":"manual","name":"name","connectionId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","namespaceFormat":"${SOURCE_NAMESPACE}","scheduleData":{"cron":{"cronExpression":"cronExpression","cronTimeZone":"cronTimeZone"},"basicSchedule":{"units":6,"timeUnit":"minutes"}},"status":"active"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/connections/search',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sync_connection(client):
    """Test case for sync_connection

    Trigger a manual sync of the connection
    """
    body = {"connectionId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/connections/sync',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_connection(client):
    """Test case for update_connection

    Update a connection
    """
    body = {"sourceCatalogId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","prefix":"prefix","namespaceDefinition":"source","resourceRequirements":{"cpu_limit":"cpu_limit","memory_request":"memory_request","memory_limit":"memory_limit","cpu_request":"cpu_request"},"schedule":{"units":0,"timeUnit":"minutes"},"breakingChange":True,"notifySchemaChanges":True,"scheduleType":"manual","geography":"auto","name":"name","syncCatalog":{"streams":[{"stream":{"sourceDefinedPrimaryKey":[["sourceDefinedPrimaryKey","sourceDefinedPrimaryKey"],["sourceDefinedPrimaryKey","sourceDefinedPrimaryKey"]],"sourceDefinedCursor":True,"supportedSyncModes":[null,null],"jsonSchema":"{}","name":"name","namespace":"namespace","defaultCursorField":["defaultCursorField","defaultCursorField"]},"config":{"aliasName":"aliasName","suggested":True,"fieldSelectionEnabled":True,"syncMode":"full_refresh","destinationSyncMode":"append","selectedFields":[{"fieldPath":["fieldPath","fieldPath"]},{"fieldPath":["fieldPath","fieldPath"]}],"cursorField":["cursorField","cursorField"],"selected":True,"primaryKey":[["primaryKey","primaryKey"],["primaryKey","primaryKey"]]}},{"stream":{"sourceDefinedPrimaryKey":[["sourceDefinedPrimaryKey","sourceDefinedPrimaryKey"],["sourceDefinedPrimaryKey","sourceDefinedPrimaryKey"]],"sourceDefinedCursor":True,"supportedSyncModes":[null,null],"jsonSchema":"{}","name":"name","namespace":"namespace","defaultCursorField":["defaultCursorField","defaultCursorField"]},"config":{"aliasName":"aliasName","suggested":True,"fieldSelectionEnabled":True,"syncMode":"full_refresh","destinationSyncMode":"append","selectedFields":[{"fieldPath":["fieldPath","fieldPath"]},{"fieldPath":["fieldPath","fieldPath"]}],"cursorField":["cursorField","cursorField"],"selected":True,"primaryKey":[["primaryKey","primaryKey"],["primaryKey","primaryKey"]]}}]},"connectionId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","namespaceFormat":"${SOURCE_NAMESPACE}","operationIds":[null,null],"scheduleData":{"cron":{"cronExpression":"cronExpression","cronTimeZone":"cronTimeZone"},"basicSchedule":{"units":6,"timeUnit":"minutes"}},"nonBreakingChangesPreference":"ignore","status":"active"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/connections/update',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

