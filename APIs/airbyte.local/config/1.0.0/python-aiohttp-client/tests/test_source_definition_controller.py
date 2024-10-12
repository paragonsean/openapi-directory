# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.custom_source_definition_create import CustomSourceDefinitionCreate
from openapi_server.models.invalid_input_exception_info import InvalidInputExceptionInfo
from openapi_server.models.not_found_known_exception_info import NotFoundKnownExceptionInfo
from openapi_server.models.private_source_definition_read import PrivateSourceDefinitionRead
from openapi_server.models.private_source_definition_read_list import PrivateSourceDefinitionReadList
from openapi_server.models.source_definition_id_request_body import SourceDefinitionIdRequestBody
from openapi_server.models.source_definition_id_with_workspace_id import SourceDefinitionIdWithWorkspaceId
from openapi_server.models.source_definition_read import SourceDefinitionRead
from openapi_server.models.source_definition_read_list import SourceDefinitionReadList
from openapi_server.models.source_definition_update import SourceDefinitionUpdate
from openapi_server.models.workspace_id_request_body import WorkspaceIdRequestBody


pytestmark = pytest.mark.asyncio

async def test_create_custom_source_definition(client):
    """Test case for create_custom_source_definition

    Creates a custom sourceDefinition for the given workspace
    """
    body = {"sourceDefinition":{"resourceRequirements":{"default":{"cpu_limit":"cpu_limit","memory_request":"memory_request","memory_limit":"memory_limit","cpu_request":"cpu_request"},"jobSpecific":[{"resourceRequirements":{"cpu_limit":"cpu_limit","memory_request":"memory_request","memory_limit":"memory_limit","cpu_request":"cpu_request"},"jobType":"get_spec"},{"resourceRequirements":{"cpu_limit":"cpu_limit","memory_request":"memory_request","memory_limit":"memory_limit","cpu_request":"cpu_request"},"jobType":"get_spec"}]},"documentationUrl":"https://openapi-generator.tech","dockerImageTag":"dockerImageTag","dockerRepository":"dockerRepository","icon":"icon","name":"name"},"workspaceId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/source_definitions/create_custom',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_source_definition(client):
    """Test case for delete_source_definition

    Delete a source definition
    """
    body = {"sourceDefinitionId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/source_definitions/delete',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_source_definition(client):
    """Test case for get_source_definition

    Get source
    """
    body = {"sourceDefinitionId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/source_definitions/get',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_source_definition_for_workspace(client):
    """Test case for get_source_definition_for_workspace

    Get a sourceDefinition that is configured for the given workspace
    """
    body = {"sourceDefinitionId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","workspaceId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/source_definitions/get_for_workspace',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_grant_source_definition_to_workspace(client):
    """Test case for grant_source_definition_to_workspace

    grant a private, non-custom sourceDefinition to a given workspace
    """
    body = {"sourceDefinitionId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","workspaceId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/source_definitions/grant_definition',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_latest_source_definitions(client):
    """Test case for list_latest_source_definitions

    List the latest sourceDefinitions Airbyte supports
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/source_definitions/list_latest',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_private_source_definitions(client):
    """Test case for list_private_source_definitions

    List all private, non-custom sourceDefinitions, and for each indicate whether the given workspace has a grant for using the definition. Used by admins to view and modify a given workspace's grants.
    """
    body = {"workspaceId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/source_definitions/list_private',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_source_definitions(client):
    """Test case for list_source_definitions

    List all the sourceDefinitions the current Airbyte deployment is configured to use
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/source_definitions/list',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_source_definitions_for_workspace(client):
    """Test case for list_source_definitions_for_workspace

    List all the sourceDefinitions the given workspace is configured to use
    """
    body = {"workspaceId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/source_definitions/list_for_workspace',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_revoke_source_definition_from_workspace(client):
    """Test case for revoke_source_definition_from_workspace

    revoke a grant to a private, non-custom sourceDefinition from a given workspace
    """
    body = {"sourceDefinitionId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","workspaceId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/source_definitions/revoke_definition',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_source_definition(client):
    """Test case for update_source_definition

    Update a sourceDefinition
    """
    body = {"resourceRequirements":{"default":{"cpu_limit":"cpu_limit","memory_request":"memory_request","memory_limit":"memory_limit","cpu_request":"cpu_request"},"jobSpecific":[{"resourceRequirements":{"cpu_limit":"cpu_limit","memory_request":"memory_request","memory_limit":"memory_limit","cpu_request":"cpu_request"},"jobType":"get_spec"},{"resourceRequirements":{"cpu_limit":"cpu_limit","memory_request":"memory_request","memory_limit":"memory_limit","cpu_request":"cpu_request"},"jobType":"get_spec"}]},"dockerImageTag":"dockerImageTag","sourceDefinitionId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/source_definitions/update',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

