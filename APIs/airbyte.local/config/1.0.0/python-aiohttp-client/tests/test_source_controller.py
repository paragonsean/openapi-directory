# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.actor_catalog_with_updated_at import ActorCatalogWithUpdatedAt
from openapi_server.models.check_connection_read import CheckConnectionRead
from openapi_server.models.discover_catalog_result import DiscoverCatalogResult
from openapi_server.models.invalid_input_exception_info import InvalidInputExceptionInfo
from openapi_server.models.not_found_known_exception_info import NotFoundKnownExceptionInfo
from openapi_server.models.source_clone_request_body import SourceCloneRequestBody
from openapi_server.models.source_create import SourceCreate
from openapi_server.models.source_discover_schema_read import SourceDiscoverSchemaRead
from openapi_server.models.source_discover_schema_request_body import SourceDiscoverSchemaRequestBody
from openapi_server.models.source_discover_schema_write_request_body import SourceDiscoverSchemaWriteRequestBody
from openapi_server.models.source_id_request_body import SourceIdRequestBody
from openapi_server.models.source_read import SourceRead
from openapi_server.models.source_read_list import SourceReadList
from openapi_server.models.source_search import SourceSearch
from openapi_server.models.source_update import SourceUpdate
from openapi_server.models.workspace_id_request_body import WorkspaceIdRequestBody


pytestmark = pytest.mark.asyncio

async def test_check_connection_to_source(client):
    """Test case for check_connection_to_source

    Check connection to the source
    """
    body = {"sourceId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/sources/check_connection',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_check_connection_to_source_for_update(client):
    """Test case for check_connection_to_source_for_update

    Check connection for a proposed update to a source
    """
    body = {"sourceId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","connectionConfiguration":{"user":"charles"},"name":"name"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/sources/check_connection_for_update',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_clone_source(client):
    """Test case for clone_source

    Clone source
    """
    body = {"sourceConfiguration":{"connectionConfiguration":{"user":"charles"},"name":"name"},"sourceCloneId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/sources/clone',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_source(client):
    """Test case for create_source

    Create a source
    """
    body = {"connectionConfiguration":{"user":"charles"},"name":"name","sourceDefinitionId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","workspaceId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/sources/create',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_source(client):
    """Test case for delete_source

    Delete a source
    """
    body = {"sourceId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/sources/delete',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_discover_schema_for_source(client):
    """Test case for discover_schema_for_source

    Discover the schema catalog of the source
    """
    body = {"sourceId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","disable_cache":True,"connectionId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","notifySchemaChange":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/sources/discover_schema',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_most_recent_source_actor_catalog(client):
    """Test case for get_most_recent_source_actor_catalog

    Get most recent ActorCatalog for source
    """
    body = {"sourceId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/sources/most_recent_source_actor_catalog',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_source(client):
    """Test case for get_source

    Get source
    """
    body = {"sourceId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/sources/get',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_sources_for_workspace(client):
    """Test case for list_sources_for_workspace

    List sources for workspace
    """
    body = {"workspaceId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/sources/list',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_sources(client):
    """Test case for search_sources

    Search sources
    """
    body = {"sourceId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","connectionConfiguration":{"user":"charles"},"name":"name","sourceDefinitionId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","sourceName":"sourceName","workspaceId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/sources/search',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_source(client):
    """Test case for update_source

    Update a source
    """
    body = {"sourceId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","connectionConfiguration":{"user":"charles"},"name":"name"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/sources/update',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_write_discover_catalog_result(client):
    """Test case for write_discover_catalog_result

    Should only called from worker, to write result from discover activity back to DB.
    """
    body = {"sourceId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","configurationHash":"configurationHash","catalog":{"streams":[{"stream":{"sourceDefinedPrimaryKey":[["sourceDefinedPrimaryKey","sourceDefinedPrimaryKey"],["sourceDefinedPrimaryKey","sourceDefinedPrimaryKey"]],"sourceDefinedCursor":True,"supportedSyncModes":[null,null],"jsonSchema":"{}","name":"name","namespace":"namespace","defaultCursorField":["defaultCursorField","defaultCursorField"]},"config":{"aliasName":"aliasName","suggested":True,"fieldSelectionEnabled":True,"syncMode":"full_refresh","destinationSyncMode":"append","selectedFields":[{"fieldPath":["fieldPath","fieldPath"]},{"fieldPath":["fieldPath","fieldPath"]}],"cursorField":["cursorField","cursorField"],"selected":True,"primaryKey":[["primaryKey","primaryKey"],["primaryKey","primaryKey"]]}},{"stream":{"sourceDefinedPrimaryKey":[["sourceDefinedPrimaryKey","sourceDefinedPrimaryKey"],["sourceDefinedPrimaryKey","sourceDefinedPrimaryKey"]],"sourceDefinedCursor":True,"supportedSyncModes":[null,null],"jsonSchema":"{}","name":"name","namespace":"namespace","defaultCursorField":["defaultCursorField","defaultCursorField"]},"config":{"aliasName":"aliasName","suggested":True,"fieldSelectionEnabled":True,"syncMode":"full_refresh","destinationSyncMode":"append","selectedFields":[{"fieldPath":["fieldPath","fieldPath"]},{"fieldPath":["fieldPath","fieldPath"]}],"cursorField":["cursorField","cursorField"],"selected":True,"primaryKey":[["primaryKey","primaryKey"],["primaryKey","primaryKey"]]}}]},"connectorVersion":"connectorVersion"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/sources/write_discover_catalog_result',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

