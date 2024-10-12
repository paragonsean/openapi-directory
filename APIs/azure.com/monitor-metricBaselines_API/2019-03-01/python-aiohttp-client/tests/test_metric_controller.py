# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.metric_baselines_response import MetricBaselinesResponse


pytestmark = pytest.mark.asyncio

async def test_baselines_list_0(client):
    """Test case for baselines_list_0

    
    """
    params = [('metricnames', 'metricnames_example'),
                    ('metricnamespace', 'metricnamespace_example'),
                    ('timespan', 'timespan_example'),
                    ('interval', 'interval_example'),
                    ('aggregation', 'aggregation_example'),
                    ('sensitivities', 'sensitivities_example'),
                    ('$filter', 'filter_example'),
                    ('resultType', 'result_type_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{resource_uri}/providers/microsoft.insights/metricBaselines'.format(resource_uri='resource_uri_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

