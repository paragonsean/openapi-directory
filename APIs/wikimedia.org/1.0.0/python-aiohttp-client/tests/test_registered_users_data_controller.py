# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.new_registered_users import NewRegisteredUsers
from openapi_server.models.problem import Problem


pytestmark = pytest.mark.asyncio

async def test_metrics_registered_users_new_project_granularity_start_end_get(client):
    """Test case for metrics_registered_users_new_project_granularity_start_end_get

    Get newly registered users counts for a project.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest_v1/metrics/registered-users/new/{project}/{granularity}/{start}/{end}'.format(project='project_example', granularity='granularity_example', start='start_example', end='end_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

