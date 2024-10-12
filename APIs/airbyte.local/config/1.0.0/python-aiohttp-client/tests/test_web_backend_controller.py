# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.connection_id_request_body import ConnectionIdRequestBody
from openapi_server.models.connection_state_type import ConnectionStateType
from openapi_server.models.invalid_input_exception_info import InvalidInputExceptionInfo
from openapi_server.models.not_found_known_exception_info import NotFoundKnownExceptionInfo
from openapi_server.models.web_backend_check_updates_read import WebBackendCheckUpdatesRead
from openapi_server.models.web_backend_connection_create import WebBackendConnectionCreate
from openapi_server.models.web_backend_connection_list_request_body import WebBackendConnectionListRequestBody
from openapi_server.models.web_backend_connection_read import WebBackendConnectionRead
from openapi_server.models.web_backend_connection_read_list import WebBackendConnectionReadList
from openapi_server.models.web_backend_connection_request_body import WebBackendConnectionRequestBody
from openapi_server.models.web_backend_connection_update import WebBackendConnectionUpdate
from openapi_server.models.web_backend_geographies_list_result import WebBackendGeographiesListResult
from openapi_server.models.web_backend_workspace_state import WebBackendWorkspaceState
from openapi_server.models.web_backend_workspace_state_result import WebBackendWorkspaceStateResult


pytestmark = pytest.mark.asyncio

async def test_get_state_type(client):
    """Test case for get_state_type

    Fetch the current state type for a connection.
    """
    body = {"connectionId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/web_backend/state/get_type',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_backend_check_updates(client):
    """Test case for web_backend_check_updates

    Returns a summary of source and destination definitions that could be updated.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/web_backend/check_updates',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_backend_create_connection(client):
    """Test case for web_backend_create_connection

    Create a connection
    """
    body = {"sourceId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","sourceCatalogId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","prefix":"prefix","destinationId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","namespaceDefinition":"source","resourceRequirements":{"cpu_limit":"cpu_limit","memory_request":"memory_request","memory_limit":"memory_limit","cpu_request":"cpu_request"},"schedule":{"units":0,"timeUnit":"minutes"},"operations":[{"name":"name","operatorConfiguration":{"webhook":{"webhookConfigId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","dbtCloud":{"accountId":0,"jobId":6},"executionUrl":"executionUrl","executionBody":"executionBody","webhookType":"dbtCloud"},"normalization":{"option":"basic"},"dbt":{"gitRepoBranch":"gitRepoBranch","dockerImage":"dockerImage","dbtArguments":"dbtArguments","gitRepoUrl":"gitRepoUrl"},"operatorType":"normalization"},"workspaceId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"},{"name":"name","operatorConfiguration":{"webhook":{"webhookConfigId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","dbtCloud":{"accountId":0,"jobId":6},"executionUrl":"executionUrl","executionBody":"executionBody","webhookType":"dbtCloud"},"normalization":{"option":"basic"},"dbt":{"gitRepoBranch":"gitRepoBranch","dockerImage":"dockerImage","dbtArguments":"dbtArguments","gitRepoUrl":"gitRepoUrl"},"operatorType":"normalization"},"workspaceId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}],"scheduleType":"manual","geography":"auto","name":"name","syncCatalog":{"streams":[{"stream":{"sourceDefinedPrimaryKey":[["sourceDefinedPrimaryKey","sourceDefinedPrimaryKey"],["sourceDefinedPrimaryKey","sourceDefinedPrimaryKey"]],"sourceDefinedCursor":True,"supportedSyncModes":[null,null],"jsonSchema":"{}","name":"name","namespace":"namespace","defaultCursorField":["defaultCursorField","defaultCursorField"]},"config":{"aliasName":"aliasName","suggested":True,"fieldSelectionEnabled":True,"syncMode":"full_refresh","destinationSyncMode":"append","selectedFields":[{"fieldPath":["fieldPath","fieldPath"]},{"fieldPath":["fieldPath","fieldPath"]}],"cursorField":["cursorField","cursorField"],"selected":True,"primaryKey":[["primaryKey","primaryKey"],["primaryKey","primaryKey"]]}},{"stream":{"sourceDefinedPrimaryKey":[["sourceDefinedPrimaryKey","sourceDefinedPrimaryKey"],["sourceDefinedPrimaryKey","sourceDefinedPrimaryKey"]],"sourceDefinedCursor":True,"supportedSyncModes":[null,null],"jsonSchema":"{}","name":"name","namespace":"namespace","defaultCursorField":["defaultCursorField","defaultCursorField"]},"config":{"aliasName":"aliasName","suggested":True,"fieldSelectionEnabled":True,"syncMode":"full_refresh","destinationSyncMode":"append","selectedFields":[{"fieldPath":["fieldPath","fieldPath"]},{"fieldPath":["fieldPath","fieldPath"]}],"cursorField":["cursorField","cursorField"],"selected":True,"primaryKey":[["primaryKey","primaryKey"],["primaryKey","primaryKey"]]}}]},"namespaceFormat":"${SOURCE_NAMESPACE}","operationIds":[null,null],"scheduleData":{"cron":{"cronExpression":"cronExpression","cronTimeZone":"cronTimeZone"},"basicSchedule":{"units":6,"timeUnit":"minutes"}},"nonBreakingChangesPreference":"ignore","status":"active"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/web_backend/connections/create',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_backend_get_connection(client):
    """Test case for web_backend_get_connection

    Get a connection
    """
    body = {"withRefreshedCatalog":True,"connectionId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/web_backend/connections/get',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_backend_get_workspace_state(client):
    """Test case for web_backend_get_workspace_state

    Returns the current state of a workspace
    """
    body = {"workspaceId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/web_backend/workspace/state',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_backend_list_connections_for_workspace(client):
    """Test case for web_backend_list_connections_for_workspace

    Returns all non-deleted connections for a workspace.
    """
    body = {"sourceId":[null,null],"destinationId":[null,null],"workspaceId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/web_backend/connections/list',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_backend_list_geographies(client):
    """Test case for web_backend_list_geographies

    Returns available geographies can be selected to run data syncs in a particular geography. The 'auto' entry indicates that the sync will be automatically assigned to a geography according to the platform default behavior. Entries other than 'auto' are two-letter country codes that follow the ISO 3166-1 alpha-2 standard. 
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/web_backend/geographies/list',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_backend_update_connection(client):
    """Test case for web_backend_update_connection

    Update a connection
    """
    body = {"sourceCatalogId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","prefix":"prefix","skipReset":True,"namespaceDefinition":"source","resourceRequirements":{"cpu_limit":"cpu_limit","memory_request":"memory_request","memory_limit":"memory_limit","cpu_request":"cpu_request"},"schedule":{"units":0,"timeUnit":"minutes"},"operations":[{"name":"name","operationId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","operatorConfiguration":{"webhook":{"webhookConfigId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","dbtCloud":{"accountId":0,"jobId":6},"executionUrl":"executionUrl","executionBody":"executionBody","webhookType":"dbtCloud"},"normalization":{"option":"basic"},"dbt":{"gitRepoBranch":"gitRepoBranch","dockerImage":"dockerImage","dbtArguments":"dbtArguments","gitRepoUrl":"gitRepoUrl"},"operatorType":"normalization"},"workspaceId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"},{"name":"name","operationId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","operatorConfiguration":{"webhook":{"webhookConfigId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","dbtCloud":{"accountId":0,"jobId":6},"executionUrl":"executionUrl","executionBody":"executionBody","webhookType":"dbtCloud"},"normalization":{"option":"basic"},"dbt":{"gitRepoBranch":"gitRepoBranch","dockerImage":"dockerImage","dbtArguments":"dbtArguments","gitRepoUrl":"gitRepoUrl"},"operatorType":"normalization"},"workspaceId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}],"notifySchemaChanges":True,"scheduleType":"manual","geography":"auto","name":"name","syncCatalog":{"streams":[{"stream":{"sourceDefinedPrimaryKey":[["sourceDefinedPrimaryKey","sourceDefinedPrimaryKey"],["sourceDefinedPrimaryKey","sourceDefinedPrimaryKey"]],"sourceDefinedCursor":True,"supportedSyncModes":[null,null],"jsonSchema":"{}","name":"name","namespace":"namespace","defaultCursorField":["defaultCursorField","defaultCursorField"]},"config":{"aliasName":"aliasName","suggested":True,"fieldSelectionEnabled":True,"syncMode":"full_refresh","destinationSyncMode":"append","selectedFields":[{"fieldPath":["fieldPath","fieldPath"]},{"fieldPath":["fieldPath","fieldPath"]}],"cursorField":["cursorField","cursorField"],"selected":True,"primaryKey":[["primaryKey","primaryKey"],["primaryKey","primaryKey"]]}},{"stream":{"sourceDefinedPrimaryKey":[["sourceDefinedPrimaryKey","sourceDefinedPrimaryKey"],["sourceDefinedPrimaryKey","sourceDefinedPrimaryKey"]],"sourceDefinedCursor":True,"supportedSyncModes":[null,null],"jsonSchema":"{}","name":"name","namespace":"namespace","defaultCursorField":["defaultCursorField","defaultCursorField"]},"config":{"aliasName":"aliasName","suggested":True,"fieldSelectionEnabled":True,"syncMode":"full_refresh","destinationSyncMode":"append","selectedFields":[{"fieldPath":["fieldPath","fieldPath"]},{"fieldPath":["fieldPath","fieldPath"]}],"cursorField":["cursorField","cursorField"],"selected":True,"primaryKey":[["primaryKey","primaryKey"],["primaryKey","primaryKey"]]}}]},"connectionId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","namespaceFormat":"${SOURCE_NAMESPACE}","scheduleData":{"cron":{"cronExpression":"cronExpression","cronTimeZone":"cronTimeZone"},"basicSchedule":{"units":6,"timeUnit":"minutes"}},"nonBreakingChangesPreference":"ignore","status":"active"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/web_backend/connections/update',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

