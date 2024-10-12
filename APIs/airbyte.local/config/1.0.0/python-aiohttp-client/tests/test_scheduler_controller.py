# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.check_connection_read import CheckConnectionRead
from openapi_server.models.destination_core_config import DestinationCoreConfig
from openapi_server.models.invalid_input_exception_info import InvalidInputExceptionInfo
from openapi_server.models.source_core_config import SourceCoreConfig
from openapi_server.models.source_discover_schema_read import SourceDiscoverSchemaRead


pytestmark = pytest.mark.asyncio

async def test_execute_destination_check_connection(client):
    """Test case for execute_destination_check_connection

    Run check connection for a given destination configuration
    """
    body = {"connectionConfiguration":{"user":"charles"},"destinationDefinitionId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","destinationId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","workspaceId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/scheduler/destinations/check_connection',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_execute_source_check_connection(client):
    """Test case for execute_source_check_connection

    Run check connection for a given source configuration
    """
    body = {"sourceId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","connectionConfiguration":{"user":"charles"},"sourceDefinitionId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","workspaceId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/scheduler/sources/check_connection',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_execute_source_discover_schema(client):
    """Test case for execute_source_discover_schema

    Run discover schema for a given source a source configuration
    """
    body = {"sourceId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","connectionConfiguration":{"user":"charles"},"sourceDefinitionId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","workspaceId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/scheduler/sources/discover_schema',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

