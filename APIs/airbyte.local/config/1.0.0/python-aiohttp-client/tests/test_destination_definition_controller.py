# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.custom_destination_definition_create import CustomDestinationDefinitionCreate
from openapi_server.models.destination_definition_id_request_body import DestinationDefinitionIdRequestBody
from openapi_server.models.destination_definition_id_with_workspace_id import DestinationDefinitionIdWithWorkspaceId
from openapi_server.models.destination_definition_read import DestinationDefinitionRead
from openapi_server.models.destination_definition_read_list import DestinationDefinitionReadList
from openapi_server.models.destination_definition_update import DestinationDefinitionUpdate
from openapi_server.models.invalid_input_exception_info import InvalidInputExceptionInfo
from openapi_server.models.not_found_known_exception_info import NotFoundKnownExceptionInfo
from openapi_server.models.private_destination_definition_read import PrivateDestinationDefinitionRead
from openapi_server.models.private_destination_definition_read_list import PrivateDestinationDefinitionReadList
from openapi_server.models.workspace_id_request_body import WorkspaceIdRequestBody


pytestmark = pytest.mark.asyncio

async def test_create_custom_destination_definition(client):
    """Test case for create_custom_destination_definition

    Creates a custom destinationDefinition for the given workspace
    """
    body = {"destinationDefinition":{"resourceRequirements":{"default":{"cpu_limit":"cpu_limit","memory_request":"memory_request","memory_limit":"memory_limit","cpu_request":"cpu_request"},"jobSpecific":[{"resourceRequirements":{"cpu_limit":"cpu_limit","memory_request":"memory_request","memory_limit":"memory_limit","cpu_request":"cpu_request"},"jobType":"get_spec"},{"resourceRequirements":{"cpu_limit":"cpu_limit","memory_request":"memory_request","memory_limit":"memory_limit","cpu_request":"cpu_request"},"jobType":"get_spec"}]},"documentationUrl":"https://openapi-generator.tech","dockerImageTag":"dockerImageTag","dockerRepository":"dockerRepository","icon":"icon","name":"name"},"workspaceId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/destination_definitions/create_custom',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_destination_definition(client):
    """Test case for delete_destination_definition

    Delete a destination definition
    """
    body = {"destinationDefinitionId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/destination_definitions/delete',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_destination_definition(client):
    """Test case for get_destination_definition

    Get destinationDefinition
    """
    body = {"destinationDefinitionId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/destination_definitions/get',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_destination_definition_for_workspace(client):
    """Test case for get_destination_definition_for_workspace

    Get a destinationDefinition that is configured for the given workspace
    """
    body = {"destinationDefinitionId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","workspaceId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/destination_definitions/get_for_workspace',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_grant_destination_definition_to_workspace(client):
    """Test case for grant_destination_definition_to_workspace

    grant a private, non-custom destinationDefinition to a given workspace
    """
    body = {"destinationDefinitionId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","workspaceId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/destination_definitions/grant_definition',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_destination_definitions(client):
    """Test case for list_destination_definitions

    List all the destinationDefinitions the current Airbyte deployment is configured to use
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/destination_definitions/list',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_destination_definitions_for_workspace(client):
    """Test case for list_destination_definitions_for_workspace

    List all the destinationDefinitions the given workspace is configured to use
    """
    body = {"workspaceId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/destination_definitions/list_for_workspace',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_latest_destination_definitions(client):
    """Test case for list_latest_destination_definitions

    List the latest destinationDefinitions Airbyte supports
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/destination_definitions/list_latest',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_private_destination_definitions(client):
    """Test case for list_private_destination_definitions

    List all private, non-custom destinationDefinitions, and for each indicate whether the given workspace has a grant for using the definition. Used by admins to view and modify a given workspace's grants.
    """
    body = {"workspaceId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/destination_definitions/list_private',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_revoke_destination_definition_from_workspace(client):
    """Test case for revoke_destination_definition_from_workspace

    revoke a grant to a private, non-custom destinationDefinition from a given workspace
    """
    body = {"destinationDefinitionId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","workspaceId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/destination_definitions/revoke_definition',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_destination_definition(client):
    """Test case for update_destination_definition

    Update destinationDefinition
    """
    body = {"resourceRequirements":{"default":{"cpu_limit":"cpu_limit","memory_request":"memory_request","memory_limit":"memory_limit","cpu_request":"cpu_request"},"jobSpecific":[{"resourceRequirements":{"cpu_limit":"cpu_limit","memory_request":"memory_request","memory_limit":"memory_limit","cpu_request":"cpu_request"},"jobType":"get_spec"},{"resourceRequirements":{"cpu_limit":"cpu_limit","memory_request":"memory_request","memory_limit":"memory_limit","cpu_request":"cpu_request"},"jobType":"get_spec"}]},"dockerImageTag":"dockerImageTag","destinationDefinitionId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/destination_definitions/update',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

