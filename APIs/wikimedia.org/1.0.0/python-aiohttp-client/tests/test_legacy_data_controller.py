# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.pagecounts_project import PagecountsProject
from openapi_server.models.problem import Problem


pytestmark = pytest.mark.asyncio

async def test_metrics_legacy_pagecounts_aggregate_project_access_site_granularity_start_end_get(client):
    """Test case for metrics_legacy_pagecounts_aggregate_project_access_site_granularity_start_end_get

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest_v1/metrics/legacy/pagecounts/aggregate/{project}/{access_site}/{granularity}/{start}/{end}'.format(project='project_example', access_site='access_site_example', granularity='granularity_example', start='start_example', end='end_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

