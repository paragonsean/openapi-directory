# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.invalid_input_exception_info import InvalidInputExceptionInfo
from openapi_server.models.not_found_known_exception_info import NotFoundKnownExceptionInfo
from openapi_server.models.source_definition_id_with_workspace_id import SourceDefinitionIdWithWorkspaceId
from openapi_server.models.source_definition_specification_read import SourceDefinitionSpecificationRead


pytestmark = pytest.mark.asyncio

async def test_get_source_definition_specification(client):
    """Test case for get_source_definition_specification

    Get specification for a SourceDefinition.
    """
    body = {"sourceDefinitionId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","workspaceId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/source_definition_specifications/get',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

