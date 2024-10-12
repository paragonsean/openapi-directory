# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.metric_definition_collection import MetricDefinitionCollection


pytestmark = pytest.mark.asyncio

async def test_metric_definitions_list(client):
    """Test case for metric_definitions_list

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$filter', 'filter_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{resource_uri}/providers/microsoft.insights/metricDefinitions'.format(resource_uri='resource_uri_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

