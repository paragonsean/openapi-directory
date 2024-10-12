# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.problem import Problem
from openapi_server.models.unique_devices import UniqueDevices


pytestmark = pytest.mark.asyncio

async def test_metrics_unique_devices_project_access_site_granularity_start_end_get(client):
    """Test case for metrics_unique_devices_project_access_site_granularity_start_end_get

    Get unique devices count per project
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest_v1/metrics/unique-devices/{project}/{access_site}/{granularity}/{start}/{end}'.format(project='project_example', access_site='access_site_example', granularity='granularity_example', start='start_example', end='end_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

