# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.taskrouter_v1_workspace_worker_workers_real_time_statistics import TaskrouterV1WorkspaceWorkerWorkersRealTimeStatistics


pytestmark = pytest.mark.asyncio

async def test_fetch_workers_real_time_statistics(client):
    """Test case for fetch_workers_real_time_statistics

    
    """
    params = [('TaskChannel', 'task_channel_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Workspaces/{workspace_sid}/Workers/RealTimeStatistics'.format(workspace_sid='workspace_sid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

