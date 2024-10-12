# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.response import Response


pytestmark = pytest.mark.asyncio

async def test_metrics_list(client):
    """Test case for metrics_list

    
    """
    params = [('timespan', 'timespan_example'),
                    ('interval', 'interval_example'),
                    ('metric', 'metric_example'),
                    ('aggregation', 'aggregation_example'),
                    ('$top', 3.4),
                    ('$orderby', 'orderby_example'),
                    ('$filter', 'filter_example'),
                    ('resultType', 'result_type_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{resource_uri}/providers/microsoft.insights/metrics'.format(resource_uri='resource_uri_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

