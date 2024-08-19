# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.pipeline_template_definition_list_result import PipelineTemplateDefinitionListResult


pytestmark = pytest.mark.asyncio

async def test_pipeline_template_definitions_list(client):
    """Test case for pipeline_template_definitions_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.DevOps/pipelineTemplateDefinitions',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

