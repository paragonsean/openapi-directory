# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.report import Report


pytestmark = pytest.mark.asyncio

async def test_get_traffic_report(client):
    """Test case for get_traffic_report

    
    """
    params = [('dimension', 'dimension_example'),
                    ('filter', 'filter_example'),
                    ('metric', 'metric_example'),
                    ('sort', 'sort_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/sell/analytics/v1/traffic_report',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

