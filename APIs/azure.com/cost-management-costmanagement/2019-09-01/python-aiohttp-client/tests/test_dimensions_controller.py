# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.dimensions_list_result import DimensionsListResult
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_dimensions_list_by_subscription(client):
    """Test case for dimensions_list_by_subscription

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$filter', 'filter_example'),
                    ('$expand', 'expand_example'),
                    ('$skiptoken', 'skiptoken_example'),
                    ('$top', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{scope}/providers/Microsoft.CostManagement/dimensions'.format(scope='scope_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

