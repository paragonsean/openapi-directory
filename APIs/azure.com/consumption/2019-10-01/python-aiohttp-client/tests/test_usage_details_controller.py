# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.usage_details_list_result import UsageDetailsListResult


pytestmark = pytest.mark.asyncio

async def test_usage_details_list(client):
    """Test case for usage_details_list

    
    """
    params = [('$expand', 'expand_example'),
                    ('$filter', 'filter_example'),
                    ('$skiptoken', 'skiptoken_example'),
                    ('$top', 56),
                    ('api-version', 'api_version_example'),
                    ('metric', 'metric_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{scope}/providers/Microsoft.Consumption/usageDetails'.format(scope='scope_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

