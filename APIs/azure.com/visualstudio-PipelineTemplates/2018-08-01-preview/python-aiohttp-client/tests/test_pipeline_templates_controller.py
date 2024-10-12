# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.pipeline_template_resource_list_result import PipelineTemplateResourceListResult


pytestmark = pytest.mark.asyncio

async def test_pipeline_templates_list(client):
    """Test case for pipeline_templates_list

    PipelineTemplates_List
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/microsoft.visualstudio/pipelineTemplates',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

